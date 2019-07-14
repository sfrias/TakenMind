import numpy as np

# Universal array functions

# arange function
A = np.arange(1,45,3)
print 'Example matrix A:', A
# addition function
print 'Addition A+A is :', np.add(A,A)
# sqrt function
print ' Square root is :', np.sqrt(A)
# exp function
print 'exp eA matrix is:', np.exp(A)
# random function


# maximum function
print 'Maximum A,A+A is:',np.maximum(A,A+A)

# minimum function
print 'Minimum A,A+A is:',np.minimum(A,A+A)

# Additional resources
# SciPy.org - functions associated with numpy array.
# on docs.scipy.org