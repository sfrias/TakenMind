from numpy import nan
from pandas import Series

s1 = Series([10, 20, 40, 50, 20, 10, 50, 40])

print s1.values
print '---'
print s1.replace(50, nan).values
print '---'
print s1.replace([10, 20, 50], [100, 200, 500]).values
print '---'
print s1.replace({10: 100, 20: nan, 40: 400}).values
