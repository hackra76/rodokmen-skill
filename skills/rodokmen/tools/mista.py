#!/usr/bin/env python3
"""Místa předků pro mapu na webu (data/mista.json).

Použití:
  mista.py pridej "Název" ["regulární výraz"] ["dotaz pro vyhledání"]
      přidá obec; výraz se hledá v údajích osob (výchozí = prvních 5 písmen názvu, aby sedělo i skloňování),
      dotaz pro OpenStreetMap (výchozí = "Název, Česko", když nic nenajde, zkusí Slovensko a další sousední země);
      historickou část obce, kterou mapa nezná, zadej jako celou obec; u víceznačných názvů (Podolí, Dub) přidej sousední obec:
      "Podolí, Odlochovice" – a ve výpisu vždy zkontroluj okres
  mista.py
      dohledá souřadnice u míst, která je ještě nemají (OpenStreetMap Nominatim, 1 dotaz za sekundu),
      a vypíše seznam. Když bod nesedí, opravte lat/lon v data/mista.json ručně.

Položka může mít "hypoteza": true a "rod": <Kekulé 8–15> – pak se na mapě ukáže jako hypotéza bez osob.
"""
import json, math, os, re, sys, time, urllib.parse, urllib.request
if sys.argv[1:2] in (["-h"], ["--help"]):   # nápoveda namiesto pádu
    sys.exit(__doc__.strip())
import os as _os, sys as _sys; _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import slusne  # noqa: E402 – brzda proti zablokování archivem (společný limit dotazů, tools/slusne.py)
for _s in (sys.stdout, sys.stderr):   # UTF-8 výstup i na Windows bez -X utf8 (cp1250 neumí třeba „→“)
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "mista.json")


VZDALENE_KM = 50   # nový bod ďalej ako toto od všetkých ostatných miest projektu = asi iná obec rovnakého mena


