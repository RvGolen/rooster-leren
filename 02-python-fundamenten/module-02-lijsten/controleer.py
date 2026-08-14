# Controleer je werk: module 2 (lijsten)
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

TITEL = "Controle van module 2 (lijsten)"
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


TIJD = re.compile(r"\b\d{1,2}[:.]\d{2}\b")
NAMEN = ["jansen", "de vries", "bakker", "smit"]


def alleen(regels, naam):
    """Staat er een regel met deze naam erin en geen van de andere namen?"""
    anderen = [n for n in NAMEN if n != naam]
    for regel in regels:
        if naam in regel and not any(n in regel for n in anderen):
            return True
    return False


# --- de stappen -------------------------------------------------------------

def stap_1(regels):
    """Het voorgedane voorbeeld: het team staat op het scherm."""
    if bevat(regels, "stap 1", "jansen"):
        return True, []
    return False, [
        "Dit stukje stond al voor je klaar, maar ik zie het niet terug.",
        "Is er bovenin opdracht.py per ongeluk iets veranderd of weggehaald?",
    ]


def stap_2(regels):
    """Het eerste en het derde element, elk apart op het scherm."""
    eerste = alleen(regels, "jansen")
    derde = alleen(regels, "bakker")

    if eerste and derde:
        return True, []
    if not eerste and not derde:
        return False, [
            "Ik zie nog geen losse namen uit de lijst, alleen de lijst als geheel.",
            "Pak je er twee elementen uit met een indexnummer tussen blokhaken?",
        ]
    if not eerste:
        return False, [
            "Het derde element staat er los, het eerste nog niet.",
            "Welk indexnummer hoort bij het eerste element? Tellen begint niet bij 1.",
        ]
    return False, [
        "Het eerste element staat er los, het derde nog niet.",
        "Welk indexnummer hoort bij het derde element? Tellen begint niet bij 1.",
    ]


def stap_3(regels):
    """Het aantal surveillanten in de lijst."""
    # tijdsloten uit stap 5 kunnen ook cijfers bevatten; die laat ik hier buiten
    kandidaten = [r for r in regels if not TIJD.search(r)]
    if any(bevat_getal(r, 3) for r in kandidaten):
        return True, []
    return False, [
        "Ik zie het aantal surveillanten nog niet als los getal op het scherm.",
        "Print je de uitkomst van len(...) en niet de lijst zelf?",
    ]


def stap_4(regels):
    """Smit erbij, daarna de hele lijst en het nieuwe aantal."""
    compleet = [r for r in regels if all(n in r for n in NAMEN)]
    kandidaten = [r for r in regels if not TIJD.search(r)]
    nieuw_aantal = any(bevat_getal(r, 4) for r in kandidaten)

    if compleet and nieuw_aantal:
        return True, []
    if not compleet:
        return False, [
            "Ik zie nog geen lijst waar alle vier de surveillanten in staan.",
            "Is de nieuwe surveillant toegevoegd, en print je de lijst daarna opnieuw?",
        ]
    return False, [
        "De lijst klopt, maar het nieuwe aantal staat er nog niet los bij.",
        "Tel je de lijst opnieuw nadat je iemand hebt toegevoegd?",
    ]


def stap_5(regels):
    """Een eigen lijst tijdsloten, en daaruit het laatste."""
    met_tijd = [r for r in regels if TIJD.search(r)]
    if not met_tijd:
        return False, [
            "Ik zie nog geen tijdslot in de uitvoer.",
            "Bestaat de lijst 'tijdsloten' al, en print je er iets uit?",
        ]

    los = [r for r in met_tijd if len(TIJD.findall(r)) == 1]
    if not los:
        return False, [
            "Ik zie wel tijdsloten, maar alleen allemaal samen op een regel.",
            "Print er ook eentje los. Welk indexnummer hoort bij het laatste?",
        ]
    return True, []


STAPPEN = [
    ("Stap 1: het voorbeeld draait", stap_1),
    ("Stap 2: het eerste en het derde element", stap_2),
    ("Stap 3: het aantal surveillanten", stap_3),
    ("Stap 4: eentje erbij, en opnieuw geteld", stap_4),
    ("Stap 5: het laatste tijdslot", stap_5),
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
