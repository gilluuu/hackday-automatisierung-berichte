#!/usr/bin/env python
# coding: utf-8
import pandas as pd

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

def getTable1():
    df_roh = pd.read_excel('data/Daten_Mietpreise.xlsx')
    df = getTableIndex(df_roh)
    columns = ['STTE_ZI', 'Total_1', 'Total_2', 'Total_3', 'Total_4', 'Total_5', 'Total_Total']

    df = df[columns]
    df.index = df['STTE_ZI']
    df = df.sort_index(ascending=False)
    df = df.iloc[:5].transpose()#print()
    df.columns = df.iloc[0]
    df = df.iloc[1:]
    df = df.reset_index()
    df['index'] = indexneu[1:]
    df.columns = [x for x in df.columns]
    df['index'] = df['index'].apply(lambda x: x.split('_')[1] + ' Zimmer')
    df['index'] = df['index'].apply(lambda x: x.replace('Total Zimmer', 'Total'))
    df.index = df['index']
    del df['index']
    df.columns = ['November ' + str(x) for x in df.columns]
    
    for column in df.columns:
        df[column] = 100 * df[column]
    
    # Veränderung berechnen. 
    df['Veränderung in %'] = 100 - 100 * df.iloc[:,1] / df.iloc[:,0]
    
    # Werte auf eine Nachkommastelle runden.
    
    return(df)


def getChart1():
    df_roh = pd.read_excel('data/Daten_Mietpreise.xlsx')
    df = getTableIndex(df_roh)
    columns = ['STTE_ZI', 'Total_1', 'Total_2', 'Total_3', 'Total_4', 'Total_5', 'Total_Total']

    df = df[columns]
    
    df.columns = ['Jahr', '1 Zimmer', '2 Zimmer', '3 Zimmer', '4 Zimmer', '5 Zimmer', 'Total']
    df.set_index('Jahr', inplace=True, drop=True)
    return(df)