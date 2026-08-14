# Rooster-leren

Een cursus Python en Cursor, opgebouwd rond één praktijkvoorbeeld: het
surveillance-rooster bij toetsen.

**Lees deze pagina eerst helemaal.** Het is de enige keer dat je iets moet
installeren. Daarna kun je gewoon beginnen.

---

## Waar dit over gaat, en waar het niet over gaat

Het doel is **niet** dat je programmeur wordt. Het doel is dat je een
AI-assistent een roostertool kunt laten bouwen, en dat je zelf kunt zien of wat
hij maakt ergens op slaat. Dat is een heel ander vak dan zelf alles typen, en
het is een stuk beter te doen.

Je hoeft van tevoren dus niets te weten. Dat is geen beleefdheidsfrase, de
cursus is er letterlijk op gebouwd: er zit een AI-tutor in die je stap voor stap
begeleidt en die expres géén kant-en-klare antwoorden geeft.

En dan het belangrijkste: **vastlopen hoort erbij.** Een foutmelding betekent
niet dat jij iets fout doet als persoon. Het is gewoon hoe dit werk eruitziet,
elke dag, ook voor mensen die het al twintig jaar doen. Het verschil tussen een
beginner en iemand met ervaring is niet dat de een geen fouten krijgt. Het is
dat de ander gewend is geraakt aan het rustig uitzoeken ervan. Dat gaat jou ook
lukken.

---

## Vooraf: je laptop is van de universiteit

Op een werklaptop mag je vaak niet zomaar alles installeren. Daar gaan we
gewoon achter komen, en dat is prima. Eén afspraak vooraf:

> **Vraagt Windows ergens om een beheerderswachtwoord dat je niet hebt, of zegt
> hij dat je geen rechten hebt? Stop daar dan en stuur me een bericht.**
> Ga er niet omheen zoeken en probeer geen trucjes van internet. Er is bijna
> altijd een andere weg, en die zoeken we samen uit. Dit is een van de twee
> dingen waarvoor je mij meteen mag storen.

Alle drie de installaties hieronder kunnen normaal gesproken zonder
beheerdersrechten. Maar dat verschilt per laptop, dus we testen het gewoon.

---

## Wat je gaat installeren, en wat het is

Drie dingen. Dit is wat ze doen, zodat je niet blind op knopjes klikt:

| Wat | Wat het is |
|-----|------------|
| **Cursor** | Het programma waar je in werkt. Het is een tekstverwerker voor code, met een AI-assistent ingebouwd waar je gewoon in het Nederlands vragen aan stelt. |
| **Python** | De taal waarin je schrijft. Dit is ook het programma dat jouw regels daadwerkelijk uitvoert. Zonder Python gebeurt er niets als je iets probeert te draaien. |
| **Git** | Het gereedschap dat deze cursus naar jouw computer haalt, en waarmee je later updates ophaalt als ik iets verbeter of een fout eruit haal. |

---

## Stap 1: Cursor installeren

1. Ga naar **cursor.com** en download Cursor voor Windows.
2. Installeer het en start het op.
3. Maak een account aan of log in. Dat is nodig, want de AI-assistent werkt
   alleen als je ingelogd bent.

Cursor installeert zichzelf normaal in je eigen gebruikersmap en heeft daarvoor
geen beheerdersrechten nodig.

---

## Stap 2: Python installeren

1. Ga naar **python.org**, klik bovenin op *Downloads*, en download de nieuwste
   versie voor Windows.
2. Start de installer. Je krijgt nu één scherm dat er ongeveer zo uitziet: een
   grote knop *Install Now*, daaronder *Customize installation*, en helemaal
   onderin een paar vinkjes.
3. **Zet onderin het vinkje bij "Add python.exe to PATH".**

   > ⚠️ Dit is het belangrijkste vinkje van deze hele pagina. Vergeet je het, dan
   > kan Windows Python later niet vinden en lijkt alles kapot terwijl er niets
   > mis is. Vergeten? Niet erg: installeer gewoon opnieuw met het vinkje aan.

4. Klik daarna op **Install Now**. Dat is de gewone installatie in je eigen
   gebruikersmap, waar je geen beheerdersrechten voor nodig hebt.

   > Klik dus **niet** op *Customize installation*, en zet geen vinkje bij iets
   > met *for all users* of *admin privileges*. Dat zijn juist de opties die om
   > een beheerderswachtwoord gaan vragen.

5. Wacht tot hij klaar is en sluit de installer.

> **Onthoud dit voor later:** op Windows heet het commando gewoon `python`. In
> sommige lesbestanden staat "of probeer `python3`". Dat is voor mensen op een
> Mac. Bij jou werkt `python`.

---

## Stap 3: Git installeren

1. Ga naar **git-scm.com** en download Git voor Windows.
2. Start de installer en klik overal gewoon op **Next**. De standaardinstellingen
   zijn prima; je hoeft niets te veranderen.
3. Vraagt Windows hier om een beheerderswachtwoord dat je niet hebt? **Stop en
   stuur me een bericht.** Er is een versie van Git die dat niet nodig heeft, die
   zet ik dan voor je klaar. Dit is niet iets om zelf mee te gaan puzzelen.

Start Cursor daarna **opnieuw op**, zodat het Python en Git kan zien.

---

## Stap 4: de cursus binnenhalen

1. Open Cursor.
2. Druk op **Ctrl+Shift+P**. Bovenin verschijnt een balkje waarin je opdrachten
   kunt zoeken.