def nominatim(par):
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode(par)
    req = urllib.request.Request(url, headers={"User-Agent": "rodokmen-skill/1.0 (family genealogy map, occasional geocoding)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        res = json.load(r)
    time.sleep(1.1)
    return res


SIDLA = {"city", "town", "village", "hamlet", "suburb", "quarter", "neighbourhood", "isolated_dwelling", "farm",
         "municipality", "borough", "cadastral_community"}   # typy v triede place; z boundary len administrative (obce, katastre)
# place=locality chýba zámerne: v OSM je to pomenované neobývané miesto (pole, trať), nie sídlo


def je_sidlo(r):
    if r.get("class") == "place":
        return r.get("type") in SIDLA
    if (r.get("class"), r.get("type")) != ("boundary", "administrative"):
        return False
    if r.get("addresstype"):   # obec má „municipality“, „village“…; kraj „state“, okres „county“
        return r["addresstype"] in SIDLA | {"city_district"}
    return int(r.get("place_rank") or 0) >= 16


def vyber(res):
    """Prvé sídlo ako (výsledok, True); bez sídla prvý výsledok (bar, ostrov, chránené územie…) s False."""
    obce = [r for r in res if je_sidlo(r)]
    return (obce[0], True) if obce else (res[0], False) if res else None


def geocode(q, zeme=None):
    """(lat, lon, adresa z OSM, je_obec); najprv len sídla (featuretype=settlement), ak nič, tak čokoľvek."""
    nalez = None
    for sidla in ({"featuretype": "settlement"}, {}):
        par = {"q": q, "format": "json", "limit": 5} | sidla | ({"countrycodes": zeme} if zeme else {})
        v = vyber(nominatim(par))
        if v and v[1]:
            nalez = v
            break
        nalez = nalez or v
    return (round(float(nalez[0]["lat"]), 4), round(float(nalez[0]["lon"]), 4), nalez[0]["display_name"], nalez[1]) if nalez else None


def vzdalenost_km(a, b):
    """Vzdušná vzdialenosť dvoch bodov (lat, lon) v km (haversine)."""
    (f1, l1), (f2, l2) = [(math.radians(x), math.radians(y)) for x, y in (a, b)]
    h = math.sin((f2 - f1) / 2) ** 2 + math.cos(f1) * math.cos(f2) * math.sin((l2 - l1) / 2) ** 2
    return 2 * 6371 * math.asin(math.sqrt(h))


def bod(e):
    """(lat, lon) ako čísla, alebo None, ak súradnice chýbajú, nie je ich možné prečítať alebo sú mimo rozsahu."""
    try:
        lat, lon = float(e["lat"]), float(e["lon"])
    except (KeyError, TypeError, ValueError):
        return None
    return (lat, lon) if -90 <= lat <= 90 and -180 <= lon <= 180 else None   # NaN ani nekonečno rozsahom neprejdú


def nejblizsi(name, cache):
    """(km, názov) najbližšieho iného miesta s použiteľnými súradnicami, alebo None."""
    a = bod(cache[name])
    d = [(vzdalenost_km(a, b), n) for n, o in cache.items() if n != name and (b := bod(o))] if a else []
    return min(d) if d else None


def main():
    cache = json.load(open(OUT, encoding="utf-8-sig")) if os.path.exists(OUT) else {}
    if len(sys.argv) > 2 and sys.argv[1] == "pridej":
        name = sys.argv[2]
        if len(name.split()) == 1:
            stem = re.escape(name.split()[0][:5])
        else:
            # Pre viacslovné obce (napr. Moravský Písek, Ostrožská Lhota) skráti každé slovo pre české aj slovenské skloňovanie
            stem = r"\b" + r"\w*\s+".join(re.escape(w[:max(3, len(w) - 2)]) for w in name.split()) + r"\w*"
        stare = cache.get(name, {})
        dotaz = sys.argv[4] if len(sys.argv) > 4 else stare.get("dotaz", f"{name}, Česko")
        cache[name] = dict(stare, re=sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] else stare.get("re", stem),
                           dotaz=dotaz)
        if "lat" in stare and dotaz != stare.get("dotaz", f"{name}, Česko"):   # iný dopyt = oprava miesta → hľadať znova
            for k in ("lat", "lon", "osm"):
                cache[name].pop(k, None)
            print(f"prepočítavam: {name} (nový dopyt „{dotaz}“)")
    pozor, nove = [], []   # varovania sa vypíšu až pod zoznamom
    for name, e in cache.items():
        if "lat" not in e:
            g = geocode(e.get("dotaz") or f"{name}, Česko")
            if not g and e.get("dotaz", f"{name}, Česko") == f"{name}, Česko":   # predvolený dopyt: skús susedné krajiny
                g = geocode(name, "sk,pl,at,de,hu")
                if g:
                    pozor.append(f"MIMO ČESKO: {name} → {g[2][:80]} – skontrolujte, či je to ono")
            if g:
                e["lat"], e["lon"], e["osm"] = g[:3]
                if not g[3]:
                    pozor.append(f"POZOR: nie je obec (není obec) – skontrolujte: {name} → {g[2][:80]}")
                nove.append(name)
            else:
                pozor.append(f"NENÁJDENÉ: {name} – upravte 'dotaz' alebo doplňte lat/lon ručne")
    for name in nove:   # až po celej dávke, nech nezáleží na poradí miest
        n = nejblizsi(name, cache)
        if n and n[0] > VZDALENE_KM:
            pozor.append(f"POZOR: {name} je {n[0]:.0f} km od najbližšieho miesta ({n[1]}) – je to ono? {cache[name]['osm'][:80]}")
    json.dump(cache, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    for n, e in cache.items():
        print(f"{n:28} {str(e.get('lat', '?')):>8} {str(e.get('lon', '?')):>8}  hľadá „{e.get('re')}“  {e.get('osm', '')[:60]}")
    for p in pozor:
        print(p)


if __name__ == "__main__":
    main()
