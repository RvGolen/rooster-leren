# Project 1 — Vind alle conflicten in een rooster
#
# Lees eerst lees-mij.md. Draai dit bestand met:  python opdracht.py
#
# Dit is je eigen fundament toepassen. De #TODO's wijzen de weg; de oplossing
# bedenk je zelf (met je tutor in Ask-modus als je vastloopt).
# ===========================================================================


# --- Gegeven: de conflict-regel (uit module 6). Lees 'm, snap je 'm nog? ---
def heeft_conflict(a, b):
    # Conflict = zelfde persoon EN zelfde tijd -> die staat op twee plekken
    return a["persoon"] == b["persoon"] and a["tijd"] == b["tijd"]


# --- Gegeven: een voorbeeldrooster (VOORBEELD-data, geen echte personen) ---
# Elk item is een 'dienst': wie, wanneer, waar.
rooster = [
    {"persoon": "Jansen",   "tijd": "09:00", "lokaal": "A1.04"},
    {"persoon": "De Vries", "tijd": "09:00", "lokaal": "B2.10"},
    {"persoon": "Bakker",   "tijd": "09:00", "lokaal": "C0.21"},
    {"persoon": "Jansen",   "tijd": "09:00", "lokaal": "D1.15"},   # Jansen om 09:00 dubbel?
    {"persoon": "De Vries", "tijd": "11:00", "lokaal": "A1.04"},
    {"persoon": "Bakker",   "tijd": "11:00", "lokaal": "B2.10"},
    {"persoon": "De Vries", "tijd": "11:00", "lokaal": "C0.21"},   # De Vries om 11:00 dubbel?
]
# VOORSPEL eerst (op papier): hoeveel conflicten zitten hierin, en welke?


# --- STAP 1: bouw de zoeker -------------------------------------------------
# TODO: schrijf een functie 'vind_conflicten(rooster)' die met een GENESTE LOOP
#       (module 7) elk paar diensten vergelijkt met heeft_conflict, en voor elk
#       gevonden conflict een duidelijke regel print, bijvoorbeeld:
#         "CONFLICT: De Vries staat om 11:00 in A1.04 en C0.21"
#
#       Denk aan:
#         - buitenste loop: for i in range(len(rooster)):
#         - binnenste loop: for j in range(i + 1, len(rooster)):  (waarom i + 1?)
#         - de velden "persoon", "tijd", "lokaal" uit elke dienst

def vind_conflicten(rooster):
    # ... jouw code hier ...
    pass   # <- verwijder deze regel zodra je je eigen code hebt geschreven


# --- STAP 2: roep je functie aan -------------------------------------------
# TODO: roep vind_conflicten(rooster) aan, zodat het script de conflicten print.

# ... jouw code hier ...


# --- STAP 3: netjes afronden -----------------------------------------------
# TODO: zorg dat het programma, als er GEEN conflicten zijn, één duidelijke regel
#       print zoals: "Geen conflicten gevonden - het rooster is conflictvrij."
#       (Tip: tel in je functie hoeveel conflicten je vond, en beslis daarna.)


# ===========================================================================
# OPTIONELE UITBREIDING (alleen als je zin hebt — niet verplicht)
# ---------------------------------------------------------------------------
# - Laat vind_conflicten het AANTAL conflicten teruggeven met 'return', en print
#   dat aantal apart: "3 conflict(en) gevonden."
# - Voeg een dienst toe die GEEN conflict is en eentje die het WEL is, en
#   controleer of je programma het nog goed ziet.
# - Denk na (nog niet bouwen): welke ANDERE regel uit jouw werk zou je hierna willen
#   controleren? Capaciteit? Beschikbaarheid? Schrijf 'm in gewone taal op in
#   voortgang.md - in fase 2 ga je zulke regels echt inbouwen.
