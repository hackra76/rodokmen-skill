# Metodika – spájanie záznamov, stotožnenie, mŕtve body, pramene mimo ČR

Čítaj podľa potreby: keď nevieš, či ide o tú istú osobu, keď sa hľadanie zasekne (mŕtvy bod), alebo keď stopa vedie
mimo ČR (Slovensko, Rakúsko, Poľsko, Nemecko, Maďarsko). Čítanie matrík a slovníček: `matriky.md`, portály a ako
z nich brať snímky: `portaly.md`, formát dát: `data.md`.

## Spájanie záznamov – čím prepojiť generácie
- **Súpisné číslo (čp./číslo domu).** Ján Novák v č. 12 v úmrtí 1820 (70 rokov) a Ján Novák v č. 12 v sobášnom zápise 1788 = najskôr
  tá istá usadlosť. **Prečíslovanie** (po požiari, novou výstavbou, v mestách a na predmestiach) rozdelí dedinu; jeden dom máva
  v čase dve čísla. Pochybnosť over na indikačnej skici stabilného katastra 1824–43 (`portaly.md` → Mapy stabilného katastra).
- **Prímeno / meno po chalupe (vulgo).** „Wenzel Schmid vulgo Bauer“ – meno gruntu prežije výmenu držiteľa a prejde aj na
  zaťa, ktorý sa priženil. **Nie je to priezvisko:** keď sa „priezvisko“ pri prevzatí statku zmení, vysvetlí to gruntová/pozemková kniha.
- **Krstní rodičia (kmotri) a svedkovia (okruh rodiny a susedov).** Rovnaké tri páry kmotrov pri ôsmich krstoch 1790–1810 = jedna rodina;
  zmena kmotrov môže znamenať nové manželstvo. Pozor: kmotri často pochádzali z ustálených „kmotrovských“ rodín, nemusia
  byť nutne príbuzní.
- **Stav v zápise.** Sedliak → výmenník (*Ausgedinger*) v rovnakom dome = starý hospodár odovzdal grunt. **Výmenník nie je automaticky
  otec** nového hospodára (môže byť svokor, nevlastný otec, cudzí predávajúci) – vzťah uvádza gruntová kniha.
  Domkár ≠ sedliak rovnakého mena; stav sa ale môže zdvihnúť sobášom na grunt.
- **Gruntová (pozemková) kniha ako doklad pôvodu.** „Václav predáva synovi Jánovi … dedičské diely bratovi Matejovi, sestre Anne“ –
  jeden zápis menuje rodičov, dieťa aj súrodencov. Pozemkové knihy bývajú dôslednejšie ako matriky („išlo o peniaze“).
  Výplaty podielov sa pripisovali aj o desiatky rokov neskôr – datuj každú zvlášť.
- **Sirotské knihy** uvádzajú vek sirôt → okno pre krsty (veky zaokrúhlené).
- **Svadobné zmluvy:** veno nevesty „od otca Juraja, sedliaka v X“ ukáže farnosť jej pôvodu. Bývajú
  v mestských knihách, nielen v knihách panstva.
- **Pozostalosti (po 1850 pri súdnom okrese)** menujú dedičov aj v iných okresoch a vo Viedni. Fondy bývajú
  výberové alebo skartované.
- **Pomenovanie:** prvý syn často po starom otcovi. Samo osebe slabý doklad.
- **Pomaďarčenie a ponemčenie mien osôb aj miest:** Kováč → Kovács, Dvorský → Dvorszkij / Dvorszky, Šimek → Schimek,
  Bytča = Nagybiccse; v maďarských prameňoch býva priezvisko pred krstným menom (*Nagy János*), v poľských prípona `-owa`
  miesto `-ová`. Hľadaj všetky jazykové tvary.
- **Miestopisné slovníky:** Retrospektivní lexikon obcí, Historický lexikon obcí (ČR), Vlastivedný slovník obcí na Slovensku,
  Helységnévtár 1877/1913 (Uhorsko, teda aj Slovensko), Słownik geograficzny (Poľsko), miestopisný slovník GenTeam / oefr
  (cca 72 000 obcí Predlitavska s farskou príslušnosťou). Farskú príslušnosť ber podľa roku udalosti.
- **Legitimizácia na okraji** (*legitimatus/legitimiert durch nachfolgende Ehe am …*) určí otca – poznámka môže byť aj v inej knihe
  (v sobášnom zápise rodičov, v neskoršom odpise).
