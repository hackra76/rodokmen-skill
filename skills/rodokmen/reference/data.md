# Formát dát projektu

Všetky dáta sú v `data/`. Web sa z nich generuje (`npm run data`), nikdy needituj `web/src/data/site.json` ručne.
Po zmenách spusti `python -I -X utf8 tools/kontrola.py`. Ukážku vyplnených dát má `SKILL_DIR/template/ukazka/`.
Položky do JSON súborov pridávaj a meň cez `python -I -X utf8 tools/zapis.py` (zachová formát súboru, pozri SKILL.md).

## `osoby.py` – predkovia
Kekulého čísla: 1 = východisková osoba, otec osoby n = 2n, matka = 2n+1.
| číslo | kto |
|---|---|
| 1 | východisková osoba (u ženy `sex="F"`) |
| 2, 3 | otec, matka |
| 4–7 | starí rodičia (4, 5 otcovi rodičia; 6, 7 matkini) |
| 8–15 | prastarí rodičia = **8 rodov** (`LINES`) |
| 16–31, 32–63 … | každá ďalšia generácia dvojnásobok |

Otec predka 22 je 44, matka 45; dieťa predka 45 je 22 (45 // 2). Muži majú párne čísla.

```python
P = {
 8: dict(n="Jan Novák", y="1890–1944", st="doc",
         f=["* 14. 2. 1890 Holice súp. č. 112", "kováč", "× 20. 6. 1919 Holice Josefa Pokorná", "† 1944 Holice"],
         r=["holice_krest_jan_novak_1890", "holice_snatek_jan_novak_josefa_pokorna_1919"],
         note="Prečo neistota / rozpor / odkiaľ údaj"),
 9: dict(n="Josefa Pokorná", y="* 1895", st="doc", f=[...], r=[...]),
 33: dict(n="otec neuvedený", st="unk", f=[], note="Nemanželský syn; otec v matrike nie je."),
}
```
- `n` meno (ženy rodným priezviskom), `y` roky pre prehľady (`"* 1895"`, `"1890–1944"`, `"asi 1720–1785"`, `"1680 – pred 1740"`,
  `"† 1940"` keď poznáme len úmrtie; nič nevieme → `""`).
- `f` fakty: začínajú `*` (narodenie), `×` (sobáš), `†` (úmrtie) alebo sú voľný text (remeslo, bydlisko).
  Názvy obcí vo faktoch používa mapa (`mista.json` → `re`).
- `r` kľúče zápisov zo `zaznamy.json`. `st` pozri `matriky.md`: `doc` prečítané v matrike, `prob` pravdepodobné,
  `fam` od rodiny (aj strom, ktorý si rodina vedie sama, napr. GEDCOM z jej MyHeritage), `mh` cudzí strom z internetu, `unk`.
- `LINES = {8: ("Novákovci", "Kováči z Holíc…"), …}` – len čísla 8–15; názov rodu = priezvisko v množnom čísle.
- `SIDE` – súrodenci a ďalší príbuzní: `dict(k=<číslo predka>, n="Josef Novák (1865–1920)", t="text", r=[kľúče])`.
- `ISSUES` – dvojice `("Otázka", "Vyriešené: … / Hypotéza: … / Otvorené: …")` → stránka „Čo hľadáme“ (vyriešené sa skryjú).
  Ide na web – nepíš sem citlivé veci (príčiny úmrtia, rodinné spory) bez súhlasu.
- `HYPOTEZY` – `dict(rod=8, nadpis="…", text="…", polozky=[("meno", "text")], zaznamy=[kľúče])` → stránka rodu.
- `SAME = {350: 140}` – predok, ktorý je v rodokmeni dvakrát (alias → hlavné číslo; alias v `P` môže mať `f=["TÁ ISTÁ OSOBA ako 140"]`).

## `zaznamy.json` – zápisy
```json
[{"klic": "holice_krest_jan_novak_1890", "svazek": "1a0b2337", "snimek": 57, "druh": "N",
  "datum": "14. 2. 1890", "nazev": "Krst Jána Nováka",
  "shrnuti": "Ján, syn Václava Nováka, kováča v Holiciach súp. č. 112, a Barbory rod. Malej z Ostřetína.",
  "odkaz": "https://aron.vychodoceskearchivy.cz/apu/…/dao/…/file/…"}]
```
- `klic`: malé písmená bez diakritiky, `obec_druh_kto_rok` (druh: krest, snatek, umrti, index, scitani…). Je to aj názov obrázka.
- `druh`: N, O, Z, I (index/register), S (sčítanie), J (iný prameň).
- `datum` formátovaný s bodkami („14. 2. 1890“, „3/1867“, „1797“) – web podľa neho radí.

## `svazky.json`
`{"1a0b2337": {"archiv": "SOA Zámrsk – Sbírka matrik…", "portal": "ARON", "svazek": "N Holice 1880–1900, sign. …",
"popis": "obce", "url": "odkaz na zväzok"}}` – pri portáli ARON zapisuje `aron_img.py <apu> svazek`.

## `prepisy.json`
`{"<klic>": {"orig": "[Dátum] 14. februára 1890\n[Dom] 112\n[Otec] …", "cs": "Slovenský preklad celou vetou…"}}`
- `orig` verný prepis po stĺpcoch, `[Názov stĺpca]` v hranatých zátvorkách, neisté „(?)“, nečitateľné „[…]“, skratky ponechať.
- `cs` zrozumiteľný preklad pre rodinu; vysvetli staré pojmy (želiar, podruh, bíreš, domkár).

## `zvyrazneni.json`
`{"<klic>": {"boxes": [[x0, y0, x1, y1]], "status": "ok", "note": ""}}` – zlomky šírky/výšky obrázka `vyrezy/<klic>.jpg`.
Zapisuje `ramecek.py`. Rámček má obopnúť celý čítaný zápis (nie len meno).

## `mista.json`
`{"Holice": {"re": "Holic", "dotaz": "Holice, Slovensko", "lat": 48.066, "lon": 17.986}}` – `re` je regulárny výraz hľadaný
vo faktoch osôb (kmeň slova, aby sedelo skloňovanie: „Holic“ nájde Holice aj v Holiciach). Spravuje `mista.py`.
Pozor na kolízie. Hypotéza: `"hypoteza": true, "rod": 8`. Keď OpenStreetMap obec nenájde, skús tretí parameter – dotaz:
`mista.py pridej "Žár" "Žár" "Žár, okres..."` alebo dotaz s väčšou obcou či okresom. Pri **viacznačných názvoch** (Podolie, Lúka, Vieska) over okres a zadaj dotaz so susednou obcou.
Miestopis najlepšie pozná rodina – keď si nie si istý, opýtaj sa.

## `dokumenty.json` – rodinné fotky a dokumenty na webe
`[{"img": "foto_svadba_1919", "popis": "Svadba Jána a Josefy, Holice 1919.", "osoby": [8, 9]}]`
Obrázok ulož cez `vyrez.py dokumenty/<sken>.jpg foto_svadba_1919` (vznikne `vyrezy/` aj `zdroje/`).

## `web.json` – nastavenie webu
Pozri `web.md`.

## Markdown poznámky
- `research_log.md` – tabuľka `| # | dátum | zdroj | rozsah | hľadané | výsledok | citácia |`, nové riadky na koniec, aj negatívne.
  Web ju zobrazuje ako „Výskumný denník“.
- `zajimavosti.md` – `## Nadpis` + text, odkazy `[Meno](/osoba/<slug>/)`.
- `pribeh.md` – „Príbeh <hlavného rodu>“: frontmatter `title`, `lead` + kapitoly `##`; keď súbor neexistuje,
  položka menu sa skryje. Ako písať: `pribehy.md`.
- Poznámky pre agenta v marcdowne píš ako `<!-- … -->` – na web nejdú.
- `archivni_dotazy.md`, `udaje_od_rodiny.md` – voľný text.

## Odkazy na osoby (slug)
Slug = meno bez diakritiky + rok, napr. `jan-novak-1890`; pri kolízii pridá číslo osoby. Presné slugy po `npm run data`
v `web/src/data/site.json` (`people`). Pri premenovaní osoby sa slug zmení – oprav odkazy v textoch.
