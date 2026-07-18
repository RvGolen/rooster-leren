# Module 4 — Het model beoordelen — OPDRACHT
#
# Draai eerst het gegenereerde model:  python gegenereerd_model.py
# Dat schrijft 'gemaakt_rooster.csv'. Daarna laat je JOUW validator erop los.
# ---------------------------------------------------------------------------
import pandas as pd
import data
import regels

# STAP 1 — VOORSPEL (als commentaar)
# TODO: het model meldt kosten van 1632 euro — goedkoper dan je greedy (1980).
#       Te mooi om waar te zijn? Welke van je VIJF regels zou het kunnen negeren?

# STAP 2 — LEES (als commentaar)
# TODO: loop het model regel voor regel na. Welke constraint zie je voor dekking?
#       Voor dubbelboeking? Voor geschiktheid? En... zie je er één voor
#       BESCHIKBAARHEID? Wordt beschikbaarheid.csv überhaupt ingelezen?

# STAP 3 — BEWIJS het met je validator
toetsen = data.lees_toetsen()
lokalen = data.lees_lokalen()
beschikbaarheid = data.lees_beschikbaarheid()
bevoegdheden = data.lees_bevoegdheden()
gemaakt = pd.read_csv("gemaakt_rooster.csv")

meldingen = (
    regels.controleer_dekking(toetsen, gemaakt)
    + regels.controleer_capaciteit(toetsen, lokalen)
    + regels.controleer_beschikbaarheid(toetsen, gemaakt, beschikbaarheid=beschikbaarheid)
    + regels.controleer_dubbelboeking(toetsen, gemaakt)
    + regels.controleer_geschiktheid(toetsen, gemaakt, bevoegdheden)
)
print("Validator op het gemaakte rooster:")
for m in meldingen:
    print(" -", m)

# STAP 4 — BEOORDEEL (als commentaar)
# TODO: welke overtreding meldt de validator? Klopt je voorspelling uit stap 1?
# TODO: het model is goedkoper OMDAT het een regel negeert. Leg uit waarom
#       "goedkoper" hier niet "beter" betekent.
# TODO: hoe zou je Cursor bijsturen? Schrijf de instructie die je hem zou geven
#       om de ontbrekende constraint toe te voegen. (Je schrijft de code NIET zelf.)
