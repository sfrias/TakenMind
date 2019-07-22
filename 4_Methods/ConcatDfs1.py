from pandas import Series, DataFrame,\
    concat as pdconcat
from numpy import arange, random,\
    concatenate as npconcat

# Create numpy arrays
a1 = random.randn(25).reshape(5,5)
b1 = arange(25).reshape(5,5)

print '--- a1 ---'
print a1
print '--- b1 ---'
print b1

# Concatenate/link numpy arrays
print '--- Concatenate a1, b1 rows(axis=0)'
print npconcat([a1,b1], axis=0)

print '--- Concatenate a1, b1 columns(axis=1)'
print npconcat([a1,b1], axis=1)

# Create Series
s1 = Series([100, 200, 300], index=['A', 'B', 'C'])
s2 = Series([400, 500], index=['D', 'E'])
print '--- s1 ---'
print s1
print '--- s2 ---'
print s2
# Concatenate/link Series
print '--- concat(s1,s2) axis = 0---'
print pdconcat([s1,s2])
print '--- concat(s2,s1) axis = 0---'
print pdconcat([s2,s1])
print '--- series concat(s1,s2) axis = 0---'
s = pdconcat([s1,s2], axis= 0,
             keys =['s1', 's2'],
             names=['idx_s', 'idx'])
print s

print '--- series concat(s1,s2) axis = 1---'
s = pdconcat([s1,s2], axis= 1, sort= False,
             keys =['s1', 's2'],
             names=['idx'])
print s
# Create Dataframes

# Concatenate/link Dataframes