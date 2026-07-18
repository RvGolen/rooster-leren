# Uitleg — diffs lezen is een supervisie-vaardigheid

Het waaróm achter "lees de diff, keur bewust goed of af". Dit lijkt een technisch knopje,
maar het is eigenlijk de kern van je toekomstige rol.

---

## Vertrouwen is geen controle

Een AI klinkt vaak zelfverzekerd, óók als hij het mis heeft. Hij kan een regel te veel
veranderen, een functie verzinnen die niet bestaat, of net iets anders doen dan je
bedoelde. Als je blind **Accept** klikt, sluipen die fouten je project in — en later zijn
ze veel lastiger terug te vinden.

De diff is je controlemoment. Het is het verschil tussen *"de AI zei dat het goed was"*
en *"ik heb gezien dat het klopt"*.

---

## Reject en restore halen de angst weg

Omdat je elke wijziging kunt **afkeuren** en naar een **checkpoint** terug kunt, is
experimenteren veilig. Je kunt niets onherstelbaar breken. Dat is bevrijdend: je durft
de AI iets te laten proberen, juist omdat je het makkelijk terugdraait als het niet
bevalt. Veiligheid maakt je een *moediger* leerling, niet een voorzichtiger.

---

## Dit is letterlijk je rol straks

Het doel van deze cursus is dat je een **geïnformeerde regisseur** wordt van code die
een AI bouwt. In Fase 4 draait alles om precies deze reflex:

- de AI klein houden (kleine taken → kleine, leesbare diffs),
- elke diff lezen vóór je 'm accepteert,
- de AI terugsturen als hij afdwaalt.

Wat hier als een simpel accept/reject-knopje begint, is straks je belangrijkste
gereedschap om AI-code te vertrouwen zónder blind te varen. Je oefent het nu vast, in het
klein.
