import numpy as np
from numpy.ma import shape

print np.array([1,2])

# Create multidimensional numpy array
my_list1 = [1,2,3,4]
my_list2 = [5,6,7,8]
my_array1 =np.array([my_list1, my_list2])

print my_array1

print my_array1.shape

print my_array1.dtype

new_array = np.zeros([5,5])
print new_array

new_array1 = np.ones([5,5])
print new_array1

new_array3 = np.eye(5)
print new_array3

new_array4 = np.arange(5,50,3)
print new_array4

new_array2 = np.empty([5,5])
print new_array2