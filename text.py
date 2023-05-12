from getBEData import getChart1

df = getChart1()
#print(df)
data = df.to_dict(orient='index')

highestyear = max(data.keys())
thisyear = data[highestyear]
lastyear = data[highestyear-1]

gesamtindex = thisyear['Total']
änderung_vorjahr = thisyear['Total'] - lastyear['Total']
gesamtänderung = (thisyear['Total'] - 1) * 100

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

gesamtindex_str = "{:.2f}".format(gesamtindex*100)
zimmer_über_str = ', '.join(str(i) for i in zimmer_über)
zimmer_unter_str = ', '.join(str(i) for i in zimmer_unter)

gesamtänderung_str = "{:.2f}".format(gesamtänderung)

hihgestwohunung = max(thisyear, key=thisyear.get)
hihgestwohunung_change = "{:.2f}".format((thisyear[hihgestwohunung] - 1) *100)

lowestwohunung = min(thisyear, key=thisyear.get)
lowesttwohunung_change = "{:.2f}".format((thisyear[lowestwohunung] - 1) *100)


def getBericht1():
# Bericht generieren
    bericht = f"Der Berner Index der Wohnungsmietpreise erreicht im November {highestyear} einen Stand von {gesamtindex_str} Punkten "
    bericht += f"(Basis: November 2003 = 100), was {zunahme_text}gegenüber dem Vorjahr entspricht. "
    bericht += f"Die Preisentwicklung der {zimmer_über_str}-Wohungen lag über dem Gesamtindex. "
    bericht += f"Bei den {zimmer_unter_str}-Wohungen lag sie darunter."
    return bericht

def getBericht2():
# Bericht generieren
    bericht = f"Seit der Basislegung November 2003 = 100, also im Zeitraum der letzten {highestyear - 2003} Jahre, "
    bericht += f"stiegen die Wohnungsmietpreise in der Stadt Bern um insgesamt {gesamtänderung_str}%. Während die {hihgestwohunung}wohnungen " 
    bericht += f"die stärkste Verteuerung erfuhren ({hihgestwohunung_change}%), wurde bei den {lowestwohunung}wohnungen"
    bericht += f"der geringste Anstiegverzeichnet ({lowesttwohunung_change}%)"
    return bericht

print(getBericht1())
print(getBericht2())
