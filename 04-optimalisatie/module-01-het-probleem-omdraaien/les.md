# Module 1 — Het probleem omdraaien

⏱️ ± 25–30 minuten · Fase 3 (start) · **Nieuw concept:** harde regels vs. zachte wensen + doelfunctie

---

## Eerst even raden 🤔

Kijk naar dit mini-rooster voor een ochtend:

| Toets | Vak | Tijd | Surveillant | Beschikbaar? |
|-------|-----|------|-------------|--------------|
| T1 | Statistiek | 09:00 | Jansen | ja |
| T3 | Microbiologie | 09:00 | De Vries | ja |

En deze drie regels:

1. Elke toets heeft het vereiste aantal surveillanten.
2. De surveillant heeft liever geen twee diensten achter elkaar.
3. Een lab-toets vereist een lab-bevoegde surveillant.

> Welke van deze drie regels *mag nooit gebroken worden*, en welke is een *wens*?
> Schrijf je antwoord voor jezelf op — aan het eind van deze les weet je of je gelijk had.

---

## Drie begrippen die je nu nodig hebt

### 1. Harde regels

Een **harde regel** is een regel die *nooit* gebroken mag worden. Elk rooster dat er toch aan komt, is ongeldig — klaar. In Project 2 valideerde je vier harde regels:

1. **Dekking** — elke toets heeft het vereiste aantal surveillanten.
2. **Capaciteit** — het lokaal is groot genoeg voor de studenten.
3. **Beschikbaarheid** — de surveillant is beschikbaar op dat tijdslot.
4. **Geen dubbelboeking** — niemand staat op twee toetsen tegelijk.

Fase 3 voegt daar een **vijfde** harde regel aan toe:

5. **Geschiktheid** — mag deze persoon deze toets überhaupt doen?

Het bekendste voorbeeld: een lab-toets zoals Microbiologie (T3) vereist een surveillant die lab-bevoegd is. Dat is geen wens — het is een harde eis. Of iemand lab-bevoegd is, staat in een nieuw bestand: `../../voorbeelddata/bevoegdheden.csv`. Open het gerust in Cursor:

```
naam,lab_bevoegd
Bakker,ja
Van Dijk,ja
Jansen,nee
...
```

Alleen Bakker en Van Dijk zijn lab-bevoegd. Iedereen die op T3 staat zonder die bevoegdheid maakt het rooster onmiddellijk ongeldig.

### 2. Zachte wensen

Een **zachte wens** is iets wat je *liever wél* hebt, maar dat een rooster niet ongeldig maakt als het er niet in zit. Voorbeelden: een eerlijke verdeling van diensten, geen twee diensten achter elkaar, rekening houden met voorkeursdagen. We benoemen ze hier — ze spelen een rol in latere fases.

### 3. Doelfunctie

Nu het spannende gedeelte. In Project 2 had je één vraag: *"klopt dit rooster?"* Dat zijn de harde regels. Maar er zijn duizenden roosters die kloppen. De meeste zijn onnodig duur.

De **doelfunctie** is het getal dat zegt hoe *goed* een rooster is, zodat je roosters met elkaar kunt vergelijken en het beste kunt kiezen. In ons geval is dat eenvoudig: de totale inhuurkosten in euro's. Je wilt ze zo laag mogelijk.

---

## Uitgewerkt voorbeeld

> ⚠️ **Voorbeeld, geen voorschrift.** We gebruiken de medewerkers en toetsen uit
> de voorbeelddata om de doelfunctie concreet te maken. Jouw eigen rooster heeft
> mogelijk andere tarieven of toetstypen.

**Kostenmodel:** één dienst duurt 3 uur (aanname voor dit voorbeeld). De kosten zijn:

```
kosten = uurtarief × 3
```

Bekijk de medewerkers:

| Naam | Type | Uurtarief | Kosten per dienst |
|------|------|-----------|-------------------|
| Jansen | intern | €38 | €38 × 3 = **€114** |
| Bakker | intern | €42 | €42 × 3 = **€126** |
| Peters | extern | €75 | €75 × 3 = **€225** |
| Van Dijk | extern | €90 | €90 × 3 = **€270** |

Een interne surveillant is goedkoper dan een externe. Dat merk je meteen in de totale kosten.

**Maar er is een uitzondering.** Een lab-bevoegde **externe** op een lab-toets rekent een specialistentarief: **€150 per uur** in plaats van zijn normale tarief.

Voorbeeld: Van Dijk is lab-bevoegd en extern. Op een gewone toets kost hij €90 × 3 = €270. Op lab-toets T3 kost hij echter **€150 × 3 = €450**.

Peters is ook extern, maar niet lab-bevoegd — hij mag T3 dus niet bewaken. Op een gewone toets kost Peters **€75 × 3 = €225**.

Dít is waarom de doelfunctie ertoe doet: de keuze wie je op welke toets zet, maakt honderden euro's verschil — terwijl alle kloppende roosters er aan de buitenkant hetzelfde uitzien.

---

## Nu jij

Open **`opdracht.py`**. Je berekent de totale inhuurkosten van het gegeven `rooster.csv`. Twee stappen, met een `TODO` bij elk.

> Vastgelopen? In **Ask-modus**: *"leg uit wat `iterrows()` doet en geef een voorbeeld"* — laat het je uitleggen, pas het dan zelf toe.

Klaar? Ga naar **`check.md`**.
