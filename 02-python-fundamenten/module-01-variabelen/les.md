# Module 1 — Variabelen

⏱️ ± 15–20 minuten · Fase 1 · **Nieuw concept:** de *variabele*

---

## Eerst even raden 🤔

Hieronder staat een klein stukje Python. Lees het, en **schrijf voor jezelf op
(of zeg hardop) wat je denkt dat er gebeurt** — vóór je verder leest.

```python
aantal_studenten = 30
aantal_studenten = 45
print(aantal_studenten)
```

> Wat verschijnt er op het scherm? `30`, `45`, allebei, of een foutmelding?
> Commit aan een antwoord. Aan het eind van de module weet je of je gelijk had.

---

## Het concept: een variabele is een doosje met een naam

Een **variabele** (Engels voor "iets dat kan veranderen") is een **naam waaraan je
een waarde koppelt**. Stel je een doosje voor met een etiket erop. Op het etiket
staat de naam; in het doosje zit de waarde.

```python
lokaal = "A1.04"
```

- `lokaal` is de **naam** (het etiket).
- `=` betekent hier **niet** "is gelijk aan" zoals in de wiskunde. Het betekent
  *"stop de waarde rechts in het doosje links"*. We noemen dat **toewijzen**
  (Engels: *assignment*).
- `"A1.04"` is de **waarde**. De aanhalingstekens maken er **tekst** van — in
  programmeertaal heet tekst een `string` (Engels voor "rijgje tekens").

Vanaf nu kun je overal `lokaal` schrijven waar je `"A1.04"` bedoelt:

```python
print(lokaal)        # toont: A1.04
```

`print(...)` is een ingebouwd commando dat iets **op het scherm zet**. Handig om te
zien wat er in een doosje zit.

### Niet alleen tekst — ook getallen

```python
aantal_studenten = 30        # een geheel getal heet een int (van het Engelse "integer")
kosten_per_uur = 28.50       # een getal met komma heet een float
```

Met getallen kun je rekenen:

```python
uren = 3
totaal = kosten_per_uur * uren    # * is keer
print(totaal)                      # toont: 85.5
```

### Het doosje kan veranderen

Wijs je een nieuwe waarde toe, dan **vervangt** die de oude. Het doosje houdt maar
één ding tegelijk vast:

```python
surveillanten = 1
surveillanten = 2     # nu zit er 2 in; de 1 is weg
```

> 💡 Dit is precies wat er gebeurde in het raadsel bovenaan. Houd je antwoord bij de
> hand.

---

## Uitgewerkt voorbeeld — uit de surveillance-context

> ⚠️ **Dit is een vóórbeeld, geen voorschrift.** De getallen en regels hieronder
> illustreren alleen het idee. Jouw echte rooster heeft eigen waarden — die komen
> later aan bod.

We beschrijven één toets met een paar variabelen, en rekenen de inhuurkosten uit.

```python
# Eén toets, beschreven met losse variabelen
lokaal = "A1.04"
aantal_studenten = 30
surveillanten = 2            # hoeveel toezichthouders nodig zijn
kosten_per_uur = 28.50       # tarief per ingehuurde surveillant
duur_in_uren = 3

# De totale inhuurkosten voor deze toets
totale_kosten = surveillanten * kosten_per_uur * duur_in_uren

print("Toets in lokaal", lokaal)
print("Aantal surveillanten:", surveillanten)
print("Inhuurkosten:", totale_kosten, "euro")
```

Dit toont:

```
Toets in lokaal A1.04
Aantal surveillanten: 2
Inhuurkosten: 171.0 euro
```

Let op hoe `print` meerdere dingen na elkaar kan tonen als je ze met komma's
scheidt — tekst tussen aanhalingstekens, en variabelen zónder.

---

## Nu jij

Open **`opdracht.py`** in deze map. Daar staan `#TODO`'s die jij invult — stap voor
stap. Je typt zelf; dat is de bedoeling.

> Vastgelopen? Vraag je AI-tutor in **Ask-modus** om een *hint* (niet om de
> oplossing): bijvoorbeeld *"ik wil twee variabelen optellen maar krijg een fout —
> wat zou er mis kunnen zijn?"*

Als je klaar bent met `opdracht.py`, ga naar **`check.md`**.
