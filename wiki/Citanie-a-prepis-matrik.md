# Čítanie a prepis matrík

Metodický návod na prácu s historickými matrikami, písmom a jazykmi.

---

## Druhy matrík

- **N – Narodenia / Krsty** (*Liber natorum / baptisatorum*, *Geburtsbuch*, *Születési anyakönyv*):
  - Uvádza dátum narodenia a krstu, dom (číslo domu), meno dieťaťa, rodičov (od roku 1784 aj starých rodičov a ich bydlisko), krstných rodičov a pôrodnú babicu.
  - Kľúčové pre posun o generáciu dozadu (rodičia matky s rodným priezviskom).
- **O – Sobáše** (*Liber copulatorum / matrimoniorum*, *Trauungsbuch*, *Házassági anyakönyv*):
  - **Najlepší prvý cieľ:** Spája dve rodiny naraz.
  - Uvádza dátum sobáša, vek a stav ženícha i nevesty, mená ich rodičov, bydlisko a svedkov.
  - *Tip:* Svadba sa takmer vždy konala v bydlisku / farnosti nevesty.
- **Z – Úmrtia** (*Liber defunctorum / mortuorum*, *Sterbebuch*, *Halotti anyakönyv*):
  - Uvádza dátum úmrtia a pohrebu, číslo domu, vek a príčinu úmrtia.
  - Pomáha určiť približný rok narodenia (vek zomrelého) a status (napr. *vdova po...*).
- **I – Indexy (Registre):**
  - Abecedné alebo chronologické zoznamy k jednotlivým zväzkom.
  - *Upozornenie:* Negatívny výsledok v registri neznamená, že zápis v knihe neexistuje (vynechané zápisy boli bežné).

---

## Archívne lehoty prístupu

- **Slovensko:** Podľa zákona o matrikách prechádzajú knihy do štátnych archívov po uplynutí **100 rokov od posledného zápisu v knihe** (platí pre N, O aj Z). Mladšie záznamy sú na matričných úradoch a prístup k nim má len priamy potomok.
- **Česko:** Lehoty pre archívy: narodenia **100 rokov**, sobáše **75 rokov**, úmrtia **30 rokov**.

---

## Písmo a jazyky

### Kurent (nemecké novogotické písmo)
V Čechách a na Morave (od konca 18. storočia do cca 1860) boli zápisy písané nemeckým kurentom.
- Na jeho spoľahlivé čítanie sa vytvára zväčšený výrez s vysokým rozlíšením:
  ```bash
  magick f.jpg -crop 1250x1650+X+Y +repage ctvrt.jpg
  ```
- Neisté písmená a skratky sa overujú porovnaním s inými slovami toho istého farára na tej istej strane.

### Jazyky na Slovensku
- **Do cca 1840/1850:** Prevažne **latinčina**. V evanjelických matrikách často slovakizovaná biblická čeština alebo nemčina.
- **1850 – 1918:** Prevažne **maďarčina** (po rakúsko-uhorskom vyrovnaní v roku 1867 povinná).
- **Po roku 1918:** Slovenčina.

### Mená a priezviská v Uhorsku
- Mená boli zapisované podľa úradného jazyka:
  - *Ján* → *Joannes* (lat.) → *János* (maď.)
  - *Štefan* → *Stephanus* → *István*
  - *Juraj* → *Georgius* → *György*
  - *Michal* → *Michael* → *Mihály*
  - *Mária* → *Maria* → *Mária*
  - *Katarína* → *Catharina* → *Katalin*
  - *Alžbeta* → *Elisabetha* → *Erzsébet*
- Priezviská sa písali foneticky maďarským pravopisom (napr. *Dvorský* ako *Dvorszky* / *Dvorszkij*, *Jurčák* ako *Jurcsák*).
- Manželky mali často príponu *-né* (napr. *Kovács Istvánné* = manželka Štefana Kovácsa).

---

## Základný genealogický slovníček

| Latinčina | Nemčina | Maďarčina | Slovenčina |
|---|---|---|---|
| *natus / baptisatus* | *geboren / getauft* | *született / keresztelt* | narodený / pokrstený |
| *copulati / sponsus / sponsa* | *getraut / Bräutigam / Braut* | *összekelt / vőlegény / menyasszony* | sobášení / ženích / nevesta |
| *mortuus / sepultus* | *gestorben / begraben* | *meghalt / eltemetett* | zomrel / pochovaný |
| *legitimus / illegitimus* | *ehelich / unehelich* | *törvényes / törvénytelen* | manželský / nemanželský |
| *viduus / vidua* | *Witwer / Witwe* | *özvegy* | vdovec / vdova |
| *patrini / testes* | *Pathen / Zeugen* | *keresztszülők / tanúk* | krstní rodičia / svedkovia |
| *agricola, rusticus* | *Bauer* | *földműves, gazda* | roľník, gazda |
| *inquilinus* | *Inwohner, Taglöhner* | *zsellér* | želiar, nádenník |
| *casarius* | *Häusler* | *házas zsellér* | domkár |
