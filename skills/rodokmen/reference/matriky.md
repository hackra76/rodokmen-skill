# Ako čítať matriky – praktický návod

## Druhy kníh
| Skratka | Kniha | Čo v nej je | Prečo je cenná |
|---|---|---|---|
| **N** | narodenia (krsty), *Liber natorum / baptisatorum*, *Geburtsbuch*, *Születési anyakönyv* | dátum narodenia a krstu, dom (súp. č.), dieťa, rodičia (od ~1784 aj ich rodičia a bydlisko), krstní rodičia, pôrodná babica | pohlavie, legitimita, rodičia matky → ďalšia generácia |
| **O** | sobáše (oddaní), *Liber copulatorum / matrimoniorum*, *Trauungsbuch*, *Házassági anyakönyv* | dátum, dom, ženích a nevesta (vek, stav, náboženstvo), ich rodičia, svedkovia | **najlepší prvý cieľ** – otvára dve rodiny naraz |
| **Z** | zomrelí, *Liber defunctorum / mortuorum*, *Sterbebuch*, *Halotti anyakönyv* | dátum úmrtia a pohrebu, dom, meno, vek, príčina | vek → odhad roku narodenia, stav (vdova po…) |
| **I** | index (register) k N/O/Z | meno → dátum / strana | rýchle hľadanie; **index býva neúplný**, negatívny výsledok v indexe nič nedokazuje |

Ďalšie pramene: sčítanie ľudu (1869 na Slovensku a v Uhorsku; 1857–1921 v Česku; domácnosti s dátumami narodenia), urbáre a pozemkové knihy (kto vlastnil aký dom – prepojí generácie cez nehnuteľnosť), vojenské záznamy, domovské listy, parte. Pozri `portaly.md` a `playbook.md` §2.

## Lehoty prístupu k matrikám
- **Slovensko (zákon č. 154/1994 Z. z. o matrikách):** Knihy prechádzajú z matričných úradov do štátnych archívov po uplynutí **100 rokov od posledného zápisu** pre všetky tri druhy (narodenia, sobáše i úmrtia). Cirkevné matriky do roku 1895 sú v štátnych archívoch a zdigitalizované na FamilySearch. Záznamy mladšie ako 100 rokov spravuje príslušný matričný úrad (výpis dostane len priamy príbuzný).
- **Česko (zákon č. 301/2000 Sb.):** Do archívu (online) ide zväzok až po uplynutí: narodenia **100 rokov**, sobáše **75 rokov**, úmrtia **30 rokov** od posledného zápisu v knihe.

Mladšie knihy sú na príslušnom matričnom úrade – výpis dostane len priamy príbuzný (žiadosť + doklady o príbuzenstve). Zapíš do `archivni_dotazy.md`.

## Ako vyzerá hľadanie v praxi
1. **Obec → farnosť.** Malé dediny patrili pod faru v susednej obci; popis zväzku vymenúva všetky obce farnosti.
   Hľadaj obec v popise zväzku, nie len v názve. Obec rozdelená medzi dve fary má dva rady kníh.
2. **Zväzok podľa roku a druhu.** Pozor na prekryvy: jedna kniha pre viac obcí, osobitné knihy pre jednotlivé obce.
   **Druhopisy** (duplikáty pre dekanát či župu/biskupstvo) mávajú N, O a Z jedného roka pri sebe –
   hodia sa, keď originál chýba, je nečitateľný alebo poškodený.
3. **Index, potom kniha.** Index radený podľa písmen a rokov dá stranu/fólio; snímku odhadni a dolaď.
   Staršie registre (18. stor.) občas ukazujú o 1–4 strany vedľa – ak zápis na udanej strane nie je, listuj okolo.
   Veľké fary majú registre aj ako **samostatné zväzky** – hľadaj ich najskôr.
   **Keď matrika chýba** (nie je online alebo sa nezachovala), skús register – býval vedený osobitne a prežil aj tam, kde kniha nie. Zápis v registri dokladá dátum, miesto a otca; zapíš ho ako `prob` (odpis, nie originál).
4. **Bez indexu: listuj chronologicky.** Odhadni pozíciu podľa rokov na prvých a posledných snímkach zväzku (polenie intervalu).
   **Neistý dátum** (číslica z neskoršej poznámky): najprv prejdi všetky možné roky v domovskej farnosti, až potom okolité fary.
5. **Prečítaj celý zápis**, potom sa pozri aj na okolie (dvojičky, ďalšie deti rovnakých rodičov).
6. **Svadba sa zvyčajne konala vo farnosti nevesty** (v jej bydlisku) – hľadaj ju najprv tam, až potom vo fare ženícha.
   V krstnom zápise dieťaťa býva (koncom 19. stor.) pripísaný dátum a miesto sobáša rodičov – over ho v oddaných.
7. **Rodina v katolíckej matrike chýba? Skús evanjelickú, reformovanú alebo židovskú.**
   Na Slovensku aj v Česku po tolerančnom patente (1781) viedli vlastné matriky evanjelické zbory (a. v. aj h. v.), pričom jeden zbor pokrýval desiatky obcí. Židovské matriky pozri v `portaly.md`.

