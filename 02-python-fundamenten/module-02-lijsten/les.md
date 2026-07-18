# Module 2 — Lijsten

⏱️ ± 15–20 minuten · Fase 1 · **Nieuw concept:** de `list` (lijst)

> Je weet uit module 1 al wat een variabele is. Dat heb je hier nodig.

---

## Eerst even raden 🤔

```python
tijdsloten = ["09:00", "11:00", "13:00"]
print(tijdsloten[0])
print(len(tijdsloten))
```

> Wat denk je dat elke `print`-regel toont? Let vooral op die `[0]`.
> Schrijf je gok op vóór je verder leest.

---

## Het concept: één naam voor een rij waarden

In module 1 had elk doosje precies één waarde. Maar een roosterdag heeft niet één
tijdslot — die heeft er meerdere. Daar gebruik je een **`list`** (Engels voor
"lijst": een **geordende rij waarden** onder één naam).

```python
tijdsloten = ["09:00", "11:00", "13:00"]
```

- De **rechte haken** `[ ]` maken er een lijst van.
- De waarden staan **op volgorde** en zijn gescheiden door komma's.
- Het mogen strings zijn, getallen, of allebei door elkaar.

### Een element eruit pakken — met zijn plek (index)

Elk element heeft een **plek-nummer**, de *index*. Let op: **tellen begint bij 0**,
niet bij 1. Dat is even wennen, maar het is overal in Python zo.

```python
tijdsloten = ["09:00", "11:00", "13:00"]
#                0          1         2     <- de index van elk element

print(tijdsloten[0])   # toont: 09:00  (het eerste element)
print(tijdsloten[2])   # toont: 13:00  (het derde element)
```

### Hoeveel zitten erin?

`len(...)` (van het Engelse *length*, lengte) geeft het **aantal** elementen:

```python
print(len(tijdsloten))   # toont: 3
```

### Er eentje bijzetten

`append` (Engels voor "achteraan toevoegen") plakt een element aan het eind:

```python
tijdsloten.append("15:00")
print(tijdsloten)        # toont: ['09:00', '11:00', '13:00', '15:00']
print(len(tijdsloten))   # toont: 4
```

---

## Uitgewerkt voorbeeld — uit de surveillance-context

> ⚠️ **Voorbeeld, geen voorschrift.** Jouw echte rooster heeft andere lokalen en
> tijden. Het gaat om het idee, niet om deze waarden.

We houden bij welke **lokalen** er vandaag in gebruik zijn, als één lijst.

```python
# De lokalen die vandaag een toets hebben
lokalen = ["A1.04", "B2.10", "C0.21"]

print("Eerste lokaal:", lokalen[0])
print("Aantal lokalen vandaag:", len(lokalen))

# Er komt een lokaal bij
lokalen.append("D1.15")
print("Na toevoegen:", lokalen)
print("Nu in gebruik:", len(lokalen), "lokalen")
```

Dit toont:

```
Eerste lokaal: A1.04
Aantal lokalen vandaag: 3
Na toevoegen: ['A1.04', 'B2.10', 'C0.21', 'D1.15']
Nu in gebruik: 4 lokalen
```

Eén lijst, en je kunt hem hele dag laten meegroeien. Veel handiger dan vier losse
variabelen `lokaal1`, `lokaal2`, …

---

## Nu jij

Open **`opdracht.py`**. Vul de `#TODO`'s in. Er is iets minder voorgekauwd dan in
module 1 — dat hoort zo; de steun neemt af.

> Vastgelopen? Vraag in **Ask-modus** om een *hint*, bijvoorbeeld: *"hoe pak ik het
> laatste element van een lijst als ik niet weet hoe lang die is?"*

Klaar? Ga naar **`check.md`**.
