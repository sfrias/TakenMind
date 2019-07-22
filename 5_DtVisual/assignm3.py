import numpy as np
import pandas as pd
import seaborn as sns
from numpy import nan
from pandas import Series, DataFrame




csv = 'https://raw.githubusercontent.com/resbaz/' \
      'r-novice-gapminder-files/master/data/' \
      'gapminder-FiveYearData.csv'

df = pd.read_csv(csv)
print df

#header = df.columns.values
#print '--- header ---'
#print header
#print '--- data ---'
#print df.values
#print '======'
dfpv = dfpv.drop_duplicates('year', 'continent')
dfpv = df.pivot('year', 'continent', 'lifeExp')

print dfpv
sns.heatmap(dfpv).get_figure().savefig('heat2.png')