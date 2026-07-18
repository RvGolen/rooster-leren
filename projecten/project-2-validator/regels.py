"""De regels waaraan een surveillance-rooster moet voldoen.

Elke functie geeft een lijst met meldingen terug. Een lege lijst betekent:
op deze regel is niets mis.
"""


def controleer_dekking(toetsen, rooster):
    """Heeft elke toets het vereiste aantal surveillanten?"""
    meldingen = []
    # TODO: loop over ALLE toetsen — ook die niet in het rooster voorkomen (module 4!)
    # TODO: tel per toets het aantal ingezette mensen; vergelijk met vereist_toezicht
    return meldingen


def controleer_capaciteit(toetsen, lokalen):
    """Passen de studenten in het toegewezen lokaal?"""
    meldingen = []
    # TODO: zoek per toets de capaciteit van het lokaal op
    # TODO: meer studenten dan plekken? Meld het.
    return meldingen


def controleer_beschikbaarheid(toetsen, rooster, beschikbaarheid):
    """Is iedereen die is ingezet, ook beschikbaar op dat tijdslot?"""
    meldingen = []
    # TODO: zoek per rij in het rooster het tijdslot van de toets op
    # TODO: staat er voor die persoon en dat tijdslot 'nee' in beschikbaarheid? Meld het.
    return meldingen


def controleer_dubbelboeking(toetsen, rooster):
    """Staat niemand op twee toetsen tegelijk?

    Deze regel bouwde je in Project 1 al — dit is je eigen heeft_conflict, nu op
    data uit een bestand.
    """
    meldingen = []
    # TODO: bepaal per rij in het rooster wie op welk tijdslot staat
    # TODO: komt een combinatie persoon+tijd meer dan één keer voor? Meld het.
    return meldingen
