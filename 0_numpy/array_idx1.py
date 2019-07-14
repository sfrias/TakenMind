import numpy as np

arr = np.arange(0,12)
print arr

print arr[0:5]

arr[2:5] = 13

print arr

arr2 = arr [1:6]
print arr2

arr2[:] = 26
print arr2

arr2 = arr.copy()
arr2[7:11] = 26
print arr2


print arr

