# Časté otázky a riešenie problémov (FAQ)

---

### 1. Čo robiť, ak neviem nájsť predka v matrike?
- **Skontrolujte susedné farnosti:** Malé obce nemali vlastný kostol a patrili pod farnosť vo vedľajšej dedine.
- **Skontrolujte iné vierovyznania:** Ak predok nie je v rímskokatolíckej matrike, skontrolujte evanjelické (a.v.), reformované (kalvínske) alebo židovské záznamy.
- **Varianty priezviska:** V 18. a 19. storočí sa pravopis líšil (fonetický zápis, maďarčina, nemčina). Vyskúšajte všetky fonetické alternatívy.
- **Hľadajte sobáš, nie narodenie:** Sobášny zápis takmer vždy uvádza presné bydlisko a rodičov oboch snúbencov.

---

### 2. Čo ak archív hlási chybu 403 alebo zablokovanie?
- Niektoré archívy (napr. SOA Třeboň alebo MZA Brno) nepovoľujú priame automatické sťahovanie cez skripty.
- V takom prípade asistent použije priamy prehliadač (nástroj `/browser` alebo Playwright), kde si matriku prezrie a nasníma ako bežný návštevník.
- Vždy dodržiavajte brzdu `tools/slusne.py`.

---

### 3. Ako zaktualizujem projekt na novú verziu skillu?
- Asistent pri otvorení priečinka projektu porovná číslo verzie v `VERZE`.
- Ak zistí novšiu verziu, sám navrhne bezpečnú aktualizáciu pomocných skriptov bez prepísania vašich genealogických dát v `data/`.

---

### 4. Môžem rodokmeň exportovať do GEDCOM?
- Áno, súbory `data/osoby.py` a `data/zaznamy.json` možno kedykoľvek previesť do formátu GEDCOM pre import do programov ako Gramps, Strom (stromapp.info) alebo rodinných webov.

---

### 5. Kde nahlásiť chybu alebo poslať návrh na zlepšenie?
- Návrhy a hlásenia chýb môžete vložiť do [GitHub Issues](https://github.com/hackra76/rodokmen-skill/issues).
- Diskusie a otázky o genealógii sú vítané v [GitHub Discussions](https://github.com/hackra76/rodokmen-skill/discussions).

