# Controleer je werk: module 1 (variabelen)
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

TITEL = "Controle van module 1 (variabelen)"
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


def bevat_getal(tekst, waarde):
    """Staat dit getal als los getal in de tekst? (24 telt niet als een 2)"""
    getal = "%g" % waarde
    return re.search(r"(?<![\d.])" + re.escape(getal) + r"(?!\d)", tekst) is not None


ONTBREEKT = "Staat de # nog voor de print-regel van deze stap? Haal die weg."


# --- de stappen -------------------------------------------------------------

def stap_1(regels):
    """Het voorgedane voorbeeld: het lokaal staat op het scherm."""
    if bevat(regels, "stap 1", "b2.10"):
        return True, []
    return False, [
        "Dit stukje stond al voor je klaar, maar ik zie het niet terug.",
        "Is er bovenin opdracht.py per ongeluk iets veranderd of weggehaald?",
    ]


def stap_2(regels):
    """Twee zelfgemaakte variabelen: het aantal studenten en surveillanten."""
    regel = zoek(regels, "stap 2")
    if regel is None:
        return False, ["Ik zie de regel van stap 2 nog niet op het scherm.", ONTBREEKT]

    if not bevat_getal(regel, 24):
        return False, [
            "Het aantal studenten op die regel klopt nog niet.",
            "Krijgt 'aantal_studenten' de waarde die in de opdracht staat?",
        ]

    staart = regel.split("surveillanten", 1)[-1]
    if not bevat_getal(staart, 2):
        return False, [
            "Het aantal surveillanten op die regel klopt nog niet.",
            "Krijgt 'surveillanten' de waarde die in de opdracht staat?",
        ]
    return True, []


def stap_3(regels):
    """De inhuurkosten: surveillanten keer tarief keer uren."""
    regel = zoek(regels, "stap 3")
    if regel is None:
        return False, ["Ik zie de regel van stap 3 nog niet op het scherm.", ONTBREEKT]

    verwacht = 2 * 28.50 * 3
    if not bevat_getal(regel, verwacht):
        return False, [
            "Het bedrag op die regel is nog niet wat ik verwacht.",
            "Staan alle drie de variabelen in je berekening, en klopt het tarief (punt, geen komma)?",
        ]
    return True, []


def stap_4(regels):
    """Dezelfde som, maar met een surveillant erbij."""
    regel = zoek(regels, "stap 4")
    if regel is None:
        return False, ["Ik zie de regel van stap 4 nog niet op het scherm.", ONTBREEKT]

    verwacht = 3 * 28.50 * 3
    if not bevat_getal(regel, verwacht):
        oud = 2 * 28.50 * 3
        if bevat_getal(regel, oud):
            return False, [
                "Op die regel staat nog hetzelfde bedrag als bij stap 3.",
                "Een variabele verandert niet vanzelf mee: wordt de som na de wijziging opnieuw gedaan?",
            ]
        return False, [
            "Het nieuwe bedrag op die regel is nog niet wat ik verwacht.",
            "Heeft 'surveillanten' de nieuwe waarde gekregen, en gebruik je daarna dezelfde formule?",
        ]
    return True, []


STAPPEN = [
    ("Stap 1: het voorbeeld draait", stap_1),
    ("Stap 2: studenten en surveillanten", stap_2),
    ("Stap 3: de inhuurkosten", stap_3),
    ("Stap 4: de kosten na de wijziging", stap_4),
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
