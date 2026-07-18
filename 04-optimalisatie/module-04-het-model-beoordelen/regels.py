"""De regels waaraan een surveillance-rooster moet voldoen.

Elke functie geeft een lijst met meldingen terug. Een lege lijst betekent:
op deze regel is niets mis.
"""


def controleer_dekking(toetsen, rooster):
    """Heeft elke toets het vereiste aantal surveillanten?"""
    meldingen = []
    for _, toets in toetsen.iterrows():
        tid = toets["toets_id"]
        vereist = int(toets["vereist_toezicht"])
        ingezet = int((rooster["toets_id"] == tid).sum())
        if ingezet < vereist:
            meldingen.append(
                f"dekking: {tid} heeft {ingezet} surveillant(en), "
                f"maar vereist {vereist}"
            )
    return meldingen


def controleer_capaciteit(toetsen, lokalen):
    """Passen de studenten in het toegewezen lokaal?"""
    meldingen = []
    cap = dict(zip(lokalen["lokaal"], lokalen["capaciteit"]))
    for _, toets in toetsen.iterrows():
        lokaal = toets["lokaal"]
        studenten = int(toets["aantal_studenten"])
        capaciteit = int(cap[lokaal])
        if studenten > capaciteit:
            meldingen.append(
                f"capaciteit: {toets['toets_id']} ({toets['vak']}) heeft "
                f"{studenten} studenten maar lokaal {lokaal} heeft maar "
                f"{capaciteit} plekken"
            )
    return meldingen


def controleer_beschikbaarheid(toetsen, rooster, beschikbaarheid):
    """Is iedereen die is ingezet, ook beschikbaar op dat tijdslot?"""
    meldingen = []
    toets_tijd = dict(zip(toetsen["toets_id"], toetsen["tijd"]))
    niet_beschikbaar = set(
        beschikbaarheid[beschikbaarheid["beschikbaar"] == "nee"]
        .apply(lambda r: (r["naam"], r["tijd"]), axis=1)
    )
    for _, rij in rooster.iterrows():
        tid = rij["toets_id"]
        naam = rij["naam"]
        tijd = toets_tijd.get(tid)
        if (naam, tijd) in niet_beschikbaar:
            meldingen.append(
                f"beschikbaarheid: {naam} staat op {tid} ({tijd}) "
                f"maar is dan niet beschikbaar"
            )
    return meldingen


def controleer_dubbelboeking(toetsen, rooster):
    """Staat niemand op twee toetsen tegelijk?"""
    meldingen = []
    toets_tijd = dict(zip(toetsen["toets_id"], toetsen["tijd"]))
    gezien = {}
    for _, rij in rooster.iterrows():
        naam = rij["naam"]
        tijd = toets_tijd.get(rij["toets_id"])
        sleutel = (naam, tijd)
        if sleutel in gezien:
            if gezien[sleutel] == 1:
                meldingen.append(
                    f"dubbelboeking: {naam} staat meerdere keren ingeroosterd "
                    f"op tijdslot {tijd}"
                )
            gezien[sleutel] += 1
        else:
            gezien[sleutel] = 1
    return meldingen


def controleer_geschiktheid(toetsen, rooster, bevoegdheden):
    """Staat er op elke lab-toets alleen een lab-bevoegde surveillant?

    Lege lijst = niets mis.
    """
    LAB_TOETSEN = ["T3"]
    lab_ok = set(bevoegdheden[bevoegdheden["lab_bevoegd"] == "ja"]["naam"])
    meldingen = []
    for _, rij in rooster.iterrows():
        if rij["toets_id"] in LAB_TOETSEN and rij["naam"] not in lab_ok:
            meldingen.append(
                f"geschiktheid: {rij['naam']} staat op lab-toets {rij['toets_id']} "
                f"maar is niet lab-bevoegd")
    return meldingen
