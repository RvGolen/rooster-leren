# Module 6 — Je script opdelen in bestanden

⏱️ ± 25–30 minuten · Fase 2 (slot) · **Nieuw concept:** `import` van je eigen
bestanden

---

## Eerst even raden 🤔

Tot nu toe stond alles in één bestand: `opdracht.py`. Deze module krijg je er
ineens **drie**: `data.py`, `regels.py` en `opdracht.py`. Bovenaan `opdracht.py`
staat dit:

```python
import data
import regels
```

> Wat denk je dat deze twee regels doen? En wat denk je dat er gebeurt als je
> `data.lees_toetsen()` aanroept? Schrijf voor jezelf op wat je verwacht,
> voordat je verderleest.

---

## De kast die je zelf vult

In module 2 zei ik over `import pandas as pd`: dit haalt gereedschap uit
Pythons eigen kast. Dat klopte — maar het was maar het halve verhaal. Vandaag
blijkt het andere deel: **die kast kun je zelf vullen.**

`import data` betekent letterlijk "gebruik `data.py`" — een bestand dat jij (of
in dit geval: wij) zelf schreven, geen kant-en-klaar pakket. En dan is
`data.lees_toetsen()` niets geheimzinnigs: het is **de functie `lees_toetsen`
uit `data.py`**, aangeroepen via de punt-notatie die je al kent van classes in
module 5. `bestuurskunde.past_in(b211)` was "vraag aan `bestuurskunde`";
`data.lees_toetsen()` is "vraag aan `data.py`".

Er verandert dus niets fundamenteels aan `import` — alleen de plek waar het
gereedschap vandaan komt. Bij `import pandas` komt het uit een extern pakket;
bij `import data` komt het uit een bestand dat naast `opdracht.py` in dezelfde
map ligt.

---

## Uitgewerkt voorbeeld

> ⚠️ **Voorbeeld, geen voorschrift.** We delen dit script op in drie stukken om
> het concept concreet te maken. Jouw eigen indeling kan er anders uitzien —
> daar kom je bij **jouw situatie** onderaan deze module op uit.

Open **`data.py`**. Vijf functies, en verder niets:

```python
"""Alles wat met het inlezen van data te maken heeft."""
import pandas as pd

MAP = "../../voorbeelddata/"


def lees_toetsen():
    return pd.read_csv(MAP + "toetsen.csv")


def lees_rooster():
    return pd.read_csv(MAP + "rooster.csv")
```

(de andere drie `lees_...`-functies staan er ook, met dezelfde vorm). Elke
functie doet precies één ding: één CSV inlezen en de tabel teruggeven. Niets
over regels, niets over wat een goed rooster is — alleen: hier komt de data
vandaan.

Open daarna **`opdracht.py`**:

```python
"""Zet alles aan elkaar: data inlezen, regels controleren, resultaat tonen."""
import data
import regels

toetsen = data.lees_toetsen()
rooster = data.lees_rooster()

meldingen = regels.controleer_dekking(toetsen, rooster)
```

Vier regels, en je ziet meteen wat er gebeurt: data ophalen, regels toepassen.
`opdracht.py` weet niet hóe `lees_toetsen` de CSV leest, en niet hóe
`controleer_dekking` telt — het hoeft dat ook niet te weten. Het zet alleen de
stukken aan elkaar.

---

## Het concept: opdelen naar verantwoordelijkheid

Drie bestanden, drie duidelijk gescheiden taken:

- **`data.py`** weet **hoe** je bestanden leest.
- **`regels.py`** weet **wat** een goed rooster is (welke regels gelden).
- **`opdracht.py`** weet **hoe de twee op elkaar volgen** — verder niets.

Geen van drieën hoeft te weten hoe de andere het precies doet.
`controleer_dekking` in `regels.py` maakt het niet uit of de toetsen uit een
CSV, een Excel-bestand of iets anders komen — hij krijgt gewoon een tabel
binnen. En `data.py` maakt het niet uit welke regels je er straks op loslaat.

---

## Waarom dit ertoe doet

Twee redenen, allebei eerlijk:

1. **Je vindt dingen terug.** Zoek je de plek waar een CSV wordt ingelezen? Dat
   is altijd `data.py`. Zoek je een regel over dekking? Dat is altijd
   `regels.py`. Bij één bestand van honderden regels moet je eerst zoeken —
   hier weet je het al voordat je iets opent.
2. **De echte reden: kleine bestanden zijn kleine opdrachten aan de AI.** Vraag
   je de AI om een regel toe te voegen aan `regels.py`, dan hoeft hij alleen
   dát bestand aan te raken — niet `data.py`, niet `opdracht.py`. Een wijziging
   die je te overzien is, is een wijziging die je nog kunt controleren. Dat is
   precies wat je in fase 4 verder uitbouwt: kleine, behapbare opdrachten aan
   de AI in plaats van "herschrijf het hele script maar".

---

## De valkuil

Deze drie bestanden werken alleen samen als je ze draait vanuit de map waar ze
staan. Draai je `opdracht.py` vanuit een andere map, dan struikelt hij over de
`../../voorbeelddata/...`-paden in `data.py` — precies de `FileNotFoundError` die
je in module 1 al zag:

```
FileNotFoundError: [Errno 2] No such file or directory: '../../voorbeelddata/toetsen.csv'
```

De oplossing is dezelfde als toen: ga eerst met `cd` naar de map van
`opdracht.py`, en draai het dan opnieuw:

```bash
cd 03-data-en-structuur/module-06-script-opdelen
python opdracht.py
```

> Er bestaat een tweede foutmelding in de buurt: `ModuleNotFoundError: No module
> named 'data'`. Die krijg je als Python `data.py` niet kan vinden — bijvoorbeeld
> als je in een kale terminal zelf `import data` typt zonder in de modulemap te
> staan. Bij het gewone `python opdracht.py` vanuit de juiste map kom je hem niet
> tegen; hij hoort bij `import`, dus goed om te herkennen. De oplossing is
> opnieuw: `cd` naar de modulemap.

---

## Nu jij

Open **`opdracht.py`**. Eén `#TODO`: print elke melding, en zeg met zoveel
woorden dat alles in orde is als er geen meldingen zijn. In stubstaat geeft
`controleer_dekking` nog een lege lijst terug — dus je script draait al
foutloos, alleen zonder nuttige uitvoer.

> Loop je tegen een foutmelding aan? In **Ask-modus**: *"leg uit wat deze
> foutmelding betekent en hoe ik hem oplos"* — plak de melding erbij, laat het je
> uitleggen, los het dan zelf op.

Klaar? Ga naar **`uitleg.md`**, en daarna naar **`check.md`**.
