# Zelfcheck — module 6

---

## 1. Voorspel zonder te draaien

```python
def dubbel(x):
    return x * 2

print(dubbel(dubbel(3)))
```

Wat komt eruit? (Tip: werk van binnen naar buiten.)

---

## 2. return of print?

Wat is het verschil tussen deze twee functies? Met welke kun je daarna
`totaal = ... ` doen om verder te rekenen?

```python
def a(x, y):
    print(x + y)

def b(x, y):
    return x + y
```

---

## 3. Lezen: klopt deze conflict-check?

Een collega (of een AI) schrijft dit. Klopt het met onze definitie van conflict
(*zelfde persoon én zelfde tijd*)? Zo niet, wat is er mis?

```python
def heeft_conflict(a, b):
    return a["persoon"] == b["persoon"] or a["tijd"] == b["tijd"]
```

> Tip: let heel goed op het woordje in het midden. Dit is precies het soort fout dat
> je straks in AI-code moet kunnen spotten.

---

## 4. Leg het in je eigen woorden uit ✍️

> Wat is een functie, en waarom is het handig om logica (zoals `heeft_conflict`) een
> naam te geven in plaats van de code telkens opnieuw te schrijven? Twee à drie
> zinnen, in `voortgang.md`.

---

## Klaar met module 6 ✅

Je hebt nu alle losse bouwstenen: variabelen, lijsten, dicts, loops, condities en
functies. En je hebt `heeft_conflict` — een functie die **twee** diensten vergelijkt.

> 🔎 **Vooruitblik (spiraalvorm):** maar een rooster heeft niet twee diensten, het
> heeft er tientallen. Je wilt **alle paren** met elkaar vergelijken. In **module 7**
> leer je de *geneste loop* (een loop in een loop) waarmee je `heeft_conflict` op een
> hele lijst van diensten loslaat. Daarna ben je klaar voor **Project 1**.

### Even mechanisch controleren 🔍

Draai in de terminal, in de map van deze module:

```bash
python controleer.py
```

Dat script draait jouw `opdracht.py` en zegt of de uitvoer klopt. Stap 3 en 4 maken
alleen functies zonder iets te printen, dus die komen samen met stap 5 aan het licht.
Zie het als hulpmiddel, niet als examen: het vertelt je of je uitvoer klopt, niet of
je het snapt. Dat laatste deed je hierboven zelf.

➡️ Door naar **`../module-07-lijsten-van-dicts/les.md`**: module 7, lijsten van dicts & geneste loops.
