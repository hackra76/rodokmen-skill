# Ochrana súkromia a etika

Genealogický výskum pracuje s osobnými a rodinnými údajmi. Projekt **Rodokmeň** preto kladie mimoriadny dôraz na ochranu súkromia.

---

## 1. Žijúci ľudia

- **Základné pravidlo:** O žijúcich príbuzných uvádza web len meno a rok narodenia (`note="Žijúci – údaje len základné."`).
- **Žiadne citlivé osobné údaje:** Nikdy nezverejňujeme adresy bydliska, rodné čísla, telefónne čísla, zdravotné záznamy, rozvody ani nemanželské deti žijúcich osôb bez ich výslovného predchádzajúceho súhlasu.
- **Citlivé udalosti z 20. storočia:** Ak zápisy spomínajú väznenie, tragické úmrtia, samovraždy alebo vážne choroby, asistent sa vždy opýta používateľa, či si rodina želá ich uvedenie.

---

## 2. Automatická kontrola (`kontrola.py`)

Pred každým zverejnením webu nástroj `tools/kontrola.py` skontroluje celú databázu:
- Vyhľadáva kľúčové slová týkajúce sa citlivých tém z posledných ~100 rokov.
- Ak nájde neoverený citlivý údaj, označí ho varovaním `CITLIVÉ`.
- Web nie je možné zverejniť na Netlify, pokiaľ používateľ citlivé údaje výslovne neschváli v `data/web.json`.

---

## 3. Dáta v Git a na GitHube

- Dáta rodokmeňa zostávajú uložené výhradne na vašom lokálnom disku.
- Ak sa rozhodnete projekt zálohovať cez Git na GitHub, úložisko musí byť nastavené ako **Private (Súkromné)**.
- Nikdy nepoužívajte verejné repozitáre na zálohu rodinných matričných výrezov a osobných poznámok.

---

## 4. Práca s archívmi a externými službami

- Pri používaní portálov ako FamilySearch, MyHeritage alebo štátnych archívov asistent dodržiava ľudské tempo bádania.
- Nepoužíva agresívny scraping – sťahuje len konkrétne snímky potrebné na overenie príbuzenstva.
