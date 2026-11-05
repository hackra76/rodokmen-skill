# Co je nového

Změny ve skillu rodokmen, nejnovější verze nahoře. Každá verze má na GitHubu i
[vydání (Releases)](https://github.com/sarsonj/rodokmen-skill/releases) – kdo chce dostávat upozornění,
dá v repozitáři **Watch → Custom → Releases**.

Projekt založený starší verzí Claude sám nabídne aktualizovat (pozná to podle souboru `VERZE`).

## 0.8.1 – 5. 11. 2026

Rýchly ARON celým skenom, kontrola integrity cache, geokódovanie sídiel a 3-cestná aktualizácia projektu.

**Nové**
- **Bezpečná 3-cestná aktualizácia projektu (`tools/novy_projekt.py`):** Nový mechanizmus aktualizácie založený na uloženej šablóne (`.skill_sablona/`) a `git merge-file`. Automaticky zlučuje zmeny v šablóne a vlastné úpravy v projekte, uchováva bezpečné zálohy (`pracovni/zaloha_<datum>/`) a umožňuje interaktívne riešenie konfliktov (`--vyreseno`). Plne zachováva generovanie Antigravity konfigurácie (`hooks.json`, `.agents/hooks.json`, `AGENTS.md`, `.vscode/launch.json`).
- **Overovanie integrity obrázkov v cache (`tools/cache.py`):** Cache ukladá iba kompletné a nepoškodené obrázky (validácia koncových značiek pre JPEG, PNG, GIF, WebP a zhoda `Content-Length`). Prerušené alebo skrátené sťahovania sa automaticky zahadzujú a opätovne sťahujú.
- **Rýchle sťahovanie ARON jedným dopytom (`tools/aron_img.py`):** Sťahovanie celého skenu v plnej kvalite jedinou požiadavkou cez `referencedfiles` (ekvivalent tlačidla „Stiahnuť“ v ARONe), lokálne zmenšenie a výrez z disku. Dlaždicové sťahovanie zostáva len ako záložný variant.
- **Geokódovanie sídiel a detekcia vzdialených obcí (`tools/mista.py`):** Nominatim vyhľadáva prednostne sídla (`featuretype=settlement`). Upozorňuje, ak výsledok nie je obec, a varuje, ak je novo pridaná obec vzdialená viac ako 50 km od ostatných miest v rodokmeni (ochrana pred zámenou obcí s rovnakým názvom).
- **Rozšírená kontrola konzistencie (`tools/kontrola.py`):** Kontrola partnerov pri sobášoch (overenie mena partnera na susednom čísle) a overenie čísel domov vo faktoch (`doc`) oproti prepisom a zhrnutiam v citovaných zápisoch s podporou viacjazyčných názvov mesiacov (latinské, nemecké, slovenské, české).

**Opravy a vylepšenia**
- **Odstránenie `trebon.py`:** Nástroj bol natrvalo odstránený na žiadosť SOA Třeboň; matriky Třebone sa prehliadajú výhradne v prehliadači.
- **PowerShell a argumenty:** Robustné spracovanie ciest a výrezov s čiarkami v prostredí PowerShell na Windows (`vyrez.py`, `overit.py`, `ramecek.py`, `aron_img.py`).
- **Skloňovanie obcí:** Podpora regulárnych výrazov pre viacslovné názvy obcí a miest.
- **Testovacie sady:** Doplnené komplexné regresné testy pre aktualizáciu (`test_aktualizace.py`), integritu medzipamäte (`test_mezipamet.py`), geokódovanie (`test_mista.py`) a čísla domov (`test_cisla.py`).

## 0.8.0 – 4. 11. 2026

Zdieľaná disková medzipamäť snímok, mapa knihy, aktualizácie archívov a opravy nástrojov.

**Nové**
- **Zdieľaná disková medzipamäť snímok (`tools/cache.py`):** Spoločná lokálna cache pre stiahnuté a zosnímané strany (`~/.cache/rodokmen_snimky/`, do 5 GB, LRU). Umožňuje opakované náhľady a výrezy bez opätovného zaťažovania archívnych serverov.
- **Knihy radené po obciach a mapa knihy (`tools/mapa_knihy.py`):** Vizualizácia rozdelenia knihy na dediny a stĺpcová montáž záhlaví pre rýchlu orientáciu v matrikách členených podľa dedín.
- **Manuálna stopka archívu v brzde:** Príkaz `slusne.py zastav <web|adresa>` pre okamžité pozastavenie požiadaviek pri blokovaní či výpadku v prehliadači.
- **Dokumentácia a Wiki:** Rozšírená metodika pre knihy po obciach, zmiešané manželstvá (náboženstvo detí), podrobné postupy pre SOA Praha (eBadatelna), SOA Třeboň a MZA Brno v prehliadači.

**Vylepšenia a opravy**
- **SOA Praha (eBadatelna):** Prechod na prácu v prehliadači s automatickým ukladaním snímok do diskovej cache (`cache.py uloz` a `cache.py najdi`) v súlade s pravidlami archívu.
- **SOA Plzeň (Porta fontium):** Plná integrácia s diskovou cache (`cache.py`) pri sťahovaní snímok a orezov.
- **SOA Zámrsk (ARON):** Paralelné sťahovanie dlaždíc (4 vlákna) a robustné opakovanie pri sieťových chybách.
- **Vejár predkov (`fan_chart.py`):** Správne zobrazenie straty predkov (pedigree collapse) na oboch vetvách rodokmeňa a ošetrenie timeoutu pri generovaní SVG.
- **Kontrola rodokmeňa (`kontrola.py`):** Detekcia chýbajúcich `LINES` v rodokmeni, kontrola GPS súradníc v `data/mista.json` a filtrácia falošných hlásení ("nie sú dlhy").
- **Import GEDCOM (`ged_import.py`):** Oprava spájania viacbajtových UTF-8 znakov rozdelených na hrane `CONC` riadkov (z exportov MyHeritage).
- **Policajné prihlášky (`policie_prihlasky.py`):** Prísnejšie overenie zhodnosti hľadaného mena a priezviska vo výsledkoch.
- **Strážca siete (`hlidac_site.py`):** Vylepšená detekcia heredoc zápisov pri zachovaní spätnej kompatibility s Antigravity `run_command` a PowerShellom.

## 0.7.0 – 3. 11. 2026

Port pre Google Antigravity so zachovaním plnej podpory Claude Code, slovenský preklad a nová dokumentácia.

**Nové**
- **Podpora pre Google Antigravity:** Pridaný manifest `plugin.json` v koreni repozitára a pravidlá `AGENTS.md`.
- **Slovenská lokalizácia:** Kompletný preklad skillu, metodických návodov, šablóny rodinného webu (Astro) a nástrojov.
- **Slovenské archívy a pramene:** Rozšírená metodika pre FamilySearch (cirkevné knihy do 1895, sčítanie ľudu 1869), štátne archívy a databázy cintorínov na Slovensku.
- **Strážca siete (lifecycle hooks):** `hlidac_site.py` a `novy_projekt.py` plne podporujú systém háčikov v Antigravity (`hooks.json` a udalosť `PreToolUse` pre `run_command`).
- **Nové projekty:** Šablóna projektu vytvára `AGENTS.md`, `hooks.json` a `.vscode/launch.json` pre náhľad webu.
- **Odporúčania modelov:** Aktualizované odporúčania pre Antigravity (Gemini Pro pre hlavný model, Gemini Flash pre pomocníkov).
- **GitHub Wiki & šablóny:** Pripravená kompletná wiki dokumentácia (`wiki/`), synchronizačný skript (`tools/publish_wiki.py`), issue šablóny a GitHub Actions CI.
- **Testy:** Regresná sada `tests/brzda/test_hlidac.py` rozšírená o testy Antigravity formátu (100% úspešnosť).

## 0.6.3 – 3. 11. 2026

Opravy po hlášeních z praxe.

**Opravy**
- Brzda: `slusne.py curl` se bez `-A` představí stejně jako nástroje. Porta fontium výchozí „curl“ odmítá (403)
  a brzda to brala jako zablokování archivu.
- SOA Litoměřice změnil koncem října cesty k obrázkům – `soal_zoomify.py` je potřeba dávat celou adresu
  obrázku (návod upraven).

**Návody**
- Příprava (Fáze 0): na macOS ověřit https – Python z python.org po instalaci nemá certifikáty.
- Prohlížeč pro Clauda: jak nainstalovat doplněk Playwright (README a příprava).
- Archivní mapy ČÚZK na nové adrese ags.cuzk.gov.cz/archiv.

Děkuji všem, kdo poslali hlášení e-mailem.

## 0.6.2 – 2. 11. 2026

SOA Třeboň jen přes prohlížeč.

**Nové**
- SOA Třeboň od 2. 11. odmítá stahovací nástroje (`trebon.py` dostává HTTP 403). Skill proto čte jihočeské
  matriky jen v prohlížeči archivu: přiblíží zápis a uloží snímek obrazovky, výřez pak jako u jiných archivů.
  `trebon.py` je zatím vypnutý a brzda skripty na digi.ceskearchivy.cz zastaví.

**Návody**
- `portaly.md`: SOA Třeboň a MZA Brno – vyzkoušené úryvky pro přiblížení zápisu v prohlížeči archivu,
  u Třeboně i trvalý odkaz přímo na zápis.

Kdo pracoval s `trebon.py`: Claude teď místo něj otevře prohlížeč (Playwright). Bez prohlížeče pošlete
snímky obrazovky sami. Děkuji všem, kdo na blokaci upozornili e-mailem.

## 0.6.1 – 2. 11. 2026

MZA Brno jen přes prohlížeč, opravy brzdy a hlídače na Windows.

**Nové**
- MZA Brno (Acta Publica) od 2. 11. blokuje stahovací skripty. Skill proto čte snímky jen v jejich prohlížeči:
  přiblíží zápis a uloží snímek obrazovky (Playwright), výřez pak jako u jiných archivů. Bez prohlížeče pošle
  snímky obrazovky uživatel sám. Skriptem jde jen hledání knih, ostatní adresy MZA brzda zastaví (#64).
- Brzda: když archiv odmítne podruhé za 24 hodin, stopka trvá 2 hodiny, potřetí 8 hodin (#53).
- Brzda hlídá i `curl`, `python` a `bash` spuštěné z Pythonu (#53).

**Opravy**
- Windows: hlídač sítě bez Git for Windows zamítal každý příkaz. Nově se spouští bez shellu, takže funguje
  v Git Bashi i v PowerShellu, i v projektu sdíleném přes OneDrive.
- Windows: brzda nepoznala u `curl` odmítnutí archivu (429/503) a po zablokování poslala další dotaz;
  `slusne.py bash` spuštěný z PowerShellu nebrzdil `curl` uvnitř skriptu (#53).
- Windows se Smart App Control: když `curl` z Gitu nejde spustit, brzda použije systémový `curl.exe`.
- Hlášky brzdy a hlídače na Windows bez rozsypané češtiny.
- Hlídač pozná i `import json, urllib.request`, `python -c "…"`, `bash -c "curl …"` a nástroj Monitor.

**Návody**
- `portaly.md`: MZA – postup v prohlížeči a tipy, jak listovat méně (části matriky, rejstříky, strana → snímek).
- `portaly.md`: židovské matriky Národního archivu ve VadeMeCum místo badatelna.eu (#54).
- README: jak aktualizovat skill (#58).

Kdo má na Windows zapnutý hlídač a Claude mu zamítá každý příkaz: nechte Claude aktualizovat projekt
(nabídne to sám), nebo hlídač vypněte příkazem `novy_projekt.py <projekt> --bez-hlidace`.

Opravy pro Windows a testy připravil svamberk (#53), blokaci MZA nahlásil HonzinaThor (#64).
Děkuji i všem, kdo e-mailem poslali zkušenosti z Windows a nápady k MZA.

## 0.6.0 – 2. 11. 2026

Brzda proti zablokování archivem.

**Nové**
- Brzda `tools/slusne.py`: společný limit dotazů pro každý archiv a všechny procesy na počítači
  (stránky 1 za 2 s, obrázky 10 za s). Když archiv dá najevo, že ho zatěžujeme, stahování se na 30 minut
  zastaví. Nástroje ji mají samy, vlastní skripty a `curl` se spouštějí přes ni (#45).
- Volitelný hlídač sítě (`novy_projekt.py --hlidac`): zamítne příkazy, které by šly na archiv mimo brzdu.
- Projekt má v `.claude/settings.json` zakázané přímé `curl` a `wget`.

**Opravy**
- Úvodní stránka webu s prázdným úvodem už nevypíše „0“.
- `kontrola.py`: žádné falešné poplachy u obce Petrovice nebo kontaktu „Petrovi“, zápisy z hypotéz
  se počítají jako citované, chybějící přihlašovací otázku hlídá až nasazení.
- Legenda vějíře neusekne popis rodu na „čp.“, „roz.“ a podobně.
- `novy_projekt.py --help` už nezaloží složku „--help“.

**Návody**
- SKILL.md: „Šetrně k archivům“ – síť jen přes brzdu, i u pomocníků, na jeden archiv nejvýš jeden pomocník.

Brzdu navrhl MarekLu (#45). Děkuji i všem, kdo poslali vlastní vyzkoušená řešení a zkušenosti s blokacemi.

## 0.5.0 – 24. 10. 2026

Zpětná vazba uživatelů (přes čtyřicet podnětů od šesti lidí).

**Nové**
- `zapis.py` – změní jednu položku dat a formát souboru nechá beze změny.
- `kontrola.py`: schválené citlivé zmínky (`citlive_schvaleno` ve `web.json`) a hranice 100 let.
- `mista.py` zkusí i sousední země.

**Opravy**
- Bezpečnost: otevřené přesměrování po přihlášení na webu.
- Konce řádků LF ve všech zápisech nástrojů.
- `soal_zoomify` bez `montage` (padal na ImageMagick 7.1.2), 4 vlákna, úklid dočasné složky.
- ImageMagick 6 (`convert`) mimo Windows.
- `vyrez` a `overit` odmítnou souřadnice v pixelech.
- `aron_search` při chybě opakuje dotaz.
- Mapa na webu přes celou šířku.

**Návody**
- ZA Opava (přepsáno), MZA Acta Publica, Geneteka API, rejstříky v Matricule.
- Druhopisy, roční výtahy, obce mezi farami, nejisté datum, chybějící nejmladší svazky.
- Přihlášení k Netlify v agentovi, oběti 2. světové války.

## 0.4.7 – 22. 10. 2026

**Opravy**
- Roky „– před 1888“ / „po 1921“ ve vějíři i na webu.
- `policie_prihlasky.py`: karta i pro pořadí nad 20.
- Konce řádků LF (`.gitattributes`, `novy_projekt` převede `.sh`).

**Návody**
- Příbuzenství doslova, datum sňatku ve křtu, špatný měsíc v oddacím zápisu, posun snímek–strana, Windows.

## 0.4.6 – 22. 10. 2026

**Opravy**
- UTF-8 výstup ve všech nástrojích (#11).
- Certifikát Porta fontium.
- `ged_import` čte Brother's Keeper (ANSI, česká data).
- `trebon`: hláška pro neznámá místa.

**Návody**
- winget, kontrola Pythonu, rejstřík místo chybějící matriky, pomocníci, Geneteka.

## 0.4.5 – 22. 10. 2026

**Opravy**
- `trebon.py`: místo bez diakritiky a mezer.
- `soal_zoomify` stahuje jen ze serverů archivů.
- `ramecek` ověří ImageMagick před zápisem.
- `.claude/launch.json` pro náhled webu v Claude desktop.

**Návody**
- Netlify Team protection, civilní matriky v Třeboni, posun stran v eBadatelně, víceznačné obce, heredoc ve Windows.

## 0.4.4 – 22. 10. 2026

**Opravy**
- Kontrola ImageMagicku před stahováním.
- `aron_search`: víc slov a řazení podle fary.
- Kontrola nefunkčních odkazů v textech webu.
- ZA Opava přes `soal_zoomify`.

**Návody**
- Rejstříky podle německého pravopisu.

## 0.4.3 – 21. 10. 2026

**Opravy**
- `overit.py` bere souřadnice jako zlomky.

**Návody**
- Rejstříky o pár stran vedle, evangelické a židovské matriky, údaje z cizích stromů ověřit jménem.

## 0.4.2 – 21. 10. 2026

**Nové**
- Claude sám nabídne aktualizaci projektu (verze skillu v `VERZE`, projekt si ji pamatuje v `.skill_verze`).
- Aktualizace projektu přepíše i změněné šablony webu (se zálohou do `pracovni/`); export odmítne starou šablonu přihlášení (#9).

**Opravy**
- `ftb_export`: vazby v rodinách jen na osoby, které jsou v exportu (#4).
- Porta fontium: odkaz spárovaný přímo se snímkem, kontrola výřezu, čekání po HTTP 429 a pauza mezi požadavky (#5).

## 0.4.1 – 21. 10. 2026

**Nové**
- Vedlejší nálezy se nezahazují (jedna věta v deníku).
- Hřbitovy jako doplňující otázka k úmrtí; formulace k hrobům bez návrhů na otevírání.
- FamilySearch: snímky filmů a limit 429.

**Bezpečnost** (podle externí analýzy)
- Nasazení bez přihlašovací otázky skončí chybou, v cookie jen otisk odpovědi.
- Escapování v mapě, v tooltipu mapy a v legendě vějíře.
- Cache ARON ve složce projektu, `novy_projekt` nepíše přes symlinky.

## 0.4.0 – 21. 10. 2026

**Nové**
- `portafontium.py` – matriky SOA Plzeň bez prohlížeče.
- `ebadatelna.py` – matriky a archiválie SOA Praha bez prohlížeče.
- `ftb_export.py` – záloha MyHeritage (`.ftb`) → GEDCOM a přehled přímé linie.
- Podpora Windows (Python bez `python3`, UTF-8, limit délky příkazu, Chrome/Edge).
- Bohatší ukázková rodina, licence MIT, upozornění v README, odkazy na genealogické společnosti, hlášení chyb přes issues.

**Opravy**
- `ged_import --osoby` escapuje jména (uvozovky ve jménu rozbily `osoby.py`).
- `vyrez.py` maže EXIF/GPS z fotek a otáčí je podle orientace.
- `fan_chart.py`: předek starší než 10. generace neshodí vějíř ani export webu.
- `ebadatelna.py`: stránkování u obcí s víc než 50 knihami; `portafontium.py`: název fary s diakritikou.

## 0.3.0 – 20. 10. 2026

- Oprava roků u neznámého narození.
- Policejní přihlášky, SOA Litoměřice.
- Pomocníci na modelu Sonnet, sporná čtení.

## 0.2.0 – 16. 10. 2026

Poučení z prvního ostrého projektu.

- Nové nástroje: `trebon.py`, `ahmp_*`, `matricula_*`, `anno*`, `kramerius.py`, `overit.py`, `ged_import.py`, `napady.py`.
- Metodika: začínat od nejmladšího zápisu, ověřování pomocníků, noviny u úředníků a vojáků.
- Zajímavosti průběžně a „Příběh rodu“ s konceptem ke schválení.
- `kontrola.py`: citlivé údaje z 20. století na webu.

## 0.1.0 – 16. 10. 2026

První verze: průvodce, nástroje, šablona webu a ukázka.
