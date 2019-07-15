from pandas import Series

sr1 = Series([100, 200, 300], index=['A', 'B', 'C'])

print sr1
print '--------'
print 'A:', sr1['A']
print 'Index 0:',sr1[0]
print 'Idx 0:2'
print sr1[0:2]
print '>150'
print sr1[sr1>150]
print '==300'
print sr1[sr1==300]