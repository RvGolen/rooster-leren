# Module 7 — Lijsten van dicts & geneste loops — OPDRACHT
#
# Vul de #TODO's in. Draai vaak:  python opdracht.py
# Dit is de moeilijkste opdracht van fase 1. Rustig, stap voor stap. Je kunt dit.
# ---------------------------------------------------------------------------


# Gegeven: de conflict-functie uit module 6 (voorgedaan, niet wijzigen)
def heeft_conflict(a, b):
    return a["persoon"] == b["persoon"] and a["tijd"] == b["tijd"]


# Gegeven: een klein rooster als lijst van dicts
rooster = [
    {"persoon": "Jansen",   "tijd": "09:00", "lokaal": "A1.04"},
    {"persoon": "De Vries", "tijd": "09:00", "lokaal": "B2.10"},
    {"persoon": "Jansen",   "tijd": "09:00", "lokaal": "C0.21"},
    {"persoon": "Bakker",   "tijd": "11:00", "lokaal": "A1.04"},
    {"persoon": "De Vries", "tijd": "11:00", "lokaal": "B2.10"},
]


# STAP 1 — Warmdraaien: één gewone loop
# TODO: print voor ELKE dienst in 'rooster' een regel: "<persoon> om <tijd>"

# ... jouw code hier ...


# STAP 2 — range begrijpen
# TODO: print de getallen 0 tot en met len(rooster) - 1 met een loop over range(len(rooster))
#       (zo zie je welke indexen er zijn)

# ... jouw code hier ...


# STAP 3 — De geneste loop: alle paren, elk één keer
# TODO: schrijf twee loops in elkaar:
#         buitenste: for i in range(len(rooster)):
#         binnenste: for j in range(i + 1, len(rooster)):
#       en print binnenin welk paar je vergelijkt, bijv:
#         "vergelijk", rooster[i]["persoon"], "met", rooster[j]["persoon"]
#       Voorspel eerst: hoeveel vergelijkingen worden dit?

# ... jouw code hier ...


# STAP 4 — Conflicten vinden
# TODO: breid stap 3 uit: roep BINNENIN heeft_conflict(rooster[i], rooster[j]) aan,
#       en print alleen iets als die True is, bijvoorbeeld:
#         "CONFLICT: <persoon> om <tijd>"
#       Klopt het aantal gevonden conflicten met wat je met de hand telt?

# ... jouw code hier ...


# KLAAR? Draai het bestand, controleer je conflicten met de hand, en ga naar check.md.
# Daarna: je eerste echte project!
