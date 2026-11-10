# Rodokmeň – skill a plugin pre Antigravity & Claude Code

![Rodokmeň z matrík a rodinný web – vejár predkov, mapa a zaujímavosti](docs/banner.jpg)

Antigravity (aj Claude) vás prevedie tvorbou rodokmeňa **od rodinných spomienok cez digitalizované matriky až po pekný rodinný web**
s vejárom predkov, mapou, príbehom rodu a výrezmi pôvodných zápisov s prepisom a prekladom.
Je určený pre ľudí, ktorí genealógiu nikdy nerobili a neprogramujú – technickú prácu robí agent, vy dodávate
znalosť rodiny a rozhodujete.

Vznikol pri skutočnom hľadaní predkov.

**Autor pôvodného skillu:** Jindřich Šaršon ([sarsonj@gmail.com](mailto:sarsonj@gmail.com), [GitHub](https://github.com/sarsonj), [pôvodný repozitár](https://github.com/sarsonj/rodokmen-skill))  
**Port pre Google Antigravity & slovenský preklad:** Radovan Dvorský ([GitHub](https://github.com/hackra76/rodokmen-skill))

**Aktuálna verzia: 0.10.0 (Antigravity port).** Zoznam zmien nájdete v [histórii repozitára](https://github.com/hackra76/rodokmen-skill/commits/main) a v [CHANGELOG.md](CHANGELOG.md).

> **Kým začnete**
>
> Tento skill **nenahrádza profesionálneho genealóga** ani skúseného bádateľa. Je to pomôcka, ktorá dokáže rýchlo prejsť veľké množstvo matrík.
> Umelá inteligencia však robí chyby: zle prečíta meno, pomýli si dve osoby s rovnakým menom z tej istej dediny alebo spojí rodiny, ktoré
> k sebe nepatria. Skill sa tomu snaží brániť – pri každom údaji je zdroj a výrez pôvodného zápisu, údaje sa navzájom
> kontrolujú a neisté veci sú označené. Za správnosť rodokmeňa však ručíte vy. Používate ho na vlastnú zodpovednosť.
>
> Projekt vznikol aj ako **test toho, kam súčasná AI dosiahne**. Staré písmo (kurent, novogotika), latinčina, maďarčina, skratky farárov,
> rovnaké mená a dlhé reťazce hypotéz predstavujú náročnú výzvu.
>
> Kto potrebuje rodokmeň, na ktorý sa dá právne spoľahnúť (dedičstvo, publikácie, sporné prípady), alebo sa zasekne na mieste,
> kam matriky nestačia, odporúčame obrátiť sa na odborníkov (napr. Slovenská genealogicko-heraldická spoločnosť pri MS v Martine,
> Česká genealogická a heraldická spoločnosť v Prahe, Moravská genealogická a heraldická spoločnosť v Brne).

## Ako vyzerá web
Ukážkový web s vymyslenou rodinou (260 predkov v 11 generáciách) má na úvodnej stránke príbeh rodu, zaujímavosti,
mapu, kde predkovia žili, osem rodov a vejár predkov. Ďalšie stránky: rodokmeň po rodinách, karty osôb, výrezy zápisov
s prepisom a prekladom, „Čo hľadáme“ a denník hľadania. **[Pozrite si celú úvodnú stránku ukážky →](docs/ukazka-web.png)**

## Čo budete potrebovať
- **Google Antigravity** (alebo Claude Code) a prístup k modelom. Rodokmeň je
  dlhá a podrobná práca. Odporúčaný hlavný model je silný uvažovací model (v Antigravity rad Pro, napr. Gemini Pro; v Claude Code Claude Opus). Pomocníci na hľadanie môžu bežať na úspornejších modeloch (Flash / Sonnet).
- **Počítač s Windows, macOS alebo Linuxom** (Windows 11 s Pythonom z python.org a Git Bashom).
- Programy **Python 3, Node.js, ImageMagick a git**. Nemusíte ich inštalovať vopred – agent skontroluje, čo chýba,
  a pomôže s inštaláciou (na Windows cez winget, na Macu cez Homebrew).
- Pre vybrané archívy (SOA Třeboň, MZA Brno, ZA Opava) **prehliadač pre agenta** – príkaz `/browser` alebo MCP server Playwright/Puppeteer. Tieto archívy sťahovacie nástroje nepúšťajú, agent preto číta matriky priamo v ich prehliadači.
- Voliteľne bezplatný účet na [Cloudflare](https://dash.cloudflare.com) (odporúčané) alebo [Netlify](https://www.netlify.com), ak chcete web zverejniť pre rodinu.

## S akými modelmi to funguje
- **Antigravity:** Hlavný model **Gemini Pro** (či ekvivalentný najsilnejší model). Pomocníci (subagenti) pre čítanie a hľadanie bežia na **Gemini Flash**. Hlavný model vždy overuje nález na snímke.
- **Claude Code:** Hlavný model **Claude Opus 5.5**, pomocníci na **Claude Sonnet 5.5**.

## Inštalácia

### Do Google Antigravity
1. **Ako globálny plugin (odporúčané):**
   Skopírujte alebo naklonujte repozitár do priečinka používateľských pluginov:
   - Na Windows: `%USERPROFILE%\.gemini\config\plugins\rodokmen`
   - Na macOS / Linuxe: `~/.gemini/config/plugins/rodokmen`
   ```bash
   git clone https://github.com/hackra76/rodokmen-skill ~/.gemini/config/plugins/rodokmen
   ```
2. **Alebo pre konkrétny projekt / workspace:**
   Skopírujte priečinok `skills/rodokmen` do `.agents/skills/rodokmen` vo vašom projekte.
3. Reštartujte Antigravity, aby sa nový plugin/skill načítal.

### Do Claude Code
```bash
/plugin marketplace add hackra76/rodokmen-skill
/plugin install rodokmen@rodokmen-skill
```
Alebo ručne skopírovaním `skills/rodokmen` do `~/.claude/skills/`.

## Prvé spustenie
1. Spustite Antigravity (či Claude Code) a napíšte:
   > Chcem urobiť rodokmeň svojej rodiny.
2. Agent skontroluje programy, založí priečinok projektu (napr. `~/Rodokmen`) a začne sa pýtať na rodinu.
   Pripravte si, čo viete o rodičoch, starých rodičoch a prastarých rodičoch, a rodinné dokumenty (rodné a sobášne listy, úmrtné listy, parte,
   fotografie, rodinné zápisky) – stačí odfotiť mobilom.
3. **Nabudúce otvárajte Antigravity priamo v priečinku projektu** (napr. `~/Rodokmen`). Agent načíta pravidlá z `AGENTS.md` a `data/STAV.md`, zistí, kde ste skončili, a nadviaže.

Chcete najprv vidieť, ako web vyzerá? Povedzte: *„Ukáž mi ukážkový web.“* Agent založí ukážkový projekt s vymyslenou rodinou a spustí náhľad.

## Ako to prebieha
| Fáza | Čo robíte vy | Čo robí agent |
|---|---|---|
| 0. Príprava | potvrdíte inštaláciu programov | založí projekt |
| 1. Rozhovor | rozprávate, dodáte dokumenty, opýtate sa príbuzných | zapisuje, číta dokumenty, navrhuje otázky |
| 2. Matriky | rozhodujete sporné miesta | hľadá zväzky, sťahuje a číta zápisy, robí výrezy, prepisy a preklady, vedie denník hľadania |
| 3. Príbehy | doplníte rodinné historky, schválite texty | priebežne zbiera zaujímavosti, napíše „Príbeh <vášho rodu>“ |
| 4. Web | pozeráte sa a hovoríte, čo upraviť | stavia web a ukazuje náhľad |
| 5. Zverejnenie | založíte účet na Cloudflare / Netlify, schválite obsah | nasadí web s prihlásením rodinnou otázkou |

Matriky sú online len do určitého dátumu: na Slovensku prechádzajú cirkevné a štátne matriky do archívu po 100 rokoch od posledného zápisu. V Česku je to 100 rokov pri narodeniach, 75 pri sobášoch a 30 pri úmrtiach. O mladšie údaje sa žiada na matričnom úrade (v ČR podľa § 25b vydajú zápisy staršie ako lehota komukoľvek aj zo zväzku na úrade). Agent vám povie, kedy je to potrebné.

## Čo je v repozitári
```
skills/rodokmen/
  SKILL.md           sprievodca pre agenta (fázy, pravidlá)
  reference/         podrobné návody: príprava počítača, čítanie matrík, portály archívov (SK, CZ, AT),
                     metodika (spájanie záznamov, mŕtve body, pramene mimo ČR), formát dát, web, súkromie
  tools/             nástroje v Pythone (ARON, výrezy, rámčeky, mapa, kontrola dát, export do webu, vejár)
  template/          šablóna projektu: prázdne dáta, ukážková rodina, web (Astro)
plugin.json          manifest pluginu pre Antigravity
.claude-plugin/      inštalácia ako plugin pre Claude Code
```

## Podpora archívov a prameňov
- **Slovensko:** Cirkevné matriky do roku 1895 (rímskokatolícke, gréckokatolícke, evanjelické, reformované, židovské) sú dostupné na **FamilySearch** v zbierke *Slovakia Church and Synagogue Books, 1592-1935*. Obrovská časť je indexovaná a vyhľadateľná podľa mena a obce. Sčítanie ľudu 1869 (*Slovakia Census 1869*) je na FamilySearch s indexom. Cintoríny pokrývajú portály `cintoriny.sk` a `virtualnycintorin.sk`. Urbáre a mapy sú na portáli `hungaricana.hu`.
- **Česko:** Východné Čechy (SOA Zámrsk / ARON), západné Čechy (SOA Plzeň / Porta fontium), stredné Čechy (SOA Praha / eBadatelna), Praha (AHMP), južné Čechy (SOA Třeboň) a Morava (MZA Brno, ZA Opava).
- **Rakúsko a Nemecko:** Portál Matricula Online (cirkevné matriky) a rakúske dobové noviny ANNO (ÖNB).
- Pri úradníkoch, vojakoch a učiteľoch hľadá aj v **dobových novinách** (Kramerius, ANNO) – kariéra, vyznamenania, parte.
- Dokáže načítať **rodinný strom z MyHeritage** a ďalších služieb (export GEDCOM) a urobiť z neho plán výskumu.
- Priebežne zbiera **zaujímavosti** (svadby na poslednú chvíľu, rod sto rokov v jednom dome…) a s vami napíše **Príbeh vášho rodu** – hlavný článok webu.
- Ku každému zápisu ukladá výrez s vyznačeným miestom, aby sa dal overiť, a neisté miesta označuje otáznikom.

## Súkromie
Projekt obsahuje osobné údaje vašej rodiny. Zostáva na vašom počítači. Web je chránený rodinnou otázkou
a nie je indexovaný vyhľadávačmi; bez nastavenej otázky ho nástroj nenasadí. Je to ochrana proti náhodným
návštevníkom: kto pozná odpoveď, vidí obsah webu. Agent má pokyn písať o žijúcich ľuďoch
len meno a rok narodenia a pred zverejnením s vami prejsť, čo o nich web uvádza.
Ak projekt chcete zálohovať na GitHub, použite **súkromný (private)** repozitár.

## Dokumentácia a Wiki
Podrobnú dokumentáciu, metodické návody na čítanie starých písiem (kurent, novogotika, maďarčina), zoznam archívov a formát dát nájdete vo [Wiki repozitára](https://github.com/hackra76/rodokmen-skill/wiki).
Otázky a skúsenosti s bádaním môžete zdieľať v [GitHub Discussions](https://github.com/hackra76/rodokmen-skill/discussions).

## Spätná väzba a vaše skúsenosti
Chyby a problémy – AI nesprávne prečítala zápis, spojila nesprávnych ľudí, nejaký krok nefunguje alebo spadol nástroj –
prosím [založte ako issue na GitHube](https://github.com/hackra76/rodokmen-skill/issues/new).
Popíšte, čo sa stalo, a ak ide o čítanie zápisu, pridajte odkaz na snímku v archíve. Issues sú verejné, preto
do nich nepíšte údaje o žijúcich ľuďoch.

## Bezpečnosť
Skill tvorí návod pre agenta a pomocné skripty v Pythone.
- **Žiadny automaticky spúšťaný kód bez kontroly.** Nástroje spúšťa agent pri práci podľa potreby.
- **Strážca siete (`hlidac_site.py`):** Projekt obsahuje voliteľný lifecycle hook (`hooks.json`), ktorý pred každým príkazom skontroluje, či agent nepristupuje na archívny web mimo brzdy.
- **Brzda proti zablokovaniu archívom:** Archívy blokujú IP adresu pri sérii rýchlych dopytov. Nástroje preto používajú brzdu (`tools/slusne.py`).
- **Kam skripty siahajú:** zapisujú do priečinka projektu rodokmeňa (stiahnuté snímky, medzivýsledky, web). Mimo projektu nič nemažú ani neprepisujú.
- **Na ktoré servery pristupujú:** archívne portály (FamilySearch, ARON, Porta fontium, eBadatelna, AHMP, Matricula), dobová tlač, OpenStreetMap (mapa a súradnice obcí) a pri inštalácii webu register npm.

## Licencia
Skill je pod licenciou [MIT](LICENSE): smiete ho voľne používať, upravovať a šíriť ďalej, so zachovaním uvedenia pôvodného autora (Jindřich Šaršon).
