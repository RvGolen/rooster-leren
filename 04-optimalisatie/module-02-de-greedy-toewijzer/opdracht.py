# Module 2 — De greedy-toewijzer — OPDRACHT
#
# Draai vanuit deze map:  python opdracht.py
# Je bouwt zelf een simpele toewijzer die per toets de goedkoopste beschikbare
# mensen pakt. Daarna laat je je eigen validator (uit fase 2) erop los.
# ---------------------------------------------------------------------------
import pandas as pd
import data
import regels

DIENSTDUUR = 3
SPECIALISTTARIEF = 150
LAB_TOETSEN = ["T3"]

toetsen = data.lees_toetsen()
medewerkers = data.lees_medewerkers()

tarief = dict(zip(medewerkers["naam"], medewerkers["uurtarief"]))
soort = dict(zip(medewerkers["naam"], medewerkers["type"]))
lab_ok = set(data.lees_bevoegdheden().query("lab_bevoegd == 'ja'")["naam"])
besch = data.lees_beschikbaarheid()
vrij = {(r["naam"], r["tijd"]) for _, r in besch.iterrows() if r["beschikbaar"] == "ja"}


def kosten_dienst(naam, toets_id):
    # (voorgedaan — je maakte dit in module 1)
    if toets_id in LAB_TOETSEN and soort[naam] == "extern":
        return SPECIALISTTARIEF * DIENSTDUUR
    return tarief[naam] * DIENSTDUUR


# STAP 1 — wie mag deze toets doen, en is beschikbaar?
# TODO: schrijf een functie mag_en_beschikbaar(naam, toets_id, tijd) die True geeft
#       als de persoon vrij is op 'tijd' EN (de toets geen lab-toets is OF de persoon
#       lab-bevoegd is).

# ... jouw code hier ...


# STAP 2 — de greedy: pak per toets de goedkoopste beschikbare mensen
# TODO: bouw een lijst 'toewijzing' van (toets_id, naam)-paren:
#   - loop over elke toets (rij in 'toetsen': toets_id, tijd, vereist_toezicht)
#   - verzamel de kandidaten die mag_en_beschikbaar zijn
#   - sorteer ze op kosten_dienst(naam, toets_id)
#   - neem de goedkoopste 'vereist_toezicht' mensen
# LET OP: kijk (nog) NIET of iemand al op een andere toets op dat tijdslot staat.
#         Dat is expres — je gaat straks zien wat er dan misgaat.

toewijzing = []
# ... jouw code hier ...


# STAP 3 — reken de totale kosten uit en toon de toewijzing
# TODO: print de toewijzing en de som van kosten_dienst over alle paren.

# ... jouw code hier ...


# STAP 4 — laat je EIGEN validator los op je greedy-rooster
# We schrijven je toewijzing naar een DataFrame met dezelfde vorm als rooster.csv
# en halen er de vier fase-2-regels + de nieuwe geschiktheidsregel overheen.
greedy_rooster = pd.DataFrame(toewijzing, columns=["toets_id", "naam"])
lokalen = data.lees_lokalen()
bevoegdheden = data.lees_bevoegdheden()

alle_meldingen = (
    regels.controleer_dekking(toetsen, greedy_rooster)
    + regels.controleer_capaciteit(toetsen, lokalen)
    + regels.controleer_beschikbaarheid(toetsen, greedy_rooster, beschikbaarheid=besch)
    + regels.controleer_dubbelboeking(toetsen, greedy_rooster)
    + regels.controleer_geschiktheid(toetsen, greedy_rooster, bevoegdheden)
)
print("\nValidator op je greedy-rooster:")
for m in alle_meldingen:
    print(" -", m)
if not alle_meldingen:
    print(" (geen overtredingen)")

# KLAAR? Zie je een DUBBELBOEKING verschijnen? Lees check.md.
