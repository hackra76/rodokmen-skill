#!/usr/bin/env python3
"""Publikovanie obsahu priečinka wiki/ do GitHub Wiki repozitára.

Použitie:
    python tools/publish_wiki.py
"""

import os
import shutil
import subprocess
import sys
import tempfile


def get_auth_token():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return token
    try:
        res = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except Exception:
        return None


def get_repo_slug():
    try:
        res = subprocess.run(["git", "config", "--get", "remote.origin.url"], capture_output=True, text=True, check=True)
        url = res.stdout.strip()
        # Parse owner/repo from URL
        if "github.com" in url:
            part = url.split("github.com")[-1].lstrip(":/")
            if part.endswith(".git"):
                part = part[:-4]
            return part
    except Exception:
        pass
    return "hackra76/rodokmen-skill"


def main():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    wiki_src = os.path.join(root_dir, "wiki")
    if not os.path.isdir(wiki_src):
        print(f"Chyba: Priečinok '{wiki_src}' neexistuje.", file=sys.stderr)
        sys.exit(1)

    token = get_auth_token()
    repo_slug = get_repo_slug()

    if token:
        remote_url = f"https://x-access-token:{token}@github.com/{repo_slug}.wiki.git"
    else:
        remote_url = f"https://github.com/{repo_slug}.wiki.git"

    temp_dir = tempfile.mkdtemp(prefix="wiki_sync_")
    try:
        print(f"Pripájam sa k GitHub Wiki ({repo_slug})...")
        clone_cmd = ["git", "clone", "--depth", "1", remote_url, temp_dir]
        res = subprocess.run(clone_cmd, capture_output=True, text=True)

        if res.returncode != 0:
            print("\n" + "=" * 60)
            print("UPOZORNENIE: Wiki repozitár ešte nie je na GitHube inicializovaný!")
            print("=" * 60)
            print(f"GitHub vytvára git úložisko pre wiki až po vytvorení prvej stránky cez web.")
            print(f"1. Otvorte v prehliadači: https://github.com/{repo_slug}/wiki")
            print("2. Kliknite na 'Create the first page' a uložte ju (Save page).")
            print("3. Následne znova spustite: python scripts/publish_wiki.py")
            print("Všetky pripravené stránky z priečinka wiki/ sa okamžite nahrajú.\n")
            sys.exit(2)

        # Skopíruj všetky .md súbory z wiki/
        copied = 0
        for fname in os.listdir(wiki_src):
            if fname.endswith(".md"):
                shutil.copy2(os.path.join(wiki_src, fname), os.path.join(temp_dir, fname))
                copied += 1

        # Git add, commit, push
        subprocess.run(["git", "config", "user.name", "GitHub Agent"], cwd=temp_dir, check=True)
        subprocess.run(["git", "config", "user.email", "agent@users.noreply.github.com"], cwd=temp_dir, check=True)
        subprocess.run(["git", "add", "."], cwd=temp_dir, check=True)

        status_res = subprocess.run(["git", "status", "--porcelain"], cwd=temp_dir, capture_output=True, text=True, check=True)
        if not status_res.stdout.strip():
            print("Wiki je už aktuálna, žiadne zmeny na publikovanie.")
            return

        subprocess.run(["git", "commit", "-m", "Aktualizácia wiki dokumentácie"], cwd=temp_dir, check=True)
        push_res = subprocess.run(["git", "push", "origin", "HEAD:master"], cwd=temp_dir, capture_output=True, text=True)
        if push_res.returncode != 0:
            # skúsime main
            subprocess.run(["git", "push", "origin", "HEAD:main"], cwd=temp_dir, check=True)

        print(f"Úspešne publikovaných {copied} stránok do GitHub Wiki.")

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
