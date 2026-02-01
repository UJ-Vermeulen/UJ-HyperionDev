# Import numpy to use array and other functions
import numpy as np

# Question: Why doesn’t np.array((1, 0, 0), (0, 1, 0), (0, 0, 1, dtype=float)
# create a two-dimensional array?
# Answer: The problem is with the () placement.  In a multi-dimensional
# array The outermost structure must be a single list,
# And not multiple arguments.
# Corrected version
np_array_2d = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)], dtype=float)
print('\nResults of np.array((1, 0, 0), (0, 1, 0), (0, 0, 1, dtype=float)'
      + ' after correcting to np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)],'
      + f' dtype=float): \n{np_array_2d}')

# Question: What is the difference between a = np.array([0, 0, 0]) and
# a = np.array([[0, 0, 0]])?
# Answer:⬇⬇
# a1 = np.array([0, 0, 0]) creates a 1D array
a1 = np.array([0, 0, 0])
# a2 = np.array([[0, 0, 0]]) creates a 2D array
a2 = np.array([[0, 0, 0]])

print(f'\na1 = np.array([0, 0, 0]) creates a 1D array: {a1.shape}')
print(f'a2 = np.array([[0, 0, 0]]) creates a 2D array: {a2.shape}')

# Question: A 3 by 4 by 4 array is created with
# arr = np.linspace(1, 48,48).reshape(3, 4, 4). Index or slice
# this array to obtain the following:
# 1: 20.0
# 2: [9.10.11.12.]
# 3: [[33.34.35.36.][37.38.39.40.][41.42.43.44.][45.46.47.48.]]
# 4: [[5.6.],[21.22.][37.38.]]
# 5: [[36.35.][40.39.][44.43.][48.47.]]
# 6: [[13.9.5.1.][29.25.21.17.][45.41.37.33.]]
# 7: [[1.4.][45.48.]]
# 8: [[25.26.27.28.],[29.30.31.32.],[33.34.35.36.],[37.38.39.40.]]

# use the array provided
arr = np.linspace(1, 48, 48).reshape(3, 4, 4)

# 1. 20.0
val_20 = arr[1, 1, 3]
print("\n1. 20.0:", val_20)

# 2. [9. 10. 11. 12.]
single_row = arr[0, 2, :]
print("\n2. [9. 10. 11. 12.]:", single_row)

# 3. [[33.34.35.36.][37.38.39.40.][41.42.43.44.][45.46.47.48.]]
list_array = arr[2, :, :]
print("\n3. Last matrix:\n", list_array)

# 4. [[5. 6.], [21. 22.], [37. 38.]]
specific_values = arr[:, 1:3, 1:3]
print("\n4. [[5. 6.], [21. 22.], [37. 38.]]:\n", specific_values)

# 5. [[36. 35.], [40. 39.], [44. 43.], [48. 47.]]
flipped_column = arr[2, :, ::-1][:, :2]
print("\n5. [[36. 35.], [40. 39.], [44. 43.], [48. 47.]]:\n", flipped_column)

# 6. [[13. 9. 5. 1.], [29. 25. 21. 17.], [45. 41. 37. 33.]]
flipped_rows = arr[:, ::-1, ::-1]
print("\n6. [[13. 9. 5. 1.], [29. 25. 21. 17.], [45. 41. 37. 33.]]:\n",
      flipped_rows)

# 7. [[1. 4.], [45. 48.]]
corner_values = arr[:, [0, -1], [0, -1]]
print("\n7. [[1. 4.], [45. 48.]]:\n", corner_values)

# 8. [[25.26.27.28.],[29.30.31.32.],[33.34.35.36.],[37.38.39.40.]]
one_block_array = arr[1, 1:, :]
print("\n8. Block of values:\n", one_block_array)
