# Eindproject — Optimaliseer het surveillance-rooster
#
# Dit is een REGIE-opdracht. Je bouwt het solver-model niet zelf; je laat Cursor
# het schrijven, in kleine stappen, en jij LEEST en BEOORDEELT elke stap.
#
# Werkwijze (in Cursor):
#   1. Zet Cursor in PLAN-modus en beschrijf de opdracht: een zo goedkoop mogelijk
#      rooster maken dat aan ALLE VIJF de regels voldoet (dekking, capaciteit,
#      beschikbaarheid, dubbelboeking, geschiktheid).
#   2. Laat Cursor het model stap voor stap opbouwen. Lees elke diff. Vraag bij elke
#      constraint: "welke van mijn vijf regels is dit?".
#   3. LET OP het gat uit module 4: controleer expliciet dat de beschikbaarheids-
#      constraint erin zit.
#   4. Draai het, schrijf de uitkomst naar 'gemaakt_rooster.csv', en laat je
#      validator (hieronder) los. Doel: 0 overtredingen EN minimale kosten (1755).
# ---------------------------------------------------------------------------
import pandas as pd
import data
import regels

# --- Hier laat je Cursor het model bouwen dat 'gemaakt_rooster.csv' produceert. ---
# (jouw gestuurde code / Cursor's code komt hier)


# --- Controle achteraf (voorgedaan): jouw validator over het resultaat ---
def controleer(pad="gemaakt_rooster.csv"):
    gemaakt = pd.read_csv(pad)
    toetsen = data.lees_toetsen()
    beschikbaarheid, bevoegdheden = data.lees_beschikbaarheid(), data.lees_bevoegdheden()
    # Capaciteit gaat over wélk lokaal een toets heeft — dat ligt vast in de
    # data en kun je niet veranderen door anders toe te wijzen. Hier checken we
    # de vier toewijzings-regels: welke surveillant staat op welke toets?
    meldingen = (
        regels.controleer_dekking(toetsen, gemaakt)
        + regels.controleer_beschikbaarheid(toetsen, gemaakt, beschikbaarheid=beschikbaarheid)
        + regels.controleer_dubbelboeking(toetsen, gemaakt)
        + regels.controleer_geschiktheid(toetsen, gemaakt, bevoegdheden)
    )
    print("Overtredingen:", len(meldingen))
    for m in meldingen:
        print(" -", m)
    return meldingen
