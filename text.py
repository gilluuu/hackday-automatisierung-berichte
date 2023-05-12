# Berichtsvariablen
monat = "November"
jahr = 2022
basis_jahr = 2003
gesamtindex = 124.3
zunahme_vorjahr = 0.0  # Keine Veränderung
zimmer_indices = {
    "1-Zimmerwohnungen": 120.5,
    "2-Zimmerwohnungen": 130.2,
    "3-Zimmerwohnungen": 135.8,
    "4-Zimmerwohnungen": 140.1,
    "5-Zimmerwohnungen": 142.7
}

# Logische Anpassung des Textes
zunahme_text = ""
if zunahme_vorjahr > 0:
    zunahme_text = f"einer Zunahme um {abs(zunahme_vorjahr)}% gegenüber dem Vorjahr"
elif zunahme_vorjahr < 0:
    zunahme_text = f"einer Abnahme um {abs(zunahme_vorjahr)}% gegenüber dem Vorjahr"
else:
    zunahme_text = "keiner Veränderung gegenüber dem Vorjahr"

# Preisentwicklungen
preisentwicklung_text = ""
if all(zimmer_indices[zimmer] > gesamtindex for zimmer in zimmer_indices):
    preisentwicklung_text = "lagen über jener des Gesamtindex"
elif all(zimmer_indices[zimmer] < gesamtindex for zimmer in zimmer_indices):
    preisentwicklung_text = "lagen unter jener des Gesamtindex"

# Bericht generieren
bericht = f"Der Berner Index der Wohnungsmietpreise erreicht im {monat} {jahr} einen Stand von {gesamtindex} Punkten "
bericht += f"(Basis: {basis_jahr} = 100), was {zunahme_text} entspricht. "
bericht += f"Die Preisentwicklung der 2- bis 5-Zimmerwohnungen {preisentwicklung_text}. "
bericht += f"Bei den 1-Zimmerwohnungen lag sie darunter."

# Ausgabe des Berichts
print(bericht)
