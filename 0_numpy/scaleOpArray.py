from __future__ import division
import numpy as np

print 5/2

array1 = np.array([[1,2,3,4],[5,6,7,8]])
print array1.dtype
print array1

# Multiplication
array2 = array1 * array1
print array2.dtype
print array2

#Exponentation
array3 = array2**(1/2)
print array3.dtype
print array3

#Substraction
array4 = array1 -array3
print array4.dtype
print array4

# Reciprocal

arrayp = 1/array1

print arrayp.dtype
print arrayp
print arrayp.min()
print arrayp.max()

#Division
arrayd = array1/arrayp

print arrayd.dtype
print arrayd
print arrayd.min()
print arrayd.max()
