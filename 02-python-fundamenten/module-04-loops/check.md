# Zelfcheck — module 4

---

## 1. Voorspel zonder te draaien

```python
getallen = [1, 2, 3]
totaal = 0
for n in getallen:
    totaal = totaal + n
print(totaal)
```

Wat komt eruit? En wat zou er gebeuren als `totaal = 0` *binnen* de loop stond
(ingesprongen)?

---

## 2. Spot de fout

```python
toetsen = ["A1.04", "B2.10"]
for toets in toetsen:
print(toets)
```

Dit geeft een foutmelding. Wat is er mis, en hoe heet die fout?

---

## 3. In eigen woorden: wat doet de loop?

Beschrijf in gewone taal wat deze loop doet, regel voor regel:

```python
aantal_groot = 0
for toets in toetsen:
    if toets["studenten"] > 40:
        aantal_groot = aantal_groot + 1
```

> (De `if` komt pas in module 5 — maar kun je nú al raden wat hij doet? Goede
> oefening in *code lezen*, je kernvaardigheid.)

---

## 4. Leg het in je eigen woorden uit ✍️

> Waarom is een loop handiger dan dezelfde regel veertig keer kopiëren? Twee zinnen,
> in `voortgang.md`.

---

## Klaar met module 4 ✅

> 🔎 **Vooruitblik (spiraalvorm):** je kunt nu door alle toetsen lopen. Maar vaak
> wil je niet *alles* doen, maar alleen iets *als* een voorwaarde klopt — "tel mee
> *als* er te weinig surveillanten zijn". In **module 5** leer je `if`/`else`: kiezen
> op basis van een voorwaarde. Vraag 3 hierboven was er al een voorproefje van.

### Even mechanisch controleren 🔍

Draai in de terminal, in de map van deze module:

```bash
python controleer.py
```

Dat script draait jouw `opdracht.py` en zegt per stap of de uitvoer klopt. Zie het
als hulpmiddel, niet als examen: het vertelt je of je uitvoer klopt, niet of je het
snapt. Dat laatste deed je hierboven zelf.

➡️ Door naar **`../module-05-condities/les.md`**: module 5, condities.
