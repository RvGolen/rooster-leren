# Module 2 — Pandas: de tabel-bril

⏱️ ± 20–25 minuten · Fase 2 · **Nieuw concept:** de DataFrame

---

## Eerst installeren: je eerste pakket

Tot nu toe deed je alles met Python zélf — geen extra spullen nodig. Vandaag ga
je voor het eerst een **pakket** gebruiken: kant-en-klaar gereedschap dat iemand
anders al voor je heeft geschreven, en dat je één keer installeert. `pandas` is
zo'n pakket: het is speciaal gemaakt om met tabellen te werken.

Open een terminal zoals je gewend bent (**Terminal → New Terminal** in Cursor)
en typ:

```
pip install pandas
```

Meestal werkt dit meteen. Maar een installatie is nieuw terrein, dus hier zijn
de drie dingen die kunnen misgaan — en de uitweg per geval:

**1. `pip: command not found`**
Je terminal kent het commando `pip` niet. Probeer `pip3 install pandas`, of nog
beter: `python -m pip install pandas`. Die laatste vorm werkt het vaakst, want
hij gebruikt gegarandeerd dezelfde Python als waarmee je straks je script
draait.

**2. De installatie lijkt te lukken, maar je script zegt
`ModuleNotFoundError: No module named 'pandas'`**
Je hebt waarschijnlijk meerdere Python's op je computer, en pandas is in de
verkeerde beland. Draai `python -m pip install pandas` — met exact hetzelfde
woord `python` waarmee je ook `python opdracht.py` start. Zo installeer je
pandas gegarandeerd op de plek waar je script hem zoekt.

**3. Je zit in de verkeerde map, of in een oude terminal**
Open een nieuwe terminal en controleer of het echt goed staat:

```
python -c "import pandas; print(pandas.__version__)"
```

Krijg je een versienummer (zoals `2.3.3`) terug? Dan staat het goed.

> Loop je vast op een foutmelding hierboven? Dit is een prima eerste oefening
> in **Ask-modus**: plak de melding en vraag *"wat betekent deze foutmelding?"*.
> Een foutmelding is geen falen — het is informatie. Lees hem, snap hem, los
> hem op.

---

## Eerst even raden 🤔

Dit is `toetsen.csv` — je kent hem al uit module 1:

```
toets_id,vak,lokaal,tijd,aantal_studenten,vereist_toezicht
T1,Statistiek,A1.04,09:00,110,2
T2,Inleiding Recht,B2.10,09:00,180,3
...
```

Straks laat je pandas dit bestand inlezen en doe je gewoon `print(toetsen)`.
Hoe denk je dat dat eruitziet, vergeleken met je `for`-loop uit module 1 die
regel voor regel `"<vak> om <tijd>"` printte? Meer regels? Minder? Anders
opgemaakt? Gok eerst.

---

## Het concept: de DataFrame

In module 1 las je `toetsen.csv` in als een **lijst van dicts**, en liep je er
rij voor rij doorheen. Dat werkt, maar je bekeek de data steeds één rij
tegelijk.

Een **DataFrame** is iets anders: een tabel die helemaal in het geheugen van
Python zit — Excel, maar dan in Python. In plaats van rij voor rij te kijken,
kijk je nu naar de **hele tabel tegelijk**: alle rijen, alle kolommen, in één
keer zichtbaar. `pandas` is het pakket dat je die tabel-bril geeft.

---

## Uitgewerkt voorbeeld

> ⚠️ **Voorbeeld, geen voorschrift.** We gebruiken `toetsen.csv` om het concept
> concreet te maken. Jouw eigen roosterexport heeft mogelijk andere kolommen.

```python
import pandas as pd

toetsen = pd.read_csv("../../voorbeelddata/toetsen.csv")

print(toetsen)              # de hele tabel
print(toetsen.head(3))      # alleen de eerste drie rijen
print(toetsen.columns)      # welke kolommen zitten erin?
print(len(toetsen))         # hoeveel rijen?
print(toetsen["vak"])       # één kolom
```

Dit toont (de eerste twee `print`'s ingekort, de rest volledig):

```
  toets_id              vak lokaal   tijd  aantal_studenten  vereist_toezicht
0       T1       Statistiek  A1.04  09:00               110                 2
1       T2  Inleiding Recht  B2.10  09:00               180                 3
...
  toets_id              vak lokaal   tijd  aantal_studenten  vereist_toezicht
0       T1       Statistiek  A1.04  09:00               110                 2
1       T2  Inleiding Recht  B2.10  09:00               180                 3
2       T3    Microbiologie  C0.22  09:00                55                 1
Index(['toets_id', 'vak', 'lokaal', 'tijd', 'aantal_studenten',
       'vereist_toezicht'],
      dtype='object')
8
0         Statistiek
1    Inleiding Recht
2      Microbiologie
3           Calculus
4      Bestuurskunde
5        Psychologie
6           Economie
7             Ethiek
Name: vak, dtype: object
```

Twee woordjes uitleg, zodat ze geen magie blijven: `import pandas as pd` haalt
het pandas-gereedschap uit de kast — net als `import csv` in module 1 — en
`as pd` is gewoon een afkorting, zodat je straks `pd.read_csv(...)` typt in
plaats van `pandas.read_csv(...)`. Meer hoef je er nu niet van te weten.

Herken je de vorm? Het is dezelfde data als in module 1, maar nu in één keer
overzichtelijk — dat contrast ís de les.

---

## Eén verschil dat je gaat helpen

Weet je nog dat `toets["aantal_studenten"]` in module 1 de tekst `"110"` was,
en dat je `int(...)` moest gebruiken om ermee te rekenen? Bij een DataFrame is
dat al opgelost: pandas herkent zelf dat een kolom met getallen ook getallen
bevat. Kijk maar:

```python
print(toetsen["aantal_studenten"].sum())
```

```
780
```

Dat werkt meteen — geen `int(...)` nodig. Pandas heeft bij het inlezen al
gezien dat die kolom getallen bevat, en behandelt hem ook zo.

---

## Nu jij

Open **`opdracht.py`**. Je krijgt minder voorgekauwd dan in module 1 — vul de
`#TODO`'s stap voor stap in, en draai vaak: `python opdracht.py`.

> Vastgelopen op een installatie-foutmelding? In **Ask-modus**: *"wat betekent
> deze foutmelding?"* — plak de melding, laat het je uitleggen, los het dan
> zelf op.

Klaar? Ga naar **`check.md`**.
