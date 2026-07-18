# Module 3 — Filteren en tellen met pandas — OPDRACHT
#
# Vul de #TODO's in. Draai vaak:  python opdracht.py
# Belangrijk: draai dit bestand vanuit DEZE map (module-03-pandas-filteren-tellen),
# anders vindt Python ../../voorbeelddata/... niet.
# ---------------------------------------------------------------------------

import pandas as pd

toetsen = pd.read_csv("../../voorbeelddata/toetsen.csv")


# STAP 1 — Filteren: welke toetsen hebben meer dan 100 studenten?
# Voorspel eerst: hoeveel van de 8 toetsen denk je dat er overblijven?
# TODO: maak 'groot' met alle rijen uit 'toetsen' waar aantal_studenten > 100.
#       Print 'groot' daarna.

# ... jouw code hier ...


# STAP 2 — Tellen: hoeveel toetsen zijn er per tijdslot?
# Voorspel: hoeveel verschillende tijdsloten verwacht je, en hoeveel toetsen elk?
# TODO: gebruik value_counts() op de kolom "tijd" en print het resultaat.

# ... jouw code hier ...


# STAP 3 — Rooster inlezen en tellen per persoon
# Voorspel: wie denk je dat de meeste diensten heeft, als je rooster.csv bekijkt?
# TODO: lees "../../voorbeelddata/rooster.csv" in met pd.read_csv en sla het op
#       in 'rooster'. Tel daarna met value_counts() hoeveel diensten elke naam
#       heeft, en print het resultaat.

# ... jouw code hier ...


# STAP 4 — Groeperen: hoeveel surveillanten staan er per toets?
# Voorspel: er zijn 8 toetsen in toetsen.csv. Hoeveel regels verwacht je hier?
# TODO: groepeer 'rooster' op "toets_id" en tel per groep het aantal rijen met
#       .size(). Print het resultaat.

# ... jouw code hier ...


# KLAAR? Vergelijk je uitkomst bij STAP 4 met de 8 toetsen in toetsen.csv.
# Klopt het aantal regels? Schrijf op wat je opvalt, en ga naar check.md.
