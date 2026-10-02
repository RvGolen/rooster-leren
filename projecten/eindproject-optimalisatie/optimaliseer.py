# Eindproject: optimaliseer het surveillance-rooster
#
# Dit is een REGIE-opdracht. Je bouwt het solver-model niet zelf; je laat Cursor
# het schrijven, in kleine stappen, en jij LEEST en BEOORDEELT elke stap.
#
# Werkwijze (in Cursor):
#   1. Zet Cursor in PLAN-modus en beschrijf de opdracht: een zo goedkoop mogelijk
#      rooster maken dat aan de VIER toewijzings-regels voldoet (dekking,
#      beschikbaarheid, dubbelboeking, geschiktheid). Capaciteit hoort niet in het
#      model: welk lokaal een toets heeft, ligt vast in de data.
#   2. Laat Cursor het model stap voor stap opbouwen. Lees elke diff. Vraag bij elke
#      constraint: "welke van mijn vier toewijzings-regels is dit?".
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
    import os
    if not os.path.exists(pad):
        print(f"⚠️  '{pad}' bestaat nog niet. Laat Cursor eerst het model bouwen")
        print("    (het gedeelte hierboven) zodat het rooster wordt weggeschreven.")
        return []
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


# Draai je de validator door 'python optimaliseer.py' te typen, dan checkt hij
# hieronder automatisch het rooster dat je model zojuist heeft weggeschreven.
if __name__ == "__main__":
    controleer()
