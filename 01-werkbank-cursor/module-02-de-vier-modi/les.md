# Module 0.2 — De vier modi

⏱️ ± 15–20 minuten · Fase 0 · **Nieuw:** Cursor als tutor (Agent / Plan / Ask / Manueel)

---

## Eerst even nadenken 🤔

Cursor heeft een AI die je kan helpen. Maar "helpen" kan twee heel verschillende
dingen betekenen:

- de AI **legt uit** wat er staat, zodat jíj het snapt en zelf typt, óf
- de AI **schrijft de code voor je**, zodat het bestand meteen af is.

> **Welke van die twee helpt je in het begin het meest om te *leren*?** Commit aan een
> antwoord voor je verder leest. (Het is niet vanzelfsprekend — lees vooral verder.)

---

## De vier modi, kort

In het chat-paneel van Cursor (open het met de chat-knop of via *View*, vaak rechts)
kies je bovenaan een **modus**. Er zijn er vier. Je hoeft ze niet uit je hoofd te
leren — herken waar elk voor is:

| Modus | Wat hij doet | Wanneer |
|-------|--------------|---------|
| **Ask** | Antwoordt op vragen en legt uit. **Verandert je code niet.** | Om te leren: "leg dit uit", "waarom werkt dit niet?" |
| **Agent** | Schrijft en wijzigt zelf code in je bestanden. | Later, als je de AI aanstuurt en controleert (Fase 3–4). |
| **Plan** | Denkt eerst een aanpak uit vóór er iets gebeurt. | Bij grotere klussen, om eerst het plan te zien. |
| **Manueel** | Geen AI; je typt alles zelf. | Als je puur zelf wilt oefenen. |

> ⚠️ **Namen en plek kunnen per Cursor-versie verschillen.** Zoek in het chat-paneel
> naar een keuzemenu met deze woorden. Vind je "Plan" of "Manueel" niet? Geen zorg —
> **Ask** en **Agent** zijn de twee die er nu toe doen.

---

## Waarom jij nu vooral **Ask** gebruikt

In deze leerfases is **Ask je tutor**. De reden: als de AI in Agent-modus de opdracht
voor je oplost, ziet het er af uit — maar jóuw brein heeft niets gedaan. Je leert dan
niets, en straks kun je niet beoordelen of AI-code klopt. Precies de vaardigheid die
deze cursus je wil geven.

Daarom is er in deze map ook een ingebouwde tutor-regel (`../../.cursor/rules/tutor.mdc`):
zelfs áls je het vraagt, geeft de AI in de leeropdrachten geen kant-en-klare oplossing,
maar een hint en één stap tegelijk. Dat is expres. Vraag om een *hint*, niet om "de
oplossing".

---

## En nog even: zet Cursor Tab uit

Los van de modi is er **Cursor Tab**: terwijl je typt, stelt Cursor voor hele regels
af te maken. Handig later, maar nú leest je brein alleen mee in plaats van zelf te
denken. Zet het uit tot Fase 2.

> **Tab uitzetten:** klik rechtsonder in de statusbalk op het Cursor Tab-icoon en zet
> het op *disabled* (of via *Settings → Tab*). Zie je het niet? Zoek op "Tab" in de
> instellingen.

---

## Nu jij — een handeling in Cursor (geen script)

Deze module oefen je *in* Cursor, niet in een `.py`-bestand:

1. Open het chat-paneel en zet de modus op **Ask**.
2. Open `../module-01-de-werkbank/opdracht.py` erbij.
3. Stel in Ask-modus een echte vraag over dat bestand, bijvoorbeeld:
   *"Kun je uitleggen wat de regel `print("Surveillant:", jouw_naam)` precies doet?"*
4. Lees het antwoord. Merk op: je code is **niet veranderd** — Ask legt alleen uit.

> Wil je het contrast voelen? Je hóéft niet, maar je mág één keer naar **Agent**
> schakelen en iets kleins vragen, puur om te zien dat die wél in je bestand schrijft.
> Zet daarna terug op **Ask** en keur een eventuele wijziging af (dat leer je in
> module 3).

Klaar? Ga naar **`check.md`**.
