# Waarom variabelen? — het *waaróm* achter module 1

De code in `opdracht.py` had je ook kunnen schrijven met de kale getallen erin:

```python
print("Inhuurkosten:", 2 * 28.50 * 3, "euro")
```

Dat werkt. Toch doen we het bijna nooit zo. Variabelen lossen drie problemen op die
je in elke echte rooster-tool tegenkomt.

## 1. Betekenis — code wordt leesbaar

Wat betekent `2 * 28.50 * 3`? Geen idee, tenzij je het uitrekent én raadt wat elk
getal voorstelt. Maar dit lees je als een zin:

```python
totale_kosten = surveillanten * kosten_per_uur * duur_in_uren
```

Een goede variabelenaam is **gratis documentatie**. Dit wordt cruciaal zodra je
straks code van de AI gaat *lezen en beoordelen*: goede namen verraden of de AI
echt jouw probleem heeft begrepen.

## 2. Eén plek om te wijzigen

Stel dat het uurtarief stijgt naar 30 euro. Met een variabele verander je dat op
**één** plek (`kosten_per_uur = 30`) en klopt de rest vanzelf. Staan de kale
getallen overal verspreid, dan moet je ze stuk voor stuk opsporen — en vergeet je
er gegarandeerd één. Een rooster zit vol van dat soort waarden die later veranderen.

## 3. De waarde mag tijdens het werk veranderen

In stap 4 gaf je `surveillanten` een nieuwe waarde, en je herberekende de kosten.
Dat "een waarde verandert onderweg" is de motor onder álle roosterlogica: een
programma probeert dingen, past aan, en rekent opnieuw. Een variabele is het
geheugen dat daarbij meebeweegt.

---

## Het raadsel van het begin

```python
aantal_studenten = 30
aantal_studenten = 45
print(aantal_studenten)   # toont: 45
```

Het antwoord is **45**. De tweede toewijzing vervangt de eerste; het doosje houdt
maar één waarde tegelijk vast. Dat voelt nu misschien logisch — maar onthoud het,
want het is een veelgemaakte denkfout: `=` *kopieert een waarde naar links*, het
legt geen blijvend verband tussen twee dingen.

---

## Termen die je vandaag tegenkwam (Engels, kort uitgelegd)

| Term | Betekenis |
|------|-----------|
| `variable` (variabele) | een naam waaraan een waarde hangt |
| `assignment` (toewijzen) | een waarde in een variabele stoppen met `=` |
| `string` | tekst, tussen aanhalingstekens: `"A1.04"` |
| `int` | een geheel getal: `30` |
| `float` | een getal met decimalen: `28.50` |
| `print()` | commando dat iets op het scherm zet |

Je hoeft deze niet uit je hoofd te leren — ze komen vanzelf terug in volgende
modules. Dat heet *spiraalvorm*: oude dingen keren steeds terug in nieuwe context.

---

➡️ Verder met **`check.md`** van deze module. Onderaan staat waar je daarna heen gaat.
