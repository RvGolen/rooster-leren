# Waarom condities? — het *waaróm* achter module 5

Een loop laat je *overal* langslopen. Een conditie laat je *kiezen* wat je doet.
Samen vormen ze de logica waarmee een tool beslissingen neemt — en beslissingen zijn
precies waar een rooster om draait.

## 1. Regels zijn condities

Denk aan de harde regels uit jouw werk: "een lokaal moet genoeg surveillanten
hebben", "studenten passen in de zaal", "iemand is beschikbaar". Elke zo'n regel
wordt in code een **voorwaarde** die waar of niet waar is. Leren een regel als `if`
te schrijven, is leren je werkelijkheid te modelleren. Dat is de overdraagbare
vaardigheid uit deze cursus.

## 2. Loop + if = controleren

Het patroon "loop door alle toetsen, en *als* er iets mis is, meld het" is de motor
onder een **validator** (Project 2). Je hebt 'm in stap 4 al gebouwd. Onthoud de
vorm:

```python
for toets in toetsen:
    if er_is_iets_mis:
        meld_het()
```

## 3. == versus = — waarom dit zo vaak misgaat

`=` en `==` lijken op elkaar maar doen iets compleet anders:

```python
nodig = 3        # ZET nodig op 3 (toewijzen, module 1)
if nodig == 3:   # VRAAGT of nodig gelijk is aan 3 (vergelijken)
```

Schrijf je per ongeluk `if nodig = 3:`, dan geeft Python een foutmelding. Dat is nog
gunstig — je ziet het meteen. Veel vervelender is dat dit soort subtiele fouten ook
in AI-gegenereerde code sluipt. Wie het verschil kent, herkent zo'n fout bij het
*lezen*. Dat is jouw rol als supervisor.

---

## Een waarschuwing voor straks

`True` en `False` (met hoofdletter) zijn de twee waarden die een voorwaarde kan
hebben. Ze heten **booleans** (genoemd naar wiskundige George Boole). Je ziet ze nu
nog niet vaak los, maar in module 6 geeft je eerste echte functie — `heeft_conflict`
— precies zo'n `True`/`False` terug. Houd het in je achterhoofd.

---

## Termen van vandaag

| Term | Betekenis |
|------|-----------|
| `if` / `elif` / `else` | kiezen op basis van een voorwaarde |
| voorwaarde (conditie) | een uitdrukking die `True` of `False` is |
| `==` | vergelijken: "is gelijk aan" (twee istekens!) |
| `!=` `<` `>` `<=` `>=` | de overige vergelijkingen |
| `boolean` | een waarde die `True` of `False` is |

---

➡️ Verder met **`check.md`** van deze module. Onderaan staat waar je daarna heen gaat.
