# Waarom een bestand inlezen? — het *waaróm* achter module 1

## 1. Data hoort niet in je code

In fase 1 stond je rooster gewoon tussen je Python-code:

```python
rooster = [
    {"persoon": "Jansen", "tijd": "09:00", "lokaal": "A1.04"},
]
```

Prima om te leren, maar denk na wat dat in de praktijk betekent: wil je volgende
week een ander rooster bekijken, dan moet je je **programma zelf aanpassen** —
de lijst herschrijven, opslaan, opnieuw draaien. Je logica (wat het programma
dóet) en je data (welk rooster het bekijkt) zitten aan elkaar vast geplakt. Bij
elke wijziging raak je aan allebei, met alle risico's van dien: een tikfout in
de data kan zomaar je logica breken, en andersom.

## 2. Eén programma, elke week nieuwe data

Zodra je data in een **apart bestand** zet — zoals `toetsen.csv` — verandert
dat. Je Python-bestand blijft precies hetzelfde. Alleen het CSV-bestand
wisselt: volgende week exporteer je een nieuw rooster uit het systeem, sleept
het over het oude bestand heen, en draait exact hetzelfde programma. Geen regel
code aangepast.

Dat is precies wat je op je werk nodig hebt: niet elke week een nieuw scriptje
schrijven, maar één keer een programma bouwen dat blijft werken zolang de
kolommen hetzelfde blijven.

## 3. Waarom dit zo weinig nieuws voelt

`csv.DictReader` levert je exact de structuur die je al kende: een lijst van
dicts. Dat is bewust. Het punt van deze module is niet een nieuwe manier van
denken over data — dat heb je al, uit module 3 en module 7 — maar een nieuwe
**bron** voor diezelfde data. Alles wat je met een lijst van dicts kon (loop
erdoorheen, tel iets, filter op een waarde), kun je hier onveranderd toepassen.

---

## Termen van vandaag

| Term | Betekenis |
|------|-----------|
| CSV | *comma-separated values* — een tabel als platte tekst, komma's tussen de waarden |
| `open(...)` | opent een bestand zodat Python erbij kan |
| `csv.DictReader(...)` | leest een geopend CSV-bestand, geeft per rij een dict terug |

---

## Door naar de volgende module

Je kunt nu data uit een bestand halen. In module 2 (pandas kennismaken) zie je
diezelfde data nog eens, maar dan als overzichtelijke tabel. Dat is handig zodra
een CSV honderden rijen heeft in plaats van acht.

---

➡️ Verder met **`check.md`** van deze module. Onderaan staat waar je daarna heen gaat.
