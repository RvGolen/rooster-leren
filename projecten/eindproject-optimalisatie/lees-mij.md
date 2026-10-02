# Eindproject — Optimaliseer het rooster

🎯 **Doel:** mét Cursor een optimalisatieprogramma bouwen dat een geldig én zo
goedkoop mogelijk surveillance-rooster maakt — en dat je **regel voor regel kunt
uitleggen**.

⏱️ ± 60–90 minuten · Capstone van fase 3

> Dit is geen nieuwe stof — het is jouw gereedschap toepassen. De vijf regels
> uit fase 2 en 3 ken je. De bouwstenen van een solver-model heb je in module 3
> en 4 gelezen. Nu stuur je Cursor om het in elkaar te zetten, en jij beoordeelt
> elke stap.

---

## Wat je gaat maken

Een script (`optimaliseer.py`) dat:

1. De data inleest met `data.py`.
2. Een zo goedkoop mogelijk rooster berekent dat aan **de vier toewijzings-regels**
   voldoet (dekking, beschikbaarheid, dubbelboeking, geschiktheid).
3. Het resultaat wegschrijft naar `gemaakt_rooster.csv`.
4. Via `controleer()` je eigen validator aanroept — en 0 overtredingen meldt.

Het doel: **0 overtredingen (op de vier toewijzings-regels)** en **totale kosten
€1.755** (goedkoper dan de greedy die €1.980 kostte).

> ⚠️ **Voorbeeld, geen voorschrift.** Dit zijn vijf plausibele regels voor dit
> rooster. Jouw eigen situatie heeft er misschien andere, of meer. De vaardigheid
> die je hier oefent is Cursor aansturen, elke diff lezen, en de AI terugsturen
> als hij afdwaalt.

---

## Hoe je dit aanpakt

Dit is een regie-oefening. Je typt het model **niet zelf** — je laat Cursor het
schrijven en jij beoordeelt.

Werk in deze volgorde:

1. **Zet Cursor in Plan-modus.** Beschrijf de opdracht in gewone taal: "Maak een
   zo goedkoop mogelijk surveillance-rooster dat aan de vier toewijzings-regels
   voldoet: dekking, beschikbaarheid, dubbelboeking en geschiktheid."
2. **Laat Cursor stap voor stap bouwen.** Vraag om één onderdeel tegelijk: eerst
   de variabelen, dan de constraints, dan de doelfunctie. Lees elke diff.
3. **Koppel elke constraint aan een regel.** Vraag bij elke stap: "welke van mijn
   vier toewijzings-regels implementeer je hier?" Als Cursor het niet kan uitleggen, stuur
   hem terug.
4. **Controleer expliciet de beschikbaarheids-constraint.** Dit is het gat uit
   module 4: een model dat de beschikbaarheidsregel weglaat, produceert een
   goedkoper maar ongeldig rooster. Controleer dat de constraint erin zit
   voordat je verder gaat.
5. **Draai het script en laat de validator los.** Roep `controleer()` aan (of
   `python optimaliseer.py`). Doel: 0 overtredingen (op de vier toewijzings-regels)
   en kosten €1.755. Meer overtredingen? Terug naar Cursor. Kosten €1.632? Dan
   mist er nog een constraint — zie `afronding.md`.

## Vastgelopen? Zo gebruik je je AI-tutor goed

Je tutor geeft je hier bewust **geen kant-en-klare oplossing** — dit is een
regie-oefening, en zelf sturen en beoordelen is precies wat je oefent. Je
**mág** Cursor hier code laten schrijven (je bent geen codeur in opleiding), maar
laat alles uitleggen vóór je accepteert, en keur af wat je niet begrijpt. Vraag
in **Ask-modus** om:

- *"leg uit wat deze constraint doet en welke van mijn vier toewijzings-regels hij afdekt"*;
- *"is de beschikbaarheids-constraint aanwezig? Wijs hem aan in de code"*;
- *"mijn validator meldt nog 2 overtredingen — welke constraint ontbreekt
  waarschijnlijk?"*

Vraag **niet** "schrijf het hele model voor mij in één keer". Kleine stappen,
elke diff lezen, elke regel begrijpen — dat is de vaardigheid.

---

## Klaar?

- Draai `controleer()` en controleer: **0 overtredingen** (op de vier toewijzings-regels) **en €1.755**.
- Lees daarna **`afronding.md`** voor de reflectie en de brug naar fase 4.
