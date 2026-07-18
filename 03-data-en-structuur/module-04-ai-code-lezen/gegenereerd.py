"""Controleert of elke toets voldoende surveillanten heeft.

Geschreven door een AI-assistent op de opdracht:
"controleer of elke toets genoeg surveillanten heeft".
"""
import pandas as pd

toetsen = pd.read_csv("../../voorbeelddata/toetsen.csv")
rooster = pd.read_csv("../../voorbeelddata/rooster.csv")

# Tel per toets hoeveel surveillanten er zijn ingeroosterd
aantal_per_toets = rooster.groupby("toets_id").size()

print("Controle op dekking\n")

for toets_id, aantal in aantal_per_toets.items():
    vereist = toetsen[toetsen["toets_id"] == toets_id]["vereist_toezicht"].iloc[0]
    if aantal < vereist:
        print(f"PROBLEEM: {toets_id} heeft {aantal} surveillanten, maar {vereist} nodig")
    else:
        print(f"ok: {toets_id} heeft {aantal} van {vereist}")

print("\nControle afgerond.")
