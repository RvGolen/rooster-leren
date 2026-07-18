# Module 1 — CSV-bestanden inlezen — OPDRACHT
#
# Vul de #TODO's in. Draai vaak:  python opdracht.py
# Belangrijk: draai dit bestand vanuit DEZE map (module-01-csv-inlezen), anders
# vindt Python ../../voorbeelddata/toetsen.csv niet.
# ---------------------------------------------------------------------------

import csv


# STAP 1 — Het bestand inlezen
# Voorspel eerst: als dit werkt, wat voor soort ding is 'toetsen' dan? Een string?
# Eén dict? Een lijst van dicts?
# TODO: maak van 'bestand' een lijst van dicts en sla die op in 'toetsen'.
#       Gebruik: list(csv.DictReader(bestand))
with open("../../voorbeelddata/toetsen.csv", newline="", encoding="utf-8") as bestand:
    toetsen = []


# STAP 2 — Print vak en tijd
# Voorspel: hoeveel regels komen eruit, en wat staat erop?
# TODO: print voor ELKE toets in 'toetsen' een regel: "<vak> om <tijd>"

# ... jouw code hier ...


# STAP 3 — Tellen: hoeveel toetsen zijn er om 09:00?
# Voorspel: hoeveel denk je dat er zijn, als je naar toetsen.csv kijkt?
# TODO: loop door 'toetsen', tel met een if hoeveel er een "tijd" van "09:00"
#       hebben, en print het totaal aan het eind.

# ... jouw code hier ...


# STAP 4 — Tellen: totaal aantal vereiste surveillanten
# Voorspel: wat verwacht je dat het totaal is?
# TODO: loop door 'toetsen' en tel de kolom 'vereist_toezicht' bij elkaar op.
#       Let op: die waarde is TEKST, net als aantal_studenten in de les. Zet hem
#       eerst om met int(...) voordat je optelt. Print het totaal aan het eind.

# ... jouw code hier ...


# KLAAR? Controleer je uitkomsten met de hand tegen toetsen.csv, en ga naar check.md.
