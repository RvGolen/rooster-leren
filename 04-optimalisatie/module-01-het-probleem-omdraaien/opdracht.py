# Module 1 — Het probleem omdraaien — OPDRACHT
#
# Draai vanuit deze map:  python opdracht.py   (of python3)
# Je berekent de INHUURKOSTEN van het gegeven rooster. Dat is de "doelfunctie"
# die we straks zo laag mogelijk willen maken.
# ---------------------------------------------------------------------------
import pandas as pd

DIENSTDUUR = 3          # uur (voorbeeld-aanname)
SPECIALISTTARIEF = 150  # een lab-bevoegde EXTERN op een lab-toets (euro/uur)
LAB_TOETSEN = ["T3"]    # deze toets vereist een lab-bevoegde surveillant

medewerkers = pd.read_csv("../../voorbeelddata/medewerkers.csv")
rooster = pd.read_csv("../../voorbeelddata/rooster.csv")

# STAP 1 (voorgedaan): een opzoek-tabel naam -> (uurtarief, type)
tarief = dict(zip(medewerkers["naam"], medewerkers["uurtarief"]))
soort = dict(zip(medewerkers["naam"], medewerkers["type"]))
print("Stap 1 - tarief van Jansen:", tarief["Jansen"], "| type:", soort["Jansen"])

# STAP 2 — kosten van EEN dienst
# TODO: schrijf een functie kosten_dienst(naam, toets_id) die teruggeeft:
#       uurtarief * DIENSTDUUR
#       MAAR: als toets_id in LAB_TOETSEN zit EN de persoon 'extern' is,
#       reken dan met SPECIALISTTARIEF in plaats van het gewone uurtarief.
# Voorspel: wat kost Peters (extern, 75) op een gewone toets? En Van Dijk op T3?

# ... jouw code hier ...

# STAP 3 — totale kosten van het rooster
# TODO: loop over alle rijen van 'rooster' (kolommen: toets_id, naam) en tel
#       de kosten van elke dienst bij elkaar op. Print het totaal.
# (Tip: for _, rij in rooster.iterrows():  geeft je rij["naam"] en rij["toets_id"])

# ... jouw code hier ...

# KLAAR? Ga naar check.md.
