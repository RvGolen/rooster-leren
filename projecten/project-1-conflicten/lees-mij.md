# Project 1 — Vind alle conflicten in een rooster

🎯 **Doel:** alles uit fase 1 samenbrengen in één klein, werkend programmaatje dat
een rooster inleest en **alle dubbelboekingen** vindt.

⏱️ ± 30–45 minuten · Capstone van fase 1

> Dit is geen nieuwe stof — het is je eigen fundament toepassen. Je hebt elke
> bouwsteen al gezien. Nu zet je ze in elkaar.

---

## Wat je gaat maken

Een script dat:
1. een rooster heeft (een lijst van diensten — al voor je klaargezet in
   `opdracht.py`);
2. **alle conflicten** vindt (zelfde persoon, zelfde tijd, twee plekken);
3. ze netjes op het scherm meldt — of zegt dat het rooster conflictvrij is.

> ⚠️ **Voorbeeld, geen voorschrift.** We gebruiken één conflict-regel (dubbelboeking).
> In jouw echte werk zijn er meer regels (beschikbaarheid, capaciteit, dekking). Die
> komen in fase 2, in Project 2 — de validator. Project 1 houdt het bij deze ene
> regel, zodat je je op de *structuur* kunt richten.

---

## Hoe je dit aanpakt

Dit is een project, geen module — dus iets meer zelfstandigheid. Werk in deze
volgorde, en draai na elke stap (`python opdracht.py`):

1. **Begrijp de data.** Lees het `rooster` bovenaan `opdracht.py`. Hoeveel conflicten
   zie je met het blote oog? Schrijf je verwachting op — dan weet je straks of je
   programma klopt.
2. **Hergebruik `heeft_conflict`.** Die staat er al in. Snap je elke regel nog?
3. **Bouw `vind_conflicten`.** Vul de `#TODO`'s in: een geneste loop (module 7) die
   `heeft_conflict` op elk paar toepast.
4. **Maak het netjes.** Geen conflicten? Zeg dat dan ook met zoveel woorden.

## Vastgelopen? Zo gebruik je je AI-tutor goed

Dit is een leeropdracht — je tutor geeft je **geen kant-en-klare oplossing**, en dat
is expres. Vraag in **Ask-modus** om:
- *"leg uit waarom mijn geneste loop niets vindt"* (hij helpt je redeneren);
- *"wat betekent deze foutmelding?"*;
- *"klopt mijn aanpak qua structuur?"* — laat je plan toetsen, niet je werk doen.

Vraag **niet** "schrijf vind_conflicten voor mij". Je leert het juist door de knoop
zelf te ontwarren, met een duwtje.

---

## Klaar?

- Controleer je gevonden conflicten met de hand tegen je verwachting uit stap 1.
- Probeer de **optionele uitbreiding** onderaan `opdracht.py` als je zin hebt.
- Lees daarna **`afronding.md`** voor de reflectie en de brug naar fase 2.
