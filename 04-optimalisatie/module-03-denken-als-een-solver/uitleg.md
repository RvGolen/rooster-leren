# Uitleg — Waarom de solver anders denkt

Bij de greedy (module 2) schreef je zelf de stappen op: pak voor elke toets de goedkoopste
beschikbare persoon, sla hem op, ga verder. Jij bepaalde *hoe* de toewijzing tot stand komt.

Een solver draait dat om. Je beschrijft alleen **wat** er moet gelden:
- dit zijn de harde regels (constraints);
- dit is wat ik wil minimaliseren (objective).

De solver doorzoekt zelf alle geldige combinaties en kiest de beste. Hij houdt alle regels
tegelijk in de gaten — precies wat met de hand zo lastig was. Bij de greedy kon je per ongeluk
iemand dubbelboeken, of een te dure keuze maken die een goedkopere combinatie verspilde. De
solver heeft dat probleem niet: hij kijkt naar het hele plaatje.

Jouw rol verschuift daardoor. Je bent niet meer de rekenmachine die stap voor stap beslist — je
bent de persoon die de spelregels goed opschrijft. Als een constraint ontbreekt, vindt de solver
een rooster dat technisch goedkoper is maar een regel breekt. Als de objective niet klopt, optimaliseert hij het verkeerde. Goed beschrijven en daarna controleren: dat is het nieuwe werk.

Dat is ook precies waarom module 4 je vraagt een *gegenereerd* model te lezen en te beoordelen:
niet om te zien of de code loopt, maar of de constraints kloppen met de regels die jij kent.

---

➡️ Verder met **`check.md`** van deze module. Onderaan staat waar je daarna heen gaat.
