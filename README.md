# Rooster-leren

Een cursus Python en Cursor, opgebouwd rond één praktijkvoorbeeld: het
surveillance-rooster bij toetsen.

**Het installeren doen we samen**, in één sessie van ongeveer een uur. Deze
pagina is daarbij ons spiekbriefje: je hoeft hem niet alleen door te werken.
Het is ook de enige keer dat er iets geïnstalleerd moet worden. Daarna ga je
zelf verder.

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

Op een werklaptop mag je vaak niet zomaar alles installeren. Daar komen we in
de sessie samen achter, en dat is prima. Alle installaties hieronder kunnen
normaal gesproken zonder beheerdersrechten, maar dat verschilt per laptop.

> **Ook later geldt: vraagt Windows ergens om een beheerderswachtwoord dat je
> niet hebt, of zegt hij dat je geen rechten hebt? Stop daar dan en stuur me een
> bericht.** Ga er niet omheen zoeken en probeer geen trucjes van internet. Er is
> bijna altijd een andere weg, en die zoeken we samen uit.

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
4. **Zie je alleen een groot chatscherm, zonder bestanden?** Dan staat Cursor in
   de agent-weergave. Klik **rechtsboven** op het knopje om naar de **editor** te
   gaan. Daar zie je links je mappen en bestanden, en daar werk je in deze cursus.

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
3. Vraagt Windows hier om een beheerderswachtwoord dat je niet hebt? Geen
   probleem: er is een versie van Git die dat niet nodig heeft. Die pakken we dan.

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

## Stap 6: kies het model voor je AI-assistent (belangrijk!)

Cursor kan verschillende AI-modellen gebruiken. Standaard staat hij op **Auto**:
dan kiest Cursor zelf, en dat is vaak een lichter model. De tutor in deze cursus
is getest met **Claude Sonnet**. Met een lichter model is hij minder scherp: hij
keurt dan sneller iets goed dat hij niet echt heeft bekeken.

1. Open de chat in Cursor met **Ctrl+L**.
2. Onderaan het chatvenster staat welk model er nu gekozen is, vaak **Auto**.
   Klik erop.
3. Zet **Auto** uit. Dan zie je de lijst met modellen.
4. Kies een model met **Sonnet** in de naam. Staan er meerdere? Neem dan de
   nieuwste.

Kijk bij een nieuwe chat even of er nog Sonnet staat. Staat er weer Auto, zet
hem dan terug.

Zie je geen Sonnet in de lijst, of krijg je een melding over je abonnement?
**Stuur me een bericht** en begin nog niet aan de cursus. De tutor is juist met
Sonnet getest.

---

## Stap 7: samen controleren of alles werkt

Als laatste kijken we samen of alles echt werkt. Dat doen we in de **terminal**:
een tekstvenster waarin je de computer opdrachten geeft. Open hem via het menu
**Terminal → New Terminal**. Hij verschijnt onderin.

Typ deze opdrachten één voor één, en druk na elke opdracht op Enter:

1. Werkt Python? Je ziet dan een versienummer, zoals `Python 3.14.0`.
   ```
   python --version
   ```
2. Werkt Git? Ook hier verschijnt een versienummer.
   ```
   git --version
   ```
3. Installeer de twee pakketten die je later in de cursus nodig hebt. Dit duurt
   even, en er komt veel tekst voorbij. Dat hoort zo.
   ```
   python -m pip install --user pandas ortools
   ```
4. Controleer of ze er staan. Zie je `klaar`, dan is alles in orde.
   ```
   python -c "import pandas, ortools; print('klaar')"
   ```

Zien we bij stap 3 iets over **SSL, een certificaat of een proxy**? Dan lossen we
dat nu samen op. Daarom doen we dit vandaag, en niet pas over drie weken,
halverwege de cursus.

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

Tot hier deden we het samen. Vanaf nu ga je zelf verder, en je hoeft geen
bestanden meer te lezen: je AI-assistent loodst je door de cursus, in de chat.

1. Open de chat met **Ctrl+I** en zet hem met **Shift+Tab** op **Ask**.
2. Typ: **Start de cursus**

Hij laat je dan stap voor stap zien wat er te doen is: eerst hoe de cursus in
elkaar zit, daarna de eerste module. Aan het eind van elke module zegt hij wat
je in een nieuwe chat moet typen om verder te gaan.

Je gids houdt aan het eind van elke module voor je bij wat je af hebt en wat
lastig was, in [`voortgang.md`](voortgang.md). Daar hoef je zelf niets voor te doen.

---

## De nieuwste versie ophalen

Deze cursus wordt onderweg nog bijgewerkt: tikfouten eruit, uitleg scherper, soms
een fix. Stuur ik je een bericht dat er een nieuwe versie is, dan haal je die zo
op:

1. Druk op **Ctrl+Shift+P**.
2. Typ `git pull` en kies **Git: Pull**.

Je eigen werk blijft daarbij gewoon staan.

Krijg je een melding over een *conflict* of over *local changes*? Stop dan en
geef een seintje. Je werk raakt niet kwijt, maar het is niets om zelf op te
lossen. Klik dus ook niet op knoppen als *Discard* of *Stash*.
