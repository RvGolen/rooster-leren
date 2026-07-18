# Module 1 — CSV-bestanden inlezen

⏱️ ± 20–25 minuten · Fase 2 (start) · **Nieuw concept:** een bestand inlezen met
`csv.DictReader`

---

## Eerst even raden 🤔

Dit ken je nog van fase 1 — een rooster dat je zelf met de hand typte:

```python
rooster = [
    {"persoon": "Jansen",   "tijd": "09:00", "lokaal": "A1.04"},
    {"persoon": "De Vries", "tijd": "09:00", "lokaal": "B2.10"},
]
```

En dit staat in `../../voorbeelddata/toetsen.csv` — een echt exportbestand:

```
toets_id,vak,lokaal,tijd,aantal_studenten,vereist_toezicht
T1,Statistiek,A1.04,09:00,110,2
T2,Inleiding Recht,B2.10,09:00,180,3
```

> Kijk goed naar allebei. Wat is hetzelfde? Wat is anders? Schrijf voor jezelf op
> wat je denkt — aan het eind van deze les weet je of je gelijk had.

---

## Wat is een CSV

`toetsen.csv` staat in `../../voorbeelddata/`. Open het gerust in Cursor: het is
gewoon platte tekst. Eén regel per rij, en de waarden binnen een rij worden
gescheiden door komma's — vandaar de naam **CSV** (Engels voor *comma-separated
values*, "door komma's gescheiden waarden"). De eerste regel is een uitzondering:
dat zijn de kolomnamen.

```
toets_id,vak,lokaal,tijd,aantal_studenten,vereist_toezicht
T1,Statistiek,A1.04,09:00,110,2
T2,Inleiding Recht,B2.10,09:00,180,3
T3,Microbiologie,C0.22,09:00,55,1
...
```

Zo simpel is het. Geen opmaak, geen kleurtjes — alleen tekst en komma's. En
precies dáárom exporteert vrijwel elk roostersysteem zijn data op deze manier:
elk programma, hoe verschillend ook, kan platte tekst lezen en schrijven.

---

## Het concept: van bestand naar lijst van dicts

Je hebt nu twee dingen nodig:

1. `open(...)` — dit **opent** het bestand, zodat Python erbij kan.
2. `csv.DictReader(...)` — dit leest de geopende inhoud, en maakt van **elke
   regel een dict**, met de kolomkoppen (`toets_id`, `vak`, ...) als sleutels.

Met andere woorden: `csv.DictReader` geeft je precies de structuur terug die je
in module 3 en module 7 zelf met de hand bouwde — een **lijst van dicts**. Het
enige dat verandert, is waar die lijst vandaan komt: niet meer uit jouw
toetsenbord, maar uit een bestand. De rest — erdoorheen loopen, waarden
opvragen met `["kolomnaam"]` — werkt exact zoals je al kent.

---

## Uitgewerkt voorbeeld

> ⚠️ **Voorbeeld, geen voorschrift.** We gebruiken `toetsen.csv` om het concept
> concreet te maken. Jouw eigen roosterexport heeft mogelijk andere kolommen —
> dat leer je verderop in deze fase juist bijbuigen.

```python
import csv

with open("../../voorbeelddata/toetsen.csv", newline="", encoding="utf-8") as bestand:
    toetsen = list(csv.DictReader(bestand))

for toets in toetsen:
    print(toets["toets_id"], toets["vak"], "om", toets["tijd"])
```

Dit toont:

```
T1 Statistiek om 09:00
T2 Inleiding Recht om 09:00
T3 Microbiologie om 09:00
T4 Calculus om 11:00
T5 Bestuurskunde om 11:00
T6 Psychologie om 11:00
T7 Economie om 14:00
T8 Ethiek om 14:00
```

Twee regels verdienen een woordje uitleg, zodat je ze niet als magie hoeft aan te
nemen: `import` (Engels voor "invoeren") haalt gereedschap uit Pythons eigen kast
— hier het `csv`-gereedschap — zodat je het kunt gebruiken. En `with` zorgt dat
het bestand na afloop netjes weer wordt afgesloten, ook als er onderweg iets
misgaat. Meer hoef je er nu niet van te weten; we komen erop terug.

---

## Twee dingen die je gaan verrassen

### 1. Alles is tekst

`csv.DictReader` maakt van élke waarde een **string** (tekst) — ook als het een
getal lijkt. `toets["aantal_studenten"]` is dus niet het getal `110`, maar de
tekst `"110"`. Kijk wat er gebeurt als je die tekst met een getal wilt
vergelijken:

```python
toets = toetsen[0]     # de eerste toets: T1, Statistiek, 110 studenten
print(toets["aantal_studenten"] > 100)
```

```
TypeError: '>' not supported between instances of 'str' and 'int'
```

Python weigert dit — terecht, want `"110"` is geen getal, het is een rijtje
tekens dat er toevallig als een getal uitziet. Om er wél mee te rekenen of te
vergelijken, moet je het eerst omzetten met `int(...)`:

```python
print(int(toets["aantal_studenten"]) > 100)   # True — 110 is meer dan 100
```

Onthoud dit: **elke waarde uit een CSV is tekst, tot jij hem omzet.** Dit gaat je
in de opdracht nog een keer opzettelijk in de weg zitten.

### 2. Het pad is relatief

`"../../voorbeelddata/toetsen.csv"` is een **relatief pad**: het wijst naar het
bestand gezien vanaf de map waar je `python` draait — niet vanaf een vaste
plek op je computer. Draai je `opdracht.py` vanuit de modulemap, dan klopt het
pad. Draai je hem vanuit een andere map, dan bestaat `../../voorbeelddata/...`
daar niet, en krijg je:

```
FileNotFoundError: [Errno 2] No such file or directory: '../../voorbeelddata/toetsen.csv'
```

Zie je die foutmelding? Ga eerst met `cd` naar de map van `opdracht.py`, en
draai het dan opnieuw.

---

## Nu jij

Open **`opdracht.py`**. Vier stappen, elk met een voorspelregel erboven: bedenk
eerst wat je verwacht te zien, draai dan pas.

> Vastgelopen op de foutmelding? In **Ask-modus**: *"leg uit wat deze
> FileNotFoundError betekent en hoe ik hem oplos"* — laat het je uitleggen,
> los het dan zelf op.

Klaar? Ga naar **`check.md`**.
