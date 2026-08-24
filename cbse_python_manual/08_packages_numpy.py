# CBSE Python reference: packages and NumPy
# Install in Anaconda Prompt (as taught in the manual):
# conda install numpy

# Import styles covered by the manual:
# import numpy
# import numpy as np
# from numpy import array
# from numpy import array as arr

import numpy as np

# Create an array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Arithmetic can be applied to the whole array
print(arr + 5)
print(arr / 5)
print(arr ** 2)

# Accessing an element (index starts at 0)
print(arr[1])

# Useful array creation functions
print(np.zeros((4, 3)))
print(np.full((3, 4), 6))
print(np.arange(0, 30, 5))

# Array properties / information
print(type(arr))
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)

# Basic mathematical functions
print(np.max(arr))
print(np.sum(arr))
