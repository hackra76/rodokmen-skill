# Správa repozitáře rodokmen-skill (Antigravity port)

Tento repozitář obsahuje plugin a skill **rodokmen** přizpůsobený pro prostředí Antigravity (se zpětnou kompatibilitou pro Claude Code).

## Struktura repozitáře
- `skills/rodokmen/SKILL.md`: Hlavní definice skillu a instrukce pro práci s rodokmenem.
- `skills/rodokmen/tools/`: Pomocné nástroje v Pythonu a bashi (stahování matrik, výřezy, kontrola, export na web).
- `skills/rodokmen/template/`: Šablona nového projektu (data, Astro web, `AGENTS.md`, `hooks.json`, `.vscode/launch.json`).
- `plugin.json`: Manifest pluginu pro Antigravity.
- `tests/brzda/`: Regresní testy brzdy a hlídače sítě.

## Spouštění testů
```bash
python -I -X utf8 skills/rodokmen/tools/slusne.py tests/brzda/test_hlidac.py skills/rodokmen
```

## Vydání nové verze
Zvedni číslo verze najednou v:
- `plugin.json` (`version`)
- `.claude-plugin/plugin.json` (`version`)
- `skills/rodokmen/VERZE`
- `README.md`

Do `CHANGELOG.md` přidej sekci `## X.Y.Z – D. M. RRRR`.
Mění-li se formát mezi `tools/` a `template/web/`, otestuj aktualizaci projektu založeného předchozí verzí (`novy_projekt.py`).