- **Domovské právo (Heimatrecht).** Viedenská policajná prihláška, kmeňový list vojaka aj domovský list uvádzajú
  domovskú obec → domovská farnosť. **Domovská obec ≠ miesto narodenia** (domovské právo sa získavalo aj pobytom alebo sobášom).

## Stotožnenie – kedy je to tá istá osoba
- **Východiskové pravidlo:** dve osoby rovnakého mena spoj len podľa **dvoch nezávislých znakov** – číslo domu, obaja rodičia,
  manžel(ka), rovnaký okruh krstných rodičov, presný dátum narodenia. Každý znak z iného zápisu (iný zapisovateľ/oznamovateľ).
  Jeden znak alebo len meno a doba = `prob` s `note` prečo; rozpor do `ISSUES`.
- **Bratranci rovnakého mena v jednej dedine:** dom sám nestačí (bývali vedľa seba aj v jednom dome) – vyžaduj rodičov **aj** manželku.
- **Vdova znova vydatá** vystupuje pod dvomi priezviskami po mužoch: spájaj podľa **rodného priezviska a mena otca**
  v oboch sobášnych zápisoch.
- **Rozpor medzi prameňmi:** originál má prednosť pred odpisom; zvažuj, kto údaj oznámil a ako dlho po udalosti
  (dátum narodenia v úmrtnom zápise, ktorý hlásil sused, je slabší ako krstný zápis). Rozpor zapíš do `ISSUES`.
- **Nevlastné rodiny:** výmenník môže byť nevlastný rodič; vzťah uvádza gruntová kniha.
- **Nájdenec (Findelkind):** bez rodičov – spoj cez číslo nálezinca (viedenský nálezinec, Findelhaus) a obec dojky.
- **Vojaci:** dva znaky sú **pluk a domovská obec** (z kmeňového listu / zoznamu strát).
- **Písanie priezvisk pred ~1800:** farár písal podľa počutia (Kovář/Kovárz, Šimek/Schimek, Ján/Joannes). Drobné odchýlky
  nie sú rozpor, pozor ale na podobné skutočne odlišné priezviská v jednej dedine.

## Najčastejšie chyby, ktoré vedú na zlú vetvu
- **Prečíslovaný dom** – rovnaká rodina, iné súpisné číslo.
- **Vek pri úmrtí bez tolerancie** – „krst nenájdený“; rozšir okno, starým ľuďom vek skôr pribúda. Vek v rokoch,
  mesiacoch a dňoch býva presnejší.
- **Miesto sobáša = pôvod nevesty** sa nepredpokladá napevno – ohlášky (poznámka o ohláškach v inej fare) a
  pozemková kniha ukážu, odkiaľ bola.
- **Latinské meno zle preložené** (Joannes ≠ Joachim, Stephanus = Štefan/Štěpán, Emericus = Imrich).
- **Maďarský alebo historický názov obce nenapárovaný** – dedina „na Slovensku neexistuje“; nájdi ju v Helységnévtári.
- **Kmotr považovaný za príbuzného, výmenník za otca** – pozri vyššie.
- **Miesto narodenia vojaka zamenené za domovskú obec.**
- **Židovské priezviská:** povinné od 1787 (Jozef II.), predtým len otcovské mená (patronymiká). Familiantské knihy.
- **Konvertita:** predošlá totožnosť zmizne; krst dospelého máva poznámku o konverzii → hľadaj v židovskej matrike.
- **Evanjelik hľadaný len v evanjelickej matrike:** aj po tolerančnom patente (1781) zapisoval narodenia, sobáše a úmrtia
  nekatolíkov zhruba do roku 1849 (v Uhorsku aj skôr/čiastočne podľa fár) aj katolícky farár – skús obe.
- **Starokatolíci** (štátne uznaní 1877) – po tomto roku môžu v katolíckej matrike chýbať; vo Viedni sú druhopisy
  starokatolíckych matrík v mestskom archíve (WStLA).
- **Úmrtie vo Viedni hľadané v domovskej fare** – zápis je vo viedenskej farnosti (alebo v protokoloch ohliadania mŕtvol).
- **Meno poangličtené v USA** – v domácich knihách „neexistuje“; pôvodný tvar dajú lodné zoznamy a naturalizácia.
- **Dieťa vojaka „chýba“** – mohlo byť zapísané vo vojenskej matrike pluku, nie vo farskej.
- **Dvojité započítanie:** druhopis a originál nie sú dva nezávislé pramene – jeden je odpis druhého.

