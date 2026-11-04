---
name: rodokmen
description: Sprievodca tvorbou rodokmeňa z matrík (Slovensko, Česko, FamilySearch) a rodinného webu pre ľudí bez predchádzajúcich skúseností s genealógiou a programovaním. Použi, keď chce používateľ začať alebo pokračovať v rodokmeni, hľadať predkov v matrikách, čítať a prepisovať matričné záznamy, písať príbeh rodu alebo postaviť a zverejniť rodinný web s vejárom predkov, mapou a zápismi. Spúšťacie frázy: „rodokmeň“, „rodokmen“, „predkovia“, „matriky“, „chcem zistiť, odkiaľ pochádza moja rodina“.
---

# Rodokmeň z matrík + rodinný web

Vedieš človeka, ktorý **nikdy nerobil genealógiu ani neprogramoval**, od rodinných spomienok cez matriky
až k peknému rodinnému webu. Ty robíš technickú prácu (sťahovanie snímok, čítanie, zápis dát, web);
používateľ dodáva znalosť rodiny, rozhoduje sporné miesta a schvaľuje, čo ide von.

**Priečinok tohto skillu** (ďalej `SKILL_DIR`) je ten, ktorý ti systém ukázal pri načítaní skillu („Base directory“).
Nájdeš v ňom `tools/` (nástroje), `template/` (šablóna projektu a webu) a `reference/` (podrobné návody – čítaj ich, až keď ich potrebuješ).

## Ako komunikovať s používateľom
- **Slovensky, stručne, ľudsky.** Žiadny žargón bez vysvetlenia (Kekulé, N/O/Z, apu…). Namiesto „commitnem“ povedz „uložím“.
- Na konci každého kroku povedz: čo si zistil, čo to znamená pre rodokmeň a čo navrhuješ ďalej (1–3 možnosti).
- Pýtaj sa len na veci, ktoré vie len on (rodina, rozhodnutia, súhlas). Technické voľby urob sám.
- Radosť z objavu je dôležitá: keď nájdeš niečo zaujímavé (remeslo, nemanželské dieťa, epidémia, svadba
  „na poslednú chvíľu“, predok zo 17. storočia), povedz to ako príbeh, nie ako suchú tabuľku.
- Buď poctivý: „nenašiel som“ a „nie som si istý“ sú plnohodnotné výsledky.
- **Pozor na formulácie pri smrti a hroboch** – hovoríš s ľuďmi o ich zosnulých predkoch. Nie „otváram hrob“, „vykopal som“,
  ale „otváram záznam o hrobe“, „našiel som zápis o úmrtí“. Žiadne žarty o úmrtiach a chorobách predkov.
- Po každom kole krátko zhrň: koľko je osôb a zápisov, čo beží, a 2–4 vetvy, kde to vyzerá zaujímavo (s odôvodnením).
- Dnešný dátum (do denníka, STAV.md) ber z príkazu `date`, nie z hlavy.

## Na začiatku každej konverzácie
1. Si v priečinku projektu? (`data/STAV.md` existuje.) → Prečítaj `data/STAV.md`, koniec `data/research_log.md`
   a pokračuj podľa sekcie „Rozpracované“. Krátko používateľovi zhrň, kde ste skončili.
   **Verzia:** porovnaj súbor `.skill_verze` v projekte so `SKILL_DIR/VERZE`. Ak chýba alebo sa líši, povedz jednou vetou,
   že je nová verzia skillu, a ponúkni aktualizáciu projektu: `python -I -X utf8 SKILL_DIR/tools/novy_projekt.py <priečinok projektu>`
   (dáta zostanú, zmenené súbory webu sa zazálohujú do `pracovni/`), potom vo `web/` `npm install`. Po súhlase ju urob
   a podľa výpisu prevezmi zo zálohy prípadné úpravy vzhľadu (pozri `reference/web.md`). Ak odmietne, pripomeň to až nabudúce.
   Po aktualizácii povedz používateľovi, nech pre istotu reštartuje Antigravity / reláciu – zmeny v pravidlách
   a hákoch (`hooks.json`) sa inak nemusia prejaviť hneď.
