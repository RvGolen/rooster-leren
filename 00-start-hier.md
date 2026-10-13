# Start hier 👋

Welkom. Je gaat de komende tijd **Python** leren — niet om programmeur te worden,
maar om iets veel praktischers te kunnen: een AI-assistent (Cursor) een
**rooster-optimalisatietool** laten bouwen en zelf kunnen **zien of het klopt**.

Je hoeft straks niet alles zelf te typen. Maar om de AI te kunnen aansturen en
controleren, moet je eerst *snappen wat code doet*. Daarom begin je met zelf kleine
dingen schrijven. Dat fundament betaalt zich later dubbel terug.

> **Het lopende voorbeeld in deze cursus is het surveillance-/toezichtrooster bij
> toetsen.** Dat is bewust gekozen omdat het jouw eigen werk raakt. Maar let op: de
> regels die je in de voorbeelden ziet (hoeveel surveillanten, wie mag wat) zijn
> *illustratief*. Jouw échte situatie heeft eigen regels. Een kernvaardigheid die je
> hier leert, is juist: **jouw eigen regels herkennen, opschrijven en de AI erop
> aansturen.**

---

## Wat je nodig hebt

Niets meer: de installatie hebben we samen gedaan. Cursor, Python en Git staan
klaar, en de voorbeelddata zit erbij.

---

## Hoe deze cursus is opgebouwd

De cursus loopt in fases. Je werkt ze op volgorde af.

| Map | Fase | Wat je doet |
|-----|------|-------------|
| `01-werkbank-cursor/` | 0 | Wegwijs in Cursor; een eerste script draaien |
| `02-python-fundamenten/` | 1 | Zelf de bouwstenen van Python schrijven |
| `03-data-en-structuur/` | 2 | Echte data inlezen; AI-code leren *lezen* |
| `04-optimalisatie/` | 3 | Van controleren naar optimaliseren (OR-Tools) |
| `projecten/` | — | Drie groeiende projecten, eindigend op je eigen tool |

> **Fase 4 (de AI betrouwbaar aansturen en controleren) volgt later.** De cursus
> die je nu hebt, loopt van fase 0 tot en met het eindproject. Dat is ruim genoeg
> werk; je hoort het wanneer fase 4 klaarstaat.

**Elke module** heeft dezelfde vier bestanden. In de modules waar je zelf code typt
staat er nog een vijfde bij:

- `les.md` — een korte uitleg met één voorbeeld. Begint met een **voorspelvraag**.
- `opdracht.py` — code met `#TODO`'s die jij zelf invult. *Hier typ je zelf.*
- `uitleg.md` — het *waaróm* achter het concept.
- `check.md` — een paar zelfcheck-vragen + "leg het in je eigen woorden uit".
- `controleer.py`: draai `python controleer.py` als je klaar denkt te zijn. Het
  draait jouw `opdracht.py` en zegt per stap of de uitvoer klopt, zonder je het
  antwoord te geven. Of je het ook *snapt*, bepaal je zelf in `check.md`.

Houd modules klein: 15–30 minuten per stuk. Liever vaker even, dan lange sessies.

---

## Drie spelregels die het verschil maken

### 1. Zet **Cursor Tab (autocomplete) uit** — voorlopig

Cursor kan tijdens het typen hele regels voor je afmaken. Handig later, maar nú
leert je brein er niets van. Je leest alleen mee in plaats van zelf te denken.

> **Tab staat al uit**: dat hebben we samen gedaan. Zie je tijdens het typen toch
> grijze tekst verschijnen die je met Tab kunt overnemen? Klik dan rechtsonder in
> de statusbalk op **Tab** en kies *Disable globally*. Je zet het pas weer aan in
> fase 2.

### 2. **Ask-modus is je tutor — niet Agent-modus**

Cursor heeft meerdere standen. In de leerfases gebruik je vooral:

- **Ask** (lezen, niet schrijven): je stelt vragen als *"leg deze regel uit"* of
  *"waarom werkt dit niet?"*. Ask verandert je code niet — perfect om te leren.
- **Agent**: schrijft en wijzigt code zelf. Krachtig, maar in fase 1 doet hij dan
  jouw werk. Die gebruik je bewust pas later.

> De volledige rondleiding langs de vier modi (Agent / Plan / Ask / Manueel) staat
> in `01-werkbank-cursor/`. Voor nu: **stel je vragen in Ask-modus.**

### 3. **Typ zelf, commit aan een antwoord, reflecteer**

Elke module vraagt je éérst te raden wat code doet, en achteraf het in je eigen
woorden uit te leggen. Sla die stappen niet over — daar zit het leren.

---

## De ingebouwde tutor

In deze map zit een set **Cursor-regels** (`.cursor/rules/`) die jouw AI-assistent
laten optreden als een geduldige tutor: hij geeft je in de leeropdrachten *geen*
kant-en-klaar antwoord, maar helpt je met hints en één stap tegelijk. Dat is
expres. Als je vastloopt, vraag dan om een *hint*, niet om "de oplossing".

---

## Klaar? Begin hier

De installatie en de instellingen hebben we samen gedaan, dus je kunt meteen
beginnen.

1. Je begint met **Fase 0**: wegwijs worden in Cursor en je eerste script
   draaien. Zeg in de chat **verder**, dan krijg je het overzicht van Fase 0
   (`01-werkbank-cursor/00-overzicht.md`).
2. Aan het eind van elke module schrijft je gids voor je in **`voortgang.md`**
   wat je af hebt en wat lastig was.

Veel plezier. Klein beginnen is precies goed.
