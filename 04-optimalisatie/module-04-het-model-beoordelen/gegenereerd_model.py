"""Maakt het goedkoopste surveillance-rooster met een solver.

Geschreven door een AI-assistent op de opdracht:
"maak een zo goedkoop mogelijk rooster dat aan de regels voldoet".
"""
import pandas as pd
from ortools.sat.python import cp_model

DIENSTDUUR = 3
SPECIALISTTARIEF = 150
LAB_TOETSEN = ["T3"]

toetsen = pd.read_csv("../../voorbeelddata/toetsen.csv")
medewerkers = pd.read_csv("../../voorbeelddata/medewerkers.csv")
bevoegdheden = pd.read_csv("../../voorbeelddata/bevoegdheden.csv")

mensen = list(medewerkers["naam"])
tarief = dict(zip(medewerkers["naam"], medewerkers["uurtarief"]))
soort = dict(zip(medewerkers["naam"], medewerkers["type"]))
lab_ok = set(bevoegdheden[bevoegdheden["lab_bevoegd"] == "ja"]["naam"])
toets_ids = list(toetsen["toets_id"])
tijd = dict(zip(toetsen["toets_id"], toetsen["tijd"]))
nodig = dict(zip(toetsen["toets_id"], toetsen["vereist_toezicht"]))


def kosten(p, t):
    if t in LAB_TOETSEN and soort[p] == "extern":
        return SPECIALISTTARIEF * DIENSTDUUR
    return tarief[p] * DIENSTDUUR


model = cp_model.CpModel()
x = {(p, t): model.NewBoolVar(f"x_{p}_{t}") for p in mensen for t in toets_ids}

# Dekking: elke toets het vereiste aantal surveillanten
for t in toets_ids:
    model.Add(sum(x[p, t] for p in mensen) == int(nodig[t]))

# Geen dubbelboeking: niemand op twee toetsen op hetzelfde tijdslot
for p in mensen:
    for moment in set(tijd.values()):
        model.Add(sum(x[p, t] for t in toets_ids if tijd[t] == moment) <= 1)

# Geschiktheid: op een lab-toets alleen lab-bevoegden
for p in mensen:
    for t in LAB_TOETSEN:
        if p not in lab_ok:
            model.Add(x[p, t] == 0)

# Doelfunctie: zo goedkoop mogelijk
model.Minimize(sum(kosten(p, t) * x[p, t] for p in mensen for t in toets_ids))

solver = cp_model.CpSolver()
solver.Solve(model)

print("Gemaakt rooster (goedkoopst gevonden):")
rijen = []
for t in toets_ids:
    for p in mensen:
        if solver.Value(x[p, t]):
            print(f"  {t} ({tijd[t]}): {p}")
            rijen.append({"toets_id": t, "naam": p})
print("Totale inhuurkosten:", int(solver.ObjectiveValue()), "euro")

pd.DataFrame(rijen).to_csv("gemaakt_rooster.csv", index=False)
