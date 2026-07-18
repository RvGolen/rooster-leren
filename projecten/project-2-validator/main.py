"""De validator: leest het rooster in en controleert alle regels."""
import data
import regels

lokalen = data.lees_lokalen()
toetsen = data.lees_toetsen()
beschikbaarheid = data.lees_beschikbaarheid()
rooster = data.lees_rooster()

# TODO: roep elke controle aan en verzamel alle meldingen
# TODO: print ze gegroepeerd per regel, zodat je ziet wélke regel wordt overtreden
# TODO: geen enkele melding? Zeg dan met zoveel woorden dat het rooster klopt
