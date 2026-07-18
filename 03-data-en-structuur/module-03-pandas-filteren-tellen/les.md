# Module 3 — Filteren en tellen met pandas

⏱️ ± 25–30 minuten · Fase 2 · **Nieuw concept:** selecteren op voorwaarde, en
tellen/groeperen

> Bouwt voort op `pd.read_csv` (module 1) en de tabel die je in module 2 leerde
> bekijken.

---

## Eerst even raden 🤔

```python
toetsen["tijd"] == "09:00"
```

> Wat denk je dat hier uitkomt? De rijen van 09:00 uit de tabel? Of iets anders?
> Gok eerst — dit is precies de aha van vandaag.

---

## Het concept, in twee stappen

### Stap 1: de vraag stellen

`toetsen["tijd"] == "09:00"` geeft **niet** de rijen om 09:00. Het geeft, voor
**elke** rij apart, het antwoord op de vraag "is `tijd` hier gelijk aan
`09:00`?" — dus een kolom met alleen `True` en `False`. Klopte je gok?

### Stap 2: de vraag als filter gebruiken

Zet je die `True`/`False`-kolom tússen vierkante haken achter de tabel, dan
gebeurt het echte werk: pandas houdt alleen de rijen over waar het antwoord
`True` was.

```python
toetsen[toetsen["tijd"] == "09:00"]
```

Dit is precies de `if` uit module 5 in fase 1 — alleen stel je de vraag nu niet
één keer per toets in een loop, maar in één keer aan **alle** rijen tegelijk.
Geen loop nodig; de tabel doet het voor je.

---

## Uitgewerkt voorbeeld

> ⚠️ **Voorbeeld, geen voorschrift.** We gebruiken `toetsen.csv` om het concept
> concreet te maken. Welke vragen jij aan jouw eigen rooster stelt, bepaal jij.

```python
import pandas as pd

toetsen = pd.read_csv("../../voorbeelddata/toetsen.csv")

# Filteren: welke toetsen zijn er om 09:00?
ochtend = toetsen[toetsen["tijd"] == "09:00"]
print(ochtend)

# Tellen: hoeveel toetsen per tijdslot?
print(toetsen["tijd"].value_counts())

# Groeperen: hoeveel studenten in totaal per tijdslot?
print(toetsen.groupby("tijd")["aantal_studenten"].sum())
```

Dit toont:

```
  toets_id              vak lokaal   tijd  aantal_studenten  vereist_toezicht
0       T1       Statistiek  A1.04  09:00               110                 2
1       T2  Inleiding Recht  B2.10  09:00               180                 3
2       T3    Microbiologie  C0.22  09:00                55                 1
tijd
09:00    3
11:00    3
14:00    2
Name: count, dtype: int64
tijd
09:00    345
11:00    270
14:00    165
Name: aantal_studenten, dtype: int64
```

Drie nieuwe stukjes gereedschap, alle drie op dezelfde tabel:

- **Filteren** (`toetsen[...]`) — geeft je de **rijen** terug die aan een
  voorwaarde voldoen.
- **Tellen** (`.value_counts()`) — telt hoe vaak elke waarde in één kolom
  voorkomt.
- **Groeperen** (`.groupby(...)`) — verdeelt de tabel in groepen (hier: per
  tijdslot) en rekent daarna per groep iets uit — hier een `.sum()`.

---

## Twee voorwaarden combineren

Wil je twee dingen tegelijk checken — bijvoorbeeld "om 09:00 én meer dan 100
studenten" — dan ligt `and` voor de hand. Dat werkt hier **niet**:

```python
toetsen[toetsen["tijd"] == "09:00" and toetsen["aantal_studenten"] > 100]
```

```
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
```

Dit is een klassieke struikelaar — het ligt niet aan jou, het ligt aan de vorm.
`and` in gewone Python verwacht twee losse `True`/`False`-waarden. Maar hier heb
je twee hele kolómmen vol `True`/`False`, één per rij, en `and` weet niet hoe
het die moet vergelijken. Pandas heeft daarom zijn eigen teken: `&`. Zet er
bovendien haakjes om elke voorwaarde, anders leest Python de regel verkeerd.

```python
toetsen[(toetsen["tijd"] == "09:00") & (toetsen["aantal_studenten"] > 100)]
```

```
  toets_id              vak lokaal   tijd  aantal_studenten  vereist_toezicht
0       T1       Statistiek  A1.04  09:00               110                 2
1       T2  Inleiding Recht  B2.10  09:00               180                 3
```

Onthoud dit ene rijtje: **in een tabel gebruik je `&` in plaats van `and`, en
altijd haakjes om elke voorwaarde.**

---

## Nu jij

Open **`opdracht.py`**. De steun neemt weer wat af — voorspel bij elke stap
eerst wat je verwacht, draai dan pas.

> Vastgelopen? In **Ask-modus**: *"leg uit waarom ik & moet gebruiken in
> plaats van and bij pandas"* — laat het je uitleggen, schrijf het dan zelf.

Klaar? Ga naar **`check.md`**.
