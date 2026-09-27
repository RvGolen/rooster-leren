# Afronding — Project 2

Goed gedaan dat je dit hebt gebouwd. Even terugkijken — en vooruit.

---

## Controleer jezelf

- Je validator hoort in de voorbeelddata **vier** overtredingen te vinden —
  precies één per regel. Komt dat overeen met je handmatige telling uit
  `lees-mij.md` stap 1?
- Vind je er **drie** in plaats van vier? Dan mist er ergens één regel iets.
  Kijk in dat geval eerst naar `controleer_dekking` — dat is de regel die
  module 4 in herinnering roept: loop je over álle toetsen, of alleen over de
  toetsen die al in het rooster staan?
- Meldt elke regel zijn overtreding **precies één keer**, niet dubbel of
  helemaal niet? Draai je programma nog eens en volg met de hand mee wat elke
  functie zou moeten vinden.

> Geen referentie-oplossing hier — expres, net als bij Project 1. Het zelf
> laten kloppen tegen je handmatige telling is precies de vaardigheid die je
> traint: *verifiëren of code doet wat hij moet doen.* Dat is je rol als
> supervisor van AI-code.

---

## Reflectie ✍️ (in `voortgang.md`)

1. Welke van de vier regels was het lastigst te vertalen naar code, en
   waarom? Wat maakte die regel anders dan de rest?
2. Welke regel uit jóuw eigen werk zou je hier als vijfde willen toevoegen?
   Schrijf 'm in gewone taal op — je hoeft hem nog niet te bouwen.
3. Wat zou jouw validator *niet* opmerken, ook al is er in werkelijkheid iets
   mis? (Denk aan iets dat niet in de vier regels zit, maar in jouw rooster
   wel een probleem zou zijn.)

---

## Wat je nu kunt

Je bent van "een CSV kunnen inlezen" naar **een validator die een echt
rooster op vier regels controleert**. Onderweg heb je échte data ingelezen,
die als tabel bevraagd, AI-code gelezen en de fout erin gevonden, een script
opgedeeld in bestanden met een duidelijke taak — en nu een regel in gewone
taal vertaald naar werkende code. Dat is fase 2, samengebald in één project.

---

## Brug naar fase 3

Je kunt nu **controleren** of een rooster klopt. Maar je validator zegt alleen
wát er mis is, niet wat je eraan moet doen — en er zijn duizenden manieren om
die vier fouten op te lossen, waarvan de meeste onnodig duur zijn. Zet er bij een
onderbezette toets zomaar iemand bij en de dekking klopt weer — maar als dat een
dure externe kracht is, kost die oplossing je twee keer zoveel aan uurtarief als
nodig was.

In fase 3 draai je de vraag om: niet "klopt dit rooster?" maar "**maak** een
rooster dat klopt én zo min mogelijk kost". Dan blijken de kolommen `type` en
`uurtarief` in `medewerkers.csv` — die je in heel fase 2 nog nergens
gebruikte — ineens het hele punt.

Neem gerust even pauze. Als je terugkomt, start je in **`../../04-optimalisatie/00-overzicht.md`**.

🎉 Tot zover fase 2 — knap werk.
