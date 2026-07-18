# Waarom geneste loops? — het *waaróm* achter module 7

Dit is de module waar "een paar regels code" verandert in "iets dat een mens niet
meer met de hand zou willen doen". Daar zit precies de waarde van een tool.

## 1. Sommige vragen gaan over paren, niet over losse items

"Heeft deze toets genoeg surveillanten?" gaat over één item — één gewone loop is
genoeg. Maar "staat iemand dubbelgeboekt?" gaat over de **relatie tussen twee
items**. Zulke vragen — conflicten, overlap, botsingen — vragen om elk paar te
bekijken. Daarvoor is de geneste loop het gereedschap.

## 2. Het rekenwerk groeit snel — goed om te beseffen

Bij 5 diensten zijn er 10 paren. Bij 100 diensten al bijna 5.000. Bij 1.000 bijna
een half miljoen. Het aantal paren groeit veel sneller dan het aantal diensten. Voor
een mens onbegonnen werk; voor een computer zo gebeurd — maar het verklaart wél
waarom een optimalisatie-tool (fase 3) slimmer te werk moet gaan dan "probeer alles".
Houd dit gevoel vast; het komt terug.

## 3. Functie + loop = leesbare macht

Merk op hoe net het hoofdstuk leest:

```python
if heeft_conflict(a, b):
    print("CONFLICT...")
```

Alle ingewikkeldheid van "wat is een conflict" zit veilig weggestopt in
`heeft_conflict` (module 6). De geneste loop hoeft alleen nog te zeggen *welke* paren
hij langsloopt. Dat samenspel — functies die details verbergen, loops die ze
toepassen — is hoe grote, leesbare programma's in elkaar zitten. Je kunt zo'n
programma straks van de AI *lezen*, omdat het in deze herkenbare lagen is opgebouwd.

---

## De valkuil: `i + 1` en vergelijken met jezelf

```python
for i in range(len(rooster)):
    for j in range(i + 1, len(rooster)):   # <- waarom i + 1?
```

Twee fouten die `i + 1` voorkomt:
1. **Jezelf vergelijken** (`i == j`): een dienst is altijd "in conflict" met
   zichzelf. Zonder bescherming zou élke dienst een vals conflict opleveren.
2. **Dubbel tellen**: paar (1, 3) en (3, 1) zijn hetzelfde paar. `i + 1` zorgt dat je
   elk paar precies één keer ziet.

Dit is het soort detail dat in AI-gegenereerde code zómaar misgaat — een model
schrijft soms `range(len(...))` voor de binnenste loop en telt alles dubbel. Wie het
mechaniek snapt, ziet zo'n fout bij het lezen. Dat is jouw rol.

---

## Termen van vandaag

| Term | Betekenis |
|------|-----------|
| geneste loop | een loop binnen een loop (een loop in een loop) |
| `range(n)` | de getallen 0 t/m n-1, om mee te tellen |
| `range(start, stop)` | de getallen van `start` t/m `stop - 1` |
| paren | combinaties van twee items uit een lijst |

---

## Je bent klaar met fase 1 🎉

Variabelen, lijsten, dicts, loops, condities, functies, geneste loops — dat is het
hele fundament. Vanaf nu ga je dit niet alleen schrijven, maar ook **AI-code ermee
lezen en beoordelen**. Eerst nog één ding: dat fundament inzetten in een echt
projectje. Door naar **Project 1**.
