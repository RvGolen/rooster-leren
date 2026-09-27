# Zelfcheck — module 5

---

## 1. Voorspel zonder te draaien

```python
nodig = 2
beschikbaar = 2
if beschikbaar < nodig:
    print("tekort")
elif beschikbaar == nodig:
    print("precies goed")
else:
    print("over")
```

Wat komt eruit? En bij `beschikbaar = 5`?

---

## 2. Spot de fout

```python
studenten = 30
if studenten = 30:
    print("dertig")
```

Wat is hier mis? (Tip: lees nog eens over `=` versus `==`.)

---

## 3. Lezen, niet schrijven

Wat doet dit blok in gewone taal? Welke lokalen worden geprint?

```python
toetsen = [
    {"lokaal": "A1.04", "studenten": 30, "capaciteit": 40},
    {"lokaal": "B2.10", "studenten": 55, "capaciteit": 40},
]
for toets in toetsen:
    if toets["studenten"] > toets["capaciteit"]:
        print(toets["lokaal"])
```

---

## 4. Leg het in je eigen woorden uit ✍️

> Een "harde regel" uit jouw werk wordt in code een voorwaarde. Kies één regel
> (bijv. "studenten passen in de zaal") en beschrijf in woorden hoe je die als `if`
> zou schrijven. In `../../voortgang.md`.

---

## Klaar met module 5 ✅

> 🔎 **Vooruitblik (spiraalvorm):** je hebt nu losse stukken logica geschreven. Maar
> sommige controles wil je telkens opnieuw kunnen doen, zonder ze te herhalen — bijv.
> "is dit een conflict, ja of nee?". In **module 6** verpak je zulke logica in een
> `function`: een herbruikbaar stukje met een naam. Je bouwt er meteen je eerste
> echte rooster-functie mee: `heeft_conflict`.

### Even mechanisch controleren 🔍

Draai in de terminal, in de map van deze module:

```bash
python controleer.py
```

Dat script draait jouw `opdracht.py` en zegt per stap of de uitvoer klopt. Zie het
als hulpmiddel, niet als examen: het vertelt je of je uitvoer klopt, niet of je het
snapt. Dat laatste deed je hierboven zelf.

➡️ Door naar **`../module-06-functies/les.md`**: module 6, functies.
