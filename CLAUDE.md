# Správa repozitára rodokmen-skill

Vydanie novej verzie: zvýš číslo na troch miestach naraz – `.claude-plugin/plugin.json` (`version`),
`skills/rodokmen/VERZE` (podľa neho agent u používateľa spozná, že má aktualizovať projekt) a README („Stav k … (verzia …)“).
Do `CHANGELOG.md` pridaj hore sekciu `## X.Y.Z – D. M. RRRR` (Nové / Opravy / Návody, krátke odrážky pre používateľa,
čísla issues ako `#11`). Po commite a pushi vytvor tag a vydanie na GitHube s textom danej sekcie:
`awk '/^## X.Y.Z /{f=1;next} /^## /{f=0} f' CHANGELOG.md > /tmp/notes.md && gh release create vX.Y.Z --target main --title "X.Y.Z" --notes-file /tmp/notes.md`.
Ak sa mení formát medzi `tools/` a `template/web/`, otestuj aj aktualizáciu projektu založeného predchádzajúcou verziou
(`novy_projekt.py` na rovnaký priečinok, `npm install`, `npm run data`, `npm run build`).
