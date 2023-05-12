from getBEData import getChart1

df = getChart1()


data = df.to_dict(orient='index')
highestyear = max(data.keys())
thisyear = data[highestyear]
lastyear = data[2021]

# Berichtsvariablen

gesamtindex = thisyear['Total']
änderung_vorjahr = thisyear['Total'] - lastyear['Total']


# Logische Anpassung des Textes
zunahme_text = ""
if änderung_vorjahr > 0:
    zunahme_text = f"einer Zunahme um {'{:.2f}'.format(abs(änderung_vorjahr))}% "
elif änderung_vorjahr < 0:
    zunahme_text = f"einer Abnahme um {'{:.2f}'.format(abs(änderung_vorjahr))}% "
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

gesamtindex_formated = "{:.2f}".format(gesamtindex)
zimmer_über_str = ', '.join(str(i) for i in zimmer_über)
zimmer_unter_str = ', '.join(str(i) for i in zimmer_unter)

def getBericht1():
# Bericht generieren
    bericht = f"Der Berner Index der Wohnungsmietpreise erreicht im November {highestyear} einen Stand von {gesamtindex_formated} Punkten "
    bericht += f"(Basis: November 2003 = 100), was {zunahme_text}gegenüber dem Vorjahr entspricht. "
    bericht += f"Die Preisentwicklung der {zimmer_über_str}-Wohungen lag über dem Gesamtindex. "
    bericht += f"Bei den {zimmer_unter_str}-Wohungen lag sie darunter."
    return bericht

print(getBericht1())