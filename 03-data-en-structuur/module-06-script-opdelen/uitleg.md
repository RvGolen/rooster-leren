# Waarom opdelen? — het *waaróm* achter module 6

## 1. Het probleem is niet de lengte

Het is verleidelijk om te denken dat een bestand van driehonderd regels
vervelend is omdát het lang is. Dat is niet het echte probleem. Het probleem
is: in zo'n bestand vind je niets meer terug, en elke wijziging kan in
principe alles raken — want je weet niet zeker welk stuk code welk ander stuk
beïnvloedt. Lengte is het symptoom; het ontbreken van een duidelijke indeling
is de ziekte.

Splits je datzelfde bestand in `data.py`, `regels.py` en `opdracht.py`, dan
verandert er aan de hoeveelheid code niets — maar je weet nu vooraf waar je
moet kijken, en, minstens zo belangrijk, waar je *niet* hoeft te kijken.

## 2. Opdelen is geen netheid, het is beheersbaarheid

Het is verleidelijk om bestandsindeling te zien als opruimen — iets voor de
liefhebber. Dat is niet het punt. Het punt is: opdelen is de manier waarop je
code beheersbaar houdt, voor jou én voor de AI. Een AI die gevraagd wordt "voeg
een regel toe aan de dekkingscontrole" kan dat in `regels.py` doen zonder ook
maar naar `data.py` te hoeven kijken. Minder bestanden die veranderen, betekent
minder kans dat er iets stiekem meeverandert dat je niet had gevraagd.

## 3. De lijn naar Project 2 en naar fase 4

Deze indeling is geen toevallige keuze voor deze cursus. Project 2 — je eerste
grotere opdracht — gebruikt exact dezelfde drie bestanden, met dezelfde namen
en dezelfde verantwoordelijkheden: een `data.py` die inleest, bestanden met
regels die controleren, en een aansturend bestand (daar heet het `main.py`) dat
ze combineert. Wat je hier leert lezen, gebruik je daar meteen weer.

En in fase 4 bouw je dit verder uit: in plaats van de AI te vragen "maak het
hele rooster kloppend", vraag je gerichte, kleine dingen — "voeg een regel toe
aan `regels.py`", "lees ook `medewerkers.csv` in `data.py`". Kleine bestanden
maken kleine opdrachten mogelijk, en een kleine opdracht levert een kleine
wijziging op — een wijziging die je nog kunt lezen en beoordelen voordat je
hem aanneemt.

---

## Termen van vandaag

| Term | Betekenis |
|------|-----------|
| `import <eigen bestand>` | gebruik de functies uit een bestand dat jij zelf (of iemand anders) schreef, ernaast in dezelfde map |
| module | de naam voor zo'n bestand, gezien vanuit `import` — `data.py` is "de module `data`" |
| opdelen naar verantwoordelijkheid | elk bestand weet één ding goed, en niets daarbuiten |
| `ModuleNotFoundError` | de foutmelding als Python het geïmporteerde bestand niet kan vinden vanaf de map waarin je draait |

---

## Fase 2 zit erop

Je hebt nu alle bouwstenen van deze fase: CSV inlezen, pandas, filteren en
tellen, AI-code kritisch lezen, een class lezen, en je code opdelen in
bestanden. In fase 3 zet je dit in voor iets groters: een rooster dat
zichzelf (deels) optimaliseert — en de vraag "wat staat er NIET, en zou dat er
moeten staan?" uit module 4 blijft daarbij je belangrijkste gereedschap.
