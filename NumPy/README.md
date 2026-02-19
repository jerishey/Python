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

# NumPy Array Properties:
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

## astype() in NumPy :
astype()  method is used to change the data type (datatype) of a NumPy array.
<br>
This method helps in type conversion.
<br>
This method is used because sometimes Data comes as string , but we need numbers.In this situation we can use astype to convert data from string to integer and also convert float to an interger.
<br>

<b>Syntax:</b>

```bash
array.astype(new_datatype)

```
<br>

Example:

```bash

# astype ()

import numpy as np

arr = np.array([1.2,2.4,3.5,4.7,5.9])
print(arr)
print(arr.dtype)

arr2 = arr.astype(int)
print(arr2)
print(arr2.dtype)

```
# Creating NumPy Arrays :
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

# NumPy Array Operations:

```bash
import numpy as np

arr= np.array([10,20,30,40,50])

print(arr + 10)  # addition
print(arr - 10)  # Substraction
print(arr * 10)  # Multiplication
print(arr / 10)  # Division
print(arr ** 2) # Exponetial
print(arr % 3)  # Modules (reminders)
print(arr // 3) # Floor division 


Output :

[20 30 40 50 60]
[ 0 10 20 30 40]
[100 200 300 400 500]
[1. 2. 3. 4. 5.]
[ 100  400  900 1600 2500]
[1 2 0 1 2]
[ 3  6 10 13 16]
```
# NumPy - Arithmetic Operations:
Arithmetic operations are used for numerical computation and we can perform them on arrays using NumPy. With NumPy we can quickly add, subtract, multiply, divide and get power of elements in an array. NumPy performs these operations even with large amounts of data.
```bash
1. Addition -> Addition is an arithmetic operation where the corresponding elements of two arrays are added together. In NumPy the addition of two arrays is done using the np.add() function.

2. Subtraction -> We can subtract two arrays element-wise using the np.subtract() function. This function subtracts each element of the second array from the corresponding element in the first array.

3. Multiplication -> Multiplication in NumPy can be done element-wise using the np.multiply() function. This multiplies corresponding elements of two arrays.

4. Division -> Division is another important operation that is performed element-wise using the np.divide() function. This divides each element of the first array by the corresponding element in the second array.

5. Exponentiation (Power) -> It allows us to raise each element in an array to a specified power. In NumPy, this can be done using the np.power() function.

6. Modulus Operation -> It finds the remainder when one number is divided by another. In NumPy, you can use the np.mod() function to calculate the modulus element-wise between two arrays.
```
## Example:
```bash
import numpy as np

a = np.array([5, 72, 13, 100])
b = np.array([2, 5, 10, 30])
res = np.add(a, b) # Addition
print(res)

res = np.subtract(a, b) # Subtraction
print(res)

res = np.multiply(a, b) # Multiplication
print(res)

res = np.divide(a, b) # Division
print(res)

res = np.power(a, b) # Exponentiation
print(res)

res = np.mod(a, b) # Modulus
print(res)

Output:-

[  7  77  23 130]
[ 3 67  3 70]
[  10  360  130 3000]
[ 2.5        14.4         1.3         3.33333333]
[                 25          1934917632        137858491849
 1152921504606846976]
 [ 1  2  3 10]

```
# Aggregation Function in NumPy :
Aggregation functions are used to combine multiple values into a single result
(like sum, average, max, min, mean, std(standard Deviation),var(Variance), median etc.).
<br>
They are very important in Data Science, ML, and Pandas.
<br>

<b>Why Aggregation Functions are used?</b>
<br>
To summarize data.
<br>
To analyze datasets.
<br>
To find patterns (mean, max, min).
<br>
Used in statistics & ML models.
<br>

<b>Example :</b>

```bash

"""
Aggregation Functions :

np.Sum(array) => It returns sum or total 

np.min(array) => It return minimum value present in an array.

np.max(array) => It return maximum value present in an array.

np.mean(array) => It returns average value

np.std(array)  => It return standard deviation

np.var(array)  => It Return variance

"""

import numpy as np

arr = np.array([10,90,50,30,80])

print(np.sum(arr))
print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))

```
<br>

