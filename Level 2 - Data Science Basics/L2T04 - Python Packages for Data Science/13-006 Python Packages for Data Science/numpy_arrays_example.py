import numpy as np
np.random.seed(0)  # seed for reproducibility

# Create various random arrays using numpy
x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

# One-dimensional array
print('x1: ')
print(x1)

# Indexing a one-dimensional array
print('x1[0]: ')
print(x1[0])

print('x1[-1]: ')
print(x1[-1])

# Two-dimensional array
print('x2: ')
print(x2)

# Indexing a two-dimensional array
print('x2[2, -1]: ')
print(x2[2, -1])

# Three-dimensional array
print('x3: ')
print(x3)

# Explore numpy array attributes
print("x3 ndim: ", x3.ndim) # number of array dimensions
print("x3 shape:", x3.shape) # tuple of array dimensions
print("x3 size: ", x3.size) # number of elements in an array
print("dtype:", x3.dtype) # type of data in the array

print("itemsize:", x3.itemsize, "bytes") # size of each element in bytes
print("nbytes:", x3.nbytes, "bytes") # total bytes for the array
