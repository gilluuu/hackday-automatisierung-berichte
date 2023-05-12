def create_sentence(index, vorjahresindex):

    print('index:',index,'vorjahr index', vorjahresindex )

    prozentsatz = "{:.2f}%".format(abs((index - vorjahresindex)/vorjahresindex * 100))


    if index > vorjahresindex:
        wort = 'einer Zunahme um ' + prozentsatz
    elif index < vorjahresindex:
        wort = 'einer Abnahme um ' + prozentsatz
    else:
        wort = 'einem unveränderten index'



    string = '''Der Berner Index der Wohnungsmietpreise erreicht im November
                2022 einen Stand von ''' + str(index) + ''' Punkten (Basis: November 2003 = 100),
                was ''' + wort + ''' gegenüber dem Vorjahr entspricht.'''
    
    return string


text = create_sentence(9, 10)

print(text)