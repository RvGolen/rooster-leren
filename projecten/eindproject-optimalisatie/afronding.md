# Afronding — Eindproject optimalisatie

Goed gedaan dat je dit hebt afgerond. Even terugkijken — en vooruit.

---

## Controleer jezelf

- Je validator hoort **0 overtredingen (op de vier toewijzings-regels)** te
  melden. Zijn dat er meer? Dan mist je model nog een constraint. Ga terug naar
  Cursor en vraag welke constraint ontbreekt.
- De totale kosten horen **€1.755** te zijn — €225 goedkoper dan de greedy
  (€1.980). Klopt dat?
- Haal je **€1.632**? Dan lijkt je model goedkoper, maar het is *niet geldig*.
  Je model mist de beschikbaarheids-constraint (module 4!). Zet Smit om 09:00
  of Willems om 14:00 in het rooster? Dat zijn mensen die dan niet beschikbaar
  zijn. Voeg de constraint toe en draai opnieuw.

### Even uitleggen: waarom vier regels, niet vijf?

In module 2 en 4 liet de validator vijf regels zien — ook de capaciteits-melding
van T5 (Bestuurskunde in lokaal B2.11: 55 studenten, capaciteit 40). Die melding
was er bewust in gebouwd als iets om te vinden.

In het eindproject optimaliseer je de **toewijzing**: welke surveillant staat op
welke toets? Capaciteit gaat over wélk lokaal een toets heeft — en dat ligt vast
in de data. Je kunt T5 niet "wegroosteren" uit B2.11. De capaciteits-melding
zegt dus niets over hoe goed jouw toewijzing is. Daarom kijkt `controleer()` hier
naar de vier regels die wél over jouw toewijzing gaan: dekking, beschikbaarheid,
dubbelboeking en geschiktheid.

> Geen referentie-oplossing hier — expres. Zelf je model laten kloppen tegen de
> validator is precies de vaardigheid die je traint: *controleren of de AI heeft
> gedaan wat jij vroeg.*

---

## Reflectie ✍️ (in `voortgang.md`)

1. Wat was moeilijker — het model *lezen* of *beoordelen*? Wat maakte het
   beoordelen lastig?
2. Welke van de vijf constraints controleerde je model bijna niet, en hoe merkte
   je dat?
3. Wat zou je anders aanpakken als je dit opnieuw deed — in de manier waarop je
   Cursor aanstuurt?

---

## Wat je nu kunt

Je bent van "een rooster controleren" naar **een rooster optimaliseren**. Onderweg
heb je een probleem als optimalisatie geformuleerd (harde regels + doelfunctie),
een simpele greedy-toewijzer gebouwd, en een gegenereerd solver-model gelezen,
gedraaid en beoordeeld. Je hebt Cursor aangestuurd in kleine stappen, elke diff
gelezen, en de AI teruggestuurd als het niet klopte.

Dat is fase 3, samengebald in één project.

---

## Hier houdt de cursus voorlopig op

Je hebt nu ervaren hoe het werkt om de AI te regisseren: goede prompts schrijven,
Plan-modus gebruiken, diffs beoordelen, en de AI terugsturen als hij afdwaalt.

**Fase 4 volgt later.** Daarin wordt dat je vaste werkwijze voor een echt project:
je schrijft een eigen `rules`-bestand voor jouw domein, zodat de AI niet van
scratch begint maar jouw regels al kent. Je hoort het wanneer die klaarstaat.

Tot die tijd is dit de beste oefening: pak je **eigen** surveillance-situatie erbij
en probeer het patroon uit deze fase erop toe te passen. Kleine stappen, lees elke
diff, en leg elke keuze terug bij de AI als je hem niet begrijpt.

🎉 Tot zover: knap werk.