3. Typ `git clone` en kies **Git: Clone**.
4. Plak dit adres en druk op Enter:

   ```
   https://github.com/RvGolen/rooster-leren.git
   ```

5. Cursor vraagt nu waar hij de map mag neerzetten. Kies een plek die je makkelijk
   terugvindt, bijvoorbeeld je map *Documenten*.
6. Als hij klaar is, vraagt Cursor of je de map wilt openen. **Zeg ja.**

---

## Stap 5: controleer dat je de hele map open hebt (belangrijk!)

Dit is de enige stap waar je iets mis kunt doen zonder dat je het merkt, dus doe
hem even.

In de Explorer aan de linkerkant hoort **`rooster-leren`** bovenaan te staan, met
daaronder mappen als `01-werkbank-cursor`, `02-python-fundamenten` en
`voorbeelddata`.

Staat er iets anders bovenaan, bijvoorbeeld alleen `01-werkbank-cursor`? Dan heb
je per ongeluk een onderliggende map geopend. Ga naar *File → Open Folder…* en
kies de map **`rooster-leren`** zelf.

**Waarom dit uitmaakt:** de ingebouwde tutor zit in een verborgen mapje
`.cursor`, en Cursor vindt dat alleen als je de hele cursusmap open hebt. Doe je
het verkeerd, dan krijg je geen foutmelding. Je AI-assistent gedraagt zich dan
alleen niet als tutor, maar geeft gewoon de antwoorden weg. En daar leer je niets van.

---

## Stap 6: laat Cursor je installatie nakijken

Nu de leuke stap: je laat de AI-assistent zelf controleren of alles goed staat.

1. Open de chat in Cursor met **Ctrl+L**.
2. Kopieer onderstaande tekst er helemaal in en druk op Enter.

```
Ik ben een complete beginner en ga in deze map een Python-cursus doen.
Ik werk op Windows, op een laptop van mijn werk waarop ik waarschijnlijk geen
beheerdersrechten heb. Controleer of mijn computer klaar is, en leg het uit in
gewone taal zonder jargon. Doe het volgende:

1. Kijk of Python werkt en welke versie het is.
2. Kijk of git werkt.
3. Kijk of ik als gewone gebruiker Python-pakketten mag installeren. Gebruik
   daarvoor een dry-run met de --user optie, zodat er nu nog niets echt wordt
   geïnstalleerd. Later in de cursus heb ik pandas en ortools nodig.
4. Let bij punt 3 ook op foutmeldingen over SSL, certificaten of een proxy. Die
   komen op werklaptops vaker voor en zijn belangrijk om nu te weten.
5. Kijk of het bestand .cursor/rules/tutor.mdc bestaat vanuit deze map.

Geef me daarna een kort lijstje: wat werkt, wat werkt niet, en wat ik eraan moet
doen. Als iets om een beheerderswachtwoord vraagt of door de beheerder wordt
geblokkeerd, zeg dat dan gewoon eerlijk en probeer het niet te omzeilen.
```

3. Lees zijn antwoord. Staat alles op groen? Dan ben je klaar om te beginnen.

Zegt hij dat punt 3 of 4 niet lukt? **Stuur me het antwoord door.** Dat is precies
waarom we dit nú testen en niet pas over drie weken, halverwege de cursus. Dan
lossen we het rustig op voordat je er last van krijgt.

---

## Als iets niet lukt

Stuur me gewoon een bericht. Serieus, daar hoef je niet lang mee te wachten en
het is nooit een domme vraag.

Doe dat in elk geval meteen bij deze dingen, want daar valt niets aan te prutsen:

- er wordt om een **beheerderswachtwoord** gevraagd, of je krijgt te zien dat je
  ergens **geen rechten** voor hebt;
- een foutmelding over **SSL, een certificaat of een proxy** bij het installeren
  van een pakket;
- een foutmelding waarin het woord **`UnicodeEncodeError`** of **`charmap`**
  voorkomt. Dat gaat over hoe jouw scherm rare tekens weergeeft en is een
  bekende Windows-eigenaardigheid, geen fout van jou;
- iets in de cursus zelf klopt niet: een link die nergens heen gaat, een script
  dat crasht, of een stap die niet kan kloppen. Dat is dan gewoon een fout van
  mij.

Voor **uitleg over de stof** heb je mij niet nodig: vraag het je AI-tutor in
Cursor, in **Ask-modus**. Vraag om een *hint*, niet om de oplossing. Daar is hij
op ingesteld.

---

## Klaar? Dan begin je hier

Open **[`00-start-hier.md`](00-start-hier.md)** in de Explorer aan de linkerkant.
Daar staat hoe de cursus is opgebouwd en wat de spelregels zijn.

Houd onderweg [`voortgang.md`](voortgang.md) bij. Dat is van jou, maar het helpt
enorm om te zien waar het schuurt.

---

## De nieuwste versie ophalen

Deze cursus wordt onderweg nog bijgewerkt: tikfouten eruit, uitleg scherper, soms
een fix. Om de laatste versie op te halen, typ je dit in de chat van Cursor:

> haal de nieuwste versie van de cursus op met git pull

Krijg je een melding over een *conflict*? Stop dan en geef een seintje. Dat
betekent dat er iets is aangepast in een bestand waar jij ook in hebt gewerkt.
Je werk raakt niet kwijt, maar het is niets om zelf op te lossen.
