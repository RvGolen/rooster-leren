# Module 3 — Denken als een solver

⏱️ ± 30 minuten · Fase 3 · **Nieuw concept:** beslissingsvariabele, constraint, objective

---

## Eerst installeren: ortools

In module 2 bouwde je zelf een greedy-toewijzer — en zag je waar hij schuurt: hij kijkt niet
vooruit, mist soms combinaties, en wordt al snel ongeldig of duur. Vandaag leer je een andere
aanpak: je beschrijft de **regels** en het **doel**, en een **solver** zoekt de beste toewijzing
voor je.

Daarvoor heb je een nieuw pakket nodig: `ortools`. Open een terminal (**Terminal → New Terminal**
in Cursor) en typ:

```
pip install ortools
```

Meestal werkt dit meteen. Maar hier zijn de drie dingen die kunnen misgaan — en de uitweg:

**1. `pip: command not found`**
Probeer `pip3 install ortools`, of nog beter: `python -m pip install ortools`. Die laatste vorm
werkt het vaakst, want hij gebruikt gegarandeerd dezelfde Python als waarmee je straks je script
draait.

**2. Het lijkt te lukken, maar je script zegt `ModuleNotFoundError: No module named 'ortools'`**
Je hebt waarschijnlijk meerdere Python's op je computer, en ortools is in de verkeerde beland.
Draai `python -m pip install ortools` — met exact hetzelfde woord `python` waarmee je ook
`python mini_model.py` start.

**3. Je zit in de verkeerde map, of in een oude terminal**
Open een nieuwe terminal en controleer of het goed staat:

```
python -c "from ortools.sat.python import cp_model; print('ok')"
```

Krijg je `ok` terug? Dan staat het goed.

> Loop je vast op een foutmelding? Dit is een prima oefening in **Ask-modus**: plak de melding
> en vraag *"wat betekent deze foutmelding?"*. Een foutmelding is geen falen — het is informatie.

---

## Eerst even raden

Hieronder staat `mini_model.py` — een klein model met drie mensen en twee toetsen. Lees het door
voordat je het draait.

```python
mensen = ["Anna", "Ben", "Carla"]
kosten = {"Anna": 40, "Ben": 38, "Carla": 90}
toetsen = ["ochtend", "middag"]
```

Anna kost 40 per dienst, Ben 38, Carla 90. Elke toets heeft precies één persoon nodig.

**Gok nu:** wie komt op "ochtend", wie op "middag"? En waarom staat Carla er waarschijnlijk
niet op? Schrijf je antwoord op voordat je het script draait.

---

## De omslag

In module 2 besloot jíj wie waar stond: pak de goedkoopste beschikbare persoon, houd een lijstje
bij, ga naar de volgende toets. Jij beschreef het *hoe*.

Bij een solver doe je dat andersom. Je beschrijft alleen:
- de **regels** (wie mag waar, hoeveel mensen per toets);
- het **doel** (zo goedkoop mogelijk).

De solver doorzoekt zelf alle mogelijke toewijzingen en kiest de beste. Jij zegt *wat*, de
machine doet het *hoe*.

> ⚠️ **Voorbeeld, geen voorschrift.** We gebruiken een mini-model met Anna, Ben en Carla om de
> drie bouwstenen concreet te maken. Je echte rooster heeft meer mensen en meer toetsen — de
> bouwstenen zijn hetzelfde.

---

## De drie bouwstenen

Open `mini_model.py` en lees mee.

### 1. Beslissingsvariabele

```python
x = {(p, t): model.NewBoolVar(f"{p}_{t}") for p in mensen for t in toetsen}
```

Een **beslissingsvariabele** is een ja/nee-knop die de solver mag omzetten. Voor elke
combinatie van persoon en toets — Anna/ochtend, Anna/middag, Ben/ochtend, enzovoort — maakt het
model één zo'n knop. De solver beslist uiteindelijk welke knoppen op "ja" (1) en welke op "nee"
(0) staan.

### 2. Constraint

```python
for t in toetsen:
    model.Add(sum(x[p, t] for p in mensen) == 1)

for p in mensen:
    model.Add(sum(x[p, t] for t in toetsen) <= 1)
```

Een **constraint** is een harde regel waar de oplossing aan moet voldoen. Hier zijn er twee:
elke toets heeft precies één persoon, en niemand staat op allebei de toetsen tegelijk. De solver
gooit elke toewijzing die deze regels breekt direct weg.

### 3. Objective (doelfunctie)

```python
model.Minimize(sum(kosten[p] * x[p, t] for p in mensen for t in toetsen))
```

De **objective** — of **doelfunctie** — is het getal dat de solver zo laag mogelijk maakt.
Hier zijn dat de totale kosten: de som van de kosten van iedereen die ergens op staat.

`from ortools.sat.python import cp_model` haalt het ortools-gereedschap uit de kast — net als
`import csv` of `import pandas` dat doet voor andere pakketten.

---

## Draai het model

Ga naar de map van deze module en typ:

```
python mini_model.py
```

Je ziet:

```
Goedkoopste toewijzing:
  ochtend: Ben (kosten 38)
  middag: Anna (kosten 40)
Totale kosten: 78
```

Ben (38) en Anna (40) zijn goedkoper dan Carla (90), dus kiest de solver hen. Carla staat er
niet op — niet omdat ze verboden is, maar omdat de solver haar niet nodig heeft om het doel te
bereiken. Klopte je voorspelling?

---

## Nu jij

Open **`opdracht.py`**. Je typt geen model — je leest en voorspelt. Lees de stappen goed, en
schrijf je antwoorden als commentaar in het bestand.

Klaar? Ga naar **`check.md`**.
