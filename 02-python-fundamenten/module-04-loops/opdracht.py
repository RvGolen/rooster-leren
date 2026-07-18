# Module 4 — Loops — OPDRACHT
#
# Vul de #TODO's in. Draai na elke stap:  python opdracht.py
# LET OP: regels binnen een loop moeten INSPRINGEN (vier spaties).
# ---------------------------------------------------------------------------


# STAP 1 — Door een lijst lopen (voorgedaan)
lokalen = ["A1.04", "B2.10", "C0.21"]
for lokaal in lokalen:
    print("Lokaal in gebruik:", lokaal)


# STAP 2 — Zelf een loop schrijven
surveillanten = ["Jansen", "De Vries", "Bakker", "Smit"]
# TODO: schrijf een for-loop die voor ELKE surveillant print:
#       "Ingepland: <naam>"
#   (denk aan de dubbele punt na de for-regel, en aan de inspringing)

# ... jouw code hier ...


# STAP 3 — Tellen met een loop
studenten_per_toets = [30, 24, 45, 18]
# TODO: maak een variabele 'totaal' die op 0 begint
# TODO: schrijf een loop die elk getal bij 'totaal' optelt
# TODO: print na de loop het totaal aantal studenten

# ... jouw code hier ...


# STAP 4 — Loop + dict samen (spiraal: dit gebruik je straks veel)
# Hieronder staat een lijst van toetsen, elk een dict.
toetsen = [
    {"lokaal": "A1.04", "studenten": 30},
    {"lokaal": "B2.10", "studenten": 24},
    {"lokaal": "C0.21", "studenten": 45},
]
# TODO: schrijf een loop die voor elke toets print:
#       "In <lokaal> zitten <studenten> studenten"
#   (binnen de loop heet het huidige item bijvoorbeeld 'toets';
#    haal er dan toets["lokaal"] en toets["studenten"] uit)

# ... jouw code hier ...


# KLAAR? Draai het bestand en ga naar check.md.
