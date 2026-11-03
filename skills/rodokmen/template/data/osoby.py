# Priami predkovia podľa Kekulého čísiel: 1 = východisková osoba (ten, pre koho rodokmeň robíme),
# otec osoby n má číslo 2n, matka 2n+1. Teda 2 = otec, 3 = matka, 4–7 starí rodičia, 8–15 prastarí rodičia…
#
# Každá osoba:  číslo: dict(n="Meno Priezvisko", y="1850–1910", st="doc", f=[...], r=[...], note="...")
#   n    meno; ženy za slobodna („Anna Dvořáková“), pri neistom čítaní otáznik („Mária Špalková (?)“)
#   y    roky života pre prehľady: "* 1931" (žije / úmrtie neznáme), "1850–1910", "asi 1720–1785", "1680 – pred 1740"
#   st   stav doloženia: doc  = doložené matrikou (čítané priamo zo snímky)
#                        prob = pravdepodobné (zhoda údajov, ale nie priamy doklad)
#                        fam  = údaj od rodiny / z rodinného dokumentu
#                        mh   = len z cudzieho rodokmeňa na internete (MyHeritage, Geni…) – neoverené
#                        unk  = neznáme (len miesto v rodokmeni)
#   f    fakty ako krátke vety: "* 12. 3. 1873 Bardejov s.č. 477", "kováč", "× 28. 1. 1897 Anna Stejskalová", "† 14. 5. 1902"
#        (* narodenie, × sobáš, † úmrtie – podľa týchto značiek web rozpozná sobáše a miesta pre mapu)
#   r    kľúče zápisov z data/zaznamy.json, ktoré osobu dokladajú
#   note poznámka: prečo je údaj neistý, rozpory, odkiaľ sa vzal
#   sex  len pri osobe 1: "M" alebo "F" (pri ostatných vyplýva z čísla)
# Žijúci ľudia: len meno a rok narodenia (súkromie), note="Žijúci – údaje len základné."
# Neznámy otec nemanželského dieťaťa: dict(n="otec neuvedený", st="unk", f=[], note="…")

P = {
}

# Rody = osem vetiev podľa prastarých rodičov (čísla 8–15). Doplňte, hneď ako ich poznáte:
# 8: ("Dvorskí", "Jedna veta, kto to bol a odkiaľ – zobrazí sa na webe pri rode."),
LINES = {
}

# Príbuzní mimo priamej línie (súrodenci, strýkovia…): k = číslo predka, ku ktorému patria.
# dict(k=16, n="Jozef Dvorský (1865–1920)", t="Brat Jána. Kováč v …", r=["klic_zapisu"])
SIDE = [
]

# Rozpory a otvorené otázky (na web do „Čo hľadáme“) ako dvojice (otázka, odpoveď). Odpoveď začnite
# „Vyriešené: …“ (na webe sa skryje), „Hypotéza: …“ alebo „Otvorené: …“. Ide na web – nič citlivé.
# ("Kedy sa narodil Ján Dvorský?", "Otvorené: rodina hovorí 1850, v matrike 1848–1852 nenájdený.")
ISSUES = [
]

# Hypotézy o pôvode rodu nad rámec doloženej línie (zobrazia sa na stránke rodu):
# dict(rod=8, nadpis="Hypotéza: Dvorskí z Lhôtky", text="…", polozky=[("Ján Dvorský", "krstný otec 1681…")], zaznamy=["klic"])
HYPOTEZY = [
]

# Príbuzenské sobáše (pedigree collapse): keď je rovnaká osoba predkom cez viac vetiev.
# SAME = {350: 140}  # alias -> hlavné číslo
SAME = {
}
