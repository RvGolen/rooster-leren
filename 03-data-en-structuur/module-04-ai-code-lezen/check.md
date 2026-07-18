# Zelfcheck — module 4

---

## 1. Waarom zag `groupby` T8 niet?

`aantal_per_toets = rooster.groupby("toets_id").size()` groepeert `rooster.csv`.
Leg uit waarom een toets die nul keer in `rooster.csv` voorkomt, ook nooit in
`aantal_per_toets` voorkomt — en dus nooit in de uitvoer van `gegenereerd.py`.

---

## 2. Waarom is "geen melding" hier gevaarlijker dan een foutmelding?

Het script crasht niet bij T8, en print geen rare waarde — het print gewoon
niets over T8, en sluit af met "Controle afgerond." Waarom is dat lastiger op
te merken dan een `TypeError` of een duidelijk verkeerd getal?

---

## 3. Wat had de AI moeten weten om dit goed te doen?

De code die de AI schreef, is op zichzelf correcte pandas. Wat ontbrak er dan —
en was dat iets wat de AI uit de vraag alleen had kunnen afleiden, of had hij
domeinkennis nodig die alleen jij had?

---

## 4. Leg in je eigen woorden uit ✍️

> Beschrijf in vier stappen hoe je voortaan code beoordeelt die een AI voor je
> schreef. Noem alle vier de stappen uit deze module bij naam, en leg bij één
> ervan uit wat "het verschil tussen voorspelling en werkelijkheid" je precies
> vertelt. Schrijf het in `../../voortgang.md`.

---

## Jouw situatie 🔎

Welk geval in jóuw rooster zou een AI over het hoofd zien, om precies dezelfde
reden als T8 — omdat het "niet in de data staat"? Denk aan een tentamen zonder
toegewezen zaal, een dag zonder rooster, een medewerker zonder ingevulde
beschikbaarheid.

Schrijf er één op in `../../voortgang.md`: welk geval, en waarom een AI dat zou
missen. Dat is een regel die je straks zelf moet bewaken — bij dit soort
ontbrekende gevallen controleert niemand anders het voor je.

---

## Klaar met module 4 ✅

➡️ Door naar de volgende module van fase 2.
