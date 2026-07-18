# Zelfcheck — module 2

---

## 1. Twee keer "toetsen", twee keer iets anders

In module 1 was `toetsen` een lijst van dicts. In module 2 is `toetsen` een
DataFrame. Wat is het verschil tussen die twee manieren om naar dezelfde data
te kijken?

---

## 2. Geen `int(...)` meer nodig

In module 1 moest je `int(toets["aantal_studenten"])` gebruiken voordat je kon
optellen. In module 2 werkte `toetsen["aantal_studenten"].sum()` meteen. Waarom
hoefde dat hier niet?

---

## 3. Wat doet `head(3)` precies?

Wat print `toetsen.head(3)`, en wat is het verschil met `print(toetsen)` zonder
`head`?

---

## 4. Leg het in je eigen woorden uit ✍️

> Beschrijf in drie à vier zinnen wat een DataFrame is, en waarom je met een
> DataFrame minder code nodig hebt voor een vraag als "hoeveel studenten in
> totaal". Schrijf het in `../../voortgang.md`.

---

## Jouw situatie 🔎

Heb je in module 1 al een eigen CSV geëxporteerd? Lees die nu in met
`pd.read_csv(...)` in plaats van met `csv.DictReader`, en print `.columns` en
`len(...)`.

Hoeveel rijen heeft jouw echte rooster? Vraag in **Ask-modus**: *"leg uit wat
deze kolommen betekenen"* — niet: laat de AI code voor je schrijven. Jij
bepaalt wat je uitprobeert; de AI legt uit wat je ziet.

Noteer kort in `../../voortgang.md` hoe jouw tabel eruitziet, vergeleken met
`toetsen.csv`.

---

## Klaar met module 2 ✅

➡️ Door naar **`module-03-pandas-filteren-tellen/`**.
