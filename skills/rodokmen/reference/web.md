# Rodinný web – stavba, nastavenie, zverejnenie

Web je statický (Astro + vyhľadávanie Pagefind), dáta preberá z `data/` cez `tools/export_web.py`.
Stránky: úvod (štatistiky, zaujímavosti, mapa, rody, vejár), príbeh, zaujímavosti, rody, stránka rodu,
mapa (OpenStreetMap), vejár cez celú obrazovku s vyhľadávaním, zoznam predkov, zápisy (s výrezom, rámčekom, prepisom
a prekladom), stránka osoby, rodiny, „Čo hľadáme“, výskumný denník, vyhľadávanie.

## Príkazy (v priečinku `web/`)
| príkaz | čo robí |
|---|---|
| `npm install` | raz na začiatku (stiahne knižnice, ~1 minúta) |
| `npm run data` | prevedie dáta do webu (vždy po zmene dát; funkčný Python 3 vyhľadá `scripts/data.mjs`) |
| `npm run build` | zostaví web do `dist/` |
| `npm run nahled` | dáta + build + náhľad na http://localhost:4321 (Ctrl+C ukončí) |
| `npm run dev` | vývojový režim pri úpravách vzhľadu |
| `npm run nasadit-cloudflare` | dáta + build + nahratie na Cloudflare Workers (odporúčané) |
| `npm run nasadit` | dáta + build + nahratie na Netlify (alternatíva) |
| `npm run overit` | kontrola nasadeného webu bez prihlásenia (rodinná otázka × ochrana tímu Netlify / Cloudflare) |

Náhľad spúšťaj na pozadí a používateľovi pošli odkaz. Vzhľad si over sám (snímka obrazovky cez prehliadač, ak je k dispozícii).

## `data/web.json`
```json
{
 "nazev": "Rodokmeň Dvorských",
 "popis": "Popis pre vyhľadávače a zdieľanie (web je noindex).",
 "zapati": "Dohľadané v digitalizovaných matrikách a archívoch",
 "kontakt": {"jmeno": "Radovanovi", "email": "radovan@example.com"},
 "prihlaseni": {"uvod": "Tento web je určený len pre rodinu.", "otazka": "Ako sa volal pes u starej mamy?", "odpoved": "Dunčo"},
 "uvod": {"nadpis": "Príbeh našich predkov", "odstavce": ["2–3 vety, ktoré zaujmú"], "foto": "kluc_obrazka_vo_vyrezoch", "foto_popis": "…"},
 "pribeh": {"menu": "Príbeh Dvorských", "rod": 8, "tlacitko": "Prečítať príbeh Dvorských"},
 "zajimavosti_na_uvodu": [{"nadpis": "Najstarší predok", "text": "Kováč Ján, okolo 1825."}]
}
```
- `kontakt.jmeno` je v datíve („Napíšte Radovanovi na …“).
- **Prihlásenie:** otázka, na ktorú pozná odpoveď len rodina (nie ľahko dohľadateľná na sociálnych sieťach).
  Odpoveď sa porovnáva bez diakritiky a veľkých písmen. Na serveri aj v cookie prehliadača je len jej odtlačok (SHA-256),
  samotná odpoveď sa nikde neukladá. Bez odpovede nasadenie (`npm run nasadit`, `deploy-caprover`)
  skončí chybou; otvorený web je možný len výslovne cez `"otevreny": true` v `prihlaseni`.
- `uvod.foto` = kľúč obrázka vo `vyrezy/` (ulož cez `vyrez.py`).
- `pribeh`: `menu` a `tlacitko` pomenuj podľa hlavného rodu („Príbeh Dvorských“), `rod` = číslo rodu (8–15).
- `citlive_schvaleno`: zoznam úryvkov textu, ktoré používateľ na webe schválil – `kontrola.py` ich potom nehlási ako `CITLIVÉ`.

## Zverejnenie na Cloudflare Workers (odporúčané, zadarmo)
Adresa `https://rodokmen.<subdoména>.workers.dev` (subdoménu si zvolí používateľ, je spoločná pre všetky jeho projekty
na Cloudflare, napr. `dvorski`). Zadarmo, bez kreditov na nasadenie (na Netlify ich je len cca 20 mesačne) a s limitom
100 000 zobrazení denne.
1. Používateľ si založí bezplatný účet na dash.cloudflare.com (stačí e-mail a heslo) – urobí sám.
2. Zvoľte názov subdomény účtu:
   - Spýtaj sa používateľa na názov (napr. priezvisko rodiny, „dvorski“), alebo použi rodinu z webu.
   - Over, či je voľný: `node scripts/nasadit_cloudflare.mjs --volno dvorski` (možno zadať aj viac variantov naraz:
     `--volno dvorski rod-dvorskych dvorsky-rodokmen`).
   - Voľný názov zapíšte do `data/web.json` ako `cloudflare: {"nazev": "dvorski"}` a spusti `npm run data`.
