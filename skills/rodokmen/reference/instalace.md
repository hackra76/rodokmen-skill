# Príprava počítača a projektu (Fáza 0)

Čítaj pri zakladaní projektu alebo keď niektorý nástroj chýba či padá pri inštalácii.

## Nástroje
Skontroluj: `python --version` (≥ 3.9; na macOS/Linuxe `python3 --version`), `node --version` (≥ 20), `magick -version` (ImageMagick 7; ak je len verzia 6 s príkazom `convert`, nástroje ju mimo Windows použijú samy), `git --version`.
Čo chýba, pomôž nainštalovať. Inštaláciu systémových vecí nechaj používateľa potvrdiť; interaktívne príkazy mu daj s predponou `!`, nech ich spustí sám.
- **macOS:** Homebrew `brew install python node imagemagick git`.
- **Windows:** winget alebo inštalátory z python.org, nodejs.org, imagemagick.org. **winget vždy s plnými prepínačmi**, inak spadne na otázke k zdroju msstore („Error reading input in prompt“):
  `winget install --id <balík> --source winget --accept-source-agreements --accept-package-agreements`
  (balíky `Python.Python.3.12` + `--scope user`, `OpenJS.NodeJS.LTS`, `ImageMagick.ImageMagick`, `Git.Git`).

## macOS: https a certifikáty
Over: `python3 -I -c "import urllib.request; urllib.request.urlopen('https://aron.vychodoceskearchivy.cz')"`.
Python z python.org po inštalácii nemá certifikáty (`CERTIFICATE_VERIFY_FAILED`) – nech používateľ spustí `Install Certificates.command` v priečinku `/Applications/Python 3.x/`, alebo použi Python z Homebrew (`/opt/homebrew/bin/python3`).

## Windows
- **Python:** `python3` tam býva len nefunkčný alias z Microsoft Store („Python nebol nájdený“) – skontroluj `python --version` (prípadne `py -3 --version`) a vo všetkých príkazoch skillu namiesto `python3 -I` používaj `python -I -X utf8` (ak funguje len launcher, tak `py -3 -I -X utf8`). `-I` ignoruje premennú `PYTHONUTF8`; bez `-X utf8` je výstup do rúry alebo súboru v cp1250 – diakritika sa pokazí a niektoré nástroje spadnú na znakoch ako „→“.
- Skontroluj, **ktorý** Python to je (`where python` / `Get-Command python`) – môže byť pribalený k inému programu (Inkscape, GIMP…) a nemať certifikáty. Over https: `python -I -c "import urllib.request; urllib.request.urlopen('https://aron.vychodoceskearchivy.cz')"`.
  Pri `CERTIFICATE_VERIFY_FAILED` nainštaluj bežný Python (winget vyššie) a volaj ho plnou cestou `"$LOCALAPPDATA/Programs/Python/Python312/python.exe"` (do PATH sa dostane až po reštarte Antigravity / terminálu).
- **ImageMagick:** `winget install --id ImageMagick.ImageMagick --source winget --accept-source-agreements --accept-package-agreements`; do PATH sa dostane až po reštarte Antigravity / terminálu (do tej doby pred príkazmi prípadne doplň do `PATH` presný priečinok z `C:\Program Files\ImageMagick-7…`). **Nikdy `convert`** (systémový nástroj Windows), vždy `magick`.
- Skripty `.sh` spúšťaj cez Git Bash (`bash tools/…`). Dlhšie jednorazové skripty v Pythone nepíš ako heredoc (`python - <<EOF`), v Git Bashi občas spadnú na „unexpected EOF“ – zapíš ich do súboru v `pracovni/` a spusti.
- V PowerShelli dávaj argumenty obsahujúce čiarky (napr. súradnice výrezu `"x0,y0,x1,y1"`) do úvodzoviek, inak ich PowerShell rozdelí na samostatné argumenty.
- Tieto pravidlá zapíš hneď po založení projektu do jeho `AGENTS.md` (prípadne aj `CLAUDE.md`), nech platia aj nabudúce, a daj je do zadania pomocníkom (ďalšie úskalia pri práci: `matriky.md` → Technické úskalia).

## Prehliadač pre agenta
Potrebuješ ho pre archívy a portály, ktoré sťahovacie nástroje nepúšťajú (SOA Praha, MZA Brno, SOA Třeboň, ZA Opava, hľadanie v SOA Litoměřice, FamilySearch za prihlásením).
- V **Antigravity** použi vstavaný prehliadač (`/browser`, browser plugin) alebo MCP server Playwright / Chrome DevTools.
- V **Claude Code**, ak chýbajú nástroje `mcp__…playwright…`, ponúkni doplnok Playwright: `/plugin install playwright@claude-plugins-official` (alebo Claude in Chrome `/chrome`); postupy v `portaly.md` sú odskúšané najmä s Playwrightom (snímka obrazovky do súboru).
- Bez prehliadača nech používateľ posiela snímky obrazovky sám (ulož do `pracovni/`).

## Založenie projektu
1. Spýtaj sa, kde má projekt byť (navrhni `~/Rodokmen` alebo priečinok v scratchi), a založ ho: `python -I -X utf8 SKILL_DIR/tools/novy_projekt.py <priečinok>`.
   Ak chce používateľ najprv vidieť, ako web vyzerá, založ vedľa ukážku: `… novy_projekt.py ~/Rodokmen-ukazka --ukazka`, potom `cd web && npm install && npm run nahled` a pošli mu odkaz http://localhost:4321.
2. Spýtaj sa, či zapnúť **strážcu siete** (`… novy_projekt.py <priečinok> --hlidac`, vypnutie `--bez-hlidace`).
   Vysvetli jednou vetou: archívy blokujú IP adresu po sérii rýchlych dopytov. Strážca je malý skript v projektu (`tools/hlidac_site.py`, hook v `hooks.json`, `.agents/hooks.json` a `.claude/settings.json`), ktorý pred každým príkazom skontroluje, že sťahovanie ide cez brzdu, a inak ho zamietne. Sám nič nesťahuje. Bez neho platia pravidlá brzdy v `AGENTS.md` / `CLAUDE.md` a zákaz priameho `curl`/`wget`.
3. V projekte urob `git init` a prvé uloženie (git = história zmien, ak by sa niečo pokazilo). Odporúčaj pokračovať **z tohto priečinka** (súbory `AGENTS.md` a `CLAUDE.md` v ňom zaistia, že nabudúce nadviažeš).
4. Vyplň v `data/STAV.md` sekciu „Pre koho“ a v `data/web.json` názov webu („Rodokmeň Dvorských“), hneď ako poznáš priezvisko východiskovej osoby (šablóna je prázdna).
