# Controleer je werk: module 5 (condities)
#
# Draai dit bestand als je denkt dat je klaar bent:
#
#     python controleer.py        (of:  python3 controleer.py )
#
# Wat het doet: het draait jouw opdracht.py apart, vangt op wat er op het scherm
# verschijnt, en kijkt of daar per stap in staat wat de opdracht belooft.
#
# Wat het NIET doet: naar je code kijken. Er zijn meerdere goede manieren om
# hetzelfde te printen, en die zijn allemaal goed. Het gaat om het resultaat.
#
# Je hoeft dit bestand niet te begrijpen. Je mag het gerust lezen, maar het
# vertelt je niet welke code je moet typen. Dat blijft aan jou.
# ---------------------------------------------------------------------------

import os
import re
import subprocess
import sys

TITEL = "Controle van module 5 (condities)"
HIER = os.path.dirname(os.path.abspath(__file__))
OPDRACHT = os.path.join(HIER, "opdracht.py")
TIJDSLIMIET = 10


# --- jouw opdracht.py draaien ----------------------------------------------

def draai_opdracht():
    """Draait opdracht.py als los programma. Geeft (uitvoer, foutmelding)."""
    if not os.path.exists(OPDRACHT):
        print("Ik kan geen opdracht.py vinden naast dit bestand.")
        print("Open in Cursor de map van deze module en draai het daar opnieuw.")
        sys.exit(1)

    omgeving = dict(os.environ, PYTHONIOENCODING="utf-8")
    try:
        resultaat = subprocess.run(
            [sys.executable, "opdracht.py"],
            cwd=HIER,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=TIJDSLIMIET,
            env=omgeving,
        )
    except subprocess.TimeoutExpired:
        print("Je opdracht.py bleef langer dan", TIJDSLIMIET, "seconden draaien.")
        print("Ik heb hem gestopt. Zit er een loop in die nooit ophoudt?")
        sys.exit(1)

    foutmelding = ""
    if resultaat.returncode != 0:
        foutmelding = (resultaat.stderr or "").strip()
        # het volledige pad naar het bestand leest rommelig; de naam is genoeg
        foutmelding = foutmelding.replace(OPDRACHT, "opdracht.py")
    return resultaat.stdout or "", foutmelding


# --- de uitvoer doorzoeken --------------------------------------------------

def opschonen(uitvoer):
    """Uitvoer opknippen in nette regels om mee te vergelijken."""
    schoon = []
    for regel in uitvoer.splitlines():
        samengeperst = re.sub(r"\s+", " ", regel).strip().lower()
        if samengeperst:
            schoon.append(samengeperst)
    return schoon


def bevat(regels, *stukken):
    """Staat er een regel waarin al deze stukken na elkaar voorkomen?"""
    patroon = ".*".join(re.escape(stuk.lower()) for stuk in stukken)
    return any(re.search(patroon, regel) for regel in regels)


def zoek(regels, anker):
    """Geeft de eerste regel waarin dit anker voorkomt, of None."""
    for regel in regels:
        if anker in regel:
            return regel
    return None


# --- de stappen -------------------------------------------------------------

def stap_1(regels):
    """Het voorgedane voorbeeld: 45 studenten passen niet in een lokaal voor 40."""
    if bevat(regels, "stap 1", "past niet"):
        return True, []
    return False, [
        "Dit stukje stond al voor je klaar, maar ik zie het niet terug.",
        "Is er bovenin opdracht.py per ongeluk iets veranderd of weggehaald?",
    ]


def stap_2(regels):
    """Bij dit aantal surveillanten hoort maar een van de twee uitkomsten."""
    if bevat(regels, "te weinig"):
        return True, []
    if bevat(regels, "voldoende"):
        return False, [
            "Je if/else kiest hier de andere tak dan ik verwacht.",
            "Lees de waarde van 'aantal_surveillanten' nog eens, en kijk of je < de goede kant op staat.",
        ]
    return False, [
        "Ik zie nog geen oordeel over het aantal surveillanten.",
        "Staat de if/else er al, en springen de print-regels eronder in?",
    ]


