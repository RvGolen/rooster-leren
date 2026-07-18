# Uitleg — Waarom dit de gevaarlijkste fout is

## Het model deed precies wat het kreeg

`gegenereerd_model.py` is niet stuk. Het rekent correct, het lost netjes op, het geeft het
allergoedkoopste antwoord op de vraag die het kreeg: "maak een zo goedkoop mogelijk rooster
dat aan de regels voldoet."

Het probleem zit in die laatste vier woorden: *welke regels?*

Het model kende drie regels: dekking, dubbelboeking, geschiktheid. Dat zijn de constraints die
erin zitten. Beschikbaarheid — de regel dat een medewerker alleen ingezet wordt als hij op dat
tijdslot beschikbaar is — staat er niet in. Niet per ongeluk weggelaten door de AI, maar omdat
die regel niet in de opdracht stond, niet als data aangeboden was, en niet in de code terechtkwam.

Een goedkoper antwoord dat een harde regel breekt, is geen oplossing. Het is een antwoord op een
verkeerde vraag.

## Waarom dit gevaarlijker is dan een crash

Als een programma crasht, weet je dat er iets mis is. Je krijgt een foutmelding, een rode tekst,
een leeg scherm. Je gaat zoeken.

Maar `gegenereerd_model.py` crasht niet. Het geeft een netjes opgemaakt rooster, een bedrag,
een CSV-bestand. Alles ziet er goed uit. Als je het niet controleert met een validator die
beschikbaarheid kent, stuur je dit rooster de deur uit — en dan bel je op maandagochtend Smit
en Willems om te vragen waarom ze niet op komen dagen terwijl ze hadden gezegd dat ze niet
beschikbaar waren.

De fout zit verstopt achter een correct antwoord. Dat is het gevaarlijkste soort fout.

## De vraag die je bij elk model stelt

Niet: "klopt wat er staat?"

Maar: **"wat staat er niet, en zou dat er moeten staan?"**

Dit is de vaardigheid die je in deze module oefent, en die je in het eindproject nodig hebt.
Een AI weet niet wat heilig is in jouw situatie — beschikbaarheid, een wettelijke eis,
een afspraak die nergens in de code staat maar die iedereen kent. Jij bent de enige die dat
weet. Jij bewaakt het.

## De capaciteitsmelding

De validator meldt ook een capaciteitsknelpunt bij T5 (55 studenten in B2.11, capaciteit 40).
Dat is een pre-existing probleem in het voorbeeldrooster — het model weet niets van lokalen,
het wijst alleen mensen toe. Die melding is niet veroorzaakt door het ontbrekende constraint;
hij stond er al. De beschikbaarheids-meldingen (Smit op T1, Willems op T7) zijn de meldingen
die dit model heeft veroorzaakt.