# Indexing and Slicing in NumPy :
Indexing and slicing are used to access specific elements or parts of an array.
<br>
This is a core concept in NumPy, Pandas, and Machine Learning.
<br>

<b>Indexing in NumPy :</b>
<br>
Indexing is used for Accessing a single element from an array using its position (index).
<br>
Indexing always start with 0.
<br>

Example:

```bash

# In case of 1D Array 

import numpy as np
arr =  np.array([10,20,30,40,50,60,70,80,90])
print(arr[0])  # it return 0th index value
print(arr[3])  # it return 3rd index value
print(arr[5])  # it return 5th index value
print(arr[-1]) # it return last index element from array


# In case of 2D Array 
# array[rows][columns]

arr_2d = np.array([[20,30,40,50],
                   [90,40,60,20]])

print(arr_2d[1][3])

```
<b>Slicing in Numpy :</b>
<br>
Extracting multiple elements from an array in the form of (a sub-array).
<br>

<b>Syntax:</b>

```bash
array_name[start : stop : step]

start = 0th index (included)
stop = start to stop - 1  (excluded)

```
<br>

<b>Example:</b>

```bash
# 1D Array Slicing

import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90])

print(arr[1:5]) # it return array value that start from index=1 to index=4 
                #because index=5 in excluded

print(arr[:3]) # print first 3 element from array

print(arr[4:]) # print from index=4 to end  element from array

print(arr[::2]) #  Every 2nd element

print(arr[::-1])  # Reverse array



# 2D Array Slicing 

# syntax:

# arr[row_start:row_end, col_start:col_end]

arr_2d = np.array([[20,30,40],
                  [10,60,70],
                  [10,20,30]])

print(arr_2d[1:3 , 1:3])

print(arr_2d[:,1]) # All rows, column 1

print(arr_2d[1, :]) # All columns, Row 1

```
# Boolean Indeing:
It allows us to filter elements from an array based on a condition and returns only those that meet it. 
<br>
We create a boolean array from a condition and use it to select elements and can combine conditions with logical operators.
<br>

<b> Example: </b>
```bash
import numpy as np

arr = np.array([10, 15, 20, 25, 30])

print(arr[arr > 20])

print(arr[(arr > 10) & (arr < 30)]) # Using Logical Operator 
```
<br>

# Fancy Indexing:
It is also known as Advanced Indexing which allows us access elements of an array by using another array or list of indices.
<br>
This allows selecting multiple elements at once even if they are not next to each other which makes it easy to pick specific values from different positions in the array.
<br>

<b>Eample: </b>
```bash
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
print(arr[indices])
```
<br>

# Reshape NumPy Array:
Reshaping is used to change the shape of an array without changing data.It does not create a copy.
<br>
For example you change an 1D array to 2D array with the help of reshape() method.
<br>
if dimensions does not match means Total element must match like (2 x 3). if total elements does not match this method not works in this codition.

<b>Syntax :</b>

```bash
array.reshape(rows , columns)
```
<b> Example: </b>
```bash
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

reshaped_arr = a.reshape(2, 3) # Total element must match like (2 x 3)

print(reshaped_arr)
```
<br>

<b>Automatic Dimension(-1) :</b>
<br>
when using this NumPy automatically calculates the size.
<br>

Example :

```bash

# Automatic Dimension(-1)

arr = np.array([10,20,30,40,50,60])

reshaped_arr = arr.reshape(3,-1)

print(reshaped_arr)

```
<br>

<b>Flattening Arrays in NumPy:</b>
<br>
Flattening means converting a multi-dimensional array (2D / 3D) into a 1D array.
<br>
There are two methods:
<br>

```bash

1. flatten() => This method returns a new copy of the array.

Exmaple :

# flatten() method :   It retun a copy 

import numpy as np 

arr = np.array([[10,20,30,40],
                [50,60,70,80]])

flat_arr = arr.flatten()

print(flat_arr)       # Changes in flat_arr do NOT affect the original array.


# output :   [10 20 30 40 50 60 70 80]



2. ravel() method => This method Returns a view (not a copy) whenever possible.This method change original array.

Example :

# ravel() method : It retun a view

import numpy as np 

arr = np.array([[10,20,30,40],
                [50,60,70,80]])

ravel_arr = arr.ravel()

print(ravel_arr)    # output : [10 20 30 40 50 60 70 80]

# If you want to modify array you can it.

ravel_arr[0]= 100

print(ravel_arr)   #output : [100  20  30  40  50  60  70  80] 

print(arr) #  when you modify ravel_arr it also change original array 

"""
output :

 [[100  20  30  40] 
 [ 50  60  70  80]]

"""

```
# Array Modification :
Array modification means changing values, shape, or structure of a NumPy array after it is created.
<br>

