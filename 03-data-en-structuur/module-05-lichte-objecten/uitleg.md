# Waarom een class? — het *waaróm* achter module 5

## 1. Een class is geen "betere dict"

Het is verleidelijk om een class te zien als een dict met een chiquer jasje.
Dat is niet het punt. Het punt is: een class is een plek waar je de data **en**
de regels erover bij elkaar zet.

Met een dict schrijf je "past deze toets in dit lokaal?" op als losse regel
code — `toets["aantal_studenten"] <= lokaal["capaciteit"]`. Staat die vraag op
vijf plekken in je programma, dan staat de definitie van *passen* ook vijf
keer. Verandert de regel later — bijvoorbeeld omdat je toch 5% marge wilt
toestaan — dan moet je alle vijf plekken vinden en aanpassen. Vergeet je er
één, dan werken twee delen van je programma met een verschillende definitie
van *passen*, zonder dat Python je waarschuwt.

## 2. Eén definitie, één plek

In een class staat `past_in` één keer, in de class zelf. Elke plek in je
programma die `toets.past_in(lokaal)` aanroept, gebruikt dezelfde definitie.
Wil je de regel aanpassen? Dan pas je hem op één plek aan, en overal waar hij
gebruikt wordt, klopt hij weer.

## 3. Wees eerlijk: voor kleine scripts is een dict prima

Voor een scriptje van twintig regels dat je één keer draait, is een class
overkill — een dict werkt prima. Het echte argument voor classes gaat niet over
jouw eigen kleine scripts. Het gaat over **leesbaarheid van andermans (AI-)
code**: zodra je code van een ander leest — of code die AI voor je genereerde
— kom je classes overal tegen. Als je weet dat een class "data plus de vragen
erover" is, hoef je niet te schrikken van het woord.

---

## Termen van vandaag

| Term | Betekenis |
|------|-----------|
| `class` | een plek die data én de vragen (methodes) erover bij elkaar houdt |
| methode | een functie die bij een class hoort |
| `__init__` | wat er gebeurt als je een nieuw ding van die class maakt: de velden invullen |
| `self` | "dit ding zelf, degene waar je het nu over hebt" |

---

## Door naar de volgende module

Je kunt nu een class lezen, en er een veld en een methode aan toevoegen. In
module 6 (script opdelen) leer je je code over meerdere bestanden verdelen. Daar
kom je classes en functies in een apart bestand tegen, klaar om
ge-`import`-eerd te worden.

---

➡️ Verder met **`check.md`** van deze module. Onderaan staat waar je daarna heen gaat.
