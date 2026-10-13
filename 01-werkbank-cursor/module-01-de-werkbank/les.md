# Module 0.1 — De werkbank

⏱️ ± 15–20 minuten · Fase 0 · **Nieuw:** rondkijken in Cursor + je eerste script draaien

---

## Eerst even raden 🤔

In deze map staat een klein bestand `opdracht.py`. Straks ga je het "draaien" —
de computer voert de regels uit. Er staat onder andere dit in:

```python
print("Hallo! Dit script draait. 🎉")
```

> **Wat denk je dat er gebeurt als je dit draait?** Verschijnt er iets, en zo ja,
> waar? Commit aan een antwoord — aan het eind weet je of je gelijk had.

---

## Je scherm

De rondleiding over je scherm heb je al met Robin gedaan: links de **Explorer**
met je bestanden, in het midden de **editor** waarin je een bestand leest en
schrijft, en onderin de **terminal** waarin je een script draait.

---

## Een bestand openen

Klik in de Explorer op de map `01-werkbank-cursor`, dan `module-01-de-werkbank`,
en dan op **`opdracht.py`**. Het bestand opent in de editor. Lees het rustig door —
de `#`-regels zijn **comments**: uitleg voor mensen, die de computer overslaat.

---

## De terminal openen en een script draaien

Nu het echte werk: je gaat het script *draaien*.

Eerst één ding dat je de hele cursus nodig hebt: **de terminal staat altijd in een
map.** Als je `python opdracht.py` typt, zoekt hij `opdracht.py` alléén in die
map. Staat hij in een andere map, dan vindt hij het bestand niet.

Daarom open je de terminal altijd zo:

1. Klik in de Explorer met de **rechtermuisknop op het bestand dat je wilt
   draaien**, hier `opdracht.py`, en kies **Open in Integrated Terminal**.
   Onderin verschijnt een tekstvenster dat al in de goede map staat.

   > **Zo zie je in welke map de terminal staat:** vlak vóór je knipperende
   > cursor staat de naam van de map, bijvoorbeeld `module-01-de-werkbank`. Staat
   > daar `rooster-leren`, dan zit je in de hoofdmap, en daar staat `opdracht.py`
   > niet. Je krijgt dan een melding als:
   >
   > ```
   > can't open file '...rooster-leren/opdracht.py': No such file or directory
   > ```
   >
   > Dat is geen ramp: open de terminal gewoon opnieuw met de rechtermuisknop op
   > het bestand.
2. Typ deze opdracht en druk op Enter:

   ```
   python opdracht.py
   ```

   Werkt dat niet (melding "command not found")? Probeer dan:

   ```
   python3 opdracht.py
   ```

3. De `print`-regels uit het bestand verschijnen nu onder je opdracht. Dít is je
   script dat "draait".

> 💡 Belangrijk misverstand om vroeg op te ruimen: het bestand **openen** in de
> editor voert het níet uit. Pas als je het in de terminal *draait*, gebeurt er iets.
> Openen = lezen; draaien = uitvoeren.

> 💾 **Opslaan hoeft niet.** Cursor bewaart je wijzigingen vanzelf (*Auto Save*
> staat aan). Zie je toch een bolletje ● naast de bestandsnaam bovenaan de editor?
> Dan is het bestand nog niet bewaard: druk op **Ctrl+S**. Een script draait altijd
> de laatst bewaarde versie.

---

## Uitgewerkt voorbeeld — wat je ongeveer ziet

> ⚠️ **Voorbeeld, geen voorschrift.** De naam en het lokaal hieronder zijn verzonnen;
> jouw echte gegevens vul je zo zelf in.

Na `python opdracht.py` verschijnt zoiets in de terminal:

```
Hallo! Dit script draait. 🎉
Surveillant: ... vul hier je naam in ...
staat om 09:00 in lokaal A1.04
```

Zie je dat de tweede regel nog een invul-plek toont? Die ga jij vervangen.

---

## Nu jij

Open **`opdracht.py`** in deze map. Er staat één `#TODO`: vervang de invul-tekst
door je eigen naam en **draai het bestand opnieuw**. Zie je je naam verschijnen?

> Vastgelopen (bijv. de terminal geeft een rode foutmelding)? Onthoud die melding —
> in module 2 leer je hoe je 'm in **Ask-modus** aan je AI-tutor voorlegt.

Klaar met `opdracht.py`? Ga naar **`check.md`**.