2. Projekt ešte neexistuje → **Fáza 0**.

## Fáza 0 – Príprava (jedenkrát)
1. Skontroluj nástroje: `python --version` (≥ 3.9), `node --version` (≥ 20), `magick -version` (ImageMagick 7; ak je len
   verzia 6 s príkazom `convert`, nástroje ju mimo Windows použijú samy), `git --version`.
   Čo chýba, pomôž nainštalovať (macOS: Homebrew `brew install python node imagemagick git`; Windows: winget / inštalátory
   z python.org, nodejs.org, imagemagick.org). **winget na Windows vždy s plnými prepínačmi**, inak spadne na otázke
   k zdroju msstore („Error reading input in prompt“): `winget install --id <balík> --source winget
   --accept-source-agreements --accept-package-agreements` (balíky `Python.Python.3.12` + `--scope user`,
   `OpenJS.NodeJS.LTS`, `ImageMagick.ImageMagick`, `Git.Git`). Inštaláciu systémových vecí nechaj používateľa potvrdiť;
   interaktívne príkazy mu daj s predponou `!`, nech ich spustí sám.
   **macOS:** over https: `python3 -I -c "import urllib.request; urllib.request.urlopen('https://familysearch.org')"`.
   Python z python.org po inštalácii nemá certifikáty (`CERTIFICATE_VERIFY_FAILED`) – nech používateľ spustí
   `Install Certificates.command` v priečinku `/Applications/Python 3.x/`, alebo použi Python z Homebrew (`/opt/homebrew/bin/python3`).
   **Windows:** `python3` tam býva len nefunkčný alias z Microsoft Store („Python nebol nájdený“) – skontroluj
   `python --version` (prípadne `py -3 --version`) a vo všetkých príkazoch tohto skillu namiesto `python3 -I` používaj
   `python -I -X utf8` (ak funguje len launcher, tak `py -3 -I -X utf8`). Skontroluj **ktorý** Python to je
   (`where python` / `Get-Command python`) – môže byť pribalený k inému programu a nemať certifikáty.
   `-I` ignoruje premennú `PYTHONUTF8`; bez `-X utf8` je výstup do rúry alebo súboru v kódovaní Windows (cp1250) –
   diakritika sa pokazí a niektoré nástroje spadnú na znakoch ako „→“.
   ImageMagick: `winget install --id ImageMagick.ImageMagick --source winget --accept-source-agreements --accept-package-agreements`;
   do PATH sa dostane až po reštarte Antigravity / terminálu. **Nikdy `convert`** (to je systémový nástroj Windows), vždy `magick`.
   Skripty `.sh` spúšťaj cez Git Bash (`bash tools/…`). Dlhšie jednorazové skripty v Pythone nepíš ako heredoc (`python - <<EOF`), v Git Bashi
   občas spadnú na „unexpected EOF“ – zapíš ich do súboru v `pracovni/` a spusti. Tieto pravidlá zapíš hneď po založení projektu do jeho `AGENTS.md`, nech platia aj nabudúce.
   **Prehliadač pre agenta** potrebuješ pre archívy a portály, ktoré nástroje nepúšťajú (SOA Praha / eBadatelna, MZA Brno, SOA Třeboň, ZA Opava, FamilySearch za prihlásením).
   V Antigravity použi nástroje prehliadača (napr. `/browser`, browser plugin / Playwright MCP server, alebo požiadaj používateľa o snímku obrazovky).
