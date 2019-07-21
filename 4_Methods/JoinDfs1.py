import numpy as np
from pandas import DataFrame

df1 = DataFrame({'data': range(5)},
                index= ['O', 'U', 'L', 'O', 'U'])
print '--- df1 ---'
print df1
print df1.index

df2 = DataFrame({'profit': [10, 20, 20]},
                 index =['O', 'O', 'U'])
print '--- df2 ---'
print df2.index

print ' - df2 joined with df1 - '
df3 = df1.join(df2)
print df3
print df3.index
print '==================='
df3 = DataFrame({'ref1': ['A', 'A', 'O', 'O', 'A'],
                 'ref2': [5, 10, 15, 20, 25],
                 'ref3': range(5)})
print '--- df3 ---'
print df3
print df3.index

df4 = DataFrame(np.arange(10).reshape(5,2)
                , index=[['A', 'A', 'O', 'O', 'O'], [20, 10, 10, 10, 20]],
                columns= [ 'col1', 'col2'])
print '--- df4 ---'
print df4
print df4.index

print '--- df4 reindexed to df3 index with level=0, problem pending---'
df5 =df4.reindex(df3.index, level=0)
print df5
print df5.index
print '============'
print df3
print df3.index
print '----'
df6 = DataFrame({ 'ref1': ['A', 'A', 'O', 'O', 'O'],
                  'ref2': [15, 20, 25, 30, 35],
                  'ref3': range(5,10)})
print '--- df6 ---'
print df6
print df6.index
print '--- df4 joined df3 ---'
df7 = df3.join(df6, lsuffix='x', rsuffix= 'y')
print df7
print df7.index
