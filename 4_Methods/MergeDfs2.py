import  numpy as np

from pandas import DataFrame, merge as Mergedf

df1 = DataFrame({'data': range(5)},
                index = ['O', 'U', 'L', 'O', 'U'])
print '--- df1 ---'
print df1

df2 = DataFrame({'profit': [10, 20, 20]},
                 index =['O', 'O', 'U'])
print '--- df2 ---'
print df2

print '- pandas merge classic index to index -'
print Mergedf(df1, df2, left_index= True, right_index= True)

print 'Real case with labels and DataFrame index as query table'
df1 = DataFrame({'reference':['O', 'U', 'L', 'O', 'U'],
                 'data': range(5)},
                )
print '--- df1 ---'
print df1

df2 = DataFrame({'profit': [10, 20]},
                 index =['O', 'U'])
print '--- df2 ---'
print df2

# Common default error of not define indexes on Dataframes....
# in _validate_specification lidx=self.left_index, ridx=self.right_index))
# MergeError: No common columns to perform merge on.
# Merge options: left_on=None, right_on=None, left_index=False, right_index=False

print  "- pandas.merge(df1, df2, left_on= 'reference', right_index = True) -"
print Mergedf(df1, df2, left_on= 'reference', right_index= True)
print '==============='
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

print "- pandas.merge(df3, df4, left_on= ['ref1', 'ref2'] , right_index= True) -"
print Mergedf(df3, df4, left_on= ['ref1', 'ref2'] , right_index= True)