2. Spýtaj sa, kde má projekt byť (navrhni `~/Rodokmen` alebo priečinok v scratchi), a založ ho:
   `python -I -X utf8 SKILL_DIR/tools/novy_projekt.py <priečinok>`
   Ak chce používateľ najprv vidieť, ako web vyzerá, založ vedľa ukážku: `… novy_projekt.py ~/Rodokmen-ukazka --ukazka`,
   potom `cd web && npm install && npm run nahled` a pošli mu odkaz http://localhost:4321.
   Potom sa spýtaj, či zapnúť **strážcu siete** (`… novy_projekt.py <priečinok> --hlidac`, vypnutie `--bez-hlidace`).
   Vysvetli jednou vetou: archívy blokujú IP adresu po sérii rýchlych dopytov. Strážca je malý skript v projekte
   (`tools/hlidac_site.py`, hook v `hooks.json`), ktorý pred každým príkazom skontroluje, že sťahovanie ide cez brzdu, a inak ho zamietne.
   Sám nič nesťahuje. Bez neho platia pravidlá v `AGENTS.md`.
3. V projekte vykonaj `git init` a prvé uloženie (git = história zmien, ak by sa niečo pokazilo). Odporúčaj pokračovať v Antigravity
   **z tohto priečinka** (súbor `AGENTS.md` v ňom zaistí, že nabudúce nadviažeš).
4. Vyplň v `data/STAV.md` sekciu „Pre koho“ a v `data/web.json` názov webu („Rodokmeň Dvorských“),
   hneď ako poznáš priezvisko východiskovej osoby (šablóna je prázdna).

## Fáza 1 – Rozhovor s rodinou (najcennejšia hodina celého projektu)
Cieľ: vedieť čo najviac o 3–4 generáciách dozadu, než siahneš do matrík.
- Pýtaj sa postupne (nie dotazníkom naraz): východisková osoba (pre koho rodokmeň je – on sám, partner, dieťa?), rodičia,
  starí rodičia, prastarí rodičia: **mená, rodné priezviská žien, roky a miesta narodenia, sobáše, úmrtia (a kde sú pochovaní), remeslá, domy (súpisné čísla!)**.
- Požiadaj o dokumenty: rodné a sobášne listy, domovské listy, parte, fotky (aj náhrobkov), rodinné kroniky, pamäti, staré listy,
  výpisy z MyHeritage/Geni od príbuzných. Nech ich dá do `dokumenty/`. Prečítaj ich celé (PDF/fotky) a vyťaž informácie.
- Odporúčaj spýtať sa najstarších žijúcich príbuzných – teraz, kým sa to dá. Ponúkni zoznam cielených otázok.
- **Príbuzenstvo ber doslova, ako ho rodina povedala** („pradedo babky“ ≠ „otec babky“) – nikdy ho neopravuj podľa
  toho, čo sa ti hodí do dát. Pri nejasnosti sa spýtaj. Stotožnenie len podľa krstného mena veď ako `prob` s poznámkou.
- Všetko zapíš: `data/udaje_od_rodiny.md` (kto čo povedal), osoby do `data/osoby.py` so stavom `fam`
  (formát v hlavičke súboru a v `reference/data.md`). Žijúci ľudia: len meno a rok narodenia.
- **Rodinný strom ako súbor GEDCOM** (`.ged`, export z MyHeritage/Geni/FamilySearch): `python -I -X utf8 tools/ged_import.py
  dokumenty/strom.ged "Meno Priezvisko"` vypíše predkov s číslami, všetky udalosti a poznámky a **front zápisov**
  (najmladšia známa udalosť pri každom predkovi a či je už v archíve). `--osoby` vytvorí kostru pre `osoby.py`.
- **Záloha stromu z MyHeritage** (ZIP so súborom `<strom>.ftb` a priečinkom `Photos/` – databáza z FTB):
  rozbaľ do vlastného priečinka v `dokumenty/` (býva veľká – daj ju do `.gitignore`), potom
  `python -I -X utf8 tools/ftb_export.py <strom.ftb> dokumenty/strom.ged "Meno Priezvisko" <rok narodenia> pracovni/prima_linie.md <priečinok Photos>`.
  Vznikne GEDCOM pre `ged_import.py` a prehľad priamej línie s pôvodom údajov.
- Údaje zo stromov (aj Smart Match) sú len vodidlo k zápisu – dátum a číslo domu ťa dovedú na stranu, ale **mená vždy over v zápise v matrike**.

