import pandas as pd
import matplotlib.pyplot as plt
from getBEData import getChart1

# Funktion zum Erstellen des Linien-Diagramms und Speichern als .png-Datei
def create_line_chart():
    # Aufruf der Funktion getChart1() aus getBEData.py, um die Daten zu erhalten
    df = getChart1()

    # Linien-Diagramm erstellen
    df.plot(kind='line')

    # Diagramm anpassen
    plt.ylabel('Index')

    # Tiefste Jahresangabe links anzeigen
    plt.gca().invert_xaxis()

    # Linienfarben als Hex-Werte angeben
    colors = ['#222017','#6E6E70', '#B4B4B6', '#F4B2A3', '#E82038', '#E86E61'] 

    for i, line in enumerate(plt.gca().get_lines()):
        line.set_color(colors[i])

    # Legende mit definierten Farben erstellen
    legend_labels = df.columns
    legend_handles = [plt.Line2D([], [], color=colors[i]) for i in range(len(legend_labels))]
    plt.legend(legend_handles, legend_labels)

    # Diagramm als .png-Datei speichern
    plt.tight_layout(savefig('diagrams/linien_diagramm.png', dpi=72))
    return plt



# Aufruf der Funktion zum Erstellen des Linien-Diagramms

