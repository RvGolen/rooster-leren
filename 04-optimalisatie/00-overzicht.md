# Fase 3 — Van controle naar optimalisatie 🎯

In fase 2 bouwde je een validator die controleert of een rooster klopt. Die
validator werkt goed: hij vindt precies de vier overtredingen in de
voorbeelddata, elke regel één keer, niet meer en niet minder. Maar je
validator zegt alleen *wát* er mis is — niet wat je eraan moet doen. En er
zijn duizenden manieren om elk probleem op te lossen, waarvan de meeste
onnodig duur zijn.

Voeg bij een onderbezette toets zomaar iemand bij en de dekking klopt
weer — maar als dat een dure externe kracht is, kost die oplossing je twee
keer zoveel als nodig was. Er zijn duizenden geldige roosters, de meeste met
ruimte voor verbetering die niemand opmerkt.

In fase 3 draai je de vraag om: niet *"klopt dit?"* maar **"maak een rooster
dat klopt én zo goedkoop mogelijk is."** Dan blijken de kolommen `type` en
`uurtarief` in `medewerkers.csv` — die je in heel fase 2 nauwelijks nodig
had — ineens het hele punt.

---

## Wat je in fase 3 doet

| Module | Wat je leert | Duur |
|--------|--------------|------|
| `module-01-het-probleem-omdraaien/` | Harde regels vs. zachte wensen + doelfunctie (kosten) | ± 25–30 min |
| `module-02-de-greedy-toewijzer/` | Zelf een simpele toewijzer bouwen — en voelen waar hij schuurt | ± 30–40 min |
| `module-03-denken-als-een-solver/` | Beslissingsvariabele, constraint, objective (OR-Tools) | ± 30 min |
| `module-04-het-model-beoordelen/` | Een gegenereerd model lezen, draaien en beoordelen | ± 35–40 min |

Doe ze op volgorde. Elke module heeft een `les.md` waar je begint, een
`opdracht.py` om te oefenen, een `uitleg.md` voor het waarom, en een
`check.md` om te toetsen of het beklijft.

---

## Wat verandert er in je werkwijze

In fase 2 codeerde je zelf alle logica, stap voor stap. In fase 3 doe je dat
ook — maar met een twist. Je begint in module 2 met het bouwen van een
eenvoudige toewijzer, helemaal zelf. Dat voelt vertrouwd, maar je zult
merken waar zo'n simpele aanpak tekortkomt.

Daarna, in module 3 en 4, laat je de AI een optimalisatiemodel genereren.
Jóuw taak is dan niet meer typen maar **lezen, draaien en beoordelen**. Je
typt dat model dus niet zelf over — je begrijpt wat het doet, koppelt het aan
de regels uit je validator, en beslist of je het kunt vertrouwen.

Dat is ook precies waarom `type` en `uurtarief` nu eindelijk het punt worden:
de solver minimaliseert de kosten, en hij weet alleen wat hij mag als hij
weet wie intern of extern is, en wat iedereen kost.

> ⚠️ **Voorbeeld, geen voorschrift.** De voorbeelddata in
> `../voorbeelddata/` (lokalen, toetsen, medewerkers, beschikbaarheid,
> rooster) zijn ons lopende voorbeeld om elk concept concreet te maken —
> niet een vaste specificatie van hoe surveillance moet werken. Jouw
> situatie kent andere regels, andere kolommen misschien. Dat leer je hier
> juist bijbuigen.

---

## Klaar? Begin hier

Open **`module-01-het-probleem-omdraaien/les.md`** en ga van start. Houd
onderweg **`../voortgang.md`** bij.
