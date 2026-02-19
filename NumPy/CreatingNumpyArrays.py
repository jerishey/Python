# creating NumPy arrays :

# from list :

import numpy as np

arr_1d = np.array([1,2,3,4,5])
print("1D array: ", arr_1d)


# 2D array

arr_2d = np.array([[1,2,3],[4,5,6]])
print("2D array: ", arr_2d)
 

# Multidimension Array

MD_array = np.array([[10,25,40] , [55,70,85] , [70,80,90]])

print(MD_array)

# Zeros(shape) , Ones(shape)  and full(shape,value)
"""
Syntax:
zeros(shape) -> It fill the array as 0 given in shape values means number of rows and column

ones(shape) -> It fill the array as 1 given in shape values means number of rows and column

full(shape , value) -> Thhis function is used in situation where you want to print specific value in an array

"""

zeros = np.zeros((3,4))
print("Zeros array: \n", zeros)


'''
 Output :

Zeros array: 
 [[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
'''

ones = np.ones((2,3))
print("Ones array: \n", ones)

"""
Output :

Ones array: 
 [[1. 1. 1.]
 [1. 1. 1.]]

"""

full = np.full((2,2), 7)
print("Full array: \n", full)


''''
Output :

Full array: 
 [[7 7]
 [7 7]]
'''

# arange (start,stop,step) :- 
# This  Method or function  is use to Generate Sequence of numbers. It is a step based sequence.

# Common uses of arange()
"""
 Loop-like sequences
 Index generation
 Time steps
 Even / odd number
 you can also generate Tables
"""

# Example :

sequence = np.arange(0, 10, 2)
print("Sequence array: \n", sequence)

"""
Output :

Sequence array: 
 [0 2 4 6 8]
"""


# linspace (start,stop,num) :-

"""
linspace() is used when :
You want exact number of values.

you want equal spacing

Used in graph , ML and Math Function

"""


LineSpace = np.linspace(1,20,5)
print(LineSpace)


# random -> np.random is a module in NumPy used to generate random numbers.

# Syntax:
# np.random.random(size)

"""
np.random → NumPy’s random module

.random() → Generates random numbers between 0.0 and 1.0

(2,3) → Shape of the array (2 rows, 3 columns)
"""
random = np.random.random((2,3))
print("Random array: \n", random)
