"""
Indexing

For 1d array
array[index]

For 2d array
array[row, column]
"""
import numpy as np

arr = np.array([10,15,20,25,30,35,40,45])
print(arr[0])  # it return 0th index value
print(arr[3])  # it return 3rd index value
print(arr[5])  # it return 5th index value
print(arr[-1]) # it return last index element from array


arr_2d = ([[10,15,20,25],
           [30,35,40,45]])
print(arr_2d[1][3])


"""
Slicing:

array_name[start : stop : step]

start = 0th index (included)

stop = start to stop - 1  (excluded)

step = Interval between elements
"""

# import numpy as np

# arr = np.array([10,15,20,25,30,35,40])

# print(arr[1:5]) # it return array value that start from index=1 to index=4 
#                 #because index=5 in excluded

# print(arr[:3]) # print first 3 element from array

# print(arr[4:]) # print from index=4 to end  element from array

# print(arr[::2]) #  Every 2nd element

# print(arr[::-1])  # Reverse array


# 2D Array Slicing 

# syntax:

# arr[row_start:row_end, col_start:col_end]

# arr_2d = np.array([[20,30,40],
#                   [10,60,70],
#                   [10,20,30]])

# print(arr_2d[1:3 , 1:3])

# print(arr_2d[:,1]) # All rows, column 1

# print(arr_2d[1, :]) # All columns, Row 1

"""
Fancy Indexing :
Fancy indexing is used to Access multiple elements using a list of indices(indexes).
"""

# import numpy as np

# arr = np.array([10,15,20,25,30,35,40])

# It returns the values at indeexs 0, 2 and 4
# print(arr[[0, 2, 4]])

"""
Boolean Indexing :
Boolean indexing is used to filter data based on condition.
"""

import numpy as np

arr = np.array([10,15,20,25,30,35,40,45])

# It returns the values that are greater than 20
print(arr[arr > 20])

# It returns the values that are less than 30
print(arr[arr < 30])
