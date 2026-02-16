# NumPy
NumPy(Numerical Python) is a fundamental library for Python numerical computing. It provides efficient multi-dimensional array objects and various mathematical functions for handling large datasets making it a critical tool for professionals in fields that require heavy computation.
<br>

## Features of NumPy
```bash
1. N-Dimensional Arrays -> NumPy's core feature is ndarray, a N-dimensional array object that supports homogeneous data types.

2. Arrays with High Performance -> Arrays are stored in contiguous memory locations, enabling faster computations than Python lists (Please see Numpy Array vs Python List for details).

3. Broadcasting -> This allows element-wise computations between arrays of different shapes. It simplifies operations on arrays of various shapes by automatically aligning their dimensions without creating new data.

4.Vectorization -> Eliminates the need for explicit Python loops by applying operations directly on entire arrays.

5. Linear algebra -> NumPy contains routines for linear algebra operations, such as matrix multiplication, decompositions, and determinants.
```
## Installing NumPy in Python
```bash
>>> pip install numpy

# You can download numpy by writing the above line in your terminal or VS code terminal.
```
### Once installed, import the library with the alias np
```bash
>>> import numpy as np

# You have to import the library before using
# You can import the library by using these lines
```
## Example:- 
```bash
import numpy as np

a1 = np.array([1, 2, 3])    # 1D array
a2 = np.array([[1, 2], [3, 4]]) # 2D array
a3 = np.array([[[1, 2], [3, 4]],    # 3D array
               [[5, 6], [7, 8]]])

print(a1)
print(a2)
print(a3)
```
# Basics of NumPy Arrays
NumPy stands for Numerical Python and is used for handling large, multi-dimensional arrays and matrices. Unlike Python's built-in lists NumPy arrays provide efficient storage and faster processing for numerical and scientific computations. It offers functions for linear algebra and random number generation making it important for data science and machine learning.

## Types of Array

### 1. One Dimensional Array
 A one-dimensional array is a type of linear array.
```bash
import numpy as np

a = [1, 2, 3, 4]

arr = np.array(a)

print("List in python : ", a)

print("Numpy Array in python :", arr)

# Output:-

List in python : [1, 2, 3, 4]
Numpy Array in python : [1 2 3 4]
```

### 2. Multi-Dimensional Array
 A Multi-Dimensional Array is an array that can store data in more than one dimension such as rows and columns. In simple terms it is a array of arrays.
<br>
For example a 2D array is like a table with rows and columns where each element is accessed by two indices: one for the row and one for the column. Higher dimensions like 3D arrays involve adding additional layers.
```bash
import numpy as np

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]

sample_array = np.array([list_1, 
                         list_2,
                         list_3])

print("Numpy multi dimensional array in python\n", sample_array)

# Output:-
Numpy multi dimensional array in python
 [[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
```