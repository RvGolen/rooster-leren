"""Een MINI-voorbeeld van een solver-model. Twee toetsen, drie mensen.
Draai het:  python mini_model.py
Doel: de drie bouwstenen zien — beslissingsvariabele, constraint, objective.
"""
from ortools.sat.python import cp_model

mensen = ["Anna", "Ben", "Carla"]
kosten = {"Anna": 40, "Ben": 38, "Carla": 90}   # per dienst (voorbeeld)
toetsen = ["ochtend", "middag"]                  # twee toetsen, elk 1 persoon nodig

model = cp_model.CpModel()

# 1) BESLISSINGSVARIABELE: staat persoon p op toets t? (ja=1 / nee=0)
x = {(p, t): model.NewBoolVar(f"{p}_{t}") for p in mensen for t in toetsen}

# 2) CONSTRAINTS (harde regels):
#    - elke toets heeft precies 1 persoon
for t in toetsen:
    model.Add(sum(x[p, t] for p in mensen) == 1)
#    - niemand op beide toetsen tegelijk (hier: max 1 toets per persoon)
for p in mensen:
    model.Add(sum(x[p, t] for t in toetsen) <= 1)

# 3) OBJECTIVE (doelfunctie): zo goedkoop mogelijk
model.Minimize(sum(kosten[p] * x[p, t] for p in mensen for t in toetsen))

solver = cp_model.CpSolver()
solver.Solve(model)

print("Goedkoopste toewijzing:")
for t in toetsen:
    for p in mensen:
        if solver.Value(x[p, t]):
            print(f"  {t}: {p} (kosten {kosten[p]})")
print("Totale kosten:", int(solver.ObjectiveValue()))
