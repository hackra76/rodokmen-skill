#!/usr/bin/env python3
"""Založí nový projekt rodokmeňa zo šablóny skillu.

Použitie: python <skill>/tools/novy_projekt.py <cieľový priečinok> [--ukazka] [--hlidac | --bez-hlidace]
  --ukazka        nakopíruje aj vymyslené ukážkové dáta (rodina Novákovcov), aby sa dal web hneď vyskúšať
  --hlidac        zapne strážcu siete (hooks.json pre Antigravity a hook v .claude/settings.json, tools/hlidac_site.py):
                  zamietne príkazy, ktoré idú na web archívu mimo brzdy tools/slusne.py; --bez-hlidace ho vypne

Vytvorí: data/ (prázdne kostry alebo ukážka), web/ (Astro web), tools/ (kópia nástrojov),
vyrezy/, zdroje/, dokumenty/, pracovni/, AGENTS.md, CLAUDE.md, hooks.json, .gitignore, .gitattributes
a .vscode/launch.json (.claude/launch.json pre Claude desktop).
Existujúce dáta neprepisuje.
Aktualizácia staršieho projektu: tools/ sa prepíše vždy a súbory webu, ktoré sa líšia od novej šablóny,
tiež – ich staré verzie sa uložia do pracovni/zaloha_web_<datum>/.
"""
import filecmp, json, os, shutil, sys, time
for _s in (sys.stdout, sys.stderr):   # UTF-8 výstup i na Windows bez -X utf8 (cp1250 neumí třeba „→“)
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def copy(src, out):
    if os.path.islink(out):   # nepsat přes symlink mimo projekt
        os.remove(out)
    shutil.copy2(src, out)


def copy_tree(src, dst, backup=None):
    """Zkopíruje chybějící soubory. S backup= přepíše i ty, které se liší, a starou verzi uloží do backup/."""
    changed = []
    for base, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in ("node_modules", "dist", ".astro", "__pycache__")]
        rel = os.path.relpath(base, src)
        os.makedirs(os.path.join(dst, rel), exist_ok=True)
        for f in files:
            new, out = os.path.join(base, f), os.path.join(dst, rel, f)
            if not os.path.lexists(out):
                copy(new, out)
            elif backup and (os.path.islink(out) or not filecmp.cmp(new, out, shallow=False)):
                keep = os.path.join(backup, os.path.normpath(os.path.join(rel, f)))
                os.makedirs(os.path.dirname(keep), exist_ok=True)
                if not os.path.islink(out):
                    shutil.copy2(out, keep)
                copy(new, out)
                changed.append(os.path.normpath(os.path.join(rel, f)))
    return changed


SIT_ZAKAZ = ["Bash(curl:*)", "Bash(wget:*)"]   # stahování z archivů jen přes tools/slusne.py (curl přes něj jde)
# Hlídač spustit, jen když soubor existuje: chybějící skript by Python ukončil kódem 2 a ten by zablokoval každý příkaz.
# mimo Windows ne cestu s číslem verze (po aktualizaci Pythonu by zmizela); na Windows lomítka (projdou Git Bash i cmd)
KOD = ("import os,runpy;p=os.path.join(os.environ.get('CLAUDE_PROJECT_DIR','.'),'tools','hlidac_site.py');"
       "os.path.isfile(p) and runpy.run_path(p,run_name='__main__')")
PY = sys.executable.replace("\\", "/") if os.name == "nt" else "python3"
HLIDAC = f'"{PY}" -I -c "{KOD}"'   # tvar se shellem (macOS, Linux)
MATCHER = "Bash|PowerShell|Monitor"   # Monitor spouští příkaz v bashi stejně jako Bash


def _python_windows():
    """Python pro hook na Windows: z PATH (projde i projekt sdílený přes OneDrive na dvou počítačích), jinak plná cesta.
    Zástupce z Microsoft Store (WindowsApps) se nepočítá – bez nainstalovaného Pythonu jen otevře obchod."""
    p = shutil.which("python")
    return "python" if p and "windowsapps" not in p.lower() else sys.executable


def hook_hlidace():
    """Hook hlídače. Na Windows bez shellu (command + args): hooky tam běží v Git Bashi, nebo v PowerShellu, když
    Git Bash chybí – a tam by příkaz s uvozovkami byl chyba syntaxe a Claude Code by pak zamítal každý příkaz."""
    if os.name == "nt":
        return {"type": "command", "command": _python_windows(), "args": ["-I", "-X", "utf8", "-c", KOD], "timeout": 10}
    return {"type": "command", "command": HLIDAC, "timeout": 10}


