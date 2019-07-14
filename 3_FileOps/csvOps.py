# Operations with csv files from/to Dataframes

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Read with pandas.read_csv, with header
df = pd.read_csv('demo_head.csv')
print df

print
# Read with pandas.read_csv, without header
df2 = pd.read_csv('demo.csv',header=None)
print df2

print
# Read with pandas.readtable adjusting separator and head
print 'With pandas.readtable, near to be deprecated'
df3 = pd.read_table('demo_readtable.csv',sep='@')
print df3

print
# Read with read_csv instead pandas.readtable(deprecation)
df4 = pd.read_csv('demo_readtable.csv',sep='@')
print 'With pandas.read_csv instead pandas.readtable'
print df4

print
# Partial rows importing
df5 = pd.read_csv('demo.csv',header=None, nrows=2)
print 'df5'
print df5

print
# Dump to csv file
df5.to_csv('output_df5.csv', header=None, sep='%')
# Read newly. Index is a new column
df6 = pd.read_csv('output_df5.csv', sep='%')
print 'Dataframe with index. Error!! header are data'
print df6

print
# Dump to csv file without index, selecting columns
# no header, and encoding utf-8
df5.to_csv('output3_df5.csv', sep='\t', columns=[0,2],
           index=False, header=False,encoding='utf-8')
# Read newly
df6 = pd.read_csv('output3_df5.csv', sep='\t', header=None)
print 'Create csv with columns 0,2. Read after to df6'
print df6
