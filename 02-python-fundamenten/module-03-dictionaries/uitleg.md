# Waarom dictionaries? — het *waaróm* achter module 3

Je had één toets ook in losse variabelen kunnen zetten (module 1) of in een lijst
(module 2). Waarom dan een dict?

## 1. Een label is duidelijker dan een nummer

Vergelijk:

```python
toets = ["A1.04", "09:00", 30, 2]   # lijst: wat is plek 2 ook alweer?
toets["studenten"]                   # dict: meteen duidelijk
```

Bij een lijst moet je onthouden dat plek 2 "studenten" is. Bij een dict staat het
er gewoon. Dat scheelt fouten — en het maakt code die je *leest* (straks van de AI)
begrijpelijk zonder raden.

## 2. Eén ding bij elkaar houden

Een toets is geen losse feiten; het is één samenhangend ding met kenmerken. Een dict
houdt die kenmerken **bij elkaar onder één naam**. Verплaats je `toets`, dan
verhuist alles mee. Geen kans dat het lokaal en de tijd per ongeluk uit de pas gaan
lopen.

## 3. De bouwsteen van je rooster

Dit is het belangrijkste: straks is je hele rooster een **lijst van dicts** — elke
toets een dict, alle toetsen samen in een lijst. Dan kun je met één loop "voor elke
toets, controleer iets" doen. Module 3 legt daar de helft van. Module 7 legt de
andere helft.

---

## Lijst of dict? — de vuistregel

| Je hebt… | Kies | Voorbeeld |
|----------|------|-----------|
| meerdere dingen van **dezelfde soort** | `list` | alle lokalen, alle tijdsloten |
| meerdere **kenmerken van één ding** | `dict` | alles over één toets |
| meerdere dingen, elk met meerdere kenmerken | **lijst van dicts** | een heel rooster |

---

## Termen van vandaag

| Term | Betekenis |
|------|-----------|
| `dict` (dictionary) | verzameling van `key: value`-paren, tussen `{ }` |
| key (sleutel) | het label waarmee je een waarde opvraagt: `toets["tijd"]` |
| value (waarde) | wat er achter de key zit |
| `KeyError` | foutmelding: je vraagt een key op die niet bestaat |

---

➡️ Verder met **`check.md`** van deze module. Onderaan staat waar je daarna heen gaat.
