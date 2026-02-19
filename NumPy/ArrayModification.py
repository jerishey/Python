"""
For using insert function
Syntax -> np.insert(array, index, value, axis=None)

Args :
array - original array
index - index where you insert value or data
value - data
axis - Not necessary in 1d array

In 2d array
axix = 0 # row-wise
axis = 1 # column-wise
"""

import numpy as np

# # Insert in 1d array
# arr = np.array([10,20,30,40,50,60])
# print(arr)

# new_arr = np.insert(arr, 2, 100, axis=0)
# print(new_arr)

# # Insert in 2d array
# arr_2d = np.array([[1,2],[3,4]])
# print(arr_2d)

# # insert a new row at index 1
# new_arr_2d = np.insert(arr_2d, 1, [5,6], axis=0)
# print(new_arr_2d)

"""
For using extend function
Syntax -> np.extand(arr_one, arr_two)
"""

arr = np.array([10,15,20])

# append is used to add elements at the end of the array
new_arr = np.append(arr, [25,30,35])
print(new_arr)