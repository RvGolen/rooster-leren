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

## Wat je gaat installeren, en wat het is

Drie dingen. Dit is wat ze doen, zodat je niet blind op knopjes klikt:

| Wat | Wat het is |
|-----|------------|
| **Cursor** | Het programma waar je in werkt. Het is een tekstverwerker voor code, met een AI-assistent ingebouwd waar je gewoon in het Nederlands vragen aan stelt. |
| **Python** | De taal waarin je schrijft. Dit is ook het programma dat jouw regels daadwerkelijk uitvoert. Zonder Python gebeurt er niets als je iets probeert te draaien. |
| **Git** | Het gereedschap dat deze cursus naar jouw computer haalt, en waarmee je later updates ophaalt als ik iets verbeter of een fout eruit haal. |

---

## Stap 1: Cursor installeren

1. Ga naar **cursor.com** en download Cursor voor jouw computer.
2. Installeer het en start het op.
3. Maak een account aan of log in. Dat is nodig, want de AI-assistent werkt
   alleen als je ingelogd bent.

> **Werk je op een laptop van de universiteit?** Kan het zijn dat je iets niet
> mag installeren, of dat er om een beheerderswachtwoord wordt gevraagd. Ga daar
> niet omheen zoeken. Stuur me even een bericht, dan kijken we er samen naar.

---

## Stap 2: Python en Git installeren

Kies hieronder **alleen het stukje dat bij jouw computer hoort**. De rest kun je
overslaan.

### Als je een Mac hebt

Op een Mac krijg je Python en Git in één keer binnen.

1. Open Cursor.
2. Open onderin een terminal: menu **Terminal → New Terminal**. Er verschijnt
   een venster met een knipperende cursor. Dat is een plek waar je de computer
   rechtstreeks opdrachten typt.
3. Typ dit en druk op Enter:

   ```
   git --version
   ```

4. Waarschijnlijk verschijnt er nu een venster van je Mac dat vraagt of je de
   *Command Line Developer Tools* wilt installeren. **Klik op Installeren** en
   wacht tot het klaar is. Dit kan een paar minuten duren. Hiermee heb je in één
   klap zowel Git als Python te pakken.
5. Als het klaar is, typ je dit om te controleren:

   ```
   python3 --version
   ```

   Je hoort nu iets als `Python 3.12.4` te zien. Het exacte nummer maakt niet uit.

> **Let op voor later:** op een Mac heet het commando `python3`, niet `python`.
> Typ je `python`, dan krijg je "command not found". Dat is geen kapotte
> computer, dat is gewoon de naam.

### Als je Windows hebt

Op Windows installeer je de twee los.

1. **Python.** Ga naar **python.org**, klik op *Downloads*, en download de
   installer voor Windows.
   > ⚠️ **Het belangrijkste vinkje van deze hele pagina:** zet tijdens het
   > installeren een vinkje bij **"Add python.exe to PATH"**, onderin het eerste
   > scherm. Vergeet je dat, dan kan je computer Python later niet vinden en
   > lijkt alles kapot. Vergeten? Gewoon opnieuw installeren met het vinkje aan.

   > Gebruik de installer van python.org en **niet** de Microsoft Store. Typ je
   > straks `python` en opent de Store, dan is Python nog niet goed geïnstalleerd.
2. **Git.** Ga naar **git-scm.com**, download Git voor Windows, en installeer
   het. Je mag overal gewoon op *Next* klikken, de standaardinstellingen zijn prima.
3. Start Cursor daarna opnieuw op, zodat het de nieuwe programma's ziet.

---

## Stap 3: de cursus binnenhalen

1. Open Cursor.
2. Druk op **Ctrl+Shift+P** (Windows) of **Cmd+Shift+P** (Mac). Bovenin verschijnt
   een balkje waarin je opdrachten kunt zoeken.
3. Typ `git clone` en kies **Git: Clone**.
4. Plak dit adres en druk op Enter:

   ```
   https://github.com/RvGolen/rooster-leren.git
   ```

5. Cursor vraagt nu waar hij de map mag neerzetten. Kies een plek die je makkelijk
   terugvindt, bijvoorbeeld je map *Documenten*.
6. Als hij klaar is, vraagt Cursor of je de map wilt openen. **Zeg ja.**

---

## Stap 4: controleer dat je de hele map open hebt (belangrijk!)

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

## Stap 5: laat Cursor je installatie nakijken

Nu de leuke stap: je laat de AI-assistent zelf controleren of alles goed staat.

1. Open de chat in Cursor met **Ctrl+L** (Windows) of **Cmd+L** (Mac).
2. Kopieer onderstaande tekst er helemaal in en druk op Enter.

```
Ik ben een complete beginner en ga in deze map een Python-cursus doen.
Controleer of mijn computer er klaar voor is, en leg het uit in gewone taal
zonder jargon. Doe het volgende:

1. Kijk of Python werkt, en met welk commando (python of python3).
2. Kijk of git werkt.
3. Kijk of ik op deze computer Python-pakketten mág installeren. Gebruik daarvoor
   een dry-run van pip, zodat er nu nog niets echt geïnstalleerd wordt. Later in
   de cursus heb ik pandas en ortools nodig.
4. Kijk of het bestand .cursor/rules/tutor.mdc bestaat vanuit deze map.

Geef me daarna een kort lijstje: wat werkt, wat werkt niet, en wat ik eraan moet
doen. Als iets om een beheerderswachtwoord vraagt of door de beheerder wordt
geblokkeerd, zeg dat dan gewoon eerlijk en probeer het niet te omzeilen.
```

3. Lees zijn antwoord. Staat alles op groen? Dan ben je klaar om te beginnen.

Werkt punt 3 niet, of zegt hij dat installeren geblokkeerd is? Dat is precies
waarom we het nú testen en niet over drie weken. Stuur me een bericht, dan lossen
we het op voor je er last van krijgt.

---

## Als iets niet lukt

Stuur me gewoon een bericht. Serieus, daar hoef je niet lang mee te wachten en
het is nooit een domme vraag.

Doe dat in elk geval meteen bij deze twee dingen, want daar valt niets aan te
prutsen:

- er wordt om een **beheerderswachtwoord** gevraagd, of je krijgt te zien dat je
  ergens **geen rechten** voor hebt;
- iets in de cursus zelf klopt niet: een link die nergens heen gaat, een script
  dat crasht, of een stap die niet kan kloppen. Dat is dan gewoon een fout van
  mij, geen fout van jou.

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
