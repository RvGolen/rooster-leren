# Module 4 — AI-code lezen

⏱️ ± 25–30 minuten · Fase 2 · **Nieuw concept:** de werkwijze *voorspel → lees →
draai → pas aan*

> Dit is de belangrijkste module van deze fase. Geen nieuwe Python-syntax vandaag —
> wel de vaardigheid waar de rest van de cursus op leunt.

---

## Eerst even terugdenken 🤔

Aan het eind van module 3 zag je iets vreemds: `groupby("toets_id").size()` op het
rooster gaf **7 regels**, terwijl `toetsen.csv` **8 toetsen** bevat. Je hebt er toen
zelf over nagedacht, zonder antwoord te krijgen.

> Hou die gedachte vast. Aan het eind van deze module weet je precies wat er
> gebeurde — en, belangrijker, hoe je dit soort dingen voortaan zelf opspoort.

---

## De werkwijze: voorspel → lees → draai → pas aan

Vanaf nu gebeurt er iets nieuws: de AI schrijft soms een eerste versie van je code.
Dat scheelt tijd — maar het verandert ook jouw taak. Jouw werk is dan niet meer
"accepteren wat er staat", maar vier stappen, in deze volgorde:

1. **Voorspel** — lees de code, en bedenk vóórdat je hem draait wat je verwacht dat
   eruit komt. Hoeveel regels? Welke waarden?
2. **Lees** — ga regel voor regel na en zeg (hardop of in je hoofd) wat elke regel
   doet. Niet "dit ziet er goed uit", maar "deze regel doet X, met dit resultaat".
3. **Draai** — voer de code echt uit en vergelijk de uitkomst met je voorspelling.
4. **Pas aan** — klopte je voorspelling niet? Zoek uit waarom, en herstel wat er
   niet klopt.

Het scharniermoment zit in stap 3: het **verschil** tussen wat je voorspelde en wat
er werkelijk gebeurde. Klopte je voorspelling niet, dan leer je iets — over de code,
óf over je eigen aanname. Beide zijn winst.

---

## Waarom dit de kernvaardigheid van de hele cursus is

Een AI-assistent schrijft code die *plausibel* is: nette namen, een vriendelijke
docstring, logische opbouw. Dat ziet er goed uit — en dat is precies het probleem.
Een AI produceert wat **waarschijnlijk klopt** op basis van je vraag, niet wat
**waar is** in jouw situatie. Dat is geen bug in het gereedschap; het is de aard
ervan. De AI kent jouw rooster niet, jouw uitzonderingen niet, jouw stille
aannames niet.

Jij bent de enige die weet wat er in jouw situatie op het spel staat — een toets
zonder toezicht is geen typefout, het is een student die tijdens een tentamen geen
enkele surveillant in de zaal heeft. Dat merk je alleen als je de code leest,
niet als je hem alleen maar draait en op de uitvoer vertrouwt.

---

## Uitgewerkt voorbeeld: `gegenereerd.py`

> ⚠️ **Voorbeeld, geen voorschrift.** We gebruiken hier de dekkingscontrole van het
> voorbeeldrooster. Jouw eigen controles kunnen andere regels nodig hebben — de
> werkwijze van deze module blijft hetzelfde.

Open **`gegenereerd.py`** in Cursor. De kopregel vertelt je precies wat er gebeurde:
een AI-assistent kreeg de opdracht *"controleer of elke toets genoeg surveillanten
heeft"*, en leverde dit script op.

Voordat je hem draait: **voorspel**. Kijk naar `toetsen.csv` — hoeveel toetsen
staan daarin? Verwacht je evenveel regels uitvoer? Schrijf voor jezelf op wat je
denkt te zien.

Draai hem dan pas (vanuit deze map, anders vindt hij het CSV-pad niet):

```bash
python gegenereerd.py
```

Vergelijk de uitvoer met je voorspelling. Klopte het? Zo niet: dat is precies het
moment waar deze module over gaat.

---

## De vaste reflex

Vraag, elke keer dat je AI-code onder ogen krijgt, in **Ask-modus**:

> *"leg uit wat deze code doet"*

Dit is de vraag die je de komende maanden waarschijnlijk duizend keer gaat
stellen. Maar laat je niet geruststellen door een zelfverzekerd antwoord — vraag
altijd door, met iets als:

> *"wat gebeurt er als er géén rij is voor een toets?"*

Die tweede vraag is waar de AI zelf zelden mee begint. Hij beschrijft graag wat de
code doet met de gevallen die hij ziet — niet wat er ontbreekt aan de gevallen die
hij niet ziet.

---

## Nu jij

Open **`opdracht.py`**. Weinig code vandaag, veel denkwerk: je voorspelt, draait,
zoekt uit wat er misging, en verklaart waarom — allemaal vóór je ook maar íets
repareert.

> Vastgelopen op wat een regel doet? In **Ask-modus**: *"leg uit wat deze code
> doet"* — en vraag meteen door met *"wat gebeurt er als er géén rij is voor een
> toets?"*

Klaar? Ga naar **`uitleg.md`** en daarna **`check.md`**.
