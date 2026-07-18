# Waarom loops? — het *waaróm* achter module 4

Een loop is misschien wel het belangrijkste idee uit fase 1. Bijna alles wat een
roostertool doet, is "doe iets voor elk item": elke toets controleren, elke
surveillant nalopen, elke combinatie afwegen.

## 1. Werk dat meeschaalt

Zonder loop schrijf je voor 3 toetsen 3 regels, en voor 300 toetsen 300 regels.
Met een loop schrijf je het **één keer**, en het werkt voor elk aantal. Je code
wordt niet langer als het rooster groeit. Dat is het verschil tussen speelgoed en
een echte tool.

## 2. Het patroon "verzamel terwijl je loopt"

Het optel-patroon uit stap 3 (`totaal` begint op 0, groeit in de loop) kom je
overal tegen:
- tel het totaal aantal studenten;
- tel hoeveel toetsen er meer dan 2 surveillanten nodig hebben;
- verzamel alle conflicten in een nieuwe lijst.

Steeds dezelfde vorm: *maak iets aan vóór de loop, vul het in de loop, gebruik het
na de loop.* Onthoud die vorm — je gebruikt hem in Project 1.

## 3. Loop + lijst + dict = je rooster komt tot leven

In stap 4 liep je door een **lijst van dicts**. Dat is, in het klein, precies een
rooster: meerdere toetsen, elk met kenmerken, en jij doet er één voor één iets mee.
Vanaf hier kun je echt iets nuttigs bouwen.

---

## De valkuil: inspringing (indentation)

Python gebruikt **inspringing** om te bepalen wat bij de loop hoort:

```python
for toets in toetsen:
    print(toets["lokaal"])     # hoort BIJ de loop (ingesprongen)
print("klaar")                  # hoort NIET bij de loop (loopt 1x, na afloop)
```

Spring je per ongeluk niet in, dan krijg je een `IndentationError`. Gebruik
consequent **vier spaties**. Cursor helpt je hierbij, maar het is goed te wéten
waaróm die witruimte er staat — straks zie je 'm ook in AI-code terug.

---

## Termen van vandaag

| Term | Betekenis |
|------|-----------|
| `for ... in ...:` | herhaal iets voor elk item in een lijst |
| body (de loop-body) | de ingesprongen regels die herhaald worden |
| indentation (inspringing) | witruimte die aangeeft wat bij de loop hoort; **4 spaties** |
| `IndentationError` | foutmelding bij verkeerde inspringing |
