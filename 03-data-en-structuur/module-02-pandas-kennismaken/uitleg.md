# Waarom een tabel-bril? — het *waaróm* achter module 2

## 1. Eén vraag, één regel — in plaats van een hele loop

Met een lijst van dicts (module 1) moet je voor bijna elke vraag zelf een loop
schrijven: wil je weten hoeveel studenten er in totaal een toets maken, dan
schrijf je een teller, een loop, een `int(...)`, en een `print` aan het eind —
minstens vier of vijf regels.

Met een DataFrame is dat:

```python
toetsen["aantal_studenten"].sum()
```

Eén regel. Pandas weet al dat de kolom getallen bevat, en telt hem in één klap
op. Bij 8 toetsen scheelt dat weinig — je zou het met de hand kunnen narekenen.
Bij de 400 toetsen van een echte toetsweek is het het verschil tussen "dit
reken ik er even bij" en "dit doe ik niet, te veel gedoe".

## 2. Waarom dit geen vervanging is van wat je al kon

Wees eerlijk tegen jezelf: pandas is niet "beter" dan je `for`-loop uit module
1. Het is een ánder gereedschap, met een andere sterkte. Je loop is precies
duidelijk in wat er gebeurt, stap voor stap — fijn om te leren en fijn om te
debuggen. Een DataFrame is sneller te bevragen zodra de tabel groot wordt, en
je typt minder code voor optellingen, filters en overzichten.

Je kiest per klus. Een paar rijen handmatig doorlopen om te snappen wat erin
zit? Een loop is prima. Snel duizend rijen willen optellen, filteren of
sorteren? Dan grijp je naar pandas.

## 3. Wat er niet is veranderd

De data zelf is identiek — dezelfde `toetsen.csv`, dezelfde kolommen. Alleen de
**bril** waarmee je ernaar kijkt is anders: rij voor rij (module 1) versus de
hele tabel tegelijk (module 2). Dat is ook waarom `import pandas as pd` er
weinig anders uitziet dan `import csv`: allebei halen ze gereedschap uit de
kast om dezelfde soort bestanden te lezen.

---

## Termen van vandaag

| Term | Betekenis |
|------|-----------|
| pakket | kant-en-klaar gereedschap van iemand anders, één keer geïnstalleerd met `pip install ...` |
| DataFrame | een tabel die volledig in het geheugen van Python zit — Excel, maar dan in Python |
| `pd.read_csv(...)` | leest een CSV-bestand in als DataFrame |

---

## Door naar de volgende module

Je kunt nu een CSV-bestand als tabel inlezen en er de basisvragen over stellen:
hoeveel rijen, welke kolommen, wat is de som. In
`module-03-pandas-filteren-tellen/` ga je die tabel gerichter bevragen —
filteren, selecteren, en meer dan alleen optellen.
