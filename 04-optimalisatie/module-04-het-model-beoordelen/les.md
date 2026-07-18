# Module 4 — Het model beoordelen

⏱️ ± 30–40 minuten · Fase 3 · **Nieuw concept:** de werkwijze *lezen → beoordelen* op een heel gegenereerd model

> Dit is de climaxmodule van deze fase. Geen nieuwe Python vandaag —
> maar de vaardigheid die je hier oefent is de kern van werken met AI-assistenten.

---

## Eerst even terugdenken 🤔

In module 2 bouwde je zelf een greedy die een geldig rooster maakte voor **€1.980**. Dat was je
baseline: duur, maar correct. Daarna vroeg je Cursor een slim optimalisatiemodel te schrijven —
een solver die het allergoedkoopste rooster berekent dat aan de regels voldoet.

Cursor leverde `gegenereerd_model.py`. Het model meldt **€1.632** — meer dan €300 goedkoper dan
je greedy. Geweldig, toch?

> Hou die gedachte even vast.

---

## De werkwijze: voorspel → lees → draai → beoordeel

Bij gegenereerde code is jouw werk niet "klik op run en klaar". Je doorloopt vier stappen:

1. **Voorspel** — lees de code, en bedenk vóórdat je hem draait: wat verwacht je? Welke regels
   kan een AI makkelijk vergeten omdat ze "vanzelfsprekend" zijn?
2. **Lees** — ga elk blok na en zeg (hardop of in je hoofd) wat het doet. Niet "dit ziet er
   goed uit", maar "dit blok doet X, en dat koppelt aan regel Y die ik ken".
3. **Draai** — voer het model echt uit en vergelijk de uitkomst met je voorspelling.
4. **Beoordeel** — bij een heel model komt er één vraag bovenop: *wat staat er NIET, en zou dat
   er moeten staan?*

Het scharniermoment zit in stap 4: niet "klopt wat er staat?", maar **"wat ontbreekt?"**

---

## Lees het model

> ⚠️ **Voorbeeld, geen voorschrift.** We gebruiken hier het surveillance-rooster van het
> voorbeeldschool. Jouw eigen situatie kan andere regels vereisen — de werkwijze blijft hetzelfde.

Open **`gegenereerd_model.py`** in Cursor. Je herkent de structuur: data inlezen, variabelen
definiëren, constraints toevoegen, oplossen. Koppel elk blok aan een regel die je kent:

| Blok in het model | Jouw regel |
|---|---|
| `model.Add(sum(x[p, t] ...) == int(nodig[t]))` | dekking — elke toets genoeg surveillanten |
| `model.Add(sum(x[p, t] ...) <= 1)` per tijdslot | dubbelboeking — niemand tegelijk op twee toetsen |
| `model.Add(x[p, t] == 0)` voor niet-lab-bevoegden | geschiktheid — alleen bevoegden op T3 |
| `model.Minimize(...)` | doelfunctie — zo goedkoop mogelijk |

Zijn dat alle vijf? Tel mee: dekking ✓, capaciteit, beschikbaarheid, dubbelboeking ✓, geschiktheid ✓.

> **Wat zie je voor beschikbaarheid?** Wordt `beschikbaarheid.csv` überhaupt ingelezen?

---

## Draai het

Draai het model vanuit deze map:

```bash
python gegenereerd_model.py
```

Het model meldt **€1.632** en schrijft `gemaakt_rooster.csv`. Goedkoper dan je greedy. Maar...

**De vaste reflex** — in Cursor in Ask-modus:

> *"leg uit wat deze code doet"*

En meteen doorvragen:

> *"welke van mijn vijf regels controleert dit model NIET?"*

Die tweede vraag is waar het om gaat. Een AI beschrijft graag wat de code doet — niet wat er
ontbreekt aan de regels die hij niet ziet.

---

## Nu jij

Open **`opdracht.py`**. Weinig code vandaag, veel denkwerk:
- STAP 3 draait automatisch je validator op het gegenereerde rooster.
- STAP 1, 2 en 4 zijn commentaar dat je invult met jouw eigen redenering.

> Draai eerst `gegenereerd_model.py`, dan `opdracht.py`. De validator laat zien wat het model
> over het hoofd zag.

**Let op de uitvoer:** de validator meldt twee soorten meldingen. Één gaat over een
capaciteitsknelpunt in het voorbeeldrooster (T5, lokaal B2.11 — dat bestond al vóór dit model).
Die is niet veroorzaakt door dit model. De melding die dit model heeft veroorzaakt, gaat over
**beschikbaarheid** — die constraint ontbrak.

Klaar? Ga naar **`uitleg.md`** en daarna **`check.md`**.