## Mŕtve body – čo skúsiť, v tomto poradí
- **Pred 1784 (staré matriky chýbajú alebo nestačia):** 1. staršie spoločné knihy N/O/Z prečítať celé (nielen register)
  → 2. gruntové knihy panstva / urbáre (na Slovensku **Urbár Márie Terézie 1767** na hungaricana.hu) → 3. sirotské knihy,
  svadobné zmluvy → 4. tereziánsky kataster (1713–57) → 5. súpis poddaných 1651, berní rula 1654 (Morava: lánové registre 1669–79).
  Spája **grunt/dom a postupnosť držiteľov**. Pri sedliakoch so zachovanými gruntovými knihami je reálne dno **okolo roku 1650**.
- **Kniha sa nezachovala:** druhopisy a samostatné registre, gruntové knihy, súpisy (konskripcie), pri mužoch
  vojenské odvodové listiny (Musterlisten). Spája číslo domu.
- **Nemanželské dieťa:** legitimizácia na okraji → neskorší sobáš matky → krstní rodičia → súdny spis o otcovstve →
  gruntová kniha. Spája matka a dom dieťaťa.
- **Odišiel do Viedne:** viedenská farnosť → policajné prihlášky: pre narodených pred 1897 zbierka „Austria, Vienna,
  Population Cards, 1850–1910“ na FamilySearch (Meldezettel, čiastočne indexovaná – meno, narodenie, príchod
  a odchod), mladšie cca 1904–1975 len písomnou žiadosťou u WStLA (platené aj pri negatívnom výsledku) → pozostalosť →
  domovská obec.
- **Vysťahoval sa do USA:** lodné zoznamy (Ellis Island / Castle Garden) → naturalizácia → cirkevné a krajanské spolky → poznámky na okraji
  v domovskej fare. Spája **názov obce v pôvodnom pravopise**.
- **Vojak:** najprv **pluk** (podľa domovskej obce; doplňovacie okresy plukov uvádza Wredeho prehľad) → do 1820
  odvodové listiny (Musterlisten, po plukoch a rokoch) / od 1820 kmeňové listy (Grundbuchblätter) → vojenské matriky
  pluku (vo Viedni, uzavreté 100 rokov) → zoznamy strát 1914–18 (`portaly.md` → Noviny a ročenky) a kartotéka strát vo Viedni.
  Kmeňové listy mužov s domovskou obcou v Čechách, na Morave a v Sliezsku: ročníky cca 1865–1886 vo VÚA–VHA Praha,
  pre územie **Slovenska** sú kmeňové listy z rokov 1865–1900 vo **VHA Bratislava** (časť po 1887–1898 skartovaná);
  staršie ročníky vo Viedni (Kriegsarchiv, cca 1820–1864 aj na mikrofilmoch FamilySearch). Pri chýbajúcich kmeňových listoch
  hľadaj v zoznamoch strát a matrikách.
- **Nájdenec:** záznamy nálezinca → fara dojky. Spája číslo nálezinca.
- **Zápis 20. storočia ešte neverejný:** matričný úrad (ČR: zápisy staršie ako lehota ktokoľvek, mladšie rodina; SK: len
  rodina – pozri nižšie), Standesamt (DE, AT), kartotéka HOK (sudetskí Nemci), policajné prihlášky. Do `archivni_dotazy.md`.
- **Sudetonemecká rodina po 1945:** Heimatortskartei (HOK) → spisy Lastenausgleich → obecné zoznamy obyvateľov a
  nezvestných (všetko Bundesarchiv Bayreuth, nižšie). Spája bydlisko k 1. 9. 1939.
- **Zmena mena, jazykové tvary:** všetky tvary osoby aj miesta (vyššie).

## Pramene mimo ČR (Slovensko, Rakúsko, Poľsko, Nemecko, Maďarsko)
Portály, ktoré skill pozná (FamilySearch, Matricula, Geneteka), a ako z nich brať snímky: `portaly.md`.
Ostatné archívy sú väčšinou len na písomnú žiadosť – zapíš do `archivni_dotazy.md`.

