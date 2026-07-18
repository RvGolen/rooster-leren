# Module 5 — Condities

⏱️ ± 20 minuten · Fase 1 · **Nieuw concept:** `if` / `elif` / `else` (kiezen)

> Bouwt op alles tot nu toe, vooral op loops (module 4).

---

## Eerst even raden 🤔

```python
studenten = 45
capaciteit = 40
if studenten > capaciteit:
    print("Past niet!")
else:
    print("Past.")
```

> Wat komt eruit? En wat als `studenten` 30 was geweest? Gok beide.

---

## Het concept: een keuze op basis van een voorwaarde

Tot nu toe deed je code altijd hetzelfde. Maar een rooster zit vol *als-dan*: *als*
de zaal te klein is, meld een probleem; *als* er te weinig surveillanten zijn,
waarschuw. Daarvoor is **`if`** (Engels voor "als").

```python
studenten = 45
capaciteit = 40

if studenten > capaciteit:
    print("Let op: te veel studenten voor dit lokaal")
```

- Na `if` staat een **voorwaarde** die waar (`True`) of niet waar (`False`) is.
- Eindigt op een **dubbele punt** `:`, en de regel eronder **springt in** — net als
  bij de loop.
- Is de voorwaarde waar, dan draait de ingesprongen regel. Zo niet, dan niet.

### `else`: het andere geval

```python
if studenten > capaciteit:
    print("Past niet")
else:
    print("Past prima")
```

`else` (Engels voor "anders") vangt **alle gevallen op** waarin de `if` niet waar
was.

### `elif`: meerdere gevallen

```python
if studenten > capaciteit:
    print("Te vol")
elif studenten == capaciteit:
    print("Precies vol")
else:
    print("Er is ruimte over")
```

`elif` is kort voor *else if*: "anders, als dit andere klopt". Python loopt van boven
naar beneden en pakt het **eerste** geval dat waar is.

### De vergelijkingen (let op de dubbele `==`)

| Schrijf je | Betekenis |
|------------|-----------|
| `a == b` | a is **gelijk** aan b — let op: **twee** istekens! |
| `a != b` | a is **niet** gelijk aan b |
| `a > b` / `a < b` | groter dan / kleiner dan |
| `a >= b` / `a <= b` | groter-of-gelijk / kleiner-of-gelijk |

> ⚠️ **Eén `=` is toewijzen (module 1), twee `==` is vergelijken.** Dit is de meest
> gemaakte beginnersfout. `studenten = 40` *zet* studenten op 40; `studenten == 40`
> *vraagt* of studenten 40 is. Heel verschillend.

---

## Uitgewerkt voorbeeld — uit de surveillance-context

> ⚠️ **Voorbeeld, geen voorschrift.** Wat "genoeg surveillanten" is, bepaalt jouw
> situatie. Hier nemen we als voorbeeld: minstens 1 surveillant per 30 studenten.

We combineren `if` met de loop uit module 4: controleer **elke** toets.

```python
toetsen = [
    {"lokaal": "A1.04", "studenten": 30, "surveillanten": 2},
    {"lokaal": "B2.10", "studenten": 60, "surveillanten": 1},   # te weinig!
    {"lokaal": "C0.21", "studenten": 25, "surveillanten": 1},
]

for toets in toetsen:
    # vuistregel (VOORBEELD): minstens 1 surveillant per 30 studenten
    minimaal_nodig = toets["studenten"] / 30
    if toets["surveillanten"] < minimaal_nodig:
        print("PROBLEEM in", toets["lokaal"], "- te weinig surveillanten")
    else:
        print(toets["lokaal"], "- oké")
```

Dit toont:

```
A1.04 - oké
PROBLEEM in B2.10 - te weinig surveillanten
C0.21 - oké
```

Zie je wat hier gebeurt? De loop gaat langs élke toets, en de `if` beslist per toets
of er een probleem is. Dit *patroon* — loop + if om iets te controleren — is letterlijk
de kern van Project 2 (de validator). Je bent er al bijna.

---

## Nu jij

Open **`opdracht.py`**. De steun is hier weer wat kleiner.

> Hint nodig? In **Ask-modus**: *"waarom moet ik == gebruiken en niet = in een
> if?"*

Klaar? Ga naar **`check.md`**.
