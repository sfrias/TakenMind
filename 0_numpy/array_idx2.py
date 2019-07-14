import numpy as np

arr2d = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,0]])

print "Arr2d Dim:",arr2d.shape,"Type:", arr2d.dtype,"Size:", arr2d.size
print arr2d

slice1 = arr2d[0:2,0:2]

print "slice1 Dim:",slice1.shape,"Type:", slice1.dtype,"Size:", slice1.size
print slice1

slice2 = arr2d[1:,1:]

print "slice2 Dim:",slice2.shape,"Type:", slice2.dtype,"Size:", slice2.size
print slice2

print "Modificacion del elemento 1,1"
arr2d[1][1] = 0

print slice1
print slice2

# Using loops to index
print len(arr2d.shape)

len_rows = arr2d.shape[0]
len_cols = arr2d.shape[1]

print len_rows, len_cols

print arr2d[1:]
print

print arr2d[1:,1:]
print