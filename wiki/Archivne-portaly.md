# Archívne portály a online pramene

Prehľad zdrojov a digitálnych archívov podporovaných v projekte **Rodokmeň**.

---

## 1. Slovensko

### FamilySearch – cirkevné matriky do roku 1895
- **Zbierka:** *Slovakia Church and Synagogue Books, 1592–1935*
- **Obsah:** Rímskokatolícke, gréckokatolícke, evanjelické (a.v.), reformované (kalvínske) a židovské matriky všetkých farností na území Slovenska.
- **Indexovanie:** Zbierka je rozsiahlo indexovaná. Umožňuje priame vyhľadávanie podľa mena, priezviska, roku a obce.
- **Prezeranie kníh (Catalog):** Ak záznam v indexe chýba, hľadajte cez *Search → Catalog → Place: Slovakia, [Stolica/Farnosť]*. Knihy sú dostupné snímku po snímke.

### Sčítanie ľudu 1869 (Slovakia Census 1869)
- **Obsah:** Záznamy celých domácností v Uhorsku v roku 1869.
- **Údaje:** Mená všetkých členov rodiny, vek, rodinný pomer, vierovyznanie, zamestnanie, gramotnosť a domáce zvieratá.
- **Význam:** Umožňuje bezpečne preklenúť prelom 19. a 20. storočia a overiť generáciu prastarých rodičov.

### Cintoríny na Slovensku
- **cintoriny.sk** a **virtualnycintorin.sk**: Fotografie náhrobkov, presné dátumy narodenia a úmrtia, čísla hrobových miest.

### Pozemkové knihy a urbáre
- **hungaricana.hu**: Tereziánsky urbár (1767) pre slovenské stolice a obce.

---

## 2. Česko

České krajinské archívy majú vlastné digitalizačné platformy:

| Archív | Oblasť | Portál | Spôsob prístupu v skille |
|---|---|---|---|
| **SOA Zámrsk** | východné Čechy | ARON | Priame sťahovanie (`aron_search.py`, `aron_img.py`) |
| **SOA Praha** | stredné Čechy | eBadatelna | Prehliadač + lokálna medzipamäť (`cache.py`, `ebadatelna.py`) |
| **SOA Plzeň** | západné Čechy | Porta fontium | Sťahovanie cez `portafontium.py` s medzipamäťou |
| **SOA Litoměřice** | severné Čechy | Digitální badatelna | Sťahovanie Zoomify (`soal_zoomify.py`) |
| **AHMP** | Praha | Pragapublica | Nástroje `ahmp_search.sh`, `ahmp_scan.py` |
| **SOA Třeboň** | južné Čechy | digi.ceskearchivy.cz | Vstavaný prehliadač archívu (Playwright) |
| **MZA Brno** | južná Morava | Acta Publica | Prehliadač (`mza.cz/actapublica`), skriptom iba hľadanie kníh |
| **ZA Opava** | severná Morava a Sliezsko | Digitální badatelna | Zoomify sťahovanie / prehliadač (CAPTCHA používateľ) |
| **Národní archiv** | ČR / Praha | digi.nacr.cz / VadeMeCum | Policajné prihlášky (`policie_prihlasky.py`), židovské matriky |

---

## 3. Zdieľaná medzipamäť snímok (`tools/cache.py`)

Na zníženie zaťaženia archívov a zrýchlenie práce skill využíva zdieľanú diskovú vyrovnávaciu pamäť (cache):
- Uložená v `~/.cache/rodokmen_snimky/` (Windows: `%LOCALAPPDATA%\rodokmen_snimky`).
- Kapacita: 5 GB s automatickým vymazávaním najstarších nepoužitých súborov (LRU).
- Umožňuje jednorazové stiahnutie snímky (napr. z eBadatelny, Porta fontium alebo manuálneho screenshotu) a opakované vytváranie náhľadov a výrezov bez zaťaženia archívneho servera.
- Príkazy: `cache.py najdi`, `cache.py uloz`, `cache.py orez`, `cache.py stats`.

---

## 4. Zahraničie

- **Rakúsko a Bavorsko – Matricula Online (`matricula-online.eu`):** Cirkevné matriky Viedne a priľahlých diecéz dostupné bezplatne a bez registrácie (`tools/matricula_dl.sh`).
- **Poľsko – Geneteka (`geneteka.genealodzy.pl`):** Dobrovoľnícke indexy narodení, sobášov a úmrtí.
- **Historická tlač – ANNO (Rakúska národná knižnica):** Noviny a úradné vestníky Rakúsko-Uhorska z rokov 1700–1950 (`tools/anno.py`).
- **Česká a slovenská periodiká – Kramerius:** Digitalizovaná dobová tlač pre úradníkov, vojakov, učiteľov a mešťanov (`tools/kramerius.py`).

---

## 5. Ochrana archívov (`tools/slusne.py`)

Digitálne archívy sú verejnou službou s obmedzenou kapacitou serverov:
- Skill využíva nástroj `slusne.py`, ktorý zabezpečuje prísne pauzy medzi požiadavkami (2 až 4 sekundy, pri prehliadaní v prehliadači 5 až 10 sekúnd).
- Archívy neprechádzame hromadne naslepo – sťahujú sa iba konkrétne snímky, ktoré sa práve čítajú.
- Zabudovaný strážca siete (`hlidac_site.py`) zabraňuje neriadeným dopytom a chráni vašu IP adresu pred banom.
- V prípade dočasného výpadku alebo správy o blokovaní je možné web manuálne pozastaviť: `python -I -X utf8 tools/slusne.py zastav <adresa>`.
