# Module 2 — Pandas: de tabel-bril — OPDRACHT
#
# Vul de #TODO's in. Draai vaak:  python opdracht.py
# Belangrijk: draai dit bestand vanuit DEZE map (module-02-pandas-kennismaken),
# anders vindt Python ../../voorbeelddata/toetsen.csv niet.
# Nog geen pandas geinstalleerd? Zie het setup-kader bovenaan les.md.
# ---------------------------------------------------------------------------

import pandas as pd


# STAP 1 — Het bestand inlezen
# Voorspel eerst: als dit werkt, wat voor soort ding is 'toetsen' dan?
# TODO: lees "../../voorbeelddata/toetsen.csv" in met pd.read_csv(...) en sla
#       het resultaat op in 'toetsen'.
toetsen = None


# STAP 2 — Kolomnamen en aantal rijen
# Voorspel: welke kolomnamen verwacht je? En hoeveel rijen heeft toetsen.csv?
# TODO: print toetsen.columns
# TODO: print len(toetsen)

# ... jouw code hier ...


# STAP 3 — De eerste 3 rijen
# Voorspel: welke 3 toetsen zie je als eerste?
# TODO: print toetsen.head(3)

# ... jouw code hier ...


# STAP 4 — Ook lokalen.csv inlezen
# Voorspel: werkt dezelfde truc (pd.read_csv) ook op een ander CSV-bestand?
# TODO: lees "../../voorbeelddata/lokalen.csv" in pandas in, sla op in 'lokalen',
#       en print de hele tabel.

# ... jouw code hier ...


# STAP 5 — Totaal aantal studenten
# Voorspel: hoeveel studenten denk je dat er in totaal een toets maken?
# TODO: print toetsen["aantal_studenten"].sum() — let op: GEEN int(...) nodig,
#       dat deed pandas al voor je bij het inlezen.

# ... jouw code hier ...


# KLAAR? Controleer je uitkomsten met de hand tegen toetsen.csv en lokalen.csv,
# en ga naar check.md.
