# Module 5 — Een class lezen — OPDRACHT
#
# Vul de #TODO's in. Draai vaak:  python opdracht.py
# De classes hieronder staan er al — jouw werk is lezen, en er klein iets aan
# toevoegen.
# ---------------------------------------------------------------------------


class Lokaal:
    def __init__(self, naam, capaciteit):
        self.naam = naam
        self.capaciteit = capaciteit


class Toets:
    def __init__(self, toets_id, vak, aantal_studenten):
        self.toets_id = toets_id
        self.vak = vak
        self.aantal_studenten = aantal_studenten

    def past_in(self, lokaal):
        return self.aantal_studenten <= lokaal.capaciteit


# STAP 1 — Lees de classes hierboven
# TODO: schrijf hieronder, als commentaarregel (met #), in je eigen woorden wat
#       past_in doet. Welke twee velden vergelijkt hij, en van welk "ding" komt
#       elk veld?

# ... jouw commentaar hier ...


# STAP 2 — Maak zelf een Lokaal en een Toets
# Voorspel eerst: als je een Toets maakt met meer studenten dan de capaciteit
# van je Lokaal, wat print past_in dan?
# TODO: maak een Lokaal met je eigen naam en capaciteit, en een Toets met je
#       eigen toets_id, vak en aantal_studenten. Print het resultaat van
#       past_in.

# ... jouw code hier ...


# STAP 3 — Voeg een veld toe aan Toets
# TODO: voeg in de __init__ van de class Toets hierboven een derde veld toe:
#       vereist_toezicht (een parameter, én de regel
#       self.vereist_toezicht = vereist_toezicht). Maak daarna opnieuw een
#       Toets aan — nu mét vereist_toezicht — en print dat veld.

# ... jouw code hier ...


# STAP 4 — Voeg een methode toe aan Toets
# Voorspel eerst: als vereist_toezicht 2 is en er staan 3 mensen ingezet, wat
# moet genoeg_toezicht dan teruggeven?
# TODO: voeg aan de class Toets hierboven een methode toe:
#       genoeg_toezicht(self, aantal_ingezet)
#       Die geeft True terug als aantal_ingezet groter dan of gelijk is aan
#       self.vereist_toezicht, anders False. Print het resultaat voor je eigen
#       toets uit stap 3.

# ... jouw code hier ...


# KLAAR? Controleer je antwoorden met de hand, en ga naar check.md.
