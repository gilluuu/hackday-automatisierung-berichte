#!/usr/bin/env python
# coding: utf-8

# Importieren der nötigen Erweiterungen. 
import pandas as pd

# Funktion zum Extrahieren der Daten zur Teuerung. 
def getTableTeuerung(df_roh):
    schnittmarken = df_roh[df_roh['Teuerung'] == 'STTE'].index

    df_teuerung = df_roh[schnittmarken[0]:schnittmarken[1]]
    df_teuerung = df_teuerung.dropna(how='any')
    df_teuerung.columns = df_teuerung.iloc[0]

    l1 = df_teuerung.iloc[0].to_list()
    l2 = df_teuerung.iloc[1].to_list()
    columns = list(zip(l1,l2))
    df_teuerung.columns = columns
    df_teuerung = df_teuerung.iloc[2:]
    return df_teuerung 

# Funktion zum Extrahieren der Daten zum Index. 
def getTableIndex(df_roh):
    schnittmarken = df_roh[df_roh['Teuerung'] == 'STTE'].index
    
    df_index = df_roh[schnittmarken[1]:schnittmarken[2]]
    df_index = df_index.dropna(how='any')
    df_index.columns = df_index.iloc[0]

    l1 = df_index.iloc[0].to_list()
    l2 = df_index.iloc[1].to_list()
    columns = list(zip(l1,l2))
    columns = [x[0] + '_' + str(x[1]) for x in columns]
    df_index.columns = columns
    df_index.columns = columns
    df_index = df_index.iloc[2:]
    df_index = df_index.sort_values(by='STTE_ZI', ascending=False)
    return df_index

#Funktion zum Extrahieren der Daten zum Durchschnitt.
def getTableDurchschnitt(df_roh):
    schnittmarken = df_roh[df_roh['Teuerung'] == 'STTE'].index
    
    df_durchschnitt = df_roh[schnittmarken[2]:]
    df_durchschnitt = df_durchschnitt.dropna(how='any')
    df_durchschnitt.columns = df_durchschnitt.iloc[0]

    l1 = df_durchschnitt.iloc[0].to_list()
    l2 = df_durchschnitt.iloc[1].to_list()
    columns = list(zip(l1,l2))
    columns = [x[0] + '_' + str(x[1]) for x in columns]
    df_durchschnitt.columns = columns
    df_durchschnitt = df_durchschnitt.iloc[2:]
    return df_durchschnitt

# Funktion zum Generieren der Tabelle 1.
def getTable1():
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT3BcxRrekN-89urzI14E0BF34fK9EthqfGn2Oi1UhLxMfjl6Sh1HQVawLTZDzEo_nFgu-OW0uPL0Id/pub?gid=1864584239&single=true&output=csv'
    df_roh = pd.read_csv(url)
    df = getTableIndex(df_roh)
    columns = ['STTE_ZI', 'Total_1', 'Total_2', 'Total_3', 'Total_4', 'Total_5', 'Total_Total']
    df = df[columns]
    df.index = df['STTE_ZI']
    df = df.sort_index(ascending=False)
    df = df.iloc[:5].transpose()
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    df = df.reset_index()
    df['index'] = df['index'].apply(lambda x: x.split('_')[1] + ' Zimmer')
    df['index'] = df['index'].apply(lambda x: x.replace('Total Zimmer', 'Total'))
    df.index = df['index']
    del df['index']
    df.columns = ['November ' + str(x) for x in df.columns]

    for column in df.columns:
        df[column] = df[column].apply(lambda x: float(x.replace(',', '.')))
        df[column] = 100 * df[column]

    # Veränderung berechnen. 
    df['Veränderung in % zum Vorjahr'] = 100 - 100 * df.iloc[:,1] / df.iloc[:,0]

    # Werte auf eine Nachkommastelle runden.
    for column in df.columns:
        df[column] = df[column].apply(lambda x: round(x,2))
    return(df)

# Funktion zum Generieren des Chart 1. 
def getChart1():
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT3BcxRrekN-89urzI14E0BF34fK9EthqfGn2Oi1UhLxMfjl6Sh1HQVawLTZDzEo_nFgu-OW0uPL0Id/pub?gid=1864584239&single=true&output=csv'
    df_roh = pd.read_csv(url)

    df = getTableIndex(df_roh)
    columns = ['STTE_ZI', 'Total_1', 'Total_2', 'Total_3', 'Total_4', 'Total_5', 'Total_Total']

    df = df[columns]
    
    df.columns = ['Jahr', '1 Zimmer', '2 Zimmer', '3 Zimmer', '4 Zimmer', '5 Zimmer', 'Total']
    df.set_index('Jahr', inplace=True, drop=True)
    
    for column in df.columns:
        df[column] = df[column].apply(lambda x: float(x.replace(',', '.')))
        df[column] = 100 * df[column]
    return(df)