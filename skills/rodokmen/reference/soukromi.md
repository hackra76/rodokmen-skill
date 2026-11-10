# Súkromie, etika a cudzie služby

## Žijúci ľudia
- Na webe uvádzaj len meno a rok narodenia (`note="Žijúci – údaje len základné."`). Žiadne adresy, telefóny, rodné čísla,
  zdravotné údaje, rozvody, nemanželské deti u žijúcich či nedávno zosnulých bez výslovného súhlasu rodiny.
- Citlivé témy z nedávnej minulosti (samovraždy, väznenie, vážne choroby) – opýtaj sa používateľa, či a ako ich spomenúť.
- Matričné údaje staršie ako archívne lehoty sú verejné, ale ohľaduplnosť platí aj pre ne (zbytočne nezosmiešňovať).

## Pred zverejnením webu prejdi s používateľom
`python -I -X utf8 tools/kontrola.py` hlási `CITLIVÉ` pri textoch z posledných ~100 rokov (samovražda, choroba, rozvod, dlhy, nemanželské
dieťa…), ktoré idú na web – v poznámkach osôb, v „Čo hľadáme“ (`ISSUES`), pri bočných príbuzných, v zaujímavostiach a v príbehu.
Čo používateľ na webe schváli, zapíš úryvkom do `web.json` → `citlive_schvaleno` (`web.md`).
Údaje z rodinného stromu (GEDCOM) a od rodiny bývajú práve také – pre výskum áno, na web len so súhlasom.
1. Zoznam žijúcich osôb na webe a čo o nich web hovorí.
2. Rodinné fotky a dokumenty – súhlasia tí, ktorí sú na nich (alebo ich rodina)?
3. Prihlasovacia otázka a odpoveď (`web.json`) – nastavená a dostatočne ťažká pre cudzích?
4. Kontakt na webe – chce tam používateľ svoj e-mail?
Až potom zverejni (`npm run nasadit-cloudflare`, kto má web na Netlify `npm run nasadit` – pozri `web.md`).

## Platené a cudzie služby (MyHeritage, Ancestry, Geni, FamilySearch)
- Prihlásenie, platby a predplatné rieši **len používateľ**. Skúšobná verzia sa po skončení automaticky platí – pripomeň,
  kedy končí a kde ju zrušiť.
- **Žiadne hromadné prechádzanie ani sťahovanie.** Automatické sťahovanie záznamov z MyHeritage vedie k zablokovaniu účtu. Čítaj len jednotlivé záznamy, ktoré sú potrebné, ľudským tempom; radšej požiadaj používateľa o export (GEDCOM) alebo o konkrétne snímky.
- Údaje odtiaľ majú stav `mh` a vždy sa overujú v matrikách.

## Archívne portály
Sú bezplatné a verejné, ale servery majú obmedzené kapacity: sťahuj len snímky, ktoré skutočne čítaš, žiadne celé zväzky naraz, paralelne maximálne niekoľko požiadaviek. Citácie uvádzaj vždy až na úroveň konkrétnej snímky.

## Dáta v gite a zdieľanie
Projekt obsahuje osobné údaje rodiny. Ak ho používateľ chce mať na GitHube, potom **len ako súkromné (private) úložisko**.
