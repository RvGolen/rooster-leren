# Fase 2 — Data en structuur 📄

Je hebt in fase 1 zelf een rooster gemodelleerd: een lijst van dicts, met de hand
getypt. Daar doorheen liep je met loops, je nam beslissingen met condities, en in
Project 1 vergeleek je elk paar diensten om conflicten te vinden — met een geneste
loop die je zelf schreef en zelf hebt geverifieerd tegen je eigen handmatige
telling. Dat is geen oefenmateriaal dat je straks weer inlevert. Dat ís je
fundament, en het blijft precies hetzelfde werken.

Wat er in fase 2 verandert, is niet de manier van denken — het is waar de data
vandaan komt. Tot nu toe typte je `rooster = [...]` zelf in je bestand. Vanaf nu
haal je diezelfde soort data uit een echt bestand: een export uit een
roostersysteem, zoals je die in het echt zou krijgen. Dezelfde lijst van dicts,
dezelfde loops — alleen komt de data nu ergens vandaan in plaats van dat jij hem
verzint.

---

## Wat je in fase 2 doet

| Module | Wat je leert | Duur |
|--------|--------------|------|
| `module-01-csv-inlezen/` | Een rooster uit een bestand halen in plaats van het te typen | ± 20–25 min |
| `module-02-pandas-kennismaken/` | Dezelfde data als tabel bekijken (pandas) | ± 25–30 min |
| `module-03-pandas-filteren-tellen/` | Selecteren op voorwaarde, tellen en groeperen | ± 25–30 min |
| `module-04-ai-code-lezen/` | AI-code voorspellen, lezen, controleren en repareren | ± 30 min |
| `module-05-lichte-objecten/` | Een `class` lezen — en er zelf iets aan toevoegen | ± 25–30 min |
| `module-06-script-opdelen/` | Je code over meerdere bestanden verdelen (`import`) | ± 25–30 min |

Doe ze op volgorde. Elke module heeft een `les.md` waar je begint, een
`opdracht.py` om te oefenen, een `uitleg.md` voor het waarom, en een `check.md`
om te toetsen of het beklijft.

---

## Wat verandert er in je werkwijze

Tot nu toe typte je alles zelf, regel voor regel. Vanaf module 4 verandert dat:
soms schrijft de AI een eerste versie van code, en is jóuw taak niet meer
"typen" maar **voorspellen → lezen → aanpassen**. Voordat je code accepteert,
voorspel je eerst wat hij denkt te doen; pas dan lees je hem echt door. Kom je
iets tegen dat je niet meteen snapt? Je vaste reflex blijft dezelfde als in
fase 0: *"leg uit wat deze code doet."*

Daarbij hoort ook een praktische wijziging: **Cursor Tab (autocomplete) mag nu
aan.** In fase 1 stond die uit, zodat je eerst zelf leerde typen zonder dat de
AI je vingers stuurde. Nu je dat fundament hebt, mag Tab je helpen — je blijft
alleen verantwoordelijk voor wat je accepteert.

Elke module sluit af met een **"jouw situatie"-haak**: een korte opdracht
waarin je het net geleerde concept toepast op jóuw eigen rooster, niet op het
voorbeeld hierboven.

> ⚠️ **Voorbeeld, geen voorschrift.** De voorbeelddata in `../voorbeelddata/`
> (lokalen, toetsen, medewerkers, beschikbaarheid, rooster) zijn ons lopende
> voorbeeld om elk concept concreet te maken — niet een vaste specificatie van
> hoe surveillance moet werken. Jouw situatie kent andere regels, andere
> kolommen misschien. Dat leer je hier juist bijbuigen.

---

## Klaar? Begin hier

Open **`module-01-csv-inlezen/les.md`** en ga van start. Houd onderweg
**`../voortgang.md`** bij.
