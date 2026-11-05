#!/usr/bin/env python3
"""Zdieľaná medzipamäť obrázkov z archívov – každý obrázok (snímka, dlaždica) sa z archívu stiahne len raz.

Ukladá ju brzda tools/slusne.py: každý obrázok stiahnutý cez brzdu (nástroje, vlastné skripty, pomocníci) sa uloží
podľa adresy a nabudúce sa vezme z disku bez dopytu na archív. Z adresy sa pred uložením odstránia len časti, ktoré
obsah nemenia (;jsessionid=, PHPSESSID, poistky proti medzipamäti typu _=1793… alebo &1793…, utm_…); neznáme
parametre zostávajú – radšej stiahnuť znova, než vrátiť cudzí snímok. Ukladá sa len úspešná odpoveď, ktorá je
naozaj obrázok. Porta fontium a eBadatelna robia výrez a náhľad z uloženého celého snímku bez siete.

Medzipamäť je spoločná pre všetky projekty na počítači: ~/.cache/rodokmen_snimky/ (Windows
%LOCALAPPDATA%\\rodokmen_snimky), iný priečinok nastaví premenná RODOKMEN_SNIMKY. Najviac 5 GB (RODOKMEN_SNIMKY_GB),
najdlhšie nepoužité súbory sa mažú samy. Celý priečinok možno kedykoľvek zmazať, nástroje si obrázky stiahnu znova.

Použitie (z koreňa projektu):
  cache.py stav                       -> koľko miesta zaberá a koľko stiahnutí z archívu ušetrila (podrobne slusne.py stav)
  cache.py uloz <subor.json> [vystup.jpg] [--nahled nahled.jpg]
                                      -> uloží snímku z prehliadača eBadatelny (výsledok úryvku v reference/portaly.md,
                                         SOA Praha); súbor .json potom zmaže
  cache.py najdi <adresa snímky> [--nahled nahled.jpg]
                                      -> cesta k uloženej snímke eBadatelny (/d/… alebo /a/…), inak kód 1
                                         (nájdená snímka sa počíta ako ušetrené otvorenie v prehliadači)
  --nahled nahled.jpg                 -> k tomu rovno náhľad široký 1600 px (na prečítanie stránky, bez siete)

Počíta sa len to, čo by inak naozaj išlo z archívu znova: pri nástrojoch cez brzdu každý obrázok vrátený z disku,
pri eBadatelne nájdenie cez „najdi“ (nie výrezy a náhľady z ebadatelna.py, tie by sa robili z disku aj bez medzipamäte).
"""
import base64, glob, hashlib, json, os, re, shutil, subprocess, sys
from urllib.parse import parse_qsl, urlencode, urlsplit

KOREN = os.environ.get("RODOKMEN_SNIMKY") or os.path.join(
    os.environ.get("LOCALAPPDATA") or os.path.join(os.path.expanduser("~"), ".cache"), "rodokmen_snimky")
LIMIT = float(os.environ.get("RODOKMEN_SNIMKY_GB") or 5) * 1024 ** 3
PRIPONY = ((b"\xff\xd8\xff", ".jpg"), (b"\x89PNG\r\n\x1a\n", ".png"), (b"GIF8", ".gif"), (b"II*\x00", ".tif"),
           (b"MM\x00*", ".tif"), (b"\x00\x00\x00\x0cjP  ", ".jp2"), (b"\xffO\xffQ", ".j2k"))


def cesta(klic):
    """Súbor v medzipamäti; kľúč je relatívna cesta s „/“."""
    return os.path.join(KOREN, *klic.split("/"))


def pripona(data):
    """Prípona podľa prvých bajtov; None = nie je obrázok (chybová stránka, „zablokované“ …)."""
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return ".webp"
    return next((p for z, p in PRIPONY if data.startswith(z)), None)


def _cely(hlava, konec, velikost):
    """Má obrázok koniec? Prerušené sťahovanie má hlavičku tiež, len mu chýba spodok snímky."""
    p = pripona(hlava)
    if p in (".jpg", ".jp2", ".j2k"):   # značka konca FF D9 (za ňou býva výplň); vnútri dát sa objaviť nemôže
        return b"\xff\xd9" in konec
    if p == ".png":
        return b"IEND" in konec[-64:]
    if p == ".gif":
        return konec.rstrip(b"\x00")[-1:] == b";"
    if p == ".webp":
        return int.from_bytes(hlava[4:8], "little") + 8 <= velikost
    return p is not None   # TIFF koniec nemá – postráži ho len dĺžka zo servera


def cely(data, delka=None):
    """Úplný obrázok: sedí dĺžka zo servera (Content-Length), ak je, a má značku konca."""
    if delka is not None and len(data) != delka:
        return False
    return _cely(data[:16], data[-1024:], len(data))


def cely_soubor(path):
    """To isté pre uložený súbor (číta len začiatok a koniec)."""
    try:
        n = os.path.getsize(path)
        with open(path, "rb") as f:
            hlava = f.read(16)
            f.seek(max(0, n - 1024))
            return _cely(hlava, f.read(), n)
    except OSError:
        return False


