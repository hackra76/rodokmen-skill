# Správa repozitára rodokmen-skill (Antigravity port)

Tento repozitár obsahuje plugin a skill **rodokmen** prispôsobený pre prostredie Antigravity (so spätnou kompatibilitou pre Claude Code).

## Štruktúra repozitára
- `skills/rodokmen/SKILL.md`: Hlavná definícia skillu a inštrukcie pre prácu s rodokmeňom.
- `skills/rodokmen/tools/`: Pomocné nástroje v Pythone a bashi (sťahovanie matrík, výrezy, kontrola, export na web).
- `skills/rodokmen/template/`: Šablóna nového projektu (dáta, Astro web, `AGENTS.md`, `hooks.json`, `.vscode/launch.json`).
- `plugin.json`: Manifest pluginu pre Antigravity.
- `tests/brzda/`: Regresné testy brzdy a strážcu siete.

## Spúšťanie testov
```bash
python -I -X utf8 skills/rodokmen/tools/slusne.py tests/brzda/test_hlidac.py skills/rodokmen
```

## Vydanie novej verzie
Zvýš číslo verzie naraz v:
- `plugin.json` (`version`)
- `.claude-plugin/plugin.json` (`version`)
- `skills/rodokmen/VERZE`
- `README.md`

Do `CHANGELOG.md` pridaj sekciu `## X.Y.Z – D. M. RRRR`.
Ak sa mení formát medzi `tools/` a `template/web/`, otestuj aktualizáciu projektu založeného predchádzajúcou verziou (`novy_projekt.py`).
