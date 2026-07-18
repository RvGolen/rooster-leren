# Module 5 — Een class lezen: data en gedrag samen

⏱️ ± 25–30 minuten · Fase 2 · **Nieuw concept:** een `class`

---

## Eerst even raden 🤔

Twee manieren om dezelfde vraag te stellen — past deze toets in dit lokaal?

```python
toets["aantal_studenten"] <= lokaal["capaciteit"]
```

```python
toets.past_in(lokaal)
```

> Kijk goed naar allebei. Welke is makkelijker te lezen, denk je — en waarom?
> Schrijf voor jezelf op wat je verwacht, voordat je verderleest.

---

## De brug vanaf dict

Je kent de dict al goed: een dict is **data**, verder niets. Wil je weten of een
toets in een lokaal past, dan schrijf je die vergelijking zelf op, elke keer
weer — `toets["aantal_studenten"] <= lokaal["capaciteit"]`. Staat die vraag op
vijf plekken in je code, dan typ je hem vijf keer.

Een **class** houdt de data én de vragen die je erover stelt bij elkaar. De
data (aantal studenten, capaciteit) en de vraag ("past dit?") wonen dan in
hetzelfde ding. Dat is het hele concept van vandaag — verder niets nieuws.

---

## Uitgewerkt voorbeeld

> ⚠️ **Voorbeeld, geen voorschrift.** We gebruiken lokalen en toetsen om het
> concept concreet te maken. Jouw situatie heeft misschien andere "dingen" die
> dit verdienen — daar kom je bij **jouw situatie** onderaan deze module op uit.

```python
class Lokaal:
    def __init__(self, naam, capaciteit):
        self.naam = naam
        self.capaciteit = capaciteit


class Toets:
    def __init__(self, toets_id, vak, aantal_studenten):
        self.toets_id = toets_id
        self.vak = vak
        self.aantal_studenten = aantal_studenten

    def past_in(self, lokaal):
        return self.aantal_studenten <= lokaal.capaciteit


b211 = Lokaal("B2.11", 40)
bestuurskunde = Toets("T5", "Bestuurskunde", 55)

print(bestuurskunde.past_in(b211))   # False — 55 studenten passen niet in 40 plekken
```

Dit toont:

```
False
```

> Herken je T5 en B2.11? Dat is bewust: het is dezelfde capaciteitsovertreding
> die in `toetsen.csv` en `lokalen.csv` staat. In Project 2 kom je hem terug.

Lees de code rustig terug. `class Lokaal:` en `class Toets:` beschrijven elk
één soort "ding" — net als je eerder een dict gebruikte voor één toets of één
lokaal. Het verschil: binnen de class staat niet alleen de data (`naam`,
`capaciteit`, `aantal_studenten`, ...), maar ook een **methode** — `past_in` —
die een vraag over die data beantwoordt. Een methode is niets anders dan een
functie die bij een class hoort.

Daarom lees je `bestuurskunde.past_in(b211)` als: "vraag aan `bestuurskunde` of
hij past in `b211`." De data en de vraag zitten aan elkaar vast.

---

## `__init__` en `self`, kort

Twee dingen vallen meteen op: `__init__` en `self`. Meer hoef je er nu niet van
te weten dan dit:

- **`__init__`** is wat er gebeurt zodra je een nieuw lokaal of een nieuwe
  toets aanmaakt — "vul de velden in". Regel `b211 = Lokaal("B2.11", 40)` roept
  `__init__` aan en zet `naam` op `"B2.11"` en `capaciteit` op `40`.
- **`self`** betekent "dit lokaal (of deze toets) zelf, degene waar je het nu
  over hebt". Meer theorie heeft het niet nodig.

Die rare dubbele underscores rond `init` zijn gewoon een Python-schrijfwijze
voor "dit is speciaal voor Python" — geen diepere betekenis. Dat scheelt je
uren piekeren.

---

## Waarom je dit vooral moet kunnen lézen

Gegenereerde code — van AI, of van een collega — zit vol classes. Jij hoeft
zelf geen classes te leren schrijven; je moet kunnen zien wat er staat als je
er een tegenkomt, en er zelfverzekerd een klein stukje aan durven toevoegen.
Daarom lees je in deze module vooral, en voeg je zelf maar één veld en één
methode toe aan een class die er al staat.

---

## Nu jij

Open **`opdracht.py`**. De classes staan er al. Vier stappen, van lezen naar
zelf een klein stukje toevoegen.

> Vastgelopen op wat een regel doet? In **Ask-modus**: *"leg uit wat deze regel
> in de class doet"* — laat het je uitleggen, ga daarna zelf verder.

Klaar? Ga naar **`check.md`**.
