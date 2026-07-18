# Module 6 — Functies

⏱️ ± 25 minuten · Fase 1 · **Nieuw concept:** de `function` (`def`)

> Bouwt op condities (module 5) en dictionaries (module 3). Dit is de module waar
> alles samenkomt in je eerste echte rooster-functie.

---

## Eerst even raden 🤔

```python
def kosten(uren, tarief):
    return uren * tarief

print(kosten(3, 28.50))
```

> Wat denk je dat dit toont? En wat zou `kosten(4, 30)` geven? Gok eerst.

---

## Het concept: logica met een naam, om te hergebruiken

Een **`function`** (functie) is een stukje code dat je een **naam** geeft, zodat je
het steeds opnieuw kunt gebruiken zonder het te herhalen. `print()` en `len()` ken
je al — dat zijn kant-en-klare functies. Nu maak je er zelf een.

```python
def kosten(uren, tarief):
    return uren * tarief
```

Ontleed:
- **`def`** (Engels, kort voor *define*, "definiëren") begint een functie.
- **`kosten`** is de naam die jij kiest.
- Tussen haakjes staan de **parameters**: `uren` en `tarief`. Dat zijn de gegevens
  die de functie nodig heeft om te werken — als ingrediënten.
- Dubbele punt + ingesprongen body, net als bij loops en if.
- **`return`** (Engels voor "teruggeven") levert het antwoord terug aan wie de
  functie aanriep.

### Een functie *aanroepen*

Definiëren is het recept opschrijven. **Aanroepen** is het recept gebruiken:

```python
totaal = kosten(3, 28.50)    # uren=3, tarief=28.50  ->  geeft 85.5 terug
print(totaal)                 # toont: 85.5
print(kosten(4, 30))          # toont: 120  (zelfde functie, andere ingrediënten)
```

Je schreef de logica **één keer**, en gebruikt 'm zo vaak je wilt. Net als een loop
herhaalt *over data*, laat een functie je code hergebruiken *door je programma heen*.

### Een functie die `True` of `False` teruggeeft

Een functie mag ook een ja/nee-antwoord teruggeven — een **boolean** (module 5):

```python
def is_te_vol(studenten, capaciteit):
    return studenten > capaciteit

print(is_te_vol(55, 40))    # toont: True
print(is_te_vol(30, 40))    # toont: False
```

Let op: `studenten > capaciteit` ís al `True` of `False`, dus dat geef je direct
terug. Zulke ja/nee-functies zijn goud waard, want je kunt ze meteen in een `if`
gebruiken: `if is_te_vol(...):`.

---

## Uitgewerkt voorbeeld — je eerste echte rooster-functie

> ⚠️ **Voorbeeld, geen voorschrift.** Wat precies een "conflict" is, hangt van jouw
> regels af. Hier nemen we de meest basale: *dezelfde persoon, op hetzelfde tijdslot,
> ingepland op twee plekken.* Die kan natuurkundig niet — dus dat is een conflict.

We beschrijven een **dienst** als een dict: wie, wanneer, waar.

```python
# Een 'dienst' = een inzet van één persoon, op één tijd, in één lokaal
def heeft_conflict(dienst_a, dienst_b):
    # Conflict: zelfde persoon EN zelfde tijd (dan staat die op twee plekken)
    zelfde_persoon = dienst_a["persoon"] == dienst_b["persoon"]
    zelfde_tijd = dienst_a["tijd"] == dienst_b["tijd"]
    return zelfde_persoon and zelfde_tijd


dienst1 = {"persoon": "Jansen", "tijd": "09:00", "lokaal": "A1.04"}
dienst2 = {"persoon": "Jansen", "tijd": "09:00", "lokaal": "B2.10"}   # botst!
dienst3 = {"persoon": "Jansen", "tijd": "11:00", "lokaal": "B2.10"}   # andere tijd

print(heeft_conflict(dienst1, dienst2))   # toont: True  (zelfde persoon én tijd)
print(heeft_conflict(dienst1, dienst3))   # toont: False (andere tijd)
```

Twee nieuwe dingen om op te merken:
- **`and`** (Engels voor "en") combineert twee voorwaarden: alléén waar als *beide*
  waar zijn. Precies wat een conflict is: zelfde persoon **én** zelfde tijd.
- De functie geeft een nette `True`/`False` terug. Wie 'm aanroept hoeft niet te
  weten *hóe* het werkt — alleen *wat* hij doet. Dat heet **abstractie**, en het is
  waarom grote programma's behapbaar blijven.

> 💡 Dit `heeft_conflict` is geen toevallig voorbeeld: het is de bouwsteen van
> **Project 1**. Daar laat je 'm los op een héél rooster.

---

## Nu jij

Open **`opdracht.py`**. Je bouwt `heeft_conflict` zelf op, in kleine stappen. De
steun is bewust kleiner dan in eerdere modules — je kunt al veel.

> Hint nodig? In **Ask-modus**: *"wat is het verschil tussen een functie definiëren
> en aanroepen?"* of *"wat doet `and` precies?"*

Klaar? Ga naar **`check.md`**.
