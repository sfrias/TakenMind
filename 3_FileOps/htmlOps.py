import pandas as pd

from pandas import DataFrame

from pandas import read_html

url= 'https://countrycode.org'

dflist = pd.io.html.read_html(url)

print 'N.Elements:',len(dflist)
print '----------'
df0 = dflist[0]
print df0.columns.values
print '----------'
df1 = dflist[1]
print df1.columns.values
print '----------'
print df0.to_csv('pref1.csv')
print '----------'
print df1.to_csv('pref2.csv')