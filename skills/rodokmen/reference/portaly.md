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
  - Ak záznam nie je v indexe, choďte cez *Search → Catalog → Place: Slovakia, [Názov stolice / okresu / farnosti]* (napr. *Slovakia, Šariš, Bardejov*). Tu sú k dispozícii celé nasnímané matričné knihy záber po zábere.

### B. Sčítanie ľudu 1869 (Slovakia Census 1869)
- Zbierka na FamilySearch: *Slovakia Census, 1869*.
- Pokrýva celé rodiny a domácnosti v roku 1869 (meno, vek, rodinný vzťah, náboženstvo, povolanie, gramotnosť, zvieratá a majetok).
- Mimoriadne cenné na zachytenie štruktúry rodiny a potvrdenie generácie prastarých rodičov.

### C. Civilné (štátne) matriky po 1. 10. 1895
- V Uhorsku bola 1. októbra 1895 zavedená štátna matrika.
- Zápisy z rokov 1895–1906+ sú postupne odovzdávané do pracovísk Štátnych archívov SR (Štátny archív v Prešove, Košiciach, Levoči, Banskej Bystrici, Bytči, Nitre, Bratislave).
- Záznamy mladšie ako 100 rokov (narodenia), 75 rokov (sobáše) a 30 rokov (úmrtia) sa nachádzajú na miestnych matričných úradoch miest a obcí. Do nich má prístup len priamy príbuzný (na základe žiadosti a preukázania príbuzenstva).

### D. Cintoríny a náhrobky na Slovensku
- Pre 20. a 21. storočie existujú vynikajúce online databázy s fotografiami hrobov a menami:
  - **cintoriny.sk** – celoslovenský portál evidencie hrobových miest.
  - **virtualnycintorin.sk** – podrobné mapy cintorínov vrátane Bardejova, Prešova a stoviek obcí na východnom aj strednom Slovensku.

### E. Pozemkové knihy a urbáre
- **Urbár Márie Terézie (1767):** pre slovenské obce dostupný na maďarskom portáli `hungaricana.hu` (databáza *Urbáre a súpisy poddanských povinností*).
- Staršie pozemkové knihy a súdne písomnosti spravujú príslušné pracoviská Štátneho archívu SR.

---

## 2. Česko – portály krajských štátnych archívov

| Archív | Oblasť | Portál s matrikami | Stav v skille |
|---|---|---|---|
| SOA Zámrsk | východné Čechy | ARON – aron.vychodoceskearchivy.cz | **hotové nástroje `aron_search.py`, `aron_img.py`** |
| SOA Praha | stredné Čechy | eBadatelna – ebadatelna.soapraha.cz | **nástroj `ebadatelna.py`** |
| SOA Plzeň | západné Čechy | Porta fontium – portafontium.eu | **nástroj `portafontium.py`** |
| SOA Třeboň | južné Čechy | digi.ceskearchivy.cz | **v prehliadači** |
| SOA Litoměřice | severné Čechy | Digitální badatelna – digi.soalitomerice.cz | **`soal_zoomify.py`** |
| AHMP | hl. m. Praha | katalog.ahmp.cz (Pragapublica) | **`ahmp_search.sh`, `ahmp_scan.py`** |
| MZA Brno | južná Morava | Acta Publica – www.mza.cz/actapublica | **v prehliadači** |
| ZA Opava | severná Morava a Sliezsko | Digitální badatelna – digi.archives.cz/da/ | **`soal_zoomify.py`** |
| Národní archiv | židovské matriky, policajné prihlášky | vademecum.nacr.cz, digi.nacr.cz | **`policie_prihlasky.py`** |

---

## 3. Ostatné krajiny

- **Rakúsko a Nemecko:** Portál **Matricula Online** (`data.matricula-online.eu`) – rímskokatolícke a evanjelické matriky Viedne, Dolného Rakúska, Burgenlandu a Bavorska bez poplatku a bez prihlásenia (`tools/matricula_dl.sh`).
- **Poľsko:** Portál **Geneteka** (`geneteka.genealodzy.pl`) – dobrovoľnícke indexy narodení, sobášov a úmrtí po vojvodstvách a farnostiach.

---

## 4. Noviny a ročenky – `tools/anno.py`, `tools/kramerius.py`
- **ANNO** (Historické noviny Rakúska a Uhorska 1700–1950, Österreichische Nationalbibliothek).
- **Kramerius** (NK ČR / SNK – digitalizovaná periodiká).
- Vhodné pre úradníkov, dôstojníkov, učiteľov, remeselníkov a mešťanov.

---

## 5. Postup zápisu do projektu
1. Snímku stiahnuť alebo zosnímať do `pracovni/`.
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
4. Výrez zápisu: `python -I -X utf8 tools/vyrez.py pracovni/<stranka>.jpg <kluc> x0,y0,x1,y1`.
5. Rámček čítaného riadku: `python -I -X utf8 tools/ramecek.py <kluc> x0,y0,x1,y1`.
6. Prepis a preklad do `data/prepisy.json`.
7. Doplnenie údajov osoby do `data/osoby.py`.