**Slovensko**
- **Cirkevné matriky** (rím. kat., gréckokatolícke, evanjelické a.v., reformované, židovské) od 1592, dnes v štátnych archívoch
  (Zbierka cirkevných matrík). Snímky a neúplný index (najmä krsty) na FamilySearch (*Slovakia Church and Synagogue Books, 1592–1935*), spravidla do ~1895.
- **Civilné (štátne) matriky** od 1. 10. 1895 (uhorský zákon), na matričnom úrade; do štátneho archívu prechádzajú až po 100 rokoch.
- **Sčítanie 1869** na FamilySearch (*Slovakia, Census, 1869*): celé domácnosti s rokmi a miestami narodenia, náboženstvom
  a povolaním; len snímky bez menného registra a najmä z archívov Bytča, Banská Bystrica a Nitra (a priľahlých stolíc). Výborná náhrada za neindexované matriky.
- **Matričný úrad (Slovensko):** kým je kniha na úrade (100 rokov od posledného zápisu), výpis dostane len osoba, ktorej sa zápis
  týka, alebo člen rodiny (manžel, rodičia, deti, vnuci, pravnuci, prapravnuci, súrodenci a ich deti) – bez ohľadu
  na vek zápisu (zákon 154/1994 Z. z., § 18). Doslovný výpis len pre úrady; súkromná osoba môže v prítomnosti
  matrikára nahliadnuť do knihy a urobiť si výpis.
- Do 1918 Uhorsko – obce hľadaj aj pod maďarským názvom (Helységnévtár).

**Rakúsko (aj Viedeň, Burgenland)**
- **Katolícke matriky do 1938** v diecéznych archívoch, snímky na Matricule (Viedeň, Linec, St. Pölten, Štajerský
  Hradec, Tirolsko, Korutánsko, Salzburg, Vorarlbersko). Burgenland (Eisenstadt) má vlastný portál matriken.at
  (zatiaľ neúplný). Matricula nemá vyhľadávanie podľa mien.
- **Evanjelické matriky** (a. v., h. v.) od 1783, časť tiež na Matricule.
- **Od 1. 1. 1939 civilné matriky** (Standesamt); cirkevné knihy po 1938 sú len cirkevné, bez práva nahliadať.
- **Kriegsarchiv (Viedeň), všetko offline:** vojenské matriky 1633–1938 (podľa pluku, 100 rokov uzavreté), kmeňové listy
  1820–1918 (ročníky cca 1790–1900; ročníky do ~1864 sú aj na mikrofilmoch FamilySearch), odvodové listiny
  1740–1820 (podľa pluku a roku), kartotéky strát 1914–18 (cca 40 miliónov kariet vrátane zajatcov a padlých, písomná žiadosť).
  Vyše 90 % písomností je nemecky – čítanie kurentu je nutnosť.
- **Wiener Stadt- und Landesarchiv (WStLA):** policajné prihlášky cca 1904–1975 (len žiadosťou, originály nepožičiava;
  staršie pre narodených pred 1897 na FamilySearch), protokoly ohliadania mŕtvol (Totenbeschauprotokolle), pozostalosti
  (Verlassenschaften), druhopisy starokatolíckych matrík.

**Poľsko (Tešínsko, Horné Sliezsko, Halič, Spiš/Orava)**
- **Farské matriky (metryki)** v diecéznych a štátnych archívoch (AP), časť snímok na Matricule a FamilySearch,
  index Geneteka.
- **Civilné matriky (USC):** v pruskom zábore od 1874, jednotne od dekrétu 25. 9. 1945; do štátneho archívu (AP)
  po uplynutí lehoty. Katalóg štátnych archívov: szukajwarchiwach.gov.pl.

**Nemecko (sudetskí Nemci, pohraničie)**
- **Standesamt** (civilné matriky) od 1. 1. 1876 (Prusko 1874).
- **Heimatortskartei Sudetendeutsche (HOK)** – kartotéka podľa bydliska k 1. 9. 1939 s povojnovou adresou;
  dnes Bundesarchiv Bayreuth (fond B 530), len písomnou žiadosťou. Tamže **spisy Lastenausgleich** (odškodnenie
  vysídlených, od 1949) a **Gemeindeseelenlisten / Gemeindevermisstenlisten**. Kirchlicher Suchdienst skončil 2015.

**Maďarsko (viedlo štátne matriky aj pre Slovensko 1895–1918)**
- **Štátne civilné matriky** od 1. 10. 1895; druhopisy do 31. 12. 1980 v župných archívoch MNL, inak matričný úrad
  (anyakönyvi hivatal).
