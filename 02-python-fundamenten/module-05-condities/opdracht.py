# Module 5 — Condities — OPDRACHT
#
# Vul de #TODO's in. Draai na elke stap:  python opdracht.py
# LET OP: == (vergelijken) is iets anders dan = (toewijzen).
# ---------------------------------------------------------------------------


# STAP 1 — Een simpele if/else (voorgedaan)
studenten = 45
capaciteit = 40
if studenten > capaciteit:
    print("Stap 1 - past niet in dit lokaal")
else:
    print("Stap 1 - past")


# STAP 2 — Zelf een voorwaarde schrijven
aantal_surveillanten = 1
# TODO: schrijf een if/else die print "te weinig" als er minder dan 2
#       surveillanten zijn, en anders "voldoende".
#       (kleiner-dan is het teken <)

# ... jouw code hier ...


# STAP 3 — Drie gevallen met elif
beschikbaar = 3   # hoeveel surveillanten beschikbaar zijn
nodig = 3         # hoeveel er nodig zijn
# TODO: schrijf if / elif / else die print:
#   - "tekort"   als beschikbaar < nodig
#   - "precies goed"  als beschikbaar == nodig   (let op: ==)
#   - "over"     in alle andere gevallen

# ... jouw code hier ...


# STAP 4 — Loop + if samen (spiraal)
toetsen = [
    {"lokaal": "A1.04", "studenten": 30, "capaciteit": 40},
    {"lokaal": "B2.10", "studenten": 55, "capaciteit": 40},
    {"lokaal": "C0.21", "studenten": 40, "capaciteit": 40},
]
# TODO: loop door 'toetsen'. Print voor elke toets of de studenten in het lokaal
#       PASSEN (studenten <= capaciteit) of NIET.
#       Bijvoorbeeld: "B2.10: PAST NIET (55 > 40)"

# ... jouw code hier ...


# KLAAR? Draai het bestand en ga naar check.md.