def nastaveni(dst, hlidac):
    """Doplní do .claude/settings.json a hooks.json zákaz curl/wget; hlidac=True/False zapne/vypne hook, None nechá, jak je."""
    # 1. Claude settings (.claude/settings.json)
    path = os.path.join(dst, ".claude", "settings.json")
    data = {}
    if os.path.exists(path):
        try:
            data = json.load(open(path, encoding="utf-8"))
        except ValueError:
            print(f"POZOR: {path} nie je platný JSON – nastavenie brzdy som nedoplnil. Opravte ho a spustite znova.")
            data = None
    if data is not None:
        puvodni = json.dumps(data, sort_keys=True)
        deny = data.setdefault("permissions", {}).setdefault("deny", [])
        deny += [r for r in SIT_ZAKAZ if r not in deny]
        pre = data.setdefault("hooks", {}).setdefault("PreToolUse", [])
        nase = [h for h in pre if "hlidac_site.py" in json.dumps(h)]
        for h in nase:   # aktualizace projektu: hook obnovit (cesta k Pythonu i tvar se mohly změnit)
            h["matcher"] = MATCHER
            h["hooks"] = [hook_hlidace()]
        if hlidac is True and not nase:
            pre.append({"matcher": MATCHER, "hooks": [hook_hlidace()]})
        elif hlidac is False:
            pre[:] = [h for h in pre if h not in nase]
        if not pre and "PreToolUse" in data.get("hooks", {}):
            del data["hooks"]["PreToolUse"]
        if not data.get("hooks"):
            data.pop("hooks", None)
        if json.dumps(data, sort_keys=True) != puvodni:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.write("\n")

    # 2. Antigravity hooks (hooks.json)
    py_cmd = f'"{_python_windows()}" -I -X utf8 tools/hlidac_site.py' if os.name == "nt" else 'python3 -I tools/hlidac_site.py'
    hook_entry = {
        "matcher": "run_command",
        "hooks": [
            {
                "type": "command",
                "command": py_cmd,
                "timeout": 10
            }
        ]
    }
    for rel_path in ("hooks.json", os.path.join(".agents", "hooks.json")):
        hpath = os.path.join(dst, rel_path)
        hdata = {}
        if os.path.exists(hpath):
            try:
                hdata = json.load(open(hpath, encoding="utf-8"))
            except ValueError:
                continue
        if hlidac is True:
            hdata.setdefault("hlidac-site", {})["PreToolUse"] = [hook_entry]
            os.makedirs(os.path.dirname(hpath) or ".", exist_ok=True)
            with open(hpath, "w", encoding="utf-8", newline="\n") as f:
                json.dump(hdata, f, ensure_ascii=False, indent=2)
                f.write("\n")
        elif hlidac is False and "hlidac-site" in hdata:
            del hdata["hlidac-site"]
            if hdata:
                with open(hpath, "w", encoding="utf-8", newline="\n") as f:
                    json.dump(hdata, f, ensure_ascii=False, indent=2)
                    f.write("\n")
            elif os.path.exists(hpath):
                os.remove(hpath)

    zapnuty = (data and any("hlidac_site.py" in json.dumps(h) for h in data.get("hooks", {}).get("PreToolUse", []))) or \
              os.path.exists(os.path.join(dst, "hooks.json"))
    print("Strážca siete:", "zapnutý" if zapnuty else "vypnutý (zapnúť: --hlidac)")


def main():
    if len(sys.argv) < 2 or sys.argv[1].startswith("-"):
        sys.exit(__doc__)
    dst = os.path.abspath(os.path.expanduser(sys.argv[1]))
    demo = "--ukazka" in sys.argv
    os.makedirs(dst, exist_ok=True)
    copy_tree(os.path.join(SKILL, "template", "ukazka" if demo else "data"), os.path.join(dst, "data"))
    if demo:
        for sub in ("vyrezy", "zdroje"):
            src = os.path.join(SKILL, "template", "ukazka_" + sub)
            if os.path.isdir(src):
                copy_tree(src, os.path.join(dst, sub))
    web = os.path.join(dst, "web")
    backup = os.path.join(dst, "pracovni", "zaloha_web_" + time.strftime("%Y%m%d-%H%M%S"))
    changed = copy_tree(os.path.join(SKILL, "template", "web"), web, backup if os.path.isdir(web) else None)
    tools = os.path.join(dst, "tools")
    os.makedirs(tools, exist_ok=True)
    for f in os.listdir(os.path.join(SKILL, "tools")):
        if f.endswith((".py", ".sh")) and f != "novy_projekt.py":
            copy(os.path.join(SKILL, "tools", f), os.path.join(tools, f))   # nástroje vždy aktualizovat
            if f.endswith(".sh"):   # skill naklonovaný na Windows (core.autocrlf) má CRLF – Git Bash by skript nespustil
                p = os.path.join(tools, f)
                data = open(p, "rb").read()
                if b"\r\n" in data:
                    open(p, "wb").write(data.replace(b"\r\n", b"\n"))
    for d in ("vyrezy", "zdroje", "dokumenty", "pracovni"):
        os.makedirs(os.path.join(dst, d), exist_ok=True)
    os.makedirs(os.path.join(dst, ".claude"), exist_ok=True)
    os.makedirs(os.path.join(dst, ".vscode"), exist_ok=True)
    for name in ("AGENTS.md", "CLAUDE.md", ".gitignore", ".gitattributes", "poznamky_pro_skill.md",
                 os.path.join(".claude", "launch.json"), os.path.join(".vscode", "launch.json")):
        out = os.path.join(dst, name)
        src = os.path.join(SKILL, "template", name)
        if os.path.lexists(src) and not os.path.lexists(out):
            copy(src, out)
    nastaveni(dst, True if "--hlidac" in sys.argv else False if "--bez-hlidace" in sys.argv else None)
    with open(os.path.join(dst, ".skill_verze"), "w", encoding="utf-8") as f:   # SKILL.md podle něj nabídne aktualizaci
        f.write(open(os.path.join(SKILL, "VERZE"), encoding="utf-8").read())
    print("Projekt pripravený:", dst)
    if changed:
        print(f"Web aktualizovaný na novú šablónu ({len(changed)} súborov). Pôvodné verzie sú v {backup}:")
        for f in changed:
            print("  web/" + f)
        print("Pokiaľ ste vzhľad webu upravovali, prevezmite úpravy zo zálohy. Potom `npm install` a `npm run data` vo web/.")


if __name__ == "__main__":
    main()