## Čítanie písma a jazyky
- **Jazyky na Slovensku (Uhorsko):** do cca 1840/1850 najmä latinčina, v rokoch 1840–1918 často maďarčina, v evanjelických matrikách bibličtina (slovakizovaná čeština) alebo nemčina, po roku 1918 slovenčina.
- **Jazyky v Čechách a na Morave:** do ~1780 latinčina alebo čeština, potom nemčina (kurent), od ~1860 často čeština, v 20. storočí čeština.
- **Kurent (nemecké novogotické písmo):** stiahni plné rozlíšenie a rozrež stránku na štvrtiny (stĺpec mien + dátumy),
  `magick f.jpg -crop 1250x1650+X+Y +repage ctvrt.jpg`. Dopisované riadky sa ľahko prečítajú nesprávne – údaj z registra vždy over v matrike.
- Priezvisko sa píše foneticky a v čase sa mení (Dvorszký / Dvorschak / Dvorský, Šaršon / Scharschon, Krupka / Kroupa). Hľadaj všetky varianty.
- Priezviská žien: v maďarčine často s príponou `-né` (podľa manžela, napr. *Kovács Jánosné* = manželka Jána Kovácsa) alebo s dievčenským priezviskom (*született* / *szül.*); v nemčine bez „-ová“ (*Maria Novak*).
- Mená v maďarčine: János = Ján, István = Štefan, József = Jozef, Ferenc = František, György = Juraj, Mihály = Michal, András = Andrej/Ondrej, Pál = Pavol, Mária = Mária, Erzsébet = Alžbeta, Katalin = Katarína, Anna, Ilona = Helena, Zsuzsanna = Zuzana.

### Slovníček pojmov (lat. / nem. / maď. → slovensky)
| latinsky | nemecky | maďarsky | slovensky |
|---|---|---|---|
| *natus / baptisatus* | *geboren / getauft* | *született / megkeresztelt* | narodený / pokrstený |
| *copulati / sponsus / sponsa* | *getraut / Bräutigam / Braut* | *összekelt / vőlegény / menyasszony* | zosobášení / ženích / nevesta |
| *mortuus / sepultus* | *gestorben / begraben* | *meghalt / eltemetett* | zomrel / pochovaný |
| *legitimus / illegitimus* | *ehelich / unehelich* | *törvényes / törvénytelen* | manželský / nemanželský |
| *viduus / vidua* | *Witwer / Witwe* | *özvegy* | vdovec / vdova |
| *filius / filia* | *Sohn / Tochter* | *fia / lánya* | syn / dcéra |
| *patrini / testes* | *Pathen / Zeugen* | *keresztszülők / tanúk* | krstní rodičia / svedkovia |
| *agricola, rusticus* | *Bauer* | *földműves, gazda* | sedliak, roľník |
| *inquilinus, inquilina* | *Inwohner, Taglöhner* | *zsellér* | želiar, podruh, nádenník |
| *casarius* | *Häusler* | *házas zsellér* | domkár |
| *civis* | *Bürger* | *polgár* | mešťan |
| *sartor / sutor / faber / textor / molitor* | *Schneider / Schuhmacher / Schmied / Weber / Müller* | *szabó / varga, csizmadia / kovács / takács / molnár* | krajčír / obuvník, čižmár / kováč / tkáč / mlynár |
| *ex, aus, von* | *aus, von* | *helyből, -ból/-ből* | z (obce) |

## Odhad rokov
- Vek pri úmrtí/sobáši je často zaokrúhlený o ±2–5 rokov. Uvádzaj „asi 1756“ a hľadaj krst v širšom časovom intervale.
- Nevesta mávala 18–28, ženích 22–32; deti prichádzali spravidla každých 1,5–3 rokov.
- „Vdovec“ u ženícha = hľadaj prvé manželstvo a deti z neho.

## Stavy údajov v dátach
| stav | kedy |
|---|---|
| `doc` | prečítané priamo na snímke zápisu, ktorý osobu jednoznačne identifikuje |
| `prob` | silná zhoda (meno, doba, miesto, dom, remeslo), ale bez priameho zápisu; vždy `note` prečo |
| `fam` | od rodiny / z rodinného dokumentu |
| `mh` | len z cudzieho stromu na internete |
| `unk` | poznáme len miesto v rodokmeni |

## Typické nástrahy
- Pisár pomýlil meno starého otca (Jozef namiesto Václava) – rozhodne viac zápisov tej istej rodiny.
- Dieťa zapísané pod iným krstným menom, ako ho volala rodina.
- Svadba pár mesiacov pred pôrodom alebo po ňom – bežná situácia; zaujímavosť pre web.
- Nemanželské dieťa nesie priezvisko matky; otec chýba alebo je dopísaný neskôr (legitimácia na okraji).
- Ten istý predok dvakrát v rodokmeni (vzdialení príbuzní sa vzali) – v dátach `SAME`.
- Index nenašiel ≠ zápis neexistuje. Zapíš, čo presne si prešiel.
- Pomocníci (subagenti) a OCR/AI čítajú historické písmo chybne – vždy overuj na snímke sám.

## Technické pravidlá (Windows)
- Python: `python -I -X utf8 tools/<nástroj>.py`. Bez `-X utf8` je výstup do rúry v cp1250 / ANSI, čo spôsobí chyby pri diakritike a špeciálnych znakoch.
- ImageMagick je `magick`, nikdy `convert` (`convert` je vo Windows systémový nástroj na prevod disku z FAT na NTFS). Písmo pre `-annotate`: `-font C:/Windows/Fonts/arial.ttf`.
- Limit dĺžky príkazového riadka je 32 767 znakov – stovky dlaždíc v jednom príkaze nespájaj naraz; skladaj po riadkoch.
- Dátové súbory zapisuj v UTF-8 **bez BOM**.
