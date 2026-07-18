# Module 0.3 — Checkpoints & diffs

⏱️ ± 15 minuten · Fase 0 · **Nieuw:** wijzigingen lezen en goed-/afkeuren

---

## Eerst even nadenken 🤔

Stel: je vraagt de AI iets aan te passen, en hij verandert vijf regels in je bestand.

> **Hoe weet je precies wélke vijf regels veranderd zijn — en hoe draai je het terug
> als het niet klopt?** Bedenk een antwoord voor je verder leest. (Blind vertrouwen is
> geen antwoord 🙂.)

---

## Wat is een "diff"?

Een **diff** (van het Engelse *difference*, verschil) is een **vóór-en-ná-vergelijking**.
Als de AI of jijzelf iets wijzigt, toont Cursor de diff: wat eruit ging en wat erin kwam.
Meestal met kleur:

- **groen** = toegevoegd (nieuwe regel),
- **rood** = verwijderd (oude regel),
- ongekleurd = ongewijzigd, staat er alleen bij voor context.

Zo hoef je niet te raden wat er veranderde — je *ziet* het, regel voor regel.

---

## Accepteren of afkeuren

Wanneer de AI (in Agent-modus) een wijziging voorstelt, staat die eerst **klaar als
voorstel** — nog niet definitief. Je krijgt twee knoppen bij de diff:

- **Accept** (goedkeuren): je bent akkoord, de wijziging blijft staan.
- **Reject** / Discard (afkeuren): weg ermee, je bestand blijft zoals het was.

> 💡 De kernhouding van deze cursus: **lees de diff vóór je Accept klikt.** Snap je
> níet wat er verandert? Vraag het dan eerst in **Ask**-modus ("leg deze wijziging
> uit"), en keur pas daarna goed of af. Nooit blind accepteren.

---

## Terug in de tijd: checkpoints

Cursor houdt tijdens een AI-gesprek **checkpoints** bij: momentopnames van je bestanden.
Ging een reeks wijzigingen de verkeerde kant op, dan kun je **terug naar een eerder
checkpoint** (zoek in het chat-paneel naar een *restore*- of terug-knop bij een eerdere
stap). Zie het als een grote "ongedaan maken" voor hele AI-acties.

> ⚠️ **Precieze knoppen verschillen per Cursor-versie.** De begrippen — *diff*,
> *accept/reject*, *checkpoint/restore* — blijven hetzelfde. Vind je een knop niet?
> Vraag in Ask-modus: *"hoe keur ik in Cursor een voorgestelde wijziging af?"*

---

## Nu jij — een handeling in Cursor (geen script)

Oefen het lézen en terugdraaien van een wijziging, veilig:

1. Zet het chat-paneel op **Agent**-modus en open `../module-01-de-werkbank/opdracht.py`.
2. Vraag iets kleins en onschuldigs, bijv.: *"voeg onderaan een print-regel toe die
   'einde' toont."*
3. Er verschijnt een **diff**. **Lees hem**: welke regel is groen (nieuw)? Klopt het
   met wat je vroeg?
4. Klik nu **Reject / Discard** — je wilde het immers alleen zien. Controleer dat je
   bestand weer precies is als daarvoor.

> Zo heb je het hele veilige lusje geoefend: laten wijzigen → diff lezen → bewust goed-
> of afkeuren. Precies wat een supervisor doet.

Klaar? Ga naar **`check.md`**.
