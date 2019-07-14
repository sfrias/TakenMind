from numpy import  nan
from pandas import DataFrame, Series

df1 = DataFrame([[0, 1, 2, nan], [4, 5, 6, 7],
                [8, 9, nan, nan], [12, nan, nan, nan]])
print df1
print '----------'
print df1.dropna(thresh=3)