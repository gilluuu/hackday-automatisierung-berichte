from getBEData import getChart1

df = getChart1()


data = df.to_dict(orient='index')
thisyear = data[2022]
lastyear = data[2021]

# Berichtsvariablen

jahr = 2022
basis_jahr = 2003
gesamtindex = thisyear['Total']
änderung_vorjahr = thisyear['Total'] - lastyear['Total']


# Logische Anpassung des Textes
zunahme_text = ""
if änderung_vorjahr > 0:
    zunahme_text = f"einer Zunahme um {abs(änderung_vorjahr)}% "
elif änderung_vorjahr < 0:
    zunahme_text = f"einer Abnahme um {abs(änderung_vorjahr)}% "
else:
    zunahme_text = "keiner Veränderung "

zimmer_über = []
zimmer_unter = []
for key, value in thisyear.items():
    if key != 'Total':
        if value > gesamtindex:
            zimmer_über.append(key)
        elif value < gesamtindex:
            zimmer_unter.append(key)

def getBericht1():
# Bericht generieren
    bericht = f"Der Berner Index der Wohnungsmietpreise erreicht im November {jahr} einen Stand von {gesamtindex} Punkten "
    bericht += f"(Basis: {basis_jahr} = 100), was {zunahme_text}gegenüber dem Vorjahr entspricht. "
    bericht += f"Die Preisentwicklung der {zimmer_über}-Wohungen lag über dem Gesamtindex. "
    bericht += f"Bei den {zimmer_unter}-Wohungen lag sie darunter."
    return bericht


print(getBericht1())