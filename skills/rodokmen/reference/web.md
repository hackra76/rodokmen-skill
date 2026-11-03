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
| `npm run nasadit` | dáta + build + nahratie na Netlify |

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

## Zverejnenie na Netlify (predvolené, zadarmo)
1. Používateľ si založí účet na netlify.com (stačí prihlásenie cez Google/GitHub).
2. Prihlásenie CLI (otvorí prehliadač): `cd web && npx -y netlify-cli@latest login`.
3. Založenie webu a prepojenie priečinka (interaktívne, raz): `cd web && npx -y netlify-cli@latest sites:create` (zvolí tím a názov → adresa `https://<nazov>.netlify.app`).
4. Nasadenie: `cd web && npm run nasadit`.
5. Overenie: otvor adresu **v anonymnom okne** → musí sa zobraziť rodinná prihlasovacia otázka; po správnej odpovedi samotný web.
   Prihlásenie zabezpečuje Netlify Edge Function `web/netlify/edge-functions/brana.js`.
Ďalšia aktualizácia = len `npm run nasadit`. Vlastnú doménu je možné nastaviť v administrácii Netlify.

## Náhľad webu (Antigravity / VS Code)
Projekt má `.vscode/launch.json` – náhľad webu spustí `npm --prefix web run dev` (port 4321). Dáta sa predtým musia vyexportovať (`cd web && npm run data`). Server beží len na tomto počítači (localhost).

## Vlastný server (pokročilé)
- Docker: `web/Dockerfile` (build Astro → nginx s `nginx.conf` z `nginx.sablona.conf`). Pred buildom image vždy `npm run data`.
- CapRover: `npm run deploy-caprover` (vyžaduje nainštalovaný a prihlásený `caprover` CLI).

## Úpravy vzhľadu
Štýly sú vo `web/src/styles/global.css` (farby v `:root`), rozloženie `web/src/layouts/Base.astro`, stránky `web/src/pages/`.
Farby rodov sú v `tools/export_web.py` (`LINE_COLORS`) a `tools/fan_chart.py` (`BASE`). Upravuj len na želanie používateľa a po úprave skontroluj web na mobile aj počítači.

## Vejár ako plagát
`python -I -X utf8 tools/fan_chart.py vystupy/` → SVG a HTML (a PNG, ak je nainštalovaný Google Chrome alebo Microsoft Edge) na tlač.

## Aktualizácia staršieho projektu
Znova spusti `python -I -X utf8 SKILL_DIR/tools/novy_projekt.py <priečinok projektu>`. Dáta (`data/`, výrezy) zostanú, `tools/` sa prepíše a zmenené súbory vo `web/` sa zálohujú do `pracovni/zaloha_web_<datum>/`. Následne vo `web/` spusti `npm install` a `npm run data`.
