# Inštalácia a nastavenie

Sprievodca inštaláciou a požiadavkami pre prevádzku asistenta **Rodokmeň**.

---

## Systémové požiadavky

- **Operačný systém:** Windows 10/11, macOS, Linux
- **AI asistent:** [Google Antigravity](https://antigravity.google) alebo [Claude Code](https://claude.ai/code)
- **Pomocné programy:**
  - **Python 3.10+** (s modulmi štandardnej knižnice)
  - **Node.js 18+** & npm (pre zostavenie rodinného webu v Astro)
  - **ImageMagick** (`magick` príkaz – pre generovanie výrezov zo snímok matrík)
  - **Git**

> *Poznámka:* Nemusíte tieto programy inštalovať manuálne pred štartom. Asistent pri prvom spustení sám otestuje systém a pomôže vám s inštaláciou chýbajúcich komponentov (cez `winget` na Windows alebo `brew` na macOS).

---

## 1. Inštalácia do Google Antigravity

### Možnosť A: Ako globálny plugin (odporúčané)
Plugin naklonujte do priečinka používateľských pluginov:

- **Windows (PowerShell):**
  ```powershell
  git clone https://github.com/hackra76/rodokmen-skill "$env:USERPROFILE\.gemini\config\plugins\rodokmen"
  ```
- **macOS / Linux:**
  ```bash
  git clone https://github.com/hackra76/rodokmen-skill ~/.gemini/config/plugins/rodokmen
  ```

### Možnosť B: Pre konkrétny projekt (Workspace)
Priečinok `skills/rodokmen` skopírujte do priečinka `.agents/skills/rodokmen` vo vašom pracovnom adresári.

Po inštalácii reštartujte Antigravity, aby sa načítal manifest `plugin.json` a definícia skillu.

---

## 2. Inštalácia do Claude Code

V prostredí Claude Code spustite:
```bash
/plugin marketplace add hackra76/rodokmen-skill
/plugin install rodokmen@rodokmen-skill
```
Alebo naklonujte repozitár manuálne do `~/.claude/skills/rodokmen`.

---

## 3. Odporúčané jazykové modely

Genealogický výskum je komplexná úloha zahŕňajúca čítanie starých textov, interpretáciu latinských/maďarských výrazov a logické prepájanie rodinných vetiev.

| Asistent | Hlavný model (uvažovanie, prepis, overovanie) | Subagenti (hľadanie, rýchle skenovanie) |
|---|---|---|
| **Google Antigravity** | **Gemini Pro** (najsilnejší model radu Pro) | **Gemini Flash** |
| **Claude Code** | **Claude Opus 5.5** | **Claude Sonnet 5.5** |

> ⚠️ **Dôležité:** Hlavný model vždy vykonáva finálne overenie zápisu priamo na výreze originálnej snímky matrika. Pomocné modely (Flash) slúžia len na orientačné indexovanie a prechádzanie stránok.

