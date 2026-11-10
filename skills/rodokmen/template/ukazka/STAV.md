# Stav rodokmeňa a pravidlá práce

Tento súbor je vstupný bod. Po každom reštarte (nová konverzácia, skrátený kontext) ho agent číta ako prvý,
potom koniec `research_log.md` a sekciu „Rozpracované“.

## Pre koho
- Východisková osoba: Jan Novák (*1890 Holice, †1965 Praha) – Kekulé 1
- Rodina: Novákovci z Holíc a Prahy
- Kto s agentom pracuje a ako chce komunikovať: ukážkový projekt na vyskúšanie rodinného webu

## Kde čo je
| Súbor | Obsah |
|---|---|
| `data/osoby.py` | Priami predkovia podľa Kekulého čísla + rody, boční príbuzní, otvorené otázky, hypotézy. |
| `data/zaznamy.json` | Každý použitý zápis z matriky (kľúč = názov obrázka). |
| `data/svazky.json` | Matričné zväzky (archív, signatúra, odkaz). |
| `data/prepisy.json` | Prepis originálu a preklad každého zápisu. |
| `data/zvyrazneni.json` | Rámčeky – ktoré miesto výrezu čítame. |
| `data/research_log.md` | Denník VŠETKÝCH hľadaní, aj neúspešných. |
| `data/udaje_od_rodiny.md` | Čo povedala rodina, rodinné dokumenty. |
| `data/zajimavosti.md`, `data/pribeh.md` | Texty na web. |
| `data/archivni_dotazy.md` | Čo by sa dalo zistiť len v archíve. |
| `data/mista.json`, `data/dokumenty.json`, `data/web.json` | Mapa, rodinné fotky a dokumenty, nastavenie webu. |
| `vyrezy/`, `zdroje/` | Výrezy zápisov pre web (1800 px) a v plnom rozlíšení. |
| `dokumenty/` | Rodinné dokumenty a fotky od používateľa (originály). |
| `pracovni/` | Pracovné súbory (stiahnuté stránky, kontrolné obrázky) – nejdú na web. |
| `web/` | Rodinný web. `cd web && npm run nahled` (dáta + zostavenie + náhľad); po zmene dát stačí `npm run data && npm run build`. |

## Pravidlá
1. Kým niečo ohlásim ako nové, prehľadám `osoby.py`, `zaznamy.json` a `research_log.md` (meno, miesto, rok).
2. Údaj je „doložené“ (doc) len vtedy, keď som ho prečítal priamo na snímke. Čítanie od pomocníkov overím sám.
3. Každé hľadanie (aj neúspešné) zapíšem do `research_log.md`.
4. Neisté čítanie označím (?) – nič nedomýšľam.
5. Ku každému novému zápisu: výrez (`tools/vyrez.py`), rámček (`tools/ramecek.py`) a prepis s prekladom.
6. Po zmene dát spustím `python -I -X utf8 tools/kontrola.py`.

## Rozpracované (aktualizovať priebežne)
- Hotová ukážková rodina Novákových (260 predkov v 11 generáciách).
