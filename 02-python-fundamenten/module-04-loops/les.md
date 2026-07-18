# Module 4 — Loops

⏱️ ± 20 minuten · Fase 1 · **Nieuw concept:** de `for`-loop (herhalen)

> Bouwt op lijsten (module 2) en dictionaries (module 3).

---

## Eerst even raden 🤔

```python
tijdsloten = ["09:00", "11:00", "13:00"]
for tijd in tijdsloten:
    print("Toetsmoment:", tijd)
```

> Hoeveel regels denk je dat dit op het scherm zet, en wat staat erop? Gok eerst.

---

## Het concept: doe iets voor élk item

Tot nu toe deed je dingen één voor één. Maar je wilt niet veertig keer met de hand
`print(...)` typen voor veertig toetsen. Een **`for`-loop** (Engels *for*, "voor")
zegt: *"voor elk item in deze lijst, doe het volgende."*

```python
tijdsloten = ["09:00", "11:00", "13:00"]
for tijd in tijdsloten:
    print("Toetsmoment:", tijd)
```

Wat hier gebeurt, stap voor stap:
- Python pakt het **eerste** item uit `tijdsloten` en stopt het in de variabele
  `tijd`. Dan voert hij de ingesprongen regel uit.
- Daarna het **tweede** item → opnieuw. Enzovoort, tot de lijst op is.
- `tijd` is een naam die **jij** kiest; het is gewoon "het huidige item".

Resultaat:

```
Toetsmoment: 09:00
Toetsmoment: 11:00
Toetsmoment: 13:00
```

### Let op de twee dingen die de loop maken

```python
for tijd in tijdsloten:
    print("Toetsmoment:", tijd)
```

1. De regel eindigt op een **dubbele punt** `:`.
2. De regel(s) eronder zijn **ingesprongen** (vier spaties). Die inspringing zegt
   tegen Python: *"dit hoort bij de loop."* Spring je niet in, dan hoort de regel er
   niet bij. In Python is die witruimte **betekenisvol** — anders dan in veel andere
   talen. Wen er maar vast aan; het is een veelvoorkomende beginnersfout.

### Optellen in een loop

Een veelgebruikt patroon: begin met een teller op 0, en tel er in de loop bij op.

```python
aantallen = [30, 24, 45]
totaal = 0
for n in aantallen:
    totaal = totaal + n      # tel het huidige getal erbij op
print("Totaal aantal studenten:", totaal)   # toont: 99
```

> Zie je hoe `totaal` hier het "geheugen" is dat meebeweegt? Precies het idee uit
> module 1 — variabelen die veranderen — nu in een loop.

---

## Uitgewerkt voorbeeld — uit de surveillance-context

> ⚠️ **Voorbeeld, geen voorschrift.**

We lopen door alle lokalen en tellen hoeveel surveillanten we in totaal nodig hebben.

```python
# Per lokaal: hoeveel surveillanten nodig zijn
benodigd_per_lokaal = [2, 2, 3, 1]

totaal_surveillanten = 0
for aantal in benodigd_per_lokaal:
    print("Dit lokaal heeft", aantal, "surveillanten nodig")
    totaal_surveillanten = totaal_surveillanten + aantal

print("In totaal nodig:", totaal_surveillanten, "surveillanten")
```

Dit toont:

```
Dit lokaal heeft 2 surveillanten nodig
Dit lokaal heeft 2 surveillanten nodig
Dit lokaal heeft 3 surveillanten nodig
Dit lokaal heeft 1 surveillanten nodig
In totaal nodig: 8 surveillanten
```

Vier lokalen of vierhonderd — de loop blijft even lang. Dat is de kracht.

---

## Nu jij

Open **`opdracht.py`**. Let goed op de dubbele punt en de inspringing.

> Hint nodig? In **Ask-modus**: *"mijn for-loop geeft een IndentationError, wat
> betekent dat?"*

Klaar? Ga naar **`check.md`**.
