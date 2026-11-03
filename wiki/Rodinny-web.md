# Rodinný web (Astro)

Súčasťou projektu je šablóna moderného statického webu postaveného na frameworku [Astro](https://astro.build) s integrovaným vyhľadávaním [Pagefind](https://pagefind.app).

---

## Čo rodinný web obsahuje

- **Úvodná stránka:** Príbeh rodu, zaujímavosti, štatistiky a interaktívna mapa obcí, kde predkovia žili.
- **Vejár predkov (Fan Chart):** Celoobrazovkový interaktívny kruhový vejár generácií s možnosťou kliknutia na osobu a vyhľadávaním.
- **Karty osôb a rodín:** Prehľadné vizitky predkov s chronologickým prehľadom udalostí ich života.
- **Zápisy z matrík:** Galéria výrezov originálnych zápisov s vyznačeným riadkom, prepisom latinského/maďarského textu a slovenským prekladom.
- **Čo hľadáme:** Otvorené genealogické otázky a hypotézy pre ďalšie bádanie.
- **Denník hľadania:** Záznam toho, ktoré matriky boli prejdené.

---

## Základné príkazy (v priečinku `web/`)

| Príkaz | Účel |
|---|---|
| `npm install` | Jednorazové stiahnutie závislostí webu |
| `npm run data` | Export genealogických dát z `data/` do webu |
| `npm run nahled` | Spustenie lokálneho náhľadu webu na `http://localhost:4321` |
| `npm run build` | Zostavenie optimalizovaného statického webu do `dist/` |
| `npm run nasadit` | Automatické nasadenie na bezplatný hosting Netlify |

---

## 🔒 Zabezpečenie rodinnou otázkou

Web je vytvorený pre vašich príbuzných, nie pre verejnosť či webové roboty:
- Stránky obsahujú značku `<meta name="robots" content="noindex, nofollow">`.
- Prístup na web je chránený **rodinnou otázkou** (napr. *Ako sa volal rodný dom u starých rodičov?*).
- Zodpovedanie otázky overuje serverless funkcia (Netlify Edge Function).
- V prehliadači ani v zdrojovom kóde nie je uložené heslo, iba kryptografický odtlačok (SHA-256 hash).

Konfigurácia sa nachádza v súbore `data/web.json`:
```json
{
  "prihlaseni": {
    "uvod": "Tento web je určený len pre rodinu Dvorských.",
    "otazka": "Ako sa volal pes u starej mamy v Bardejove?",
    "odpoved": "Dunčo"
  }
}
```

---

## Zverejnenie na Netlify (zadarmo)

1. Vytvorte si bezplatný účet na [netlify.com](https://www.netlify.com).
2. V priečinku `web/` sa jednorazovo prihláste:
   ```bash
   npx netlify-cli login
   npx netlify-cli sites:create
   ```
3. Spustite nasadenie:
   ```bash
   npm run nasadit
   ```
Web bude dostupný na privátnej adrese typu `https://rodokmen-dvorsky.netlify.app`.
