import pandas as pd
import matplotlib.pyplot as plt
from getBEData import getChart1,getTable1
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


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
    plt.grid(axis="y", color = "black")

    plt.savefig('./diagrams/linien_diagramm.png', dpi=72, transparent=True)

def createtable1():
    df = getTable1()
    df.insert(0, '', ['1 Zimmer', '2 Zimmer', '3 Zimmer', '4 Zimmer', '5 Zimmer', 'Total'])
    fig, ax = plt.subplots()
    ax.axis('off')
    font_path = "UniversLTStd-Light.ttf"  # Make sure the path is correct
    font_prop = fm.FontProperties(fname=font_path)
    table = plt.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    highlight_color = (248 / 255, 199 / 255, 186 / 255)

    for key, cell in table.get_celld().items():
        cell.set_fontsize(12)
        cell.get_text().set_fontproperties(font_prop)
        cell.get_text().set_horizontalalignment('right')  # Align text to the right
        cell.set_linewidth(0)  # Set edge linewidth to zero
        if key[1] == df.columns.get_loc('November 2022') + 1 and key[0] != 0:  # Exclude header row
            cell.set_facecolor(highlight_color)


    plt.savefig('table.png',dpi=1000,transparent=True)


