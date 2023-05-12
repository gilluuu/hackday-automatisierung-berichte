import pandas as pd
import matplotlib.pyplot as plt
from plotnine import ggplot, aes, geom_line, geom_bar



data = {'Name': ['John', 'Jane', 'Sue', 'Bob'],
        'Age': [35, 28, 42, 21],
        'Gender': ['M', 'F', 'F', 'M'],
        'Salary': [50000, 75000, 60000, 40000]}


data2 = {
    'year': [2015, 2016, 2017, 2018, 2019, 2020],
    'sales': [1000, 1500, 2000, 200, 3000, 3500]
}

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)

salary_bar = ggplot(df) + aes(x='Name', y='Salary') + geom_bar(stat='identity')
sales_line = ggplot(df2) + aes(y= 'sales', x='year') + geom_line()

salary_bar.save('diagrams/salary_bar_chart.png')
sales_line.save('diagrams/sales_line.png')

def create_sentence():

    string = 'Der Berner Index der Wohnungsmietpreise erreicht im November 2022 einen Stand von 124,3 Punkten (Basis: November 2003 = 100), was einer Zunahme um 1,1% gegenüber dem Vorjahr entspricht.'
    
    return string


text = create_sentence()

print(text)