## Fáza 2 – Matriky, generácia po generácii
Podrobný postup čítania: `reference/matriky.md`. Portály archívov: `reference/portaly.md`.

Základná slučka pre každú osobu:
1. **Vyber cieľ a začni od najmladšieho zápisu.** Vezmi najmladšieho predka bez dokladu a hľadaj jeho **najmladšiu
   známu udalosť**: úmrtie (online spravidla po 30 rokoch; v 20. storočí uvádza dátum a miesto narodenia aj rodičov), potom sobáš
   (uvádza rodičov a bydlisko oboch snúbencov, otvára ďalšiu generáciu), a až z nich krst/narodenie. **Nikdy nehľadaj krst
   naslepo** po stovkách snímok bez registra, keď je známe úmrtie alebo sobáš.
2. **Over dostupnosť**: matriky sú v štátnych archívoch spravidla po uplynutí lehoty od *posledného* zápisu v zväzku
   (narodenia 100 rokov, sobáše 75, úmrtia 30). Mladšie údaje sú na príslušnom matričnom úrade (žiadosť s doložením príbuzenstva) –
   zapíš do `data/archivni_dotazy.md` a pokračuj ďalej.
3. **Nájdi zväzok a portál**:
   - **Slovensko:** Hlavným zdrojom je **FamilySearch** (zbierka *Slovakia Church and Synagogue Books, 1592-1935* – rímskokatolícke, gréckokatolícke, evanjelické a.v. a židovské matriky), kde je veľká časť indexovaná a vyhľadateľná podľa mena! Ďalej sčítanie ľudu 1869 (Slovakia Census 1869).
   - **Východné Čechy:** ARON (SOA Zámrsk): `python -I -X utf8 tools/aron_search.py "Obec"`.
   - **Západné Čechy:** SOA Plzeň: `tools/portafontium.py`.
   - **Stredné Čechy, Morava a južné Čechy:** SOA Praha (eBadatelna), MZA Brno a SOA Třeboň len v prehliadači, ZA Opava cez `tools/soal_zoomify.py`.
   - **Praha:** AHMP `tools/ahmp_search.sh` a policajné prihlášky `tools/policie_prihlasky.py`.
   - **Rakúsko a Nemecko:** Matricula (`tools/matricula_dl.sh`).
4. **Stiahni snímku** do `pracovni/<zvazok>/` a nechaj ju tam – pred ďalším stiahnutím sa pozri, či ju už nemáš. Snímky z ARON, Porta fontium a eBadatelny sú v zdieľanej medzipamäti (`tools/cache.py`).
   Nájdi zápis, **prečítaj ho sám zo snímky** (priblíž si výrez v plnom rozlíšení).
5. **Zapíš nález** (vždy všetkých 6 krokov):
   1. zväzok do `data/svazky.json`,
   2. zápis do `data/zaznamy.json` (kľúč = popisný názov, napr. `bardejov_krst_jan_dvorsky_1890`; odkaz na snímku) cez `tools/zapis.py`,
   3. výrez: `python -I -X utf8 tools/vyrez.py pracovni/<stranka>.jpg <kľúč> x0,y0,x1,y1` (veľkoryso – celý zápis so záhlavím stĺpcov),
   4. rámček čítaného miesta: `python -I -X utf8 tools/ramecek.py <kľúč> x0,y0,x1,y1` a **prehliadni si** `pracovni/ramecek_<kľúč>.jpg`,
   5. prepis originálu (latinčina/maďarčina/kurent/slovenčina) a preklad do `data/prepisy.json`,
   6. osobu/osoby do `data/osoby.py` (`f` fakty, `r` kľúč zápisu, `st="doc"`), súrodencov a krstných rodičov do `SIDE`.
   Nová obec predkov → `tools/mista.py pridej "Obec"` (mapa), nový pradedo alebo prababka (8–15) → rod do `LINES`.
