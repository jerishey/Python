"""
Array Properties:

1. .shape -> This function is used to find the shape of an array in rows and columns

2. .size -> This function is used to find the number of elements in an array

3. .ndim -> This function is used to find the dimension of an array

4. .dtype -> This function is used to find the types of elements present in an array

5. .astype(type) -> This function is used to change the datatype of an array
"""

import numpy as np

# aar_2d = np.array([[1, 2, 3],
#                    [4, 5, 6]])

# # It returns how many rows and columns are present in an array
# print(aar_2d.shape) 

# aar = np.array([[10,20,30],
#                 [40,50,60]])

# # It print(return) total how Many numbers of element are present in an array.
# print(aar.size)

# arr_1d = np.array([1,2,3])
# arr_2d = np.array([[1,2,3],[4,5,6]])
# arr_3d = np.array([[[1,2],[3,4],[5,6],[7,8]]])

# # It returns number of dimensions of an array
# print(arr_1d.ndim)
# print(arr_2d.ndim)
# print(arr_3d.ndim)

# arr = np.array([10,20,30.5,40])

# # It returns the data type of elements present in an array
# print(arr.dtype)


arr = np.array([1.2, 2.5, 3.8])
print(arr.dtype)
int_arr = arr.astype(int)

print(int_arr)
print(int_arr.dtype)