# --- obrázky podľa adresy (ukladá brzda slusne.py) ----------------------------------------------------------------
def klic_url(url):
    """Kľúč podľa adresy bez častí, ktoré obsah nemenia. Neznáme parametre zostávajú."""
    u = urlsplit(url)
    path = re.sub(r";jsessionid=[^/?#;]*", "", u.path, flags=re.I)
    q = []
    for k, v in parse_qsl(u.query, keep_blank_values=True):
        kl = k.lower()
        if kl in ("jsessionid", "phpsessid") or kl.startswith("utm_"):
            continue
        if (kl == "_" and v.isdigit()) or (not v and re.fullmatch(r"\d{10,}", k)):   # poistka proti medzipamäti
            continue
        q.append((k, v))
    host = (u.hostname or "").lower()
    port = f":{u.port}" if u.port and u.port not in (80, 443) else ""   # http i https = ten istý obrázok
    norm = f"{host}{port}{path}?{urlencode(sorted(q))}"
    h = hashlib.sha1(norm.encode()).hexdigest()
    return f"web/{host}/{h[:2]}/{h}"


def najdi_url(url):
    """Uložený obrázok pre adresu, alebo None."""
    k = cesta(klic_url(url))
    for _, p in PRIPONY + ((None, ".webp"),):
        if os.path.exists(k + p):
            if not cely_soubor(k + p):   # skrátený (uložený staršou verziou) – zmazať a stiahnuť znova
                try:
                    os.remove(k + p)
                except OSError:
                    pass
                return None
            _pouzito(k + p)
            return k + p
    return None


_ulozeno = [0]


def uloz_url(url, data, delka=None):
    """Uloží obrázok stiahnutý z adresy (len skutočný a úplný obrázok). Vracia cestu alebo None."""
    p = pripona(data)
    return uloz(klic_url(url) + p, data) if p and cely(data, delka) else None


# --- spoločné ---------------------------------------------------------------------------------------------------
def _pouzito(p):
    try:
        os.utime(p)   # naposledy použité – upratovanie maže najdlhšie nepoužité
    except OSError:
        pass


def uklid():
    """Nad limitom zmaže najdlhšie nepoužité súbory."""
    polozky = []
    for d, _, fs in os.walk(KOREN):
        for f in fs:
            p = os.path.join(d, f)
            try:
                st = os.stat(p)
                polozky.append((st.st_mtime, st.st_size, p))
            except OSError:
                pass
    polozky.sort()   # najstaršie naposledy použité prvé
    celkem = sum(s for _, s, _ in polozky)
    while celkem > LIMIT and polozky:
        _, s, p = polozky.pop(0)
        try:
            os.remove(p)
            celkem -= s
        except OSError:
            pass


def uloz(klic, data):
    """Zapíše obrázok pod kľúčom. Vracia cestu, pri chybe zápisu None."""
    p = cesta(klic)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    tmp = f"{p}.tmp.{os.getpid()}"
    try:
        with open(tmp, "wb") as f:
            f.write(data)
        os.replace(tmp, p)
    except OSError:
        try:
            os.remove(tmp)
        except OSError:
            pass
        return None
    _ulozeno[0] += 1
    if _ulozeno[0] % 50 == 0:
        uklid()
    return p


# --- odvodenie výrezu / náhľadu zo snímky --------------------------------------------------------------------------
def _magick():
    m = (shutil.which("magick") or next(iter(sorted(glob.glob(r"C:\Program Files\ImageMagick*\magick.exe"))), None)
         or (os.name != "nt" and shutil.which("convert")))
    return m


def odvod(src, out, crop=None, zmenseni=1):
    """Z celého uloženého obrázka urobí výrez (crop: x0,y0,x1,y1) a/alebo zmenšenie. Bez siete."""
    if not crop and zmenseni <= 1:
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        shutil.copyfile(src, out)
        return True
    M = _magick()
    if not M:
        return False
    args = [M, src + "[0]"]
    if crop:
        r = subprocess.run([M, src + "[0]", "-format", "%w %h", "info:"], capture_output=True, text=True)
        try:
            W, H = map(int, r.stdout.split())
        except ValueError:
            return False
        x0, y0, x1, y1 = crop
        args += ["-crop", f"{round((x1 - x0) * W)}x{round((y1 - y0) * H)}+{round(x0 * W)}+{round(y0 * H)}", "+repage"]
    if zmenseni > 1:
        args += ["-resize", f"{100 / zmenseni:g}%"]
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    return subprocess.run(args + ["-quality", "90", out], capture_output=True).returncode == 0


# --- snímky z prehliadača (eBadatelna) -------------------------------------------------------------------------------
EBAD = re.compile(r"ebadatelna\.soapraha\.cz/(d|a)/(\d+)/(\d+)")


EBAD_WEB = "ebadatelna.soapraha.cz"