3. Prihlásenie CLI: daj používateľovi príkaz `! cd web && npx wrangler login`. Otvorí sa prehliadač Cloudflare, kde klikne
   na „Allow“ (oprávnenie pre Workers). Príkaz beží v termináli ďalej a po schválení sám skončí.
   Pozor: ak už používateľ na Cloudflare subdoménu má z minulosti, Cloudflare ju nezmení a názov z `web.json` sa nepoužije –
   adresu potom povie až nasadenie.
4. Nasadenie: `cd web && npm run nasadit-cloudflare` (spusti sám). Vypíše adresu a sám spustí kontrolu
   `scripts/overit.mjs`. Pri novej adrese kontrola počká, kým sa rozšíri (pár minút); ak ju počítač ešte nepozná, povie to
   a skončí bez chyby – potom over neskôr `npm run overit`. Do tej doby adresu v prehliadači neotváraj: počítač alebo
   router by si zapamätal, že neexistuje, a až 30 minút by ju nevidel (inde, napr. v telefóne na mobilných dátach,
   web už funguje). Povedz to používateľovi, nech sa nezľakne.
5. Overenie aj v anonymnom okne: rodinná otázka, po správnej odpovedi web.
   Bránu (`web/cloudflare/worker.js`) a `web/wrangler.jsonc` vyrába export – ručne neupravovať. Brána musí bežať
   pred každým súborom (`run_worker_first`), inak by sa stránky a fotky dali stiahnuť bez prihlásenia.
Ďalšia aktualizácia = len `npm run nasadit-cloudflare`.

**Úskalia:**
- „You need to verify your email address to use Workers“ (403) pri novom účte: Cloudflare vyžaduje overený e-mail – overenie
  v dashboarde (pruh hore / My Profile), potvrdiť odkaz v pošte, nasadiť znova (subdoména už zostane vytvorená).
- Safari s blokátorom obsahu ukáže namiesto overovacej stránky Cloudflare prázdnu stránku 403 – skús iný prehliadač
  (kontrola to spozná).
- Nepoužívaj `wrangler pages project create/deploy` ani „Import a repository“ v administrácii – založí iný typ projektu,
  prípadne sám prepíše `astro.config`/`package.json`. Nasadzuj len cez `npm run nasadit-cloudflare`.
- V cloudovom prostredí bez interaktívneho prehliadača použi Netlify (`login --request`).

## Zverejnenie na Netlify (druhá možnosť)
Pre používateľov, ktorí už web na Netlify majú. Bezplatný účet vystačí len na cca 20 nasadení mesačne (pozri kredity nižšie).
1. Používateľ si založí účet na netlify.com (stačí prihlásenie cez Google/GitHub).
2. Prihlásenie CLI (otvorí prehliadač): `cd web && npx -y netlify-cli@latest login`.
   Keď `!` nejde (cloudové prostredie): `npx -y netlify-cli@latest login --request "Rodokmen"` vypíše odkaz a číslo.
3. Založenie webu a prepojenie priečinka (interaktívne, raz): `cd web && npx -y netlify-cli@latest sites:create` (zvolí tím a názov → adresa `https://<nazov>.netlify.app`).
   **Nový web býva predvolene „Private“ (ochrana tímu)** – rodina by namiesto rodinnej otázky videla prihlásenie k Netlify.
   Vypnúť sa dá so súhlasom používateľa príkazom:
   `npx -y netlify-cli@latest api updateSite --data '{"site_id":"<siteId z web/.netlify/state.json>","body":{"sso_login":false}}'`
   (v administrácii: Project configuration → Access & security → Visitor access → Project visibility → Edit visibility → Public).
4. Nasadenie: `cd web && npm run nasadit`. Na konci sa automaticky spustí kontrola `scripts/overit.mjs` (ručne `npm run overit`).
5. Overenie: otvor adresu **v anonymnom okne** → musí sa zobraziť rodinná prihlasovacia otázka; po správnej odpovedi samotný web.
   Prihlásenie zabezpečuje Netlify Edge Function `web/netlify/edge-functions/brana.js`.
Ďalšia aktualizácia = len `npm run nasadit`. Vlastnú doménu je možné nastaviť v administrácii Netlify.

**Kredity Netlify (bezplatný účet):** 300 kreditov mesačne, neprenášajú sa. Každé nasadenie stojí 15 (nepodarené nič),
1 GB prenosu 20 → cca 20 nasadení mesačne, alebo menej, ak rodina sťahuje veľké výrezy zo `zdroje/`. Po vyčerpaní
Netlify nasadzovanie pozastaví a `npm run nasadit` skončí „Forbidden“ – to sú vyčerpané kredity, nie chyba webu
(stav kreditov je v administrácii Netlify). Preto nasadzuj na pokyn používateľa alebo raz na konci sedenia, medzitým len
náhľad. Povedz to používateľovi hneď pri prvom zverejnení.

**Pozor:** „Netlify Drop“ (pretiahnutie priečinka v prehliadači) nepodporuje Edge Functions → web by bol bez prihlásenia. Nepoužívať.

