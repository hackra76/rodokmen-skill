# Formát dát rodokmeňa

Všetky genealogické údaje projektu sú uložené v textových súboroch v priečinku `data/`.

---

## 1. `osoby.py` – predkovia a Kekulého číslovanie

Predkovia používajú celosvetovo štandardné **Kekulého číslovanie (Ahnentafel)**:
- **1:** Východisková osoba (proband).
- **2, 3:** Otec, matka.
- **4, 5, 6, 7:** Starí rodičia (4-5 zo strany otca, 6-7 zo strany matky).
- **8 – 15:** Prastarí rodičia = **8 základných rodov** (`LINES`).
- Každá ďalšia generácia zdvojnásobuje číslo (otec osoby $n = 2n$, matka $= 2n+1$).

### Príklad zápisu v `osoby.py`:
```python
P = {
    8: dict(
        n="Ján Dvorský",
        y="1890–1944",
        st="doc",
        f=[
            "* 14. 2. 1890 Bardejov súp. č. 112",
            "kováč",
            "× 20. 6. 1919 Bardejov Mária Pokorná",
            "† 1944 Bardejov"
        ],
        r=["bardejov_krest_jan_dvorsky_1890", "bardejov_sobas_jan_dvorsky_1919"],
        note="Overené v matrike pokrstených aj oddaných."
    ),
    9: dict(
        n="Mária Pokorná",
        y="* 1895",
        st="doc",
        f=[...],
        r=[...]
    ),
}
```

### Význam polí:
- `n`: Meno a priezvisko (u žien vždy rodné priezvisko za slobodna).
- `y`: Roky života pre prehľady (`"1890–1944"`, `"* 1895"`, `"asi 1720–1785"`, `"† 1940"`).
- `st`: Úroveň dôveryhodnosti údaja:
  - `doc`: Overené a prečítané v primárnom prameni (matrika).
  - `prob`: Pravdepodobné (odvodené, napr. z indexu alebo veku pri úmrtí).
  - `fam`: Poskytnuté rodinou (spomienky, súkromný strom).
  - `mh`: Nájdené v cudzom strome na internete (vyžaduje overenie).
  - `unk`: Neznáme.
- `f`: Zoznam faktov. Znaky `*` (narodenie), `×` (sobáš), `†` (úmrtie). Názvy obcí sa automaticky párujú do mapy.
- `r`: Zoznam kľúčov zápisov zo `zaznamy.json`.

---

## 2. `zaznamy.json` – matričné zápisy

Evidencia konkrétnych listinných prameňov a fotografií matrík.

```json
[
  {
    "klic": "bardejov_krest_jan_dvorsky_1890",
    "svazek": "sk_bardejov_rk_1880_1900",
    "snimek": 57,
    "druh": "N",
    "datum": "14. 2. 1890",
    "nazev": "Krst Jána Dvorského",
    "shrnuti": "Ján, syn Václava Dvorského, kováča v Bardejove č. 112, a Barbory rod. Malej.",
    "odkaz": "https://www.familysearch.org/ark:/61903/..."
  }
]
```

---

## 3. `prepisy.json` – prepisy a preklady

Doslovné prepisy stĺpcov matrík a zrozumiteľné slovenské preklady pre rodinu.

```json
{
  "bardejov_krest_jan_dvorsky_1890": {
    "orig": "[Dátum] 14. februára 1890\n[Číslo domu] 112\n[Dieťa] Joannes, legitimus\n[Rodičia] Wenceslaus Dvorszky, faber ferreus...",
    "cs": "14. februára 1890 sa v Bardejove č. 112 narodil Ján, manželský syn kováča Václava Dvorského a Barbory rodenej Malej."
  }
}
```

---

## 4. Kontrola integrity dát

Kedykoľvek môžete spustiť kontrolu platnosti dát:
```bash
python -I -X utf8 tools/kontrola.py
```
Skript skontroluje:
- Logiku dátumov (narodenie pred smrťou, vek matky pri pôrode 14–50 rokov).
- Prepojenie kľúčov medzi `osoby.py`, `zaznamy.json` a výrezmi vo `vyrezy/`.
- Citlivé údaje u žijúcich osôb pred publikáciou na web.

