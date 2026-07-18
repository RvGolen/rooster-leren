# Uitleg — Waarom schiet greedy tekort?

Greedy is niet dom. Het is een echte, veelgebruikte techniek. Maar hij is **kortzichtig**.

Door per toets apart de goedkoopste te pakken, zonder te kijken naar wat er daarna nog nodig is, loopt de greedy in twee vallen tegelijk:

**Val 1 — Dubbelboeking.** Als je bijhoudt wie je al hebt ingeroosterd kan je dit vermijden, maar zonder die controle zet je dezelfde persoon twee keer op hetzelfde tijdslot. Dat is exact de fout die jouw validator in Project 2 moest betrappen. Nu veroorzaak je hem zelf.

**Val 2 — De verspilde specialist.** De greedy ziet niet dat Bakker (de goedkope lab-bevoegde intern) later op de dag nodig is voor de lab-toets. Hij roostert Bakker vroeg in op een gewone toets — slim op dat moment — en moet dan voor de lab-toets Van Dijk inhuren voor het specialistentarief van €150/uur. Zelfs als je de dubbelboeking handmatig repareert, ben je duurder uit dan nodig.

Dit is de kern van het probleem: met losse, lokale keuzes krijg je alles tegelijk goed én goedkoop bijna niet voor elkaar. Je kunt twee conflicten tegelijk zien — de dubbelboeking en de dure specialist — maar elke lokale keuze die het ene oplost, maakt het andere erger.

**Daarom bestaat een solver.** Een solver kijkt niet één stap vooruit — hij bekijkt alle mogelijke toewijzingen tegelijk en kiest de goedkoopste die aan alle regels voldoet. Dat is precies wat module 3 introduceert.
