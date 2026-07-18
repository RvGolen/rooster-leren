# Module 6 — Functies — OPDRACHT
#
# Vul de #TODO's in. Draai na elke stap:  python opdracht.py
# Je bouwt hier je eerste echte rooster-functie. Rustig, stap voor stap.
# ---------------------------------------------------------------------------


# STAP 1 — Een functie definiëren en aanroepen (voorgedaan)
def kosten(uren, tarief):
    return uren * tarief

print("Stap 1 - kosten van 3 uur a 28.50:", kosten(3, 28.50))


# STAP 2 — Zelf een functie schrijven
# TODO: schrijf een functie 'past_in_lokaal(studenten, capaciteit)'
#       die True teruggeeft als studenten <= capaciteit, anders False.
#       (denk aan def, de dubbele punt, inspringen, en return)

# ... jouw code hier ...

# Test (haal de # weg zodra je functie bestaat):
# print("Stap 2:", past_in_lokaal(30, 40))   # verwacht: True
# print("Stap 2:", past_in_lokaal(55, 40))   # verwacht: False


# STAP 3 — heeft_conflict, deel 1: de twee deelvragen
# Een dienst is een dict met "persoon", "tijd" en "lokaal".
# We bouwen het conflict-idee in stukjes op.
#
# TODO: schrijf een functie 'zelfde_persoon(a, b)' die True teruggeeft als
#       a["persoon"] gelijk is aan b["persoon"].
# TODO: schrijf een functie 'zelfde_tijd(a, b)' die True teruggeeft als
#       a["tijd"] gelijk is aan b["tijd"].

# ... jouw code hier ...


# STAP 4 — heeft_conflict, deel 2: combineren
# TODO: schrijf 'heeft_conflict(a, b)' die True teruggeeft als de twee diensten
#       ZOWEL dezelfde persoon ALS dezelfde tijd hebben.
#       Tip: je mag je functies uit stap 3 hier hergebruiken, met 'and' ertussen.

# ... jouw code hier ...


# STAP 5 — Uitproberen
dienst1 = {"persoon": "Jansen", "tijd": "09:00", "lokaal": "A1.04"}
dienst2 = {"persoon": "Jansen", "tijd": "09:00", "lokaal": "B2.10"}
dienst3 = {"persoon": "De Vries", "tijd": "09:00", "lokaal": "C0.21"}
# TODO: print heeft_conflict(dienst1, dienst2)   # verwacht je True of False?
# TODO: print heeft_conflict(dienst1, dienst3)   # en hier?
#       Voorspel het antwoord VOORDAT je draait.

# ... jouw code hier ...


# KLAAR? Draai het bestand en ga naar check.md.
