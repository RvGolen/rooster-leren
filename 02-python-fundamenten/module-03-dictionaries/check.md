# Zelfcheck — module 3

---

## 1. Voorspel zonder te draaien

```python
toets = {"lokaal": "A1.04", "tijd": "09:00", "studenten": 30}
toets["studenten"] = 50
print(toets["studenten"])
```

Wat komt eruit? Is er een gegeven verloren gegaan, of alleen veranderd?

---

## 2. Spot de fout

```python
toets = {"lokaal": "A1.04", "tijd": "09:00"}
print(toets["studenten"])
```

Dit geeft een foutmelding. Welke (zie `uitleg.md`), en waaróm?

---

## 3. Lijst of dict?

Voor elk van deze, kies je een lijst of een dict — en waarom?
- a) alle tijdsloten van vandaag
- b) alle kenmerken van één surveillant (naam, beschikbaar vanaf, tarief)
- c) de namen van alle ingehuurde surveillanten

---

## 4. Leg het in je eigen woorden uit ✍️

> Leg in twee zinnen uit wat het verschil is tussen een lijst en een dictionary,
> met een rooster-voorbeeld. Schrijf het in `voortgang.md`.

---

## Klaar met module 3 ✅

> 🔎 **Vooruitblik (spiraalvorm):** je kunt nu één toets netjes beschrijven. Maar
> een dag heeft tientallen toetsen, en je wilt voor *elke* toets iets controleren
> zonder dat veertig keer te typen. In **module 4** leer je de `for`-loop: "doe dit
> voor elk item in een lijst". Dáár komen lijst en dict samen tot leven.

➡️ Door naar **module 4 — loops**.
