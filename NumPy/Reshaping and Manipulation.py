"""
1. .reshape() -> This function is used to change the shape of an array

Syntax:
array.reshape(rows, columns)
"""

import numpy as np

arr = np.array([1,2,3,4,5,6])
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)

"""
2. .fallten() -> Returns a new copy of the array.

Syntax:
array.flatten() 

3. .ravel() -> Returns a view of the original array.
Syntax:
array.ravel() 
"""

import numpy as np

arr_2d = np.array([[10,15,20],[25,30,35]])
print(arr_2d.ravel())
print(arr_2d.flatten()) 