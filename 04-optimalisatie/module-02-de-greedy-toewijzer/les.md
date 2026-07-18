# Module 2 — De greedy-toewijzer

⏱️ ± 30–40 minuten · Fase 3 · **Nieuw concept:** greedy

---

## Eerst even raden 🤔

Stel je voor: je moet voor elke toets een of meer surveillanten inroosteren. Je keuze is simpel — pak per toets steeds de goedkoopste beschikbare persoon die mag.

Twee vragen om over na te denken vóór je begint:

1. Geeft die aanpak het goedkoopste rooster in totaal?
2. Blijft het rooster ook geldig — klopt elke regel die je in Project 2 hebt gebouwd?

Gok eerst. Je ziet het antwoord straks vanzelf.

---

## Het concept: greedy

**Greedy** (Engels voor "gulzig") is een aanpak waarbij je bij elke stap de lokaal beste keuze maakt, zonder vooruit te kijken. Per toets pak je wat op dat moment het goedkoopst lijkt — en dan ga je verder naar de volgende.

Het is snel en simpel. En het werkt best goed... totdat het niet meer werkt.

Het probleem: een keuze die er nu gunstig uitziet, kan later voor een probleem zorgen. Soms verbruik je iemand op een goedkope toets, terwijl je diezelfde persoon daarna hard nodig hebt voor een duurdere — en dan zit je vast.

---

## Uitgewerkt voorbeeld

> ⚠️ **Voorbeeld, geen voorschrift.** Dit voorbeeld gebruikt ons fictieve rooster om het idee concreet te maken. Jouw eigen situatie is anders.

Stel: het tijdslot 09:00 heeft drie toetsen — T1, T2 en T3. De beschikbare mensen om 09:00 zijn (gesorteerd op goedkoopst):

| Naam      | Uurtarief | Type   | Lab-bevoegd |
|-----------|-----------|--------|-------------|
| Jansen    | €38       | intern | nee         |
| De Vries  | €38       | intern | nee         |
| Willems   | €38       | intern | nee         |
| Bakker    | €42       | intern | ja          |
| Van Dijk  | €90       | extern | ja          |

Een greedy pakt voor T1 (2 surveillanten nodig) de goedkoopsten: **Jansen** en **De Vries**. Voor T2 (3 nodig) pakt hij de volgende goedkoopsten: **Willems**, **Bakker** en dan iemand anders. Voor T3 (1 nodig, lab-toets) is de lab-bevoegde **Bakker** al weg — de greedy huurt **Van Dijk** in voor het specialistentarief (€150/uur).

Je ziet twee valkuilen die je gaat tegenkomen in de opdracht:

**Valkuil 1 — Dubbelboeking.** Als je niet bijhoudt wie je al hebt ingeroosterd, kun je dezelfde persoon twee keer op hetzelfde tijdslot zetten. Dat is ongeldig. Je validator zal het betrappen.

**Valkuil 2 — De dure specialist.** Door Bakker vroeg te verbruiken op een gewone toets, moet je later de duurdere Van Dijk inhuren voor de lab-toets. Een greedy kijkt niet vooruit — hij ziet dat Bakker nu goedkoop is, maar niet dat hij hem straks hard nodig heeft.

Open `opdracht.py` en bouw de greedy stap voor stap. In stap 2 van de opdracht laat je bewust de dubbelboeking toe — dan zie je precies wat de validator meldt.

---

## Wat je daarna ziet

Nadat je greedy klaar is, draait de validator (stap 4 van `opdracht.py`) alle vijf checks over je toewijzing. Je zult meldingen zien verschijnen.

De validator draait ook de capaciteitscheck — die vergelijkt het aantal studenten per toets met de grootte van het lokaal. Let op: die check zit al in de data verwerkt en staat los van jouw toewijzer. Voor T5 (Bestuurskunde) geldt dat het lokaal B2.11 maar 40 plekken heeft terwijl er 55 studenten zijn — die melding verschijnt dus ook, maar dat is een bestaand probleem in de data, niet iets wat jouw greedy heeft veroorzaakt. Je toewijzer gaat niet over lokalen; de melding om op te focussen is de **dubbelboeking die je greedy zélf veroorzaakte**.

Klaar? Ga naar **`check.md`**.