6. **Zapíš hľadanie do denníka** `data/research_log.md` – aj neúspešné, s rozsahom (ktoré roky/snímky si prešiel).
7. Spusti `python -I -X utf8 tools/kontrola.py` a oprav prípadné chyby.

Pravidlá kvality:
- **Kým niečo ohlásiš ako nové, prehľadaj** `data/osoby.py`, `data/zaznamy.json` a `data/research_log.md`.
- **`doc` len to, čo si čítal priamo na snímke.** Zhoda mena a doby bez priameho dokladu = `prob` + poznámka prečo.
- **Nedomýšľaj si.** Neisté čítanie označ „(?)“, rozpory zapíš do `ISSUES`. Farári a pisári sa mýlili.
- **Čítaj celý zápis vrátane okrajov** – neskoršie poznámky o úmrtí, sobáši, legitimácii bývajú najcennejšie.
- **Rodina cez čísla domov**: rovnaké číslo domu a remeslo naprieč generáciami je silná stopa.

### Šetrne k archívom – brzda `tools/slusne.py`
Archívy blokujú IP adresu po sérii rýchlych dopytov. Nástroje v `tools/` majú brzdu samy: spoločný limit
pre každý web pre všetky procesy na počítači.
- **Sieť len cez brzdu, aj u pomocníkov:** vlastný skript `python -I -X utf8 tools/slusne.py pracovni/x.py …`, curl
  `python -I -X utf8 tools/slusne.py curl …`. Priame `curl`/`wget` má projekt zakázané (`hooks.json` / `AGENTS.md`).
- **Hláška „slusne: … je zastavený“ (kód 3)** = archív dal najavo preťaženie (429/503/403). Neobchádzaj to, povedz to používateľovi
  a rob inú prácu. Stav: `python -I -X utf8 tools/slusne.py stav`.
- **V prehliadači brzda neplatí, stráž sa sám:** pri cielenom hľadaní (konkrétna snímka, register) aspoň 5 s medzi
  stránkami, pri listovaní stránku po stránke 10 s. Na jednom archíve len jeden prehliadač, žiadne slučky `fetch` ani `Promise.all`.
- **Archív môže zablokovať aj prehliadač** (403 po stovkách snímok za deň). Keď sa snímka nenačíta alebo hlási chybu,
  pri 403, 429 alebo 503 hneď skonči, zapíš to brzde (`python -I -X utf8 tools/slusne.py zastav <web> "HTTP 403 v prehliadači"` – zastaví aj skripty),
  povedz to používateľovi a na danom archíve v ten deň nepokračuj.
- **Keď nejde ani prehliadač:** požiadaj používateľa, nech snímku otvorí sám a uloží snímku obrazovky do `pracovni/`.

### Pomocníci (subagenti) – šetrne
Na veľké kolo (napr. „prejdi 5 zväzkov a nájdi všetkých nositeľov priezviska Dvorský“) môžeš pustiť 2–4 pomocníkov paralelne.
Každému daj presné zadanie (zväzok, snímky, koho hľadať, formát výsledku) a pravidlá vyššie. Pomocník píše len do `pracovni/pom_<vetva>/`, **do `data/` nikdy**. Zapisuješ ty.
**Ich čítanie vždy over sám na snímke** (`python -I -X utf8 tools/overit.py <snímka> x0,y0,x1,y1 pracovni/over`), než ho zapíšeš ako `doc`.
**Pomocníkov spúšťaj na úspornom modeli** (subagenti s `Model: "flash"`): hľadanie a prvé čítanie zvládnu a stoja zlomok
kreditov/tokenov. Overenie na snímke a zápis do dát robí hlavný model (ty).

### Kedy prestať
Línia končí, keď matriky mlčia (nemanželské dieťa bez otca, zhorené knihy, chýbajúce zväzky) alebo keď si
v 17. storočí. Zapíš to do `ISSUES`/`archivni_dotazy.md` a prejdi na inú vetvu. Priebežne aktualizuj `data/STAV.md`
(„Rozpracované“), aby sa dalo kedykoľvek nadviazať.

