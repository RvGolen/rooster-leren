# Waarom lijsten? — het *waaróm* achter module 2

In module 1 zou je een team van surveillanten zo kunnen opslaan:

```python
persoon1 = "Jansen"
persoon2 = "De Vries"
persoon3 = "Bakker"
```

Dat werkt bij drie. Maar een rooster heeft tientallen mensen, lokalen en tijdsloten,
en je weet vooraf niet hoeveel. Losse genummerde variabelen lopen dan vast.

## 1. Eén naam voor "allemaal"

Met een lijst praat je over de hele groep tegelijk: `surveillanten`. Je kunt hem
tellen (`len`), erin zoeken, en — vanaf module 4 — er in één keer **doorheen lopen**
met een loop. Dat laatste is de echte reden dat lijsten zo belangrijk zijn: bijna
elke roosterbewerking is "doe iets met *elk* item in een lijst".

## 2. De volgorde blijft bewaard

Een lijst is **geordend**. `tijdsloten[0]` is altijd het eerste tijdslot. Dat is
precies wat je wilt voor een rooster, waar volgorde betekenis heeft (eerst 09:00,
dan 11:00).

## 3. Hij kan groeien en krimpen

Met `.append()` groeit de lijst mee terwijl je programma draait. Een rooster is
nooit "klaar" op één moment — er komen lokalen bij, mensen vallen uit. Een lijst
beweegt mee.

---

## De valkuil: tellen begint bij 0

Dit is dé klassieke beginnersfout, dus expres benoemd:

```python
lokalen = ["A1.04", "B2.10", "C0.21"]
print(lokalen[1])   # toont B2.10, NIET A1.04
```

De index is geen "hoeveelste", maar een "afstand vanaf het begin". Het eerste
element staat op afstand 0. Daarom is het **laatste** element `lokalen[len(...) - 1]`:
bij 3 elementen is dat index 2.

> Vraag `lokalen[3]` op in een lijst van 3 en je krijgt een `IndexError` — Python
> zegt: "die plek bestaat niet". Een veelvoorkomende fout die je straks ook in
> AI-code zult herkennen.

---

## Termen van vandaag

| Term | Betekenis |
|------|-----------|
| `list` (lijst) | geordende rij waarden onder één naam, tussen `[ ]` |
| index | het plek-nummer van een element; **begint bij 0** |
| `len()` | geeft het aantal elementen |
| `.append()` | voegt een element achteraan toe |
| `IndexError` | foutmelding: je vraagt een plek op die niet bestaat |