def _slusne():
    """Brzda tools/slusne.py z rovnakého priečinka (python -I nepridáva priečinok skriptu do cesty)."""
    d = os.path.dirname(os.path.abspath(__file__))
    if d not in sys.path:
        sys.path.insert(0, d)
    import slusne
    return slusne


def _zapocti(host, velikost, z_disku=True):
    """Štatistika pre slusne.py stav (stiahnuté z archívu / vzaté z disku). Bez brzdy sa nič nepočíta."""
    try:
        slusne = _slusne()
        slusne.zapocti(host, velikost, z_disku)
    except Exception:   # noqa: BLE001 – štatistika nesmie zastaviť prácu
        pass


def klic_ebadatelna(druh, xid, n):
    return f"ebadatelna/{druh}/{xid}/sn{int(n):04d}.jpg"


def _ze_souboru(path):
    d = json.loads(open(path, encoding="utf-8").read())
    if isinstance(d, str):   # Playwright ukladá výsledok ako reťazec JSON
        d = json.loads(d)
    return d


NAHLED_PX = 1600


def _nahled(src, out, sirka=None):
    """Náhľad široký NAHLED_PX (menšia snímka sa len skopíruje)."""
    if not out:
        return
    if not sirka:
        M = _magick()
        r = subprocess.run([M, src + "[0]", "-format", "%w", "info:"], capture_output=True, text=True) if M else None
        sirka = int(r.stdout) if r and r.stdout.strip().isdigit() else NAHLED_PX
    if odvod(src, out, zmenseni=max(1, int(sirka) / NAHLED_PX)):
        print("náhľad:", out)
    else:
        print("náhľad sa nepodaril (chýba ImageMagick?) – snímka je uložená, náhľad urobte cez ebadatelna.py snimek … nahled")


def main(a):
    for s in (sys.stdout, sys.stderr):   # UTF-8 výstup aj na Windows bez -X utf8
        if hasattr(s, "reconfigure"):
            s.reconfigure(encoding="utf-8", errors="replace")
    if not a or a[0] in ("-h", "--help"):
        sys.exit(__doc__)
    nahled = None
    if "--nahled" in a:
        i = a.index("--nahled")
        if i + 1 >= len(a):
            sys.exit("--nahled potrebuje súbor, napr. --nahled pracovni/nahled.jpg")
        nahled = a[i + 1]
        a = a[:i] + a[i + 2:]
    if a[0] == "stav":
        n = s = 0
        for d, _, fs in os.walk(KOREN):
            for f in fs:
                n += 1
                s += os.path.getsize(os.path.join(d, f))
        print(f"{KOREN}: {n} súborov, {s / 1024 ** 2:.0f} MB z {LIMIT / 1024 ** 3:g} GB "
              "(najdlhšie nepoužité sa nad limitom mažú samy)")
        try:
            slusne = _slusne()
            slusne._stav_mezipameti(slusne._slozka())
        except Exception:   # noqa: BLE001
            pass
    elif a[0] == "uloz" and len(a) > 1:
        d = _ze_souboru(a[1])
        m = EBAD.search(d.get("adresa", ""))
        if not m or not str(d.get("data", "")).startswith("data:image/"):
            sys.exit("súbor nie je výsledok úryvku pre eBadatelnu (chýba adresa snímky alebo obrázok)")
        klic = klic_ebadatelna(*m.groups())
        znovu = os.path.exists(cesta(klic))   # snímka už bola uložená – prehliadač ju načítal z archívu zbytočne
        data = base64.b64decode(d["data"].split(",", 1)[1])
        if not cely(data):
            sys.exit("snímka z prehliadača nie je celá (chýba koniec obrázka) – počkajte na načítanie a uložte ju znova")
        p = uloz(klic, data)
        _zapocti(EBAD_WEB, len(data), z_disku=False)
        if not p:
            sys.exit(f"do {KOREN} nie je možné zapisovať")
        os.remove(a[1])
        print("uložené:", p, f"({d.get('w')} × {d.get('h')})")
        if znovu:
            print("pozor: táto snímka už v medzipamäti bola – nabudúce sa najprv opýtajte „cache.py najdi <adresa>“")
        if len(a) > 2:
            os.makedirs(os.path.dirname(os.path.abspath(a[2])), exist_ok=True)
            shutil.copyfile(p, a[2])
            print(a[2])
        _nahled(p, nahled, d.get("w"))
    elif a[0] == "najdi" and len(a) > 1:
        m = EBAD.search(a[1])
        p = cesta(klic_ebadatelna(*m.groups())) if m else None
        if not p or not os.path.exists(p):
            sys.exit(1)
        if not cely_soubor(p):   # skrátený – zmazať, snímka sa uloží znova z prehliadača
            try:
                os.remove(p)
            except OSError:
                pass
            sys.exit(1)
        _pouzito(p)
        _zapocti(EBAD_WEB, os.path.getsize(p))   # snímka sa nemusí znova otvárať v prehliadači
        print(p)
        _nahled(p, nahled)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])