<b>Here are many ways to modify an array understand with example :</b>

```bash

import numpy as np 

arr = np.array([10,20,30,40,50,60,70])

# 1. Modify Single Element (Indexing)
arr[1]=100
print(arr) # [ 10 100  30  40  50  60  70]


#2. Modify Multiple Elements (Slicing)
# array[start:end-1]
arr[1:3] = 1
print(arr) #[10  1  1 40 50 60 70]


# 3. Boolean Indexing
arr[arr >40] = 22
print(arr) #[10  1  1 40 22 22 22] 


# 4. Replace Using where()
# where(condition , value_if_true, value_if_false)
new_arr= np.where(arr % 2 ==0 ,0 ,1)
print(new_arr)   #[0 1 1 0 0 0 0]


# 5. Append Elements
# np.append(array,value)
append_element= np.append(arr,100) # does not change original array
print(append_element) #[ 10   1   1  40  22  22  22 100]


# 6. Insert Elements
# np.insert(array,indexNo,value)
insert_element= np.insert(arr,1,200)
print(insert_element) #[ 10 200   1   1  40  22  22  22]

# 7. Delete elements
# np.delete(array,indexNo)
print(arr) # [10  1  1 40 22 22 22]

arr2 = np.delete(arr,2) # [10  1 40 22 22 22]
print(arr2)
```
<b>Splitting Arrays:</b>
<br>
Splitting means dividing one array into multiple smaller arrays.
<br>

<b>Syntax :</b>

```bash
np.split(array, number of array dividing)
```
<br>

<b>Example:</b>

```
# 1. np.split() => it split(divide) an array into equal parts.

# splitting an Array :

import numpy as np

# splitting a 1D array
arr = np.array([10,20,30,40,50,60,70,80])
print(np.split(arr,2))

# splitting a 2D array 
arr_2d = np.array([[20,30,40],
                   [50,60,70],
                   [1,2,3]])

print(np.split(arr_2d,3))
```
# Broadcasting in NumPy :
Broadcasting allows NumPy to perform operations on arrays of different shapes without using loops.
<br>
It automatically adjusts the smaller array to match the larger array's shape by replicating its values along the necessary dimensions.
<br>

<b>Rules of Broadcasting :</b>

```bash
# RULES :
NumPy compares array shapes from right to left (last dimension first).

Rule 1 => Dimensions must be equal. Means if the size of dimension are the same, they are compatible.

Example:


# Rule 1: Dimensions must be equal


import numpy as np

a = np.array([[30,40,50],[60,70,80]])  # 2 x 3 

b= np.array([[10,20,30],[5,10,15]]) # 2 x 3 

print(a + b)


# Rule 2 => One of the dimensions must be 1
#If one of the dimensions is 1, NumPy stretches(expand) it to match the other.
import numpy as np

a = np.array([[30,40,50],[60,70,80]])  # 2 x 3 

b= np.array([10,20,30]) # 1 x 3 

print(a + b)

```

<b>Why Broadcasting is needed :</b>
<br>
Broadcasting is needed to perform operations on arrays of different shapes easily, efficiently, and without writing loops.

```bash
# Problem Without Broadcasting:
NumPy normally works when array shapes are the same.

import numpy as np

a = np.array([30,40,40])
b= np.array([10,20])

print(a + b) # it shows an error because the shape of an array are not same



# Broadcasting Solves This Problem :
# solution : 1
If you want element-wise addition, both arrays must have the same length.

import numpy as np

a = np.array([30,40,40])
b= np.array([10,20,30])

print(a + b)


# solution : 2
# Use a Scalar (Broadcasting Friendly) 
If you want to add one value to all elements:

import numpy as np

a = np.array([30,40,40])

print(a + 10)

```