def stap_3(regels):
    """Beschikbaar en nodig zijn hier aan elkaar gelijk."""
    if bevat(regels, "precies goed"):
        return True, []
    if bevat(regels, "tekort") or bevat(regels, "over"):
        return False, [
            "Je keten kiest hier een andere tak dan ik verwacht.",
            "Vergelijk 'beschikbaar' en 'nodig' nog eens: gelijk is iets anders dan kleiner of groter.",
        ]
    return False, [
        "Ik zie nog geen oordeel over beschikbaar tegenover nodig.",
        "Staan alle drie de takken er, en eindigt elke voorwaarde op een dubbele punt?",
    ]


def stap_4(regels):
    """Per toets een oordeel. Let op de toets die er precies in past."""
    verwacht = [("a1.04", False), ("b2.10", True), ("c0.21", False)]
    ontbreekt = []
    verkeerd = []

    for lokaal, hoort_niet_te_passen in verwacht:
        regel = zoek(regels, lokaal)
        if regel is None:
            ontbreekt.append(lokaal.upper())
        elif ("niet" in regel) != hoort_niet_te_passen:
            verkeerd.append(lokaal.upper())

    if not ontbreekt and not verkeerd:
        return True, []

    if len(ontbreekt) == len(verwacht):
        return False, [
            "Ik zie nog geen oordeel per lokaal in de uitvoer.",
            "Loop je door 'toetsen' en print je binnen de loop iets voor elke toets?",
        ]
    if ontbreekt:
        return False, [
            "Ik mis nog een oordeel voor: " + ", ".join(ontbreekt) + ".",
            "Komt elke toets in de lijst aan de beurt?",
        ]
    if "C0.21" in verkeerd:
        return False, [
            "Het oordeel voor " + ", ".join(verkeerd) + " klopt nog niet.",
            "Kijk naar de toets waar het aantal studenten precies gelijk is aan de capaciteit: past dat nog wel?",
        ]
    return False, [
        "Het oordeel voor " + ", ".join(verkeerd) + " klopt nog niet.",
        "Vergelijk je het aantal studenten met de capaciteit van diezelfde toets?",
    ]


STAPPEN = [
    ("Stap 1: het voorbeeld draait", stap_1),
    ("Stap 2: genoeg surveillanten of niet", stap_2),
    ("Stap 3: tekort, precies goed of over", stap_3),
    ("Stap 4: past het per lokaal", stap_4),
]


# --- alles aan elkaar -------------------------------------------------------

def main():
    uitvoer, foutmelding = draai_opdracht()

    print()
    print(TITEL)
    print("=" * len(TITEL))
    print()

    regels = opschonen(uitvoer)
    niets_gedraaid = foutmelding and not regels

    if foutmelding:
        print("⚠️  Python kon je bestand niet helemaal uitvoeren.")
        print("    Dit zegt Python erover:")
        print()
        for regel in foutmelding.splitlines()[-6:]:
            print("      " + regel)
        print()
        print("    In die melding staat een regelnummer. Kijk daar eerst.")
        print("    Snap je de melding niet? Vraag hem na in Ask-modus in Cursor.")
        if not niets_gedraaid:
            print("    Hieronder zie je wel hoe ver je gekomen bent.")
        print()

    if niets_gedraaid:
        # Bij een fout als deze leest Python eerst het hele bestand en draait
        # dan niets. Er is dus geen uitvoer om te beoordelen, en alle stappen
        # afkeuren zou onterecht zijn. Eerst die ene fout oplossen.
        print("Verder kijken heeft nu geen zin: er verscheen nog niets op het")
        print("scherm. Los eerst de fout hierboven op en draai deze controle")
        print("daarna opnieuw.")
        return 1

    goed = 0

    for titel, controle in STAPPEN:
        klopt, hint = controle(regels)
        if klopt:
            goed += 1
            print("✅ " + titel)
        else:
            print("❌ " + titel)
            for zin in hint:
                print("   " + zin)
        print()

    totaal = len(STAPPEN)
    if goed == 1:
        print("1 van de " + str(totaal) + " stappen klopt.")
    else:
        print(str(goed) + " van de " + str(totaal) + " stappen kloppen.")

    if goed == totaal and not foutmelding:
        print()
        print("Mooi. 🎉 Ga nu naar check.md: daar kijk je of je ook snapt")
        print("wat je gedaan hebt. Dat is het deel dat dit bestand niet kan zien.")
        return 0

    print("Pas aan, draai je opdracht.py opnieuw, en probeer deze controle daarna nog eens.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
