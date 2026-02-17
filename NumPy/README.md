# What is NumPy :
NumPy is a core Python library for numerical computing, built for handling large arrays and matrices efficiently.
Numpy was created in 2005 Travis Oliphant.It is an open source project that you can use it freely.
<br>
NumPy Stands for Numerical Python.
<br>

# What is NumPy Used for?
```bash
With NumPy, you can perform a wide range of numerical operations, including:

1. Creating and manipulating arrays.
2. Performing element-wise and matrix operations.
3. Generating random numbers and statistical calculations.
4. Conducting linear algebra operations.
5. Working with Fourier transformations.
6. Handling missing values efficiently in datasets.
```
<br>

# Why Learn NumPy?
```bash
1. NumPy speeds up math operations like addition and multiplication on large groups of numbers compared to regular Python.

2. It’s good for handling large lists of numbers (arrays), so you don’t have to write complicated loops.

3. It gives ready-to-use functions for statistics, algebra and random numbers.

4. Libraries like Pandas, SciPy, TensorFlow and many others are built on top of NumPy.

5. NumPy uses less memory and stores data more efficiently, which matters when working with lots of data.
```
# NumPy Introduction :
NumPy (Numerical Python) is an open source Python library that’s widely used in science and engineering. The NumPy library contains multidimensional array data structures, such as the homogeneous, N-dimensional ndarray, and a large library of functions that operate efficiently on these data structures
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

arr = np.array([10 ,20,30,40,50])

print(arr)

print(type(arr))
```
<br>

# Basics of NumPy Arrays
NumPy’s main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of non-negative integers. In NumPy dimensions are called axes.

## NumPy array attributes and methods
```bash
1. arange() 
Creates a NumPy array containing evenly spaced values within a specified range.
It is commonly used to generate sequences of numbers automatically.

2. reshape()
Changes the structure (shape) of an existing array without altering its data.
The total number of elements must remain the same.

3. shape
Returns a tuple representing the size of each dimension of the array.
It tells how many rows, columns, or higher dimensions the array has.

4. ndim
Returns the number of dimensions (axes) of the array.
It helps determine whether the array is 1D, 2D, 3D, etc.

5. dtype
Returns the data type of the elements stored in the array.
All elements in a NumPy array share the same data type.

6. dtype.name
Returns the name of the array’s data type as a string.
It provides a readable format of the data type.

7. itemsize
Returns the size in bytes occupied by each element of the array.
It shows how much memory one element uses.

8. size
Returns the total number of elements present in the array.
It is equal to the product of the array’s dimensions.

9. type()
Returns the class type of an object.
For NumPy arrays, it indicates that the object is an ndarray.

10. array()
Creates a NumPy array from a list, tuple, or other sequence.
It converts input data into a fixed-type, efficient array structure.
```

<b> Example : </b>
```bash
>>> import numpy as np
>>> a = np.arange(15).reshape(3, 5)
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])

>>> a.shape
(3, 5)

>>> a.ndim
2

>>> a.dtype.name
'int64'

>>> a.itemsize
8

>>> a.size
15

>>> type(a)
<class 'numpy.ndarray'>

>>> b = np.array([6, 7, 8])
>>> b
array([6, 7, 8])

>>> type(b)
<class 'numpy.ndarray'>
```
## Creating NumPy Arrays :
NumPy provides multiple efficient methods for creating arrays, each suited to different use cases and data sources. This article covers the most commonly used techniques for creating NumPy arrays, along with when and why to use each method.

```bash
1. numpy.array(): Numpy array object in Numpy is called ndarray. We can create ndarray using this function.

>>> Syntax: numpy.array(parameter)

2. numpy.fromiter(): The fromiter() function create a new one-dimensional array from an iterable object.

>>> Syntax: numpy.fromiter(iterable, dtype, count=-1)

3. . numpy.arange(): This is an inbuilt NumPy function that returns evenly spaced values within a given interval.

>>> Syntax:  numpy.arange( start , stop, step , dtype=None )

4. numpy.linspace(): This function returns evenly spaced numbers over a specified between two limits. 

>>> Syntax: numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)

5. numpy.empty(): This function create a new array of given shape and type without initializing value.

>>> Syntax: numpy.empty(shape, dtype=float, order='C')

6.  numpy.ones(): This function is used to get a new array of given shape and type filled with ones (1).

>>> Syntax: numpy.ones(shape, dtype=None, order='C')

7. numpy.zeros(): This function is used to get a new array of given shape and type filled with zeros (0). 

>>> Syntax: numpy.zeros(shape, dtype=None, order='C')

```
<b> Example : </b>
```bash
import numpy as np

# numpy.array()
student_marks = np.array([78, 85, 90, 66, 72])
print("Student Marks:", student_marks)
# Output: Student Marks: [78 85 90 66 72]


# numpy.fromiter()
square_numbers = np.fromiter((x*x for x in range(5)), dtype=int)
print("Square Numbers:", square_numbers)
# Output: Square Numbers: [ 0  1  4  9 16]


# numpy.arange()
numbers = np.arange(1, 11, 2)
print("Numbers using arange:", numbers)
# Output: Numbers using arange: [1 3 5 7 9]


# numpy.linspace()
line_values = np.linspace(0, 1, 5)
print("Linspace Values:", line_values)
# Output: Linspace Values: [0.   0.25 0.5  0.75 1.  ]


# numpy.empty()
empty_array = np.empty((2, 3))
print("Empty Array:\n", empty_array)
# Output: (Random uninitialized values, example)
# [[1.482e-323 1.976e-323 2.470e-323]
#  [2.964e-323 3.458e-323 3.952e-323]]


# numpy.ones()
ones_array = np.ones((2, 2))
print("Ones Array:\n", ones_array)
# Output:
# [[1. 1.]
#  [1. 1.]]


# numpy.zeros()
zeros_array = np.zeros((3, 2))
print("Zeros Array:\n", zeros_array)
# Output:
# [[0. 0.]
#  [0. 0.]
#  [0. 0.]]
```