## Náhľad webu (Antigravity / VS Code)
Projekt má `.vscode/launch.json` – náhľad webu spustí `npm --prefix web run dev` (port 4321). Dáta sa predtým musia vyexportovať (`cd web && npm run data`). Server beží len na tomto počítači (localhost).

## Vlastný server (pokročilé)
- Docker: `web/Dockerfile` (build Astro → nginx s `nginx.conf` z `nginx.sablona.conf`). Pred buildom image vždy `npm run data`.
  Bez Node.js na počítači: `python -I -X utf8 tools/export_web.py --nasazeni`, potom `docker build` vo `web/` (Astro sa zostaví v image).
- Prestavba necháva na disku starý image bez tagu (stovky MB). Po `docker build` zmaž len starý image tohto webu:
  ```bash
  OLD=$(docker images -q rodokmen-web:latest); docker build -t rodokmen-web .
  docker rm -f rodokmen-web; docker run -d --name rodokmen-web --restart unless-stopped -p 8080:80 rodokmen-web
  [ -n "$OLD" ] && [ "$OLD" != "$(docker images -q rodokmen-web:latest)" ] && docker image rm "$OLD"
  ```
  `docker system/image/builder prune` nepoužívaj – platí pre celý server a zmaže aj veci iných projektov.
- Web počíta s behom v koreni domény (odkazy, cookie prihlásenia aj hľadanie od `/`) – za reverse proxy mu daj
  subdoménu (`rodokmen.server.sk`), nie podadresár (`server.sk/rodokmen/`).
- **Iba cez https** (reverse proxy s Let's Encrypt, DSM, CapRover to dokáže): prihlasovacia stránka počíta odtlačok odpovede
  v prehliadači a ten to cez obyčajné http (mimo localhost) nedovolí – prihlásenie by nefungovalo.
- CapRover: `npm run deploy-caprover` (vyžaduje nainštalovaný a prihlásený `caprover` CLI).

## Úpravy vzhľadu
Štýly sú vo `web/src/styles/global.css` (farby v `:root`), rozloženie `web/src/layouts/Base.astro`, stránky `web/src/pages/`.
Farby rodov sú v `tools/export_web.py` (`LINE_COLORS`) a `tools/fan_chart.py` (`BASE`). Upravuj len na želanie používateľa a po úprave skontroluj web na mobile aj počítači.

## Vejár ako plagát
`python -I -X utf8 tools/fan_chart.py vystupy/` → SVG a HTML (a PNG, ak je nainštalovaný Google Chrome alebo Microsoft Edge) na tlač.

## Aktualizácia staršieho projektu
Znova spusti `python -I -X utf8 SKILL_DIR/tools/novy_projekt.py <priečinok projektu>`. Dáta (`data/`, výrezy) zostanú. Projekt má
v `.skill_sablona/` kópiu šablóny `web/` a `tools/`, z ktorej vznikol (commitovať s projektom), a skript podľa nej rozhodne
o každom súbore a vypíše zoznam:
- **Přepsáno**: súbor projekt neupravoval, nahradila ho nová verzia.
- **Ponecháno**: vlastná úprava, šablóna sa nezmenila.
- **Sloučeno**: zmenila sa úprava aj šablóna, každá inde; `git merge-file` ich spojil. Over, že súbor dáva zmysel.
- **Ke kontrole**: úprava aj šablóna zmenili rovnaké miesta, chýba `git`, súbor pridal projekt aj nová šablóna, alebo ho
  projekt zmazal a šablóna zmenila. Súbor zostal, ako bol; nová verzia je v `pracovni/zaloha_<datum>/nova_sablona/`
  (pri konflikte zlúčenia, ak je `git`, vedľa aj návrh so značkami `<<<<<<<` ako `.konflikt`). Prevezmi zmeny šablóny
  ručne a potom spusti `python -I -X utf8 SKILL_DIR/tools/novy_projekt.py <priečinok projektu> --vyreseno web/src/…` (voľbu možno
  opakovať). Ako základ uloží presne ten návrh, ktorý je v zálohe (zapamätaný v `.skill_sablona/cekajici.json`),
  takže neskoršie zmeny šablóny prídu pri ďalšej aktualizácii; súbor v projekte nezmení.
- **Smazáno v projektu**: súbor projekt zmazal a šablóna ho nezmenila, zostane zmazaný.
- **Šablona už nemá**: súbor zostal (skript nič nemaže) a hlási sa pri každej aktualizácii. Skontroluj, či ho web
  ešte potrebuje; prípadne ho zmaž ručne a spusti `--vyreseno` s jeho cestou.
- **Přepsáno, původní verze v záloze**: projekt zo staršej verzie bez `.skill_sablona/`. Upravené súbory nahradila nová
  verzia a pôvodné sú v `pracovni/zaloha_<datum>/puvodni/`; vlastné úpravy z nich prevezmi.

`web/package-lock.json` (mení ho `npm install`) sa nezlučuje: ak ho zmenila šablóna, vezme sa nový a starý ide do zálohy.
Následne vo `web/` spusti `npm install` a `npm run data`.
