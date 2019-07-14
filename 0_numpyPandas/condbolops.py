import numpy as np

# Each member 'a'
x = np.array([100, 400, 500, 600])
# Each member 'b'
y = np.array([10, 15, 20, 25])
# Each member condition
cond = np.array([True, True, False, False])

# Use loops indirectly to perform this.
z = [a if cd else b for a, cd, b in zip(x, cond, y)]
print z
#np.where(cd, ValueYes, ValueNo)
z2 = np.where(cond, x, y)
print z2

z3 = np.where( x > 0, 0, 1)
print z3

# Standard functions of numpy

print x.sum()

n2 = np.array([[1,2],[3,4]])
# Column sum
print n2.sum(0)
# Row sum
print n2.sum(1)

print x.mean()
print x.std()
print x.var()

# logical operations
cond2 = np.array([True, False, True])
print cond2.all()  # and operation
print cond2.any()  # or operation

# Sorting in numpy arrays
uns = np.array([1, 2, 8, 10, 7, 3])
uns.sort()
print uns

arr2 = np.array(['solid', 'solid', 'liquid', 'solid', 'solid', 'solid', 'gas'])
print np.unique(arr2)

# Ini function, contains or not
print np.in1d(['solid', 'liquid', 'plasma'], arr2)