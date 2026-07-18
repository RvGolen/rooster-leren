# Project 2 — De validator

🎯 **Doel:** alles uit fase 2 samenbrengen in één werkend programma dat een
surveillance-rooster controleert op **vier regels tegelijk**.

⏱️ ± 60–90 minuten · Capstone van fase 2

> Dit is geen nieuwe stof — het is je eigen fundament toepassen. CSV inlezen,
> pandas bevragen, AI-code lezen, een script opdelen: je hebt elk stuk al
> gezien. Nu zet je ze in elkaar tot iets dat je echt kunt gebruiken.

---

## Wat je gaat maken

Een validator die, op basis van de bestanden in `voorbeelddata/`, vier dingen
controleert:

1. **Dekking** — heeft elke toets genoeg surveillanten?
2. **Capaciteit** — passen de studenten in het toegewezen lokaal?
3. **Beschikbaarheid** — is iedereen die is ingezet, ook echt beschikbaar op
   dat tijdslot?
4. **Dubbelboeking** — staat niemand op twee toetsen tegelijk?

Het resultaat: een script dat per regel meldt wat er mis is — of, als alles
klopt, dat met zoveel woorden zegt.

> ⚠️ **Voorbeeld, geen voorschrift.** Dit zijn vier plausibele regels voor een
> surveillance-rooster. Jouw eigen situatie heeft er misschien zes, of andere.
> De vaardigheid die je hier oefent is niet "deze vier regels kennen" — het is
> **een regel in gewone taal kunnen vertalen naar code**. Dat kun je straks op
> elke regel toepassen die jóuw rooster nodig heeft.

---

## Hoe je dit aanpakt

Dit is een project, geen module — dus meer zelfstandigheid en minder steun dan
je gewend bent. Werk in deze volgorde, en draai na elke stap
(`python main.py`):

1. **Tel eerst met de hand.** Open de bestanden in `voorbeelddata/` en zoek
   zelf naar overtredingen — één voor elke regel hierboven. Schrijf op wat je
   vindt (toets-ID's, namen, tijden). Dat is je meetlat: straks weet je of je
   programma klopt, omdat je het al met de hand hebt nagekeken.
2. **Bouw één regel tegelijk.** Vul in `regels.py` telkens één functie in, en
   draai daarna meteen `main.py`. Niet alle vier in één keer proberen — dan
   weet je bij een fout niet welke regel hem veroorzaakt.
3. **Begin met `controleer_dubbelboeking`.** Die logica heb je al eens
   geschreven, in Project 1: `heeft_conflict` vergeleek twee diensten op
   dezelfde persoon en dezelfde tijd. Hier doe je hetzelfde, nu op data uit een
   bestand in plaats van een lijst die je zelf intikte.
4. **Doe `controleer_dekking` als laatste.** Denk aan module 4 (AI-code
   lezen): een toets die niet in het rooster voorkomt, mist niet automatisch
   in je resultaat — je moet over de toetsen loopen, niet over het rooster.
5. **Maak het overzichtelijk.** Groepeer de uitvoer per regel, zodat je in één
   oogopslag ziet welke regel wordt overtreden. Geen enkele melding? Zeg dat
   dan ook met zoveel woorden.

## Vastgelopen? Zo gebruik je je AI-tutor goed

Je tutor geeft je hier bewust **geen kant-en-klare oplossing** — dit is het
sluitstuk van fase 2, en de vertaalslag van regel naar code is precies wat je
moet oefenen. Vraag in **Ask-modus** om:

- *"leg uit wat een `#TODO` hier van me vraagt"*;
- *"klopt mijn aanpak qua structuur, voordat ik ga typen?"*;
- *"waarom geeft deze regel geen melding terwijl ik er wel eentje verwacht?"*
  (hij helpt je redeneren over je eigen code).

Vraag **niet** "schrijf `controleer_capaciteit` voor mij". Je leert het
vertalen van regel naar code juist door het zelf te doen, met een duwtje waar
nodig.

---

## Klaar?

- Controleer je vier gevonden overtredingen met de hand tegen je telling uit
  stap 1.
- Lees daarna **`afronding.md`** voor de reflectie en de brug naar fase 3.
