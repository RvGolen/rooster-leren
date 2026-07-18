# Waarom deze fout zo gevaarlijk is — het *waaróm* achter module 4

## 1. Deze fout is niet dom

Het is verleidelijk om te denken dat de AI slordig was. Dat is niet wat er
gebeurde. De opdracht was: *"tel de surveillanten per toets"*. De AI groepeerde
`rooster.csv` op `toets_id` en telde per groep — precies wat er gevraagd werd, en
op zichzelf volkomen correcte pandas-code. `groupby` kan alleen tellen wat er ís.
Een toets die nul keer in het rooster voorkomt, vormt geen groep — en iets dat
geen groep vormt, kun je niet tellen.

De AI wist niet dat een **ontbrekende toets het ergste geval is**, erger dan een
toets met te wéinig surveillanten. Dat is geen programmeerkennis, dat is
**domeinkennis** — kennis over hoe surveillance-roosters werken, over wat er op
het spel staat als niemand in de zaal staat. Die kennis had de AI niet, en kón hij
ook niet hebben: hij zag alleen de tabellen, niet de tentaminering.

Van jou dus. Niet omdat je beter kunt programmeren dan de AI, maar omdat jij weet
wat een lege zaal betekent en de AI niet.

## 2. Het patroon achter bijna elke stille fout

Dit is niet een eenmalige valkuil van `groupby`. Het is het patroon achter bijna
elke stille fout in gegenereerde code: niet een **verkeerde berekening**, maar een
**ontbrekend geval**. De code die er wél staat, klopt meestal gewoon. Het gevaar
zit in wat er nooit werd overwogen: de lege lijst, de rij die niet bestaat, de
uitzondering die niemand noemde omdat hij zo zeldzaam is.

Dat maakt de vraag die je jezelf stelt anders dan je zou denken. Niet:

> "Klopt wat hier staat?"

maar:

> "Wat staat er NIET, en zou dat er moeten staan?"

Die tweede vraag dwingt je om na te denken over wat de code *niet* laat zien, in
plaats van alleen te controleren of wat je wél ziet correct is. Een script dat
"Controle afgerond" print, voelt afgerond — en is toch onvolledig. Dat gevoel van
afgerond-zijn is precies waarom deze categorie fouten zo lang onopgemerkt blijft.

## 3. Waarom "geen melding" gevaarlijker is dan een foutmelding

Een `TypeError` of een verkeerd getal valt op: het script crasht, of de uitkomst
oogt onzinnig. Je gaat op onderzoek uit omdat iets je duidelijk waarschuwt. Maar
`gegenereerd.py` crasht niet, en meldt niets vreemds — hij meldt gewoon niets over
T8, en sluit af met een geruststellende zin. Er is geen enkel signaal dat je
aandacht trekt. De enige manier om dit te vinden, is weten wát je verwacht (acht
toetsen) en dat actief vergelijken met wat je kreeg (zeven regels). Vandaar de
werkwijze uit `les.md`: zonder een voorspelling vooraf, heb je niets om de uitkomst
tegen af te zetten.

---

## Termen van vandaag

| Term | Betekenis |
|------|-----------|
| voorspel → lees → draai → pas aan | de werkwijze om AI-code te beoordelen, in vier stappen |
| ontbrekend geval | een situatie die in de data kán voorkomen, maar waar de code niet aan dacht |
| domeinkennis | kennis over jouw praktijk (surveillance, tentaminering) die de AI niet heeft |

---

## Door naar de volgende module

Je hebt nu de kernvaardigheid van deze cursus: niet alleen lezen wat code doet,
maar zoeken naar wat hij overslaat. In fase 3 pas je precies deze vraag toe op een
heel optimalisatiemodel — daar is de inzet nog groter, en de fouten nog stiller.
