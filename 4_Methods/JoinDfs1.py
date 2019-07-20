from pandas import DataFrame, merge as Mergedf

df1 = DataFrame({'data': range(5)},
                index = ['O', 'U', 'L', 'O', 'U'])
print '--- df1 ---'
print df1

df2 = DataFrame({'profit': [10, 20, 20]},
                 index =['O', 'O', 'U'])
print '--- df2 ---'
print df2


df3 = DataFrame({ 'ref1': ['A', 'A', 'O', 'O', 'A'],
                  'ref2': [5, 10, 15, 20, 25],
                  'ref3': range(5)})
print '--- df3 ---'
print df3

df4 = DataFrame(np.arange(10).reshape(5,2)
                , index=[['A', 'A', 'O', 'O', 'O'], [20, 10, 10, 10, 20]],
                columns= [ 'col1', 'col2'])
print '--- df4 ---'
print df4
