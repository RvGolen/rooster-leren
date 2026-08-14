# Controleer je werk: module 7 (lijsten van dicts)
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

TITEL = "Controle van module 7 (lijsten van dicts)"
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


def bevat_getal(tekst, waarde):
    """Staat dit getal als los getal in de tekst? (24 telt niet als een 2)"""
    getal = "%g" % waarde
    return re.search(r"(?<![\d.])" + re.escape(getal) + r"(?!\d)", tekst) is not None


TIJD = re.compile(r"\b\d{1,2}[:.]\d{2}\b")
NAMEN = ["jansen", "de vries", "bakker"]
DIENSTEN = 5


def tel_namen(regel):
    """Hoe vaak komt er een naam uit het rooster op deze regel voor?"""
    return sum(regel.count(naam) for naam in NAMEN)


def paar_regels(regels):
    """Regels waarop twee diensten met elkaar vergeleken worden."""
    return [
        regel for regel in regels
        if tel_namen(regel) >= 2 and "conflict" not in regel
    ]


def vroege_regels(regels):
    """Alles vóór de eerste vergelijking: daar hoort stap 1 en 2 te staan."""
    for nummer, regel in enumerate(regels):
        if tel_namen(regel) >= 2 or "conflict" in regel:
            return regels[:nummer]
    return regels


# --- de stappen -------------------------------------------------------------

def stap_1(regels):
    """Elke dienst uit het rooster met zijn persoon en tijd."""
    vroeg = vroege_regels(regels)
    diensten = [r for r in vroeg if tel_namen(r) == 1 and TIJD.search(r)]

    if not diensten:
        return False, [
            "Ik zie nog geen regel met een naam en een tijd erin.",
            "Loop je door 'rooster' en print je binnen de loop iets voor elke dienst?",
        ]

    combinaties = [
        ("Jansen", "09:00"), ("De Vries", "09:00"),
        ("Bakker", "11:00"), ("De Vries", "11:00"),
    ]
    ontbreekt = [
        persoon for persoon, tijd in combinaties
        if not any(persoon.lower() in r and tijd in r for r in diensten)
    ]
    if ontbreekt:
        return False, [
            "Ik mis nog een regel voor: " + ", ".join(ontbreekt) + ".",
            "Komt elke dienst in het rooster aan de beurt?",
        ]
    if len(diensten) < DIENSTEN:
        return False, [
            "Ik tel minder regels dan er diensten in het rooster staan.",
            "Twee diensten lijken sterk op elkaar. Slaat je loop er per ongeluk een over?",
        ]
    return True, []


def stap_2(regels):
    """De indexnummers van het rooster, kaal op het scherm."""
    kaal = [r for r in regels if tel_namen(r) == 0 and not TIJD.search(r)]
    ontbreekt = [
        str(nummer) for nummer in range(DIENSTEN)
        if not any(bevat_getal(r, nummer) for r in kaal)
    ]

    if not ontbreekt:
        return True, []
    if len(ontbreekt) == DIENSTEN:
        return False, [
            "Ik zie de indexnummers nog niet op het scherm.",
            "Loop je met range over de lengte van het rooster, en print je het getal zelf?",
        ]
    return False, [
        "Ik mis nog het indexnummer: " + ", ".join(ontbreekt) + ".",
        "Bij welk getal begint range, en tot welk getal telt hij door?",
    ]


def stap_3(regels):
    """Alle paren, elk precies een keer."""
    paren = paar_regels(regels)
    verwacht = DIENSTEN * (DIENSTEN - 1) // 2

    if len(paren) == verwacht:
        return True, []
    if not paren:
        return False, [
            "Ik zie nog geen regels waarop twee diensten met elkaar vergeleken worden.",
            "Staan de twee loops al in elkaar, en print je binnen de binnenste loop?",
        ]
    if len(paren) == 2 * verwacht:
        return False, [
            "Ik tel precies twee keer zo veel vergelijkingen als ik verwacht.",
            "Loopt je binnenste loop weer vanaf het begin, of staat er per ongeluk een tweede lus omheen?",
        ]
    return False, [
        "Ik tel " + str(len(paren)) + " vergelijkingen, en dat is niet het aantal dat ik verwacht.",
        "Waar begint je binnenste loop? Elk paar hoort er een keer bij te staan, en niets vergelijk je met zichzelf.",
    ]


def stap_4(regels):
    """De conflicten. Er zit er precies een in dit rooster."""
    conflicten = [r for r in regels if "conflict" in r]
    if not conflicten:
        return False, [
            "Ik zie nog geen gemeld conflict.",
            "Roep je heeft_conflict binnen de binnenste loop aan, en print je alleen iets als die True is?",
        ]

    raak = [r for r in conflicten if "jansen" in r and "09:00" in r]
    if not raak:
        return False, [
            "Er wordt wel iets gemeld, maar niet over de dienst die ik verwacht.",
            "Welke twee diensten hebben dezelfde persoon op dezelfde tijd?",
        ]
    if len(conflicten) > 1:
        return False, [
            "Ik tel meer meldingen dan er conflicten in dit rooster zitten.",
            "Print je alleen iets als heeft_conflict True teruggeeft?",
        ]
    return True, []


STAPPEN = [
    ("Stap 1: elke dienst op een regel", stap_1),
    ("Stap 2: de indexnummers", stap_2),
    ("Stap 3: alle paren, elk een keer", stap_3),
    ("Stap 4: het conflict gevonden", stap_4),
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
