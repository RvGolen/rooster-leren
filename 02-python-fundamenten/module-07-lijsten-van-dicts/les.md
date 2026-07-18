# Module 7 — Lijsten van dicts & geneste loops

⏱️ ± 25–30 minuten · Fase 1 (slot) · **Nieuw concept:** de *geneste loop* om **alle
paren** te vergelijken

> Dit is de laatste module vóór Project 1, en hij brengt alles samen: lijst (mod 2),
> dict (mod 3), loop (mod 4), conditie (mod 5), functie (mod 6). De steun is hier het
> kleinst — dat hoort: je kunt dit nu zelf.

---

## Eerst even raden 🤔

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

> Hoeveel regels komen hieruit, denk je? En welke combinaties? Gok eerst — dit is de
> kern van vandaag.

---

## Deel 1: een rooster *is* een lijst van dicts

Je weet het eigenlijk al. Eén dienst is een dict; alle diensten samen zijn een lijst:

```python
rooster = [
    {"persoon": "Jansen",   "tijd": "09:00", "lokaal": "A1.04"},
    {"persoon": "De Vries", "tijd": "09:00", "lokaal": "B2.10"},
    {"persoon": "Jansen",   "tijd": "09:00", "lokaal": "C0.21"},
]
```

Met één loop kun je er al doorheen (module 4):

```python
for dienst in rooster:
    print(dienst["persoon"], "om", dienst["tijd"])
```

Maar voor conflicten is dat niet genoeg. Een conflict zit tússen **twee** diensten.
Je moet dus elke dienst met elke andere vergelijken. Daarvoor heb je een **loop in
een loop** nodig.

## Deel 2: `range()` — tellen met nummers

Om paren te vergelijken hebben we de **index** (het plek-nummer, module 2) nodig.
`range(n)` (Engels voor "bereik") geeft je de getallen `0, 1, ... t/m n-1`:

```python
for i in range(3):
    print(i)        # toont 0, dan 1, dan 2
```

Combineer met `len()` en je loopt langs alle plekken van een lijst:

```python
for i in range(len(rooster)):
    print(rooster[i]["persoon"])   # rooster[0], rooster[1], rooster[2]
```

## Deel 3: de geneste loop — alle paren

Nu het hart van de module. Twee loops in elkaar:

```python
for i in range(len(rooster)):
    for j in range(i + 1, len(rooster)):
        a = rooster[i]
        b = rooster[j]
        # vergelijk a en b...
```

Waarom begint de **binnenste** loop bij `i + 1`? Denk aan **handen schudden** in een
groep: jij schudt ieder ander één keer de hand. Je schudt jezelf niet (`j` mag niet
gelijk zijn aan `i`), en als jij Jansen al de hand gaf, hoeft Jansen jou niet
nógmaals. `i + 1` zorgt precies daarvoor: elk paar één keer, nooit met zichzelf.

> Zonder die `i + 1` zou je elk paar twee keer checken én elke dienst met zichzelf
> vergelijken — en een dienst is áltijd "in conflict" met zichzelf (zelfde persoon,
> zelfde tijd). Die `i + 1` is dus niet alleen netter, hij voorkomt een echte fout.

---

## Uitgewerkt voorbeeld — alle conflicten in een rooster

> ⚠️ **Voorbeeld, geen voorschrift.** We gebruiken de conflict-definitie uit module
> 6 (zelfde persoon én tijd). Jouw situatie kan extra of andere regels hebben.

```python
def heeft_conflict(a, b):
    return a["persoon"] == b["persoon"] and a["tijd"] == b["tijd"]


rooster = [
    {"persoon": "Jansen",   "tijd": "09:00", "lokaal": "A1.04"},
    {"persoon": "De Vries", "tijd": "09:00", "lokaal": "B2.10"},
    {"persoon": "Jansen",   "tijd": "09:00", "lokaal": "C0.21"},   # Jansen dubbel!
    {"persoon": "Jansen",   "tijd": "11:00", "lokaal": "A1.04"},   # andere tijd: ok
]

# Vergelijk elk paar precies één keer
for i in range(len(rooster)):
    for j in range(i + 1, len(rooster)):
        a = rooster[i]
        b = rooster[j]
        if heeft_conflict(a, b):
            print("CONFLICT:", a["persoon"], "om", a["tijd"],
                  "in", a["lokaal"], "en", b["lokaal"])
```

Dit toont:

```
CONFLICT: Jansen om 09:00 in A1.04 en C0.21
```

Eén conflict, precies één keer gemeld. Jansen staat om 09:00 in twee lokalen; de
inzet om 11:00 is geen probleem. **Dit is, in het klein, Project 1.**

---

## Nu jij

Open **`opdracht.py`**. Hier krijg je het minst voorgekauwd van alle modules tot nu
toe. Bouw rustig op, draai vaak, en voorspel telkens wat je verwacht.

> Vastgelopen op de geneste loop? In **Ask-modus**: *"leg uit waarom de binnenste
> loop bij i + 1 begint"* — laat het je uitleggen, schrijf het dan zélf.

Klaar? Ga naar **`check.md`** — en daarna naar je eerste project. 🎉
