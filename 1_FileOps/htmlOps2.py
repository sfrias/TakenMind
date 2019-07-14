import pandas as pd

from pandas import DataFrame

from pandas import read_html

url= 'https://www.fdic.gov/bank/' \
     'individual/failed/banklist.html'

dflist = pd.io.html.read_html(url)

print 'N.Tables:',len(dflist)
print 'N.Elements first table:',len(dflist[0])
print '----------'
df0 = dflist[0]
print 'HEADERS'
print df0.columns.values
print '----------'
df0.to_csv('failbank1.csv', encoding='utf-8', index=None)
print '----------'