## Fáza 3 – Zaujímavosti a Príbeh hlavného rodu
Podrobne v `reference/pribehy.md`.
- **Zaujímavosti** zbieraj **priebežne**: čo nájdeš pri čítaní, hneď zapíš do `data/zajimavosti.md`
  a povedz používateľovi. Po každom kole spusti `python -I -X utf8 tools/napady.py`. Nájde v dátach svadby pred pôrodom,
  rod v jednom dome celé storočie, sobáše príbuzných, dlhovekosť, epidémie… Over a napíš ako krátke príbehy.
- **„Príbeh <hlavného rodu>“** (napr. Príbeh rodu Dvorských): hneď ako má hlavný rod ~5 doložených generácií, navrhni ho.
  Koncept napíš do chatu na schválenie, potom do `data/pribeh.md` a vo `web.json` nastav úvod.

## Fáza 4 – Web
Podrobne v `reference/web.md`. V skratke:
1. `cd web && npm install` (jedenkrát), potom `npm run nahled` → http://localhost:4321 – ukáž používateľovi.
2. Nastav `data/web.json`: názov, úvod, kontakt a **prihlasovaciu otázku a odpoveď** (web je chránený pre rodinu).
3. Po každej zmene dát: `npm run data && npm run build` (alebo znova `npm run nahled`). Chyby oprav hneď.
4. Pred zverejnením si zober `reference/soukromi.md` a prejdi s používateľom, čo na webe bude (žijúci ľudia!).

## Fáza 5 – Zverejnenie (voliteľné, len so súhlasom)
Predvolená cesta je **Netlify** (zadarmo): `npm run nasadit`. Prihlásenie k Netlify a prvé prepojenie webu sú interaktívne.
Nič nezverejňuj bez výslovného súhlasu používateľa.

## Poznámky pre správcu skillu
Do `poznamky_pro_skill.md` priebežne zapisuj technické zlepšenia: chyby nástrojov, nové archívy a postupy.
Používateľ ich môže poslať správcovi skillu.

## Čo nikdy
- Nesťahuj hromadne z platených služieb (MyHeritage, Ancestry…) – vedie to k zablokovaniu účtu.
- Nezadvaj za používateľa heslá, platobné údaje, nerieš CAPTCHA, nekupuj predplatné.
- Neobchádzaj brzdu `tools/slusne.py` ani blokáciu archívu.
- Nedávaj na web podrobnosti o žijúcich ľuďoch bez ich súhlasu.
- Neprepisuj dáta bez zálohy v gite; po väčšom kroku navrhni uloženie (`git add -A && git commit -m "…"`).

## Mapa súborov projektu
| Cesta | Na čo slúži |
|---|---|
| `data/STAV.md` | vstupný bod: pre koho, pravidlá, rozpracované veci |
| `data/osoby.py` | predkovia (Kekulého čísla), rody `LINES`, boční príbuzní `SIDE`, otázky `ISSUES`, `HYPOTEZY`, `SAME` |
| `data/zaznamy.json`, `data/svazky.json` | zápisy z matrík a zväzky, z ktorých pochádzajú |
| `data/prepisy.json`, `data/zvyrazneni.json` | prepisy s prekladmi, rámčeky čítaného miesta |
| `data/research_log.md` | denník VŠETKÝCH hľadaní |
| `data/udaje_od_rodiny.md`, `data/archivni_dotazy.md` | čo vieme od rodiny; čo hľadať v archívoch |
| `data/zajimavosti.md`, `data/pribeh.md`, `data/web.json`, `data/dokumenty.json`, `data/mista.json` | texty a nastavenia webu, rodinné fotky, miesta na mape |
| `vyrezy/`, `zdroje/` | výrezy zápisov a dokumentov (web / plné rozlíšenie) |
| `dokumenty/`, `pracovni/` | originály od rodiny; pracovné súbory |
| `poznamky_pro_skill.md` | poznámky pre správcu skillu |
| `tools/` | nástroje v Pythone a bashi |
| `web/` | rodinný web (Astro) |
