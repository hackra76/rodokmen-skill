# Rodokmeň – Vitajte v dokumentácii

![Rodokmeň z matrík a rodinný web](../docs/banner.jpg)

Vitajte vo wiki dokumentácii projektu **Rodokmeň** – AI asistenta a skillu pre **Google Antigravity** a **Claude Code**.

Tento projekt vás prevedie tvorbou rodokmeňa od prvých rodinných spomienok cez bádanie v digitalizovaných matrikách (Slovensko, Česko, FamilySearch, Rakúsko) až po moderný, zabezpečený rodinný web s interaktívnym vejárom predkov, mapou a výrezmi originálnych záznamov.

---

## 🚀 Rýchly štart

1. **Inštalácia do Google Antigravity:**
   ```bash
   git clone https://github.com/hackra76/rodokmen-skill ~/.gemini/config/plugins/rodokmen
   ```
2. **Inštalácia do Claude Code:**
   ```bash
   /plugin marketplace add hackra76/rodokmen-skill
   /plugin install rodokmen@rodokmen-skill
   ```
3. **Spustenie výskumu:**
   Otvorte asistenta a zadajte:
   > *„Chcem urobiť rodokmeň svojej rodiny.“*

Asistent skontroluje potrebné programy (Python 3, Node.js, ImageMagick, Git), založí projekt a začne úvodným rozhovorom.

---

## 📚 Obsah dokumentácie

| Sekcia | Popis |
|---|---|
| **[[Inštalácia a nastavenie\|Instalacia-a-nastavenie]]** | Systémové požiadavky, inštalácia pluginu a odporúčané jazykové modely. |
| **[[Archívne portály\|Archivne-portaly]]** | Prehľad archívov na Slovensku (FamilySearch), v Česku (ARON, Porta fontium...) a v zahraničí. |
| **[[Čítanie a prepis matrík\|Citanie-a-prepis-matrik]]** | Druhy matrík (N, O, Z), staré písma (kurent), jazyky (latinčina, maďarčina) a slovníček. |
| **[[Formát dát rodokmeňa\|Format-dat]]** | Štruktúra `data/`, Kekulého číslovanie, osoby, zápisy a verifikácia faktov. |
| **[[Príbehy rodu\|Pribehy-rodu]]** | Ako agent vyhľadáva zaujímavosti a generuje pútavé rodové kroniky. |
| **[[Rodinný web\|Rodinny-web]]** | Zostavenie statického Astro webu, vejár predkov, prihlasovacia rodinná otázka a hosting na Netlify. |
| **[[Ochrana súkromia\|Ochrana-sukromia]]** | Etické zásady, ochrana osobných údajov žijúcich predkov a bezpečnosť. |
| **[[Časté otázky a riešenie problémov\|FAQ]]** | Tipy na riešenie bežných ťažkostí pri bádaní. |

---

## 🛡️ Kľúčové zásady projektu

1. **Dáta zostávajú u vás:** Celý projekt sa ukladá lokálne na vašom disku. Web je predvolene zabezpečený kontrolnou rodinnou otázkou a vyhľadávače ho neindexujú (`noindex`).
2. **Overovanie každého zápisu:** Každý fakt v rodokmeni má presnú citáciu a výrez originálneho matričného zápisu. Neisté údaje sa označujú otáznikom.
3. **Ochrana archívov (slusne.py):** Integrovaná sieťová brzda chráni servery archívov pred preťažením a vás pred zablokovaním IP adresy.

