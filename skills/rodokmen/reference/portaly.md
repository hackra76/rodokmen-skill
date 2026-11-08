# Portály archívov a ako z nich získať matričné snímky

Matriky a pramene pre predkov zo **Slovenska, Česka a strednej Európy** sú dostupné online prostredníctvom špecializovaných archívnych portálov a databáz.

---

## 1. Slovensko – cirkevné a štátne matriky, sčítania ľudu

Pre rodokmeň zo Slovenska (Horné Uhorsko pred rokom 1918) je situácia špecifická a v mnohých ohľadoch veľmi priaznivá vďaka rozsiahlej digitalizácii:

### A. Cirkevné matriky do roku 1895 (FamilySearch)
- **Kde sú:** Cirkevné matriky (rímskokatolícke, gréckokatolícke, evanjelické a.v., reformované/kalvínske a židovské) zo všetkých slovenských farností do cca roku 1895/1900 boli v 90. rokoch na mikrofilmoch kompletne zdigitalizované Genealogickou spoločnosťou Utahu (FamilySearch).
- **Kolekcia:** *Slovakia Church and Synagogue Books, 1592–1935* (Slovensko, cirkevné a synagógové knihy).
- **Veľká výhoda:** Zbierka je **veľmi detailne indexovaná**! Na rozdiel od väčšiny českých archívov je možné na FamilySearch fulltextovo vyhľadávať podľa mena, priezviska, roku narodenia a lokality.
- **Prístup:** Vyžaduje bezplatné prihlásenie na [familysearch.org](https://www.familysearch.org). Používateľ si vytvorí bezplatný účet, v ktorom si prezerá indexy a záznamy.
- **Ako čítať záznamy:**
  - Jazyky zápisov na Slovensku: do cca 40. rokov 19. storočia prevažne **latinčina** (zriedkavejšie nemčina alebo biblická čeština v evanjelických matrikách), od polovice 19. storočia a najmä po rakúsko-uhorskom vyrovnaní (1867) **maďarčina**, po roku 1918 **slovenčina**.
  - Priezviská: Priezviská môžu byť zapísané maďarským pravopisom (napr. Dvorský ako *Dvorszkij* / *Dvorszky*, Jurčák ako *Jurcsák*, Kováč ako *Kovács*).
  - Krstné mená: latinsky (*Joannes*, *Stephanus*, *Georgius*, *Maria*), maďarsky (*János*, *István*, *György*).
- **Prezeranie celých kníh (Catalog):**
  - Ak záznam nie je v indexe, choďte cez *Search → Catalog → Place: Slovakia, [Názov stolice / okresu / farnosti]* (napr. *Slovakia, Šariš, Bardejov*), alebo cez *Keywords: Farský úrad <obec>* (napr. *Farský úrad Bardejov*). Tu sú k dispozícii celé nasnímané matričné knihy záber po zábere.
  - Cirkevné knihy na Slovensku na FamilySearch spravidla končia rokom **1895** (keď začala štátna matrika).
  - Dobrovoľnícke indexy sú často neúplné – pri neúspechu listujte priamo v knihe príslušnej farnosti.
- **Uloženie snímky v plnom rozlíšení do medzipamäte (`cache.py`):**
  - Z prihláseného prehliadača (Playwright) možno snímku uložiť v plnom rozlíšení:
    `python -I -X utf8 tools/cache.py uloz pracovni/fs.json pracovni/fs.jpg --nahled pracovni/nahled.jpg`
  - Snímka sa v medzipamäti uloží pod svojím ARK kódom a ďalšie výrezy už nevyžadujú prehliadač.
  - Náhradný postup: stiahnutie tlačidlom *Download* do `~/Downloads` a presun do `pracovni/`.

### B. Sčítanie ľudu 1869 (Slovakia Census 1869)
- Zbierka na FamilySearch: *Slovakia Census, 1869*.
- Pokrýva celé rodiny a domácnosti v roku 1869 (meno, vek, rodinný vzťah, náboženstvo, povolanie, gramotnosť, zvieratá a majetok).
- Mimoriadne cenné na zachytenie štruktúry rodiny a potvrdenie generácie prastarých rodičov.

### C. Civilné (štátne) matriky po 1. 10. 1895
- V Uhorsku bola 1. októbra 1895 zavedená štátna matrika.
- Zápisy z rokov 1895–1906+ sú postupne odovzdávané do pracovísk Štátnych archívov SR (Štátny archív v Prešove, Košiciach, Levoči, Banskej Bystrici, Bytči, Nitre, Bratislave).
- Záznamy mladšie ako 100 rokov (narodenia), 75 rokov (sobáše) a 30 rokov (úmrtia) sa nachádzajú na miestnych matričných úradoch miest a obcí. Do nich má prístup len priamy príbuzný (na základe žiadosti a preukázania príbuzenstva).

### D. Cintoríny a náhrobky na Slovensku
- Pre 20. a 21. storočie existujú online databázy s fotografiami hrobov a menami:
  - **cintoriny.sk** – celoslovenský portál evidencie hrobových miest.
  - **virtualnycintorin.sk** – podrobné mapy cintorínov vrátane stoviek obcí a miest.

### E. Pozemkové knihy a urbáre
- **Urbár Márie Terézie (1767):** pre slovenské obce dostupný na maďarskom portáli `hungaricana.hu` (databáza *Urbáre a súpisy poddanských povinností*).
- Staršie pozemkové knihy a súdne písomnosti spravujú príslušné pracoviská Štátneho archívu SR.

---

## 2. Česko – portály krajských štátnych archívov

Matriky v ČR sú online u ôsmich štátnych oblastných archívov podľa toho, **kde predkovia žili**:

| Archív | Oblasť | Portál s matrikami | Stav v skille |
|---|---|---|---|
| SOA Zámrsk | východné Čechy (Hradecký a Pardubický kraj) | ARON – aron.vychodoceskearchivy.cz | **áno – hotové nástroje** |
| SOA Praha | stredné Čechy | eBadatelna – ebadatelna.soapraha.cz | **iba v prehliadači** – medzipamäť `cache.py` (archivársky nástroj od 2. 11. 2026 zakazuje robots.txt) |
| SOA Plzeň | západné Čechy | Porta fontium – portafontium.eu | **áno – nástroj `portafontium.py`** (s medzipamäťou) |
| SOA Třeboň | južné Čechy | digi.ceskearchivy.cz | **iba v prehliadači** – archív nástroj od 2. 11. 2026 odmieta (HTTP 403) |
| SOA Litoměřice | severné Čechy | Digitální badatelna – digi.soalitomerice.cz | **čiastočne – `soal_zoomify.py`** (knihu nájdi v prehliadači) |
| AHMP | hl. m. Praha | katalog.ahmp.cz (Pragapublica) | **áno – `ahmp_search.sh`, `ahmp_scan.py`** |
| MZA Brno | južná Morava, časť Vysočiny | Acta Publica – www.mza.cz/actapublica | **iba v prehliadači** – snímka obrazovky priblíženého zápisu |
| ZA Opava | severná Morava a Sliezsko, Olomoucko | Digitální badatelna – digi.archives.cz/da/ | **čiastočne – `soal_zoomify.py`** (len s prehliadačom, CAPTCHU rieši používateľ) |
| Národní archiv | židovské matriky (HBMa), pražské policajné prihlášky 1850–1914 | VadeMeCum NA – vademecum.nacr.cz; digi.nacr.cz/prihlasky2 | prihlášky **áno – `policie_prihlasky.py`** |

### Zdieľaná medzipamäť snímok – `tools/cache.py`
Portály často opakovane sťahujú rovnaké dáta. Na úsporu siete a ochranu pred zablokovaním slúži zdieľaná medzipamäť na disku:
- Umiestnenie: `~/.cache/rodokmen_snimky/` (na Windows `%LOCALAPPDATA%\rodokmen_snimky`).
- Limit veľkosti: 5 GB s automatickým uvoľňovaním najstarších súborov (LRU).
- Kontrola pred stiahnutím / otvorením:
  `python -I -X utf8 tools/cache.py najdi <url_alebo_kluc> [--nahled pracovni/nahled.jpg]`
- Uloženie do medzipamäte:
  `python -I -X utf8 tools/cache.py uloz <subor_alebo_json> [--url <url>] [--nahled pracovni/nahled.jpg]`
- Výrez priamo z medzipamäte bez sťahovania:
  `python -I -X utf8 tools/cache.py orez <url_alebo_kluc> x0,y0,x1,y1 pracovni/vyrez.jpg`
- Štatistika využitia: `python -I -X utf8 tools/cache.py stats`.

### ARON (SOA Zámrsk) – hotové nástroje
- **Hľadanie zväzkov:** `python -I -X utf8 tools/aron_search.py "Holice"` → riadky `apu_id | signatura, roky | druh, obce`.
- **Informácie o zväzku:** `python -I -X utf8 tools/aron_img.py <apu_id> info` → názov a počet snímok.
- **Stiahnutie snímky:** `python -I -X utf8 tools/aron_img.py <apu_id> <snímka> 1 pracovni/holice_n_57.jpg`
  (úroveň 1 = polovičné rozlíšenie; 0 = plné rozlíšenie na čítanie a výrez).
  Výrez priamo v plnom rozlíšení: `… <snímka> 0 pracovni/detail.jpg 0.0,0.4,1.0,0.7`.
  Nástroj stiahne celý sken jednou požiadavkou (ako tlačidlo „Stiahnuť“ v ARONe cez referencedfiles) a zmenšenie aj výrez robí z disku; dlaždice slúžia len ako záloha pri zlyhaní celého skenu.
- **Trvalý odkaz:** `python -I -X utf8 tools/aron_img.py <apu_id> link <snímka>`.
- **Zväzok do dát:** `python -I -X utf8 tools/aron_img.py <apu_id> svazek`.

### SOA Praha (eBadatelna, soapraha.cz) – iba v prehliadači s medzipamäťou
- Od 2. 11. 2026 archív zakazuje robotické sťahovanie cez robots.txt.
- **Postup čítania a ukladania:**
  1. Zisti, či už snímku nemáš na disku:
     `python -I -X utf8 tools/cache.py najdi <adresa_snimky> --nahled pracovni/nahled.jpg`
     Ak existuje, prehliadač vôbec neotváraj a čítaj z náhľadu!
  2. Ak snímka nie je v medzipamäti, otvor adresu v prehliadači (Playwright / Claude in Chrome / ručne). Po načtení ulož cez evaluate do JSON a naimportuj:
     `python -I -X utf8 tools/cache.py uloz pracovni/ebad.json --nahled pracovni/nahled.jpg`
  3. Pre výrez z uloženej snímky bez siete použi:
     `python -I -X utf8 tools/ebadatelna.py snimek <matrikaId> <snimok> pracovni/x.jpg [nahled] [x0,y0,x1,y1]`

### SOA Plzeň (Porta fontium, portafontium.eu) – `tools/portafontium.py`
- **Obec → knihy:** `python -I -X utf8 tools/portafontium.py obec "<obec>"` → všetky knihy s obcou v popise, zoskupené podľa fary a zoradené podľa rokov (kniha | obce | roky a druhy | popis). Zobrazuje aj prechod obce medzi farami a civilné matriky okresných úradov.
- `python -I -X utf8 tools/portafontium.py fara <fara>` → zoznam kníh farnosti. Rovnomenné fary majú príponu okresu (`plana-ps`, `radnice-ro`) – správnu adresu ukáže `obec`.
- `python -I -X utf8 tools/portafontium.py info <kniha>` → počet snímok, roky, obce a rozvrhnutie strán.
- `python -I -X utf8 tools/portafontium.py snimek <kniha> <cislo> pracovni/x.jpg` → stiahnutie snímky (automaticky cachované cez `cache.py`).
- Výrez: `python -I -X utf8 tools/portafontium.py snimek <kniha> <cislo> pracovni/x.jpg 0,0,1,1`.
- **Tempo:** portál vyžaduje 10 s medzi dopytmi (robots.txt „Crawl-delay: 10“) – brzda `slusne.py` to dodržiava automaticky.

### SOA Třeboň (digi.ceskearchivy.cz) – iba v prehliadači
- Od 2. 11. 2026 archív odmieta nástroj (HTTP 403). Matriky čítaj v prehliadači (Playwright alebo používateľ).
- Stránka Zoomify je v rámci `ram_obsah`.
- Pozor: každé zobrazenie sťahuje dlaždice znova, preto si na zobrazenej strane prečítaj a ulož všetko potrebné pred prechodom ďalej. Dodržuj tempo 5–10 s medzi stránkami.

### MZA Brno (Acta Publica, mza.cz/actapublica) – iba v prehliadači
- Od 2. 11. 2026 MZA blokuje sťahovacie skripty (ochrana Altcha, jednorazové tokeny dlaždíc).
- Skriptom je povolené **iba hľadanie kníh**:
  `python -I -X utf8 tools/slusne.py curl -s "https://www.mza.cz/actapublica/matrika/hledani?typ=obec&search_by_obec=<obec>&page=<n>"`
  (limit brzdy 1 dotaz za 4 s).
- Zobrazenie matrík a snímky rob výhradne v prehliadači: listuj v otvorenej relácii (`viewer.goToPage(n-1)`), návrat späť ide z cache prehliadača.
- **Prehliadač: Playwright** (uloží snímku do súboru). **Vstavaný prehliadač Claude desktop pre MZA nepoužívaj** – podľa hlásení používateľov dostáva na snímky 403 aj po dni pauzy, zatiaľ čo bežný prehliadač prejde. Bez Playwrightu nech používateľ otvorí snímku vo svojom prehliadači a pošle snímky obrazovky sám (celá dvojstrana na orientáciu, potom priblížený zápis – koliesko myši, macOS Cmd+Shift+4, Windows Win+Shift+S) a ulož ich do `pracovni/`.
- **Blokácia snímok (403):** MZA po zhruba 45–60 snímkach za deň (počíta sa každé priblíženie – sťahuje nové dlaždice) prestane vydávať obraz: stránka aj overenie prejdú, ale snímka zostane biela a dlaždice vracajú 403. **Nie je to pomalé načítanie – okamžite prestaň**, neskúšaj znova a povedz to používateľovi. Blokácia trvala aj na druhý deň; ďalší deň skús najviac jednu snímku.
- Dlaždica vracajúca **410** nie je blokácia – vypršal token v adrese; stačí znova otvoriť rovnakú adresu snímky (`?image=…jp2`).
- Uloženie priblíženého výrezu ako snímka obrazovky.
- **Pozor:** Doména `actapublica.eu` nepatrí archívu MZA a je zablokovaná. Používaj výhradne `www.mza.cz/actapublica`.

### AHMP Praha – `tools/ahmp_search.sh`, `tools/ahmp_scan.py`
- `bash tools/ahmp_search.sh "Smíchov"` → zoznam zväzkov.
- `python -I -X utf8 tools/ahmp_scan.py <XID> <snimok> pracovni/x.jpg [1] [x0,y0,x1,y1]`.
- Trvalý odkaz: `https://katalog.ahmp.cz/pragapublica/permalink?xid=<XID>&scan=<N>`.

### SOA Litoměřice – `tools/soal_zoomify.py`
- Digitálna bádateľňa vyžaduje počiatočné overenie v prehliadači.
- Zisti celú adresu obrázka z network trafficu (`https://images.soalitomerice.cz/.../ImageProperties.xml`).
- Snímku stiahni nástrojom: `python -I -X utf8 tools/soal_zoomify.py "<cela_adresa>" 0 pracovni/x.jpg`.
- Pozor: po cca 100 požiadavkách portál blokuje na 30 minút.

### ZA Opava – `tools/soal_zoomify.py`
- Portál `https://digi.archives.cz/da/` vyžaduje pripojený prehliadač a CAPTCHU rieši používateľ.
- Získaj adresu obrázka a stiahni cez `soal_zoomify.py`. Dodržuj pauzy 3–6 s medzi dopytmi.

### Pražské policajné prihlášky 1850–1914 (Národní archiv) – `tools/policie_prihlasky.py`
- Prihlášky pražských rodín (otec, matka, deti, dátumy a miesta narodenia, sobáš, bydliská).
- Hľadanie: `python -I -X utf8 tools/policie_prihlasky.py Kolar [Jan] [1850] [1870]`.
- Stiahnutie karty: `python -I -X utf8 tools/policie_prihlasky.py karta <poradie> pracovni/karta.jpg Kolar [Jan] [1850] [1870]`.

---

## 3. Ostatné krajiny

- **Rakúsko a Nemecko:** Portál **Matricula Online** (`data.matricula-online.eu`) – rímskokatolícke a evanjelické matriky Viedne, Dolného Rakúska, Burgenlandu a Bavorska bez poplatku a bez prihlásenia (`tools/matricula_dl.sh`).
- **Poľsko:** Portál **Geneteka** (`geneteka.genealodzy.pl`) – dobrovoľnícke indexy narodení, sobášov a úmrtí po vojvodstvách a farnostiach. Dodržuj pravidlo „linkujeme, nesťahujeme masovo“.

---

## 4. Noviny a ročenky – `tools/anno.py`, `tools/kramerius.py`
- **ANNO** (Historické noviny Rakúska a Uhorska 1700–1950, Österreichische Nationalbibliothek):
  `python -I -X utf8 tools/anno.py "priezvisko" 1880 1900`
- **Vojaci 1. svetovej vojny – zoznamy strát (ANNO):**
  `python -I -X utf8 tools/anno.py '"Priezvisko Meno"' 1914 1919 3 --snip --ztraty`
  Hľadá v rakúsko-uhorských zoznamoch strát (`vll` Verlustliste, register `vlv`, ranení `nvv`). Záznam uvádza: hodnosť, pluk, stotina, **domovská obec, ročník**, zranený / zajatý / padlý.
- **Kramerius** (NK ČR / SNK – digitalizované periodiká a monografie):
  `python -I -X utf8 tools/kramerius.py hladaj "priezvisko"`
- Vhodné pre úradníkov, dôstojníkov, učiteľov, remeselníkov a mešťanov.

---

## 5. Mapy stabilného katastra a indikačné skice
- Na `ags.cuzk.gov.cz/archiv` vyhľadajte katastrálne územie, kliknite do mapy → „Indikační skici“ → ID rastru (napr. `HRA235018400`).
- Skica sa dá otvoriť priamo: `https://ags.cuzk.gov.cz/archiv/openmap.html?typ=skicic&idrastru=<ID>` (načítava sa cca 20 s).
- **Čítanie:** v budove je **červeno číslo popisné** a **čierne číslo stavebnej parcely** (pozemkové parcely majú čísla červené); zámena prečíta celú dedinu naopak. Pri pochybnosti over na pár domoch: vrstva pozemkového katastra (archiv_spojene_pk) s adresnými bodmi RÚIAN ukáže, na ktorej parcele stojí dnešné súpisné číslo. „N° 35 Priezvisko“ pri pozemku = patrí k domu č.p. 35. Žltá stavba je drevená, ružová/červená murovaná.
- Zosnímajte výrez so zakrúžkovaným domom predkov a uložte na web k rodine.

---

## 6. Postup zápisu do projektu
1. Snímku stiahnuť alebo zosnímať do `pracovni/` (alebo načítať cez `cache.py`).
2. Zväzok zapísať do `data/svazky.json`:
   ```json
   "fs_bardejov_rk_1890": {
     "archiv": "Štátny archív v Prešove / FamilySearch",
     "portal": "familysearch.org",
     "svazek": "Bardejov, rímskokatolícka matrika krstov 1880–1900",
     "popis": "Rímskokatolícky farský úrad Bardejov",
     "url": "https://www.familysearch.org/ark:/61903/..."
   }
   ```
3. Zápis do `data/zaznamy.json` pomocou `tools/zapis.py`.
4. Výrez zápisu: `python -I -X utf8 tools/vyrez.py pracovni/<stranka>.jpg <kluc> "x0,y0,x1,y1"`.
5. Rámček čítaného riadku: `python -I -X utf8 tools/ramecek.py <kluc> "x0,y0,x1,y1"`.
6. Prepis a preklad do `data/prepisy.json`.
7. Doplnenie údajov osoby do `data/osoby.py`.
