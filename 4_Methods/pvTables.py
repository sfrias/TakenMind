import numpy as np
import pandas as pd
import seaborn as sns
from numpy import nan
from pandas import Series, DataFrame

# Examples for video were wrong. Now are images
# Not datatable on wikipedia Pivot_tables
url = "https://www.w3schools.com/html/html_tables.asp"

df = pd.read_html(url)
df = df[0]
print type(df)
print df

# iloc[0] as header if is not formatted table
header = df.columns.values

print '--- header ---'
print header
print '--- data ---'
print df.values
print '======'
print df.pivot('Country', 'Company', 'Contact')
print
print '====='
url = 'https://github.com/mwaskom/seaborn-data/blob/master/flights.csv'

df = pd.read_html(url)
df = df[0]
print type(df)
print df

# iloc[0] as header if is not formatted table
header = df.columns.values

print '--- header ---'
print header
print '--- data ---'
print df.values
print '======'
dfpv = df.pivot('year', 'month', 'passengers')
print dfpv
sns.heatmap(dfpv).get_figure().savefig('heat1.png')