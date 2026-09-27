# Waarom filteren en tellen? — module 3

Bij een rooster stel je eigenlijk steeds twee soorten vragen. De eerste is:
**welke rijen voldoen hieraan?** — welke toetsen zijn er om 09:00, welke
lokalen zijn te klein, welke medewerker is vandaag niet beschikbaar. Dat is
filteren. De tweede is: **hoeveel per categorie?** — hoeveel toetsen per
tijdslot, hoeveel diensten per persoon, hoeveel surveillanten per toets. Dat is
tellen of groeperen.

Vrijwel elke controle die je in deze cursus nog gaat bouwen — of het nu een
dekkingscheck is, een capaciteitscheck, of een beschikbaarheidscheck — is een
combinatie van precies die twee vragen. Als je filteren en groeperen
beheerst, heb je de bouwstenen voor bijna alles wat volgt.

## Wat, niet hoe

In fase 1 schreef je zelf een loop met een `if` erin om te tellen: je liep
regel voor regel door je rooster, en hield handmatig een teller bij. Dat werkt,
maar je moest zelf uitschrijven *hoe* Python moest tellen — regel voor regel,
stap voor stap.

`toetsen[toetsen["tijd"] == "09:00"]` en `toetsen.groupby("tijd").size()`
werken anders. Jij zegt alleen *wat* je wilt weten — "de rijen om 09:00", "het
aantal per tijdslot" — en pandas rekent zelf uit hoe dat moet. Dat is niet
alleen minder typwerk. Het is ook makkelijker te controleren: één regel die
zegt wat hij doet, is minder foutgevoelig dan tien regels die het stap voor
stap voordoen. En dat is precies waar je bij het superviseren van AI-code op
gaat letten: klopt wat deze regel *zegt* dat hij doet, met wat je zelf
verwacht?

---

➡️ Verder met **`check.md`** van deze module. Onderaan staat waar je daarna heen gaat.
