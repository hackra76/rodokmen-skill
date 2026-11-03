# Zaujímavosti a príbeh rodu

Pre toto rodina web skutočne číta. Tabuľka mien a dátumov málokoho zaujme, ale „prapradedo sa narodil 267 dní po svadbe“
alebo „rod žil sto rokov v jednom dome“ áno. Nečakaj s tým až na koniec výskumu.

## Zaujímavosti („fun facts“) – zbieraj priebežne
Kedykoľvek pri čítaní zápisu narazíš na niečo nezvyčajné, **hneď** to zapíš do `data/zajimavosti.md` ako krátky odsek
a povedz to používateľovi ako príbeh. Po každom väčšom kole spusti `python -I -X utf8 tools/napady.py`. Nástroj prejde dáta
a vypíše námety (svadby krátko pred pôrodom, rod v jednom dome, sobáše príbuzných, dlhovekosť, epidémie…).
Každý námet si over v zápise predtým, než ho zapíšeš.

Čo býva zaujímavé:
| Typ | Príklad, ako to napísať |
|---|---|
| Svadby na poslednú chvíľu | tabuľka: svadba – dieťa – o koľko dní; „presná trefa“: narodený 267 dní po svadbe – počatý zrejme počas svadobnej noci |
| Nemanželské deti, legitimácia | „Meno prežilo vďaka slobodnej matke“ – priezvisko sa dedilo po matke; poznámka o legitimácii na okraji zápisu |
| Sto rokov v jednom dome | rovnaké číslo domu cez 3–5 generácií, kto sa v ňom narodil a zomrel |
| Predok v rodokmeni viackrát | dedo a babka boli vzdialení príbuzní (`SAME`) – kde sa vetvy spojili |
| Neobvyklé mená | krstné meno po svätici (a ako sa meno v matrikách skomolilo) |
| Významní svedkovia a krstní rodičia | richtár, farár, panský úradník na svadbe remeselníka |
| Dišpenz | svadba s povolením od biskupa (príbuzenstvo, zákaz ohlášok, adventné obdobie) |
| Remeslá v rode | kováči, krajčíri, mlynári, kolári… ako jeden ucelený odsek |
| Osudy žien | dvakrát vdova v priebehu desiatich rokov; slúžka, ktorá si vzala o 25 rokov staršieho vdovca |
| Deti, ktoré skoro osireli | matka zomrela po pôrode, otec počas epidémie – kto deti vychoval |
| Epidémie a vojny | cholera 1831/1855/1866, prvá svetová vojna, španielska chrípka 1918 (príčina úmrtia v zápise!) |
| Moderná doba | civilný sobáš na úrade; presťahovanie po roku 1945 |
| Rodinné rozprávanie vs. matrika | „rodina hovorila Mária, v skutočnosti Anna“; potvrdená rodinná povesť |
| Stratený začiatok | kde línia končí a prečo (vyhorené matriky, nemanželské dieťa bez otca) |
| Noviny | výstrižok o menovaní, vyznamenaní, parte – pridaj obrázok do `dokumenty.json` |

Štýl: nadpis `## Krátky a pútavý`, 2–5 viet, konkrétne dátumy a miesta, odkazy na osoby `[Meno](/osoba/<slug>/)`.
Najlepšie 2–4 daj aj na úvod webu (`web.json` → `zajimavosti_na_uvodu`).
Citlivé veci z 20. storočia (samovraždy, choroby, rozvody, nemanželské deti) píš len so súhlasom používateľa (`reference/soukromi.md`). `kontrola.py` ich stráži.

## Príbeh hlavného rodu
**Hlavný rod** je rod východiskovej osoby (rodné priezvisko, zvyčajne rod č. 8 v `LINES`). Ak používateľ chce iný, nastav
`web.json` → `pribeh.rod`. Príbeh sa volá **„Príbeh <rodu v genitíve>“** (Príbeh Novákovcov, Príbeh Dvorských).
Má vlastnú položku v menu a tvorí hlavný obsah na úvodnej stránke.

**Kedy písať:** len čo má hlavný rod zhruba 5 generácií doložených matrikou. Nečakaj, kým bude „hotovo“, pretože príbeh
sa dá neskôr kedykoľvek doplniť. `kontrola.py` na to upozorní.

**Postup:**
1. Zozbieraj materiál: fakty a poznámky osôb hlavného rodu, `SIDE`, zaujímavosti, `udaje_od_rodiny.md`,
   rodinné spomienky a dokumenty, novinové výstrižky.
2. Napíš **koncept do chatu** a nechaj si ho schváliť používateľom (dĺžka, tón, čo uviesť a čo vynechať). Pod koncept pripíš, čo je z matrík a čo od rodiny. Až po schválení ho ulož.
3. Ulož do `data/pribeh.md`:
   ```markdown
   ---
   title: Príbeh Dvorských
   lead: Jedna pútavá veta – od koho ku komu príbeh vedie.
   ---

   ## Prológ v hmle (1700–1750)
   …
   ## Kováči z čísla 112 (1777–1874)
   …
   ```
4. Nastav `web.json` → `"pribeh": {"menu": "Príbeh Dvorských", "rod": 8, "tlacitko": "Prečítať príbeh Dvorských"}`
   a úvod (`uvod.nadpis`, 2–3 odseky, fotografia).

**Ako má vyzerať** (rozsah cca 800–1500 slov):
- Kapitoly po generáciách, od najstaršieho predka k dnešku. Nadpis = človek alebo jeho rola + roky
  („Kováč z Holíc (asi 1756–1812)“, „Slúžka, ktorá zachránila meno“).
- Každá kapitola 1–3 krátke odseky: kde žil, čím sa živil, svadba, deti, niečo ľudské zo zápisov.
- Konkrétne: dátumy, miesta, čísla domov, citácie zo zápisu v úvodzovkách. Odkazy na osoby `[Meno](/osoba/<slug>/)`.
- Poctivo: čo nevieme s istotou, napíš ako otázku alebo domnienku („zrejme“, „podľa rodiny“). Nič nevymýšľaj kvôli plynulosti.
- Na konci kapitola o dnešku: len mená a vzťahy žijúcich, bez podrobností a citlivých údajov.
- Ostatné rody dostanú svoj priestor na stránkach rodov (popis v `LINES`, `HYPOTEZY`) a v zaujímavostiach.
