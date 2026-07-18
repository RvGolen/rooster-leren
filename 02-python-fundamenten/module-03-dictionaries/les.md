# Module 3 — Dictionaries

⏱️ ± 20 minuten · Fase 1 · **Nieuw concept:** de `dict` (dictionary)

> Bouwt op variabelen (module 1) en lijsten (module 2).

---

## Eerst even raden 🤔

```python
toets = {"lokaal": "A1.04", "tijd": "09:00", "studenten": 30}
print(toets["tijd"])
```

> Wat denk je dat dit toont? En waarin verschilt `toets["tijd"]` van de `[0]` die
> je bij lijsten zag? Gok eerst.

---

## Het concept: waarden met een label

Een lijst pak je aan met een **nummer** (`lokalen[0]`). Maar bij een toets is "het
nulde gegeven" onzin — je wilt vragen om *de tijd*, *het lokaal*, *het aantal
studenten*. Daarvoor is een **`dict`** (Engels *dictionary*, "woordenboek"): een
verzameling **label → waarde**-paren.

```python
toets = {
    "lokaal": "A1.04",
    "tijd": "09:00",
    "studenten": 30,
    "surveillanten": 2,
}
```

- De **accolades** `{ }` maken er een dict van.
- Elk paar is `"label": waarde`. Het label heet de **key** (Engels voor "sleutel"),
  de waarde heet de **value**.
- Je pakt een waarde op met de **key tussen rechte haken**:

```python
print(toets["tijd"])          # toont: 09:00
print(toets["studenten"])     # toont: 30
```

Dat leest bijna als een zin: *"van deze toets, de tijd"*. Veel duidelijker dan
`toets[1]` — want wie weet uit zijn hoofd dat plek 1 de tijd is?

### Een waarde wijzigen

```python
toets["surveillanten"] = 3    # er moet eentje bij
print(toets["surveillanten"]) # toont: 3
```

### Een nieuw gegeven toevoegen

Geef je een key die nog niet bestaat een waarde, dan komt hij erbij:

```python
toets["duur_in_uren"] = 3
print(toets)
```

---

## Uitgewerkt voorbeeld — uit de surveillance-context

> ⚠️ **Voorbeeld, geen voorschrift.** Welke gegevens jij per toets nodig hebt,
> bepaalt jouw situatie. Misschien wil jij ook "afdeling" of "type toets" erbij.

We beschrijven één toets volledig in één dict, en gebruiken de velden.

```python
# Eén toets als dictionary
toets = {
    "lokaal": "A1.04",
    "tijd": "09:00",
    "studenten": 30,
    "surveillanten": 2,
}

print("Toets in lokaal", toets["lokaal"], "om", toets["tijd"])
print("Er zijn", toets["surveillanten"], "surveillanten nodig voor",
      toets["studenten"], "studenten")

# De zaal wordt voller; er komt een surveillant bij
toets["studenten"] = 45
toets["surveillanten"] = 3
print("Bijgewerkt:", toets)
```

Dit toont:

```
Toets in lokaal A1.04 om 09:00
Er zijn 2 surveillanten nodig voor 30 studenten
Bijgewerkt: {'lokaal': 'A1.04', 'tijd': '09:00', 'studenten': 45, 'surveillanten': 3}
```

> 💡 **Lijst vs dict — wanneer wat?** Een **lijst** is voor *meerdere dingen van
> dezelfde soort* (alle lokalen). Een **dict** is voor *meerdere kenmerken van één
> ding* (alles over één toets). Straks combineer je ze: een lijst *van* dicts =
> een heel rooster. Daar werk je naartoe.

---

## Nu jij

Open **`opdracht.py`**. Vul de `#TODO`'s in.

> Hint nodig? In **Ask-modus**: *"hoe voeg ik een nieuw veld toe aan een dict dat er
> nog niet in zit?"*

Klaar? Ga naar **`check.md`**.
