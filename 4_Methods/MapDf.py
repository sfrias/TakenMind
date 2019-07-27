from pandas import DataFrame

df = DataFrame({'city': ['Tarragona', 'Barcelona', 'Lleida', 'Girona'],
                'pref': ['977', '93', '973', '972']})

print df

Habs = {'Tarragona': 0.8,
        'Barcelona': 5.6,
        'Lleida': 0.4,
        'Girona': 0.7}

df['Mhabs'] = df['city'].map(Habs)

print df