- **Cirkevné matriky** v cirkevných archívoch – každý má vlastné lehoty (napr. 90 rokov od založenia knihy).

## Lehoty prístupu mimo ČR
(ČR pozri `matriky.md`.) Počty rokov narodenia / sobáše / úmrtia:
| krajina | lehota | počíta sa od | poznámka |
|---|---|---|---|
| **Slovensko** | 100 / 100 / 100 | posledného zápisu | potom prechádza do štátneho archívu; aj úmrtia po ~1926 sú na matričnom úrade |
| **Rakúsko** | 100 / 75 / 30 | zápisu (zákon) – diecézny archív Viedeň počíta od uzavretia knihy | 100 a 75 rokov len ak sa zápis netýka žijúcej osoby; po 1938 Standesamt |
| **Nemecko** | 110 / 80 / 30 | roku registra | úmrtia Sonderstandesamt Bad Arolsen 80 rokov; skôr len priami príbuzní alebo právny záujem |
| **Poľsko** | 100 / 80 / 80 | uzavretia knihy | do štátneho archívu do 2 rokov po lehote – online dostupnosť sa oneskoruje |
| **Maďarsko** | 110 / 86 / 30 | roku po založení registra | staršie stránky archívov MNL uvádzajú neplatné lehoty z 2014; citlivé údaje (náboženstvo, nemanželský pôvod, príčina smrti) až 60 rokov po smrti |

Lehoty počítané od roku registra alebo uzavretia knihy (DE, PL) sa posúvajú raz ročne. Citlivé údaje pri nedávno zosnulých nezverejňuj – pozri `soukromi.md`.

## Míľniky vedenia záznamov
| rok | čo sa zmenilo | čo to znamená pre hľadanie |
|---|---|---|
| 1651 | súpis poddaných podľa viery (Čechy) | celé rodiny s vekom; neúplný, bez registra mien |
| 1654 | berní rula (Čechy) | len hospodári s pôdou; kotva postupnosti na grunte |
| 1715 / 1720 | regnikolárne súpisy port (Uhorsko/Slovensko) | súpis hláv rodín poddaných podľa stolíc a obcí |
| 1740–1820 | vojenské odvodové listiny (Musterlisten) | vek, pôvod, rodina vojaka – potrebuješ pluk |
| 1767 | tereziánsky urbár (Uhorsko/Slovensko) | zoznam sedliakov, želiarov a podželiarov v obci (hungaricana.hu) |
| 1770/71 | konskripcia a číslovanie domov (Čechy, Morava; Uhorsko 1784–87) | súpisné číslo sa stáva kľúčom k prepojeniu; pozor na neskoršie prečíslovanie |
| 1781 | tolerančný patent | vznikajú evanjelické zbory, nekatolíkov ale ďalej zapisuje aj katolícky farár |
| 1784 | jozefínsky patent: oddelené knihy N/O/Z s predpísanými stĺpcami | jednotné stĺpce; ďalej pozri `matriky.md` |
| 1785–89 | jozefský kataster | majitelia pozemkov po obciach |
| 1820 | kmeňové listy vojakov (Grundbuchblätter) | osobný list s civilným povolaním, sobášom a deťmi |
| 1850 | koniec panstiev, vznik okresných úradov a súdnych okresov | pozemkové a sirotské záznamy prechádzajú z fondov panstiev do súdnych fondov |
| 1869 | prvé sčítanie ľudu v Uhorsku (Slovensko) | celé domácnosti a dátumy narodenia (FamilySearch – najmä Bytča, BB, Nitra) |
| 1871 | nové pozemkové knihy pri súdoch | do 1950/64 pri katastrálnych úradoch |
| 1895 | civilné matriky v Uhorsku (aj Slovensko) | súbežný štátny rad od 1. 10. 1895, cirkevné knihy pokračujú |
| 1914–18 | zoznamy strát, kartotéky strát | hlavná náhrada za stratené kmeňové listy |
| 1919 | kmeňové listy ročníkov 1865–1900 s domovom v nástupníckych štátoch | Čechy vo VHA Praha, Slovensko vo VHA Bratislava (mladšie čiastočne skartované) |
| 1939 | Rakúsko: civilné matriky | cirkevné knihy po 1938 bez práva nahliadať |
| 1950 | Československo: jednotné štátne matriky | farské knihy prestávajú byť úradnými záznamami |
