# Waarom functies? — het *waaróm* achter module 6

Functies zijn hoe je van losse regels code naar een echte *tool* gaat. Ze doen drie
dingen die alles daarna mogelijk maken.

## 1. Niet herhalen (hergebruik)

Schreef je de conflict-check elke keer opnieuw uit, dan stond dezelfde logica overal
verspreid — en als je regel verandert, moet je 'm overal aanpassen. Met een functie
schrijf je 'm **één keer** en roep je 'm overal aan met een nette naam:
`heeft_conflict(a, b)`. Verandert je definitie van "conflict", dan pas je één plek
aan.

## 2. Een naam verbergt de details (abstractie)

Wie `heeft_conflict(dienst1, dienst2)` leest, hoeft niet te weten *hoe* het werkt —
de naam zegt genoeg. Dat heet **abstractie**: complexe logica achter een begrijpelijke
naam stoppen. Het is precies waarom je straks een groot, door Cursor gegenereerd
programma kunt *lezen*: het bestaat uit functies met namen die je vertellen wat ze
doen, zonder dat je elke regel hoeft te ontcijferen.

> Sterker nog: als een AI je een functie geeft met een naam die niet klopt bij wat
> hij doet, is dat een **rode vlag**. Goede namen zijn een controle-instrument.

## 3. Testbaar in stukjes

Omdat `heeft_conflict` een duidelijk antwoord teruggeeft (`True`/`False`), kun je 'm
los uitproberen met een paar voorbeelden — zoals je in stap 5 deed. Je hoeft niet het
hele programma te draaien om te weten of dit stukje klopt. Dat "in kleine stukjes
controleerbaar" is goud bij het superviseren van AI-code: je kunt elk onderdeel apart
narekenen.

---

## `return` versus `print` — een belangrijk verschil

Beginners halen dit vaak door elkaar:

```python
def kosten(uren, tarief):
    print(uren * tarief)     # toont het op het scherm, maar geeft niets terug
```

```python
def kosten(uren, tarief):
    return uren * tarief     # geeft het terug, zodat je ermee verder kunt rekenen
```

`print` is voor *jou*, om iets te zien. `return` is voor je *programma*, om de
waarde verder te gebruiken: `totaal = kosten(3, 30) * aantal_dagen`. Met de
`print`-versie kun je dat niet — er komt niets terug om mee te rekenen. Onthoud:
**`return` geeft, `print` toont.**

---

## Termen van vandaag

| Term | Betekenis |
|------|-----------|
| `function` (functie) | herbruikbaar stukje code met een naam |
| `def` | sleutelwoord om een functie te definiëren |
| parameter | een ingrediënt dat de functie meekrijgt (`uren`, `tarief`) |
| `return` | geeft een waarde terug aan wie de functie aanriep |
| aanroepen (call) | de functie gebruiken: `kosten(3, 30)` |
| `and` | combineert twee voorwaarden; waar als **beide** waar zijn |
| abstractie | details verbergen achter een begrijpelijke naam |

---

➡️ Verder met **`check.md`** van deze module. Onderaan staat waar je daarna heen gaat.
