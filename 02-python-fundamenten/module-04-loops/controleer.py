# Controleer je werk: module 4 (loops)
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

TITEL = "Controle van module 4 (loops)"
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


# --- de vier stappen --------------------------------------------------------

def stap_1(regels):
    """Het voorgedane voorbeeld: drie lokalen in gebruik."""
    for lokaal in ["A1.04", "B2.10", "C0.21"]:
        if not bevat(regels, "lokaal in gebruik", lokaal):
            return False, [
                "Dit stukje stond al voor je klaar, maar ik zie het niet terug.",
                "Is er bovenin opdracht.py per ongeluk iets veranderd of weggehaald?",
            ]
    return True, []


def stap_2(regels):
    """Elke surveillant krijgt een regel die met 'Ingepland:' begint."""
    namen = ["Jansen", "De Vries", "Bakker", "Smit"]
    ontbreekt = [n for n in namen if not bevat(regels, "ingepland:", n)]

    if not ontbreekt:
        return True, []
    if len(ontbreekt) == len(namen):
        return False, [
            'Ik zie nog geen enkele regel die met "Ingepland:" begint.',
            "Staat de loop er al, en springen de regels eronder in?",
        ]
    return False, [
        "Ik mis nog: " + ", ".join(ontbreekt) + ".",
        "Kijk nog eens naar je loop: komt elke surveillant aan de beurt?",
    ]


def stap_3(regels):
    """Het opgetelde aantal studenten staat ergens in de uitvoer."""
    totaal = sum([30, 24, 45, 18])
    if any(re.search(r"\b" + str(totaal) + r"\b", regel) for regel in regels):
        return True, []
    return False, [
        "Ik zie nog geen kloppend totaal in de uitvoer.",
        "Begint je teller op 0 voordat de loop start, en print je hem erna?",
    ]


def stap_4(regels):
    """Per toets een regel met het lokaal en het aantal studenten erin."""
    toetsen = [("A1.04", "30"), ("B2.10", "24"), ("C0.21", "45")]
    ontbreekt = [
        lokaal for lokaal, aantal in toetsen
        if not bevat(regels, lokaal, "zitten", aantal, "studenten")
    ]

    if not ontbreekt:
        return True, []
    if len(ontbreekt) == len(toetsen):
        return False, [
            'Ik zie nog geen regel in de vorm "In ... zitten ... studenten".',
            "Loop je door de lijst, en haal je binnen de loop beide waarden uit de dict?",
        ]
    return False, [
        "Ik mis nog de regel voor: " + ", ".join(ontbreekt) + ".",
        "Krijgt elke toets in de lijst zijn eigen beurt?",
    ]


STAPPEN = [
    ("Stap 1: het voorbeeld draait", stap_1),
    ("Stap 2: elke surveillant ingepland", stap_2),
    ("Stap 3: het totaal aantal studenten", stap_3),
    ("Stap 4: lokaal en aantal per toets", stap_4),
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
