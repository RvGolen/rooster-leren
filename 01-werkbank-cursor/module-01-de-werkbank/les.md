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

1. Open de terminal **in de map van deze module**: klik in de Explorer met de
   rechtermuisknop op de map `module-01-de-werkbank` en kies **Open in
   Integrated Terminal**. Onderin verschijnt een tekstvenster met een
   knipperende cursor.

   > Waarom zo? De terminal zoekt `opdracht.py` in de map waar hij staat. Open je
   > hem via het menu, dan staat hij in de hoofdmap `rooster-leren`, en daar staat
   > dit bestand niet.
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
