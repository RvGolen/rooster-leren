# Controleer je werk: module 6 (functies)
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
# In deze module maken stap 3 en 4 alleen functies, zonder iets te printen.
# Ik kan ze dus niet los zien: ze komen samen met stap 5 aan het licht.
#
# Je hoeft dit bestand niet te begrijpen. Je mag het gerust lezen, maar het
# vertelt je niet welke code je moet typen. Dat blijft aan jou.
# ---------------------------------------------------------------------------

import os
import re
import subprocess
import sys

TITEL = "Controle van module 6 (functies)"
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


def bevat_getal(tekst, waarde):
    """Staat dit getal als los getal in de tekst? (24 telt niet als een 2)"""
    getal = "%g" % waarde
    return re.search(r"(?<![\d.])" + re.escape(getal) + r"(?!\d)", tekst) is not None


def booleans(regels):
    """Alle True- en False-waarden uit de uitvoer, op volgorde."""
    gevonden = []
    for regel in regels:
        gevonden.extend(re.findall(r"\b(true|false)\b", regel))
    return gevonden


# --- de stappen -------------------------------------------------------------

def stap_1(regels):
    """Het voorgedane voorbeeld: de kosten van drie uur inhuur."""
    verwacht = 3 * 28.50
    for regel in regels:
        if "stap 1" in regel and bevat_getal(regel, verwacht):
            return True, []
    return False, [
        "Dit stukje stond al voor je klaar, maar ik zie het niet terug.",
        "Is er bovenin opdracht.py per ongeluk iets veranderd of weggehaald?",
    ]


def stap_2(regels):
    """De twee testregels onder stap 2, met het antwoord dat erachter staat."""
    eigen = [regel for regel in regels if "stap 2" in regel]
    if not eigen:
        return False, [
            "Ik zie de twee testregels van stap 2 nog niet op het scherm.",
            "Staat de # nog voor die print-regels? Haal die weg zodra je functie bestaat.",
        ]

    waarden = booleans(eigen)
    if waarden[:2] == ["true", "false"]:
        return True, []
    if len(waarden) < 2:
        return False, [
            "Ik zie maar een van de twee testregels terug.",
            "Staan allebei de print-regels van stap 2 nu aan?",
        ]
    return False, [
        "De testregels geven nog niet de antwoorden die er als commentaar achter staan.",
        "Vergelijkt je functie de twee getallen de goede kant op, en geeft hij het antwoord terug?",
    ]


def stap_345(regels):
    """De uitkomsten van heeft_conflict. Stap 3 en 4 zie je hier terug."""
    overig = [regel for regel in regels if "stap 2" not in regel]
    waarden = booleans(overig)

    if len(waarden) < 2:
        return False, [
            "Ik zie de twee uitkomsten van heeft_conflict nog niet op het scherm.",
            "Bestaan de drie functies van stap 3 en 4 al, en print je allebei de tests uit stap 5?",
        ]
    if waarden[-2:] == ["true", "false"]:
        return True, []
    return False, [
        "De twee uitkomsten zijn nog niet wat de diensten hierboven laten verwachten.",
        "Kijk goed naar dienst 1 en 3: moeten voor een conflict allebei de dingen gelijk zijn, of is een van de twee al genoeg?",
    ]


STAPPEN = [
    ("Stap 1: het voorbeeld draait", stap_1),
    ("Stap 2: past_in_lokaal", stap_2),
    ("Stap 3 t/m 5: heeft_conflict", stap_345),
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
        print("1 van de " + str(totaal) + " controles klopt.")
    else:
        print(str(goed) + " van de " + str(totaal) + " controles kloppen.")

    if goed == totaal and not foutmelding:
        print()
        print("Mooi. 🎉 Ga nu naar check.md: daar kijk je of je ook snapt")
        print("wat je gedaan hebt. Dat is het deel dat dit bestand niet kan zien.")
        return 0

    print("Pas aan, draai je opdracht.py opnieuw, en probeer deze controle daarna nog eens.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
