"""Zet alles aan elkaar: data inlezen, regels controleren, resultaat tonen."""
import data
import regels

toetsen = data.lees_toetsen()
rooster = data.lees_rooster()

meldingen = regels.controleer_dekking(toetsen, rooster)

# TODO: print elke melding. Zijn er geen meldingen? Zeg dat dan met zoveel woorden.
