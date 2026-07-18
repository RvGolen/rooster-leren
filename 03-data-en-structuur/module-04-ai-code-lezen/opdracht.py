# Module 4 — AI-code lezen — OPDRACHT
#
# Geen #TODO's om code te schrijven vandaag — wel vijf #TODO's om te denken,
# te draaien en te onderzoeken. Schrijf je antwoorden als commentaar, gewoon
# onder de vraag. Dit bestand hoeft niet te "draaien" om iets te printen; het
# moet vooral kloppen als Python (compileren), zodat je stap voor stap kunt
# invullen zonder foutmeldingen.
# ---------------------------------------------------------------------------


# STAP 1 — VOORSPEL
# Open gegenereerd.py, maar draai hem nog NIET. Lees de code regel voor regel
# en beantwoord, vóórdat je iets uitvoert:
#   - Hoeveel regels uitvoer verwacht je (los van de kopregel en de afsluiting)?
#   - Welke toets_id's verwacht je erin terug te zien?
#   - Verwacht je een PROBLEEM-melding? Voor welke toets, en waarom?
#
# TODO: schrijf hier je voorspelling.


# STAP 2 — DRAAI
# Draai nu, vanuit deze map, het echte script:
#   python gegenereerd.py
#
# TODO: schrijf hier wat er werkelijk uit kwam. Klopte je voorspelling uit
#       stap 1? Zo niet: wat was anders dan je dacht?


# STAP 3 — ZOEK
# Tijd om uit te zoeken wát er anders was.
#   - Open ../../voorbeelddata/toetsen.csv. Hoeveel toetsen staan hierin?
#   - Tel de regels die gegenereerd.py printte (zonder de kopregel en de
#     afsluiting). Hoeveel zijn dat er?
#   - Welke toets_id ontbreekt in de uitvoer?
#   - Open ../../voorbeelddata/rooster.csv. Hoeveel rijen heeft die ontbrekende
#     toets daarin?
#
# TODO: schrijf hier je antwoorden op deze vier punten.


# STAP 4 — VERKLAAR
# gegenereerd.py groepeert rooster.csv per toets_id, en loopt vervolgens over
# die groepering heen.
#
# TODO: leg in je eigen woorden uit waarom een toets die NUL keer voorkomt in
#       rooster.csv nooit in aantal_per_toets terechtkomt, en dus ook nooit in
#       de uitvoer van het script. Wat had er moeten gebeuren in plaats daarvan?


# STAP 5 — REPAREER (denkwerk, geen kant-en-klare oplossing)
# Je hoeft de code hieronder niet te schrijven — dat komt in een latere module.
# Beschrijf wél, in woorden, hoe een versie van dit script eruit zou zien die
# WEL over alle acht toetsen loopt.
#
# Hint: waar loop je nu overheen (rooster.csv, via de groepering), en waar zou
# je overheen moeten lopen om zeker te weten dat je geen enkele toets mist?
# Als een toets helemaal niet in de groepering voorkomt — hoeveel surveillanten
# heeft hij dan, en wat betekent dat voor de vergelijking met vereist_toezicht?
#
# TODO: schrijf hier in woorden (geen code) hoe jouw reparatie eruit zou zien.


# KLAAR? Ga naar uitleg.md, en daarna naar check.md.
