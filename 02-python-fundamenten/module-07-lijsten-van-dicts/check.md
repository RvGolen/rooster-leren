# Zelfcheck — module 7

---

## 1. Voorspel zonder te draaien

```python
for i in range(2):
    for j in range(2):
        print(i, j)
```

Welke regels komen eruit, en in welke volgorde?

---

## 2. Het belang van i + 1

In een rooster van 4 diensten: hoeveel paren zijn er om te vergelijken? En wat zou er
misgaan als je de binnenste loop bij `range(len(rooster))` liet beginnen in plaats van
`range(i + 1, len(rooster))`?

---

## 3. Lezen: spot de fout

Een AI levert deze conflict-zoeker. Er zit een fout in. Welke?

```python
for i in range(len(rooster)):
    for j in range(len(rooster)):
        if heeft_conflict(rooster[i], rooster[j]):
            print("conflict")
```

> Tip: draai het in gedachten op een rooster met één persoon. Hoeveel "conflicten"
> meldt het, en klopt dat?

---

## 4. Leg het in je eigen woorden uit ✍️

> Beschrijf in drie à vier zinnen hoe je *alle conflicten* in een rooster vindt:
> welke bouwstenen (lijst, dict, loop, functie, geneste loop) zet je in, en hoe
> werken ze samen? Schrijf het in `voortgang.md` — dit is meteen je samenvatting van
> heel fase 1.

---

## Klaar met module 7 ✅ — en met fase 1!

Vul `voortgang.md` bij: welk concept zat het lekkerst, en welk vond je het lastigst?
Dat lastige concept is precies wat je in Project 1 nog eens oefent.

➡️ Door naar **`projecten/project-1-conflicten/`** — je eerste echte project, waarin
alles samenkomt.
