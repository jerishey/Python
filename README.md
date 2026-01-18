# Python

Python is one of the most popular programming languages. It's simple to use, packed with features and supported by a wide range of libraries and frameworks. Its clean syntax makes it beginner-friendly.
Python was created by <b>Guido van Rossum and first released in 1991</b>. It focuses on readability and uses simple, English-like syntax.
Python is a Object Oriented Programming language.

# Features of Python:
```bash
1. Simple and easy to learn due to its readable, English-like syntax

2. Interpreted language, so code runs line by line without compilation

3. Supports object-oriented, procedural, and functional programming

4. Large standard library and vast collection of third-party modules

5. Platform-independent, works on Windows, Linux, and macOS

6. Dynamic typing - no need to declare variable types

7. Automatic memory management with garbage collection
```

# Python Interpreter:
The Python interpreter is a program that reads and executes Python code line by line. It converts Python source code into bytecode and runs it on the Python Virtual Machine, allowing developers to test and debug programs easily without separate compilation.
<br>
There is no separate compilation step, which makes Python an interpreted language.
<br>

<b>How interpreter Works:</b>

```bash

1. You write Python code.

2. Interpreter reads the code line by line.

3. Code is converted into bytecode.

4. Bytecode is executed by the Python Virtual Machine (PVM).

```
# Python as a Calculator:
Python can be used as a simple calculator to perform mathematical operations like addition, subtraction, multiplication, division, and more. It supports integers, decimals, and complex expressions, making it useful for quick calculations and learning basic arithmetic operations. This is usually done using the Python interpreter in interactive mode.
<br>

<b>How to use python as a calculator:</b>

```bash
1. Open command prompt or Terminal.

2. Type "python" . This open REPL(Read , Evaluate , Print ,Loop) in your cmd or terminal.

3. Type any calculation just like:
   
 4+2 = 6
 10**2 = 100
 15/3 = 5.0

4. For exit python type:
  
   exit()

```

# indentation in python:
Indentation in Python refers to the spaces at the beginning of a line of code. It is used to define blocks of code such as loops, conditions, and functions.
<br>
 Unlike C, C++ or Java (which use { }), Python uses indentation to show structure or define the block of code.
<br>

<b>Why Indentation is important:</b>

```bash
1.It tells Python which statements belong together.

2.Controls the flow of:

if-else

for and while loops

functions

classes

3.Wrong indentation causes an Indentation error

4.Standard practice is to use 4 spaces per indentation level
```
Example:

```bash
num=10

if num%2==0:
    print("even number")
else:
    print(" odd number")    

# Output -> even number
```

# Comments in Python:
Comments are lines in a program that are ignored by the Python interpreter.
<br>
They are used to explain code, make programs easy to understand, and improve readability.
<br>

<b>Types of comments:</b>
<br>
There are Two types of comments in python:
<br>

1. Single-Line comments:
<br>
Single-Line commnets starts with hash sign (#). Anything written after hash sign is consider as comments and that line id ignored by python interpreter.
<br>
Example:

```bash
# This is a single-line comment
x = 15  # variable storing value

```
2. Multi-Line Comments:
<br>
Python does not have a separate multi-line comment syntax.
But we use triple quotes (''' or """) for multi-line comments (actually multi-line strings).
<br>
Example:

```bash
"""
This is a multi-line comment
used to explain
multiple lines of code
"""
```

<b>Best Practices for Comments:</b>

```bash
1. Write comments that explain WHY, not WHAT (code shows what)

2. Keep comments up-to-date when code changes

3. Use comments for complex logic or non-obvious solutions

4. Avoid over-commenting simple code
```

# Variable in Python:
In Python, variables are used to store data values that can be reused and modified during program execution. A variable acts like a container that holds information. Python is a dynamically typed language, so you do not need to declare the data type of a variable explicitly. You simply assign a value using the " = " operator.
<br>

<b>Rules for Naming Variables</b>

```bash
1. Variable names must start with a letter (a–z, A–Z) or an underscore (_).

2. A variable name cannot start with a digit (0-9).

3. They can contain letters, numbers, and underscores.

4. Variable names are case-sensitive (myVar and myvar are different).

5. Python keywords (if, else, for) cannot be used as variable names.

6. Use descriptive names (age, total_price) instead of single letters for better readability.
```
Example:

```bash

# Creating variables

name = "Rakesh"
age = 21
price = 99.99
_isActive = True


# Multiple assignment

a, b, c = 10, 20, 30

# Assigning same value to multiple variables
x = y = z = 100

```

# Identifiers:
An identifier is the name given to a variable, function, class, object, or module in Python. <br>
Identifiers are used to identify program elements uniquely. <br>

<b> Rules for Identifiers in Python:</b>

```bash

1. Identifiers must start with a letter (a–z, A–Z) or an underscore (_).

2. They cannot start with a digit.

3. Identifiers can contain letters, digits, and underscores only.

4. They are case-sensitive (total and Total are different).

5. Python keywords cannot be used as identifiers.

6. Special characters such as @, #, $, % are not allowed.

```
<b>Here are some valid Identifiers:</b>

```bash
name
_age
total_marks
student1
```
<b>Some invalid Identifiers:</b>

```bash

1name      # starts with a number
total-marks  # contains special character (-)
class      # Python keyword
```

# Keywords:
Keywords in Python are special reserved words that are part of the language itself. They define the rules and structure of Python programs which means you cannot use them as names for your variables, functions, classes or any other identifiers.

<b>List of keyword in python:</b>
<br>
There are total 35 keyword in python:

```bash

False    None     True
and      as       assert
async    await    break
class    continue def
del      elif     else
except   finally  for
from     global   if
import   in       is
lambda   nonlocal not
or       pass     raise
return   try
while    with     yield

```
Example of keywords in use:

```bash

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

    # Here if and else are keywords

```

<b>Categories of Keywords (For Simple Understanding):</b>

```bash

1. Control flow :- if, else, elif, for, while, break, continue

2. Logical:-  and, or, not

3. Value :- True, False, None

4. Function & class :- def, return, class

5. Exception handling :- try, except, finally, raise

6. Others :- import, from, pass, lambda, yield

```

<br>

<b>How to check keywords in python:</b>

```bash

import keyword
print(keyword.kwlist)

# Output -> ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 
 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
 'return', 'try', 'while', 'with', 'yield']
```

# Literals in python:
Literals in Python are fixed values written directly in the code that represent constant data. They provide a way to store numbers, text, or other essential information that does not change during program execution. Python supports different types of literals, such as numeric literals, string literals, Boolean literals, and special values like None.
<br>
<b> For example:</b>

```bash

10, 3.14, and 5 + 2j are numeric literals.
'Hello' and "Python" are string literals.
True and False are Boolean literals.

```

<b><u>Types of Literals:</u></b>
<br>

<b>1. Numeric Literals:</b>

<br>
Numeric literals represent numbers and are classified into three types:

1. Integer Literals -> Whole numbers (positive, negative, or zero) without a decimal point. 
<br>
   Example: 10, -25, 0
<br>

2. Floating-point (Decimal) Literals -> Numbers with a decimal point, representing real numbers.
<br>
   Example: 3.14, -0.01, 2.0
<br>

3. Complex Number Literals -> Numbers in the form a + bj, where a is the real part and b is the imaginary part.
<br>
  Example: 5 + 2j, 7 - 3j
<br>

Example:

```bash

# Integer literals
a = 100
b = -50

# Floating-point literals
c = 3.14
d = -0.005

# Complex number literals
e = 4 + 7j
f = -3j

print(a, b, c, d, e, f)

```
<br>

<b>2. String Literals:</b>

<br>
String literals are sequences of characters enclosed in quotes. They are used to represent text in Python.
<br>

<b>Types of String Literals:</b>

<br>
1. Single-quoted strings ->  Enclosed in single quotes (' ').
<br>
   Example: 'Hello, World!'
<br>

2. Double-quoted strings -> Enclosed in double quotes (" ").
<br>
   Example: "Python is fun!"
<br>

3. Triple-quoted strings -> Enclosed in triple single (''' ''') or triple double (""" """) quotes, generally used for multi-line strings or docstrings.
<br>
   Example:
   '''This is
   a multi-line
   string'''
<br>

4. Raw strings -> Prefix with r to ignore escape sequences (\n, \t, etc.). Example: r"C:\Users\Python" (backslashes are treated as normal characters).
<br>

Example of String Literals:

```bash

# Different string literals

a = 'Hello'      # Single-quoted
b = "Python"     # Double-quoted

c = '''This is 
a multi-line string'''  # Triple-quoted

d = r"C:\Users\Python"  # Raw string

print(a)
print(b)
print(c)
print(d)

                  Output:
                  Hello
                  Python
                  This is 
                  a multi-line string
                  C:\Users\Python
```
<br>

<b>3. Boolean Literals:</b>

<br>
Boolean literals represent truth values in Python. They help in decision-making and logical operations. Boolean literals are useful for controlling program flow in conditional statements like if, while, and for loops.
<br>
Types of Boolean Literals:
<br>
True ->  Represents a positive condition (equivalent to 1)
<br>
False -> Represents a negative condition (equivalent to 0)
<br><br>
Example:

```bash
# Boolean literals
a = True
b = False

print(a, b)       # Output: True False
print(1 == True)  # Output: True
print(0 == False) # Output: True
print(True + 5)   # Output: 6 (1 + 5)
print(False + 7)  # Output: 7 (0 + 7)

```
<br>

<b>4. Collection Literals:</b>

<br>
Python provides four different types of literal collections:
<br>
1. List literals: [1, 2, 3]
<br>
2. Tuple literals: (1, 2, 3)
<br>
3. Dictionary literals: {"key": "value"}
<br>
4. Set literals: {1, 2, 3}
<br><br>
Example:

```bash
Rank = ["First", "Second", "Third"]  # List

colors = ("Red", "Blue", "Green")  # Tuple

Class = { "Jai": 10, "Anaya": 12 }  # Dictionary

unique_num = {1, 2, 3}  # Set

print(Rank, colors, Class, unique_num)

```

<b>5. Special Literal - None:</b>

<br>
None is a special literal in Python that represents the absence of a value or a null value.
<br>
It is often used to define a variable that doesn't have a value yet.
<br>

Example:

```bash
result = None
print(result)  # Output: None

# Checking if a variable is None
if result is None:
    print("No value assigned")
```

# Operator :
In Python programming, Operators are used to perform operations on values and variables.
<br>
Operators: Special symbols like -, + , * , /, etc.
<br>
Operands: Value on which the operator is applied.
<br>

<b>Types of operators:</b>
<br>
<b>1. Arithmetic operators</b> -> Arithmetic operators are used to perform mathematical operations on numeric values.
 
```bash
Operator     	  Name        	Example	

+	            Addition	       x + y	

-	            Subtraction    	   x - y	

*	            Multiplication     x * y

/  	            Division           x / y

%	            Modulus	           x % y

**     	        Exponentiation     x ** y

//	            Floor division	   x // y

```
<br>
Example:

```bash
a=20
                               
b=4

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

                    #Output ->
                    24
                    16
                    80
                    5.0
                    0
                    5
                    160000
```
<br>
<b>2.Assignment operators</b> -> Assignment operators are used to assign values to a variable.
  
```bash
Operator	    Example	   Same As

=	            x = 6	   Assign

+=	            x += 3	   x = x + 3

-=	            x -= 2	   x = x - 2

*=	            x *= 2	   x = x * 2

/=	            x /= 2     x = x / 2

%=              x %= 2     x = x % 2

//=             x //= 2    x = x // 2

**=             x **= 2    x = x ** 2

```
<b>3.Comparison / Relation operators</b> -> Comparison operators are used to compare two values and return a Boolean values.

```bash

Operator         	Meaning      	       Example

   ==	            Equal to	           5 == 5

   !=	            Not equal	           5 != 3

   >	            Greater than	       5 > 3

   <	            Less than	           5 < 3

   >=	            Greater or equal	   5 >= 5

   <=	            Less or equal	       5 <= 3
```   

<b>4.Logical operators</b> -> Logical operators are used to combine conditional statements.

```bash

Operator	                Meaning   	                                         Example	

and 	          Returns True if both statements are true	                  x < 5 and  x < 10	

or	              Returns True if one of the statements is true	              x < 5 or x < 4	

not	              Reverse the result, returns False if the result is true	  not(x < 5 and x < 10)

```

<b>5.Bitwise operators</b> -> Bitwise operators are used to compare (binary) numbers.

```bash
Operator	   Name	                               Meaning     	                             Example

   &           AND	             Sets each bit to 1 if both bits are 1	                      x & y	

   |	       OR	             Sets each bit to 1 if one of two bits is 1	                  x | y	

   ^	       XOR	             Sets each bit to 1 if only one of two bits is 1	          x ^ y	

   ~	       NOT	             Inverts all the bits	                                      ~x

   <<	       left shift	     Shift left by pushing zeros in from the right and let 
                                 the leftmost bits fall off	                                  x << 2	
   >>	       right shift	     Shift right by pushing copies of the leftmost bit in from 
                                 the left, and let the rightmost bits fall off	              x >> 2
```
Example:

```bash
# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 2 = 0010

print(6 & 3)
                      
                       output:
                       2
```

<b>6. Identity operators</b> -> Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

```bash
Operator                    	Meaning               	                           Example	

is 	              Returns True if both variables are the same object	          x is y	

is not	          Returns True if both variables are not the same object	      x is not y

```
Example:

```bash

# is

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)     #True
print(x is y)     #False
print(x == y)     #True


# is not 

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)    #True

```

<b>7.Membership operators</b> -> Check if a value exists in a sequence.

```bash

Operator                Meaning     	                                        Example

in               Returns True if a sequence with the specified
                  value is present in the object                            'a' in "apple"

not in	         Returns True if a sequence with the specified value 
                  is not present in the object	                             5 not in [1,2,3]

```

# Data Types in Python:
Data types define the type of value a variable can hold. Python has several built-in data types that are automatically determined based on the value assigned.
<br>

<b>Main Data Types:</b>

```bash
1. Numeric Types:
   - int (integers): 10, -5, 0
   - float (decimals): 3.14, -0.5
   - complex: 2 + 3j

2. Text Type:
   - str (string): "Hello", 'Python'

3. Sequence Types:
   - list: [1, 2, 3]
   - tuple: (1, 2, 3)
   - range: range(5)

4. Mapping Type:
   - dict (dictionary): {"name": "Rakesh", "age": 21}

5. Set Types:
   - set: {1, 2, 3}
   - frozenset: frozenset({1, 2, 3})

6. Boolean Type:
   - bool: True, False

7. None Type:
   - None
```

<b>Checking Data Type:</b>

```bash
x = 5
print(type(x))  # Output: <class 'int'>

y = "Hello"
print(type(y))  # Output: <class 'str'>
```

<b>Type Conversion:</b>

```bash
# Converting between types
x = "10"
y = int(x)      # String to integer
z = float(x)    # String to float

a = 5
b = str(a)      # Integer to string

print(y, z, b)  # 10 10.0 5
```

# String in Python:
Strings are a data type in python that is used to represent collections of characters.String is a sequence of character that are enclosed in Single-quotes(' '),Double-quotes(" "),Triple-quotes(''' '''/""" """).
<br>
Python strings are immutable, which means once a string is created, it cannot be changed.

Example:

```bash

fname="Rakesh"
lastName="Kumar"

print(fname+" "+lastName)

```

<b>Indexing :</b> Indexing is used to access individual characters or elements of a sequence (like string, list, tuple) using their position number.
<br>

Example:

```bash

text ="Python"

 Index  0  1  2  3  4  5 

 Char   P  y  t  h  o  n
 
 
# How to access character using Indexing

text="Python"

print(text[4])

# Output-> o

 ```

<b>Negative Indexing:</b>
<br>
Python also supports negative indexing, which starts from the end of the string.
<br>

```bash
text = "Python"

# Negative Index  -6 -5 -4 -3 -2 -1
# Char             P  y  t  h  o  n

print(text[-1])  # Output: n
print(text[-3])  # Output: h
```

<b> String operators:</b>

```bash

Operator	       Use           	Example

   +	     Concatenation	    "Hi" + " All"

   *	     Repetition	        "Hi" * 3

   in	     Membership	        "P" in "Python"

```
<br>
 Example:

 ```bash
fname="Rakesh"
lastName="Kumar"

print(fname+" "+lastName)  # concatenation

print(fname*3)     # Repetaion

print("R" in fname)   # Membership

```
<br>
<b>Slicing:</b> A string in python can be sliced for getting a part of the strings.

```bash

# syntax:

slice= name[index_start : index_end]

index_start -> first index included
index_end -> last index is not included


# Example:
text="Hello World"

print(text[0:4])   # start from index 0 all the way till 4 (excluding index 5)

# Output-> Hell   
```

<b>Common String Methods:</b>

```bash
Method	             Description

upper()	          Convert to uppercase

lower()	          Convert to lowercase

capitalize()	  First letter capital

title()	          Capitalize each word

strip()	          Remove spaces

replace()         Replace text

split()	          Split string

find()	          Find substring

len()	          Length of string

count()           Count occurrences

startswith()      Check if starts with

endswith()        Check if ends with

isdigit()         Check if all digits

isalpha()         Check if all alphabets

```
<br>
Example:

```bash
msg= " hello world from python"

print(msg.upper())  #uper()

print(msg.lower())  #lower()

print(len(msg))  #len()

print(msg.title())  #title()

print(msg.capitalize())  #captalize()

print(msg.strip())  #strip()

print(msg.find("python"))  #find()

print(msg.count("o"))  #count()

# Output->    HELLO WORLD FROM PYTHON
#             hello world from python
#            24
#             Hello World From Python
#             hello world from python
#            hello world from python
#            18
#            3

```

<b>String Formatting:</b>

```bash
# Using f-strings (Python 3.6+)
name = "Rakesh"
age = 21
print(f"My name is {name} and I am {age} years old")

# Using format() method
print("My name is {} and I am {} years old".format(name, age))

# Using % operator
print("My name is %s and I am %d years old" % (name, age))
```

# Input and Output Statements:
In Python, input and output statements are used to take data from the user and display results on the screen. They are very important for writing interactive programs.
<br>

<b>input statements:</b>

<br>
An input statement is used to accept data (taking input) from the user at runtime.
<br>
Python uses the input() function to take input from users.
<br>
The data entered by the user is always in string format, so we must convert it when needed.
<br>

<b>Syntax:</b>

```bash
variable = input("Message to user")

```
<br>
Example:

```bash
name = input("Enter your name: ")
print("Hello", name)

```
<br>

<b>Input with Type Conversion:</b>

```bash
age = int(input("Enter your age: "))
print("Your age is", age)


# int() → converts input to integer
#float() → converts input to decimal number

```

<b>Taking Multiple Inputs:</b>

```bash
# Multiple inputs in one line
a, b = input("Enter two numbers: ").split()
print(f"First: {a}, Second: {b}")

# Multiple inputs with type conversion
x, y = map(int, input("Enter two numbers: ").split())
print(f"Sum: {x + y}")
```

<br>

<b>Output Statements:</b>
 An output statement is used to display information or result on the screen.
 <br>
 Python uses the print() function for output.
<br><br>
 Syntax:

 ```bash
print(value)
print(value1, value2)


#Example: 

print("Hello World")

```

<b>Print with Separators and End:</b>

```bash
# Using sep parameter
print("Rakesh", "Kumar", "Singh", sep="-")  # Output: Rakesh-Kumar-Singh

# Using end parameter
print("Hello", end=" ")
print("World")  # Output: Hello World (on same line)

# Combining both
print("Python", "is", "fun", sep=" | ", end="!\n")
```

# List:
In Python a list is a versatile data structure that allow you to store and organize multiple items in a single variable.Lists are defined by enclosing a sequence of elements within a square bracket and seprating them with commas.
<br>
Lists are ordered, mutable (changeable), and can store different data types.
<br><br>
Example:

```bash
numbers = [10, 20, 30, 40]

names = ["Rakesh", "Nitish", "Shivam"]

mixed = [1, "Python", 3.5, True]

```   
<br>

<b>List Indexing:</b>
<br>
A list can be indexed just like string.
<br>

```bash
number =[1,2,4,5,3,2,3,5,8]

print(number[1])

# Negative indexing
print(number[-1])  # Last element: 8
print(number[-2])  # Second last: 5

```
<br>

<b> List Slicing:</b>

```bash
number =[1,2,4,5,3,2,3,5,8]

print(number[1:6])  #[2, 4, 5, 3, 2]

print(number[0:4])   #[1, 2, 4, 5]

print(number[:3])    # From start to index 3: [1, 2, 4]

print(number[5:])    # From index 5 to end: [2, 3, 5, 8]

print(number[::2])   # Every 2nd element: [1, 4, 3, 3, 8]

```
<b>Adding Elements to List</b>

```bash
   Method	        Use	                  Example

   append()	      Add one element	   list.append(50)

   insert()	      Add at position	   list.insert(1, 15)

   extend()	      Add multiple	       list.extend([60,70])
```
<br>

Example:

```bash
number =[1,2,4,5,3,2,3,5,8]

number.append(23)  #append()
number.insert(2,3)  #insert()
number.extend([123,22]) #extend()
print(number)

```

<b>Removing Elements from List:</b>

```bash
number = [1, 2, 4, 5, 3, 2, 3, 5, 8]

number.remove(5)    # Removes first occurrence of 5
number.pop()        # Removes last element
number.pop(2)       # Removes element at index 2
del number[1]       # Deletes element at index 1
number.clear()      # Removes all elements
```

<b>LIST METHODS:</b>

<br>
Consider the following list:

```bash
l1 = [1,8,7,2,21,15]
• l1.sort(): updates the list to [1,2,7,8,15,21]

• l1.reverse(): updates the list to [15,21,2,7,8,1]

• l1.append(8): adds 8 at the end of the list

• l1.insert(3,8): This will add 8 at 3 index

• l1.pop(2): Will delete element at index 2 and return its value.

• l1.remove(21): Will remove 21 from the list. 

• l1.index(7): Returns the index of first occurrence of 7

• l1.count(8): Returns how many times 8 appears in the list

• l1.copy(): Creates a shallow copy of the list
```

<b>List Comprehension:</b>
<br>
List comprehension provides a concise way to create lists.
<br>

```bash
# Creating a list of squares
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Creating a list with condition
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8]
```

# Tuple:
A tuple is an immutable ordered collection of elements enclosed in paranthesis (). It is used to stored related data that should not be modified. 
<br>
Tuples are immutable, meaning their values cannot be changed after creation.
<br><br>
Example:

```bash
t1 = (10, 20, 30)

t2 = ("Rakesh", "Nitish", "Shivam")

t3 = (1, "Python", 3.5)

# Single element tuple (note the comma)
t4 = (5,)

```

<b>Accessing Tuple Elements:</b>

```bash
t1 = (10, 20, 30, 40, 50)

print(t1[0])     # First element: 10
print(t1[-1])    # Last element: 50
print(t1[1:4])   # Slicing: (20, 30, 40)
```

<b>Common Tuple Functions</b>

```bash
      Function	        Use

      len()	           Length

      max()	           Largest

      min()	           Smallest

      sum()	           Total

      count()	       Count value

      index()	       Find position

      tuple()          Convert to tuple
```

<b>Tuple Unpacking:</b>

```bash
# Unpacking tuple values into variables
person = ("Rakesh", 21, "BCA")
name, age, course = person
print(name, age, course)  # Rakesh 21 BCA
```

<b>Why Use Tuples:</b>

```bash
1. Faster than lists

2. Protect data from accidental modification

3. Can be used as dictionary keys

4. Good for storing related constant values
```

# Dictionary in Python:
A dictionary in Python is a collection of data stored in key-value pairs.
<br>
Each key is unique and is used to access its value.
<br>
Dictionaries are unordered, mutable (changeable), and written using curly braces { }.
<br>

syntax:

```bash

dictionary_name = {
    key1: value1,
    key2: value2
}

```
<br>

Example:

```bash
students ={
    "name":"Rakesh",
    "age":21,
    "class": "BCA",
    "RollNo":24
}
```

Accessing dictionary values:

```bash

print(students["name"])


# Accessing by using get method also.

print(students.get("age"))


# how add elements in dictionary
students["State"] ="Haryana"
print(students)


# how to updates elements in dictionary
students["age"]=22
print(students)


```
<br>

<b>Looping Through Dictionary:</b>

```bash
# Loop through keys
for key in students:
    print(key)

# Loop through values
for value in students.values():
    print(value)

# Loop through key-value pairs
for key, value in students.items():
    print(f"{key}: {value}")
```

<b>Removing Items:</b>

```bash
student.pop("course")       # removes specific key
student.popitem()           # removes last inserted item
del student["age"]          # deletes key-value pair
student.clear()             # removes all items

```
<br>

<b>Method	Description</b>

```bash

clear()	  ->   Removes all the elements from the dictionary.

copy()	  ->   Returns a copy of the dictionary.

fromkeys()	 ->  Returns a dictionary with the specified keys and value.

get()	      ->  Returns the value of the specified key.

items()	  ->   Returns a list containing a tuple for each key value pair.

keys()	   ->  Returns a list containing the dictionary's keys.

pop()	      ->  Removes the element with the specified key.

popitem()	  -> Removes the last inserted key-value pair.

setdefault()   ->	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

update()	 -> Updates the dictionary with the specified key-value pairs.

values()  ->	Returns a list of all the values in the dictionary.

```

<b>Nested Dictionaries:</b>

```bash
# Dictionary containing dictionaries
students = {
    "student1": {"name": "Rakesh", "age": 21},
    "student2": {"name": "Nitish", "age": 22}
}

print(students["student1"]["name"])  # Rakesh
```

# Sets:
A set in Python is a collection of unique elements.
<br>
It is unordered, mutable, and does not allow duplicate values.
<br>

Syntax:

```bash

set_name = {value1, value2, value3}

```
Example:

```bash
numbers = {1, 2, 3, 4, 5}
print(numbers)

```
<br>

<b>PROPERTIES OF SETS</b>

```bash
1. Sets are unordered => Element's order doesn't matter.
2. Sets are unindexed => Cannot access elements by index
3. There is no way to change items in sets.
4. Sets cannot contain duplicate values.

```
<br>

<b>some important points with example:</b>

```bash
# how to create sets:
mysets = {1,2,3,7,8,9,4,3,5,6,7,8}
print(mysets)  # Duplicates automatically removed

#How to create an empty sets:
sts = set()
print(type(sts))

# how to add an elements:
mysets.add(234)
print(mysets)

# add multiple elements in sets:

mysets.update([123,345,678,890])
print(mysets)

# Removing elements
mysets.remove(5)      # Raises error if not found
mysets.discard(100)   # No error if not found
mysets.pop()          # Removes random element

```
<br>

<b>Operation on Sets:</b>

```bash

# Union  -> It combines both sets in single one.

set1 ={12,13,14,15,16}

set2 ={1,2,3,4,5,6,7,8,9,10,11}

print(set1 | set2)


# Intersection   ->  It searches common elements in both sets

set1 ={12,13,1,15,16,4,6,7,2}

set2 ={1,2,3,4,5,6,7,8,9,10,11}

print(set1 & set2)


# Difference -> It returns elements that are present in the first set but NOT in the second set.

set1 ={12,13,1,15,16,4,6,7,2}

set2 ={1,2,3,4,5,6,7,8,9,10,11}

print(set1 - set2)

# Symmetric Difference -> Elements in either set but not in both
print(set1 ^ set2)

```
<br>

<b>Set Methods:</b>

```bash

Method	                   Use

add()            	    Add element

update()	            Add multiple elements

remove()	            Remove element

discard()	            Remove without error

union()	                Combine sets

intersection()	        Common elements

difference()	        Remaining elements

symmetric_difference()  Elements in either but not both

clear()	                Empty set

issubset()              Check if subset

issuperset()            Check if superset
 
```

# Conditional Statements:
Conditional statements are used to make decisions in a program.
They allow the program to execute different blocks of code based on a condition.
<br>

1.<b>If Statements:</b> The if Statements is used in python to Executes a block of code only if the condition is true.
<br>

Syntax:

```bash

if condition:
    statement

```
<br>

Example:

```bash
age = 20
if age >= 18:
    print("Eligible to vote")

```
<br>

2.<b>If else</b> : The if else statements in python provides a way to perform different action based on a evaluation of a condition. It allows us to executes first block of code if condition is true and executes another block if condition is false.
<br>

<b>Syntax:</b>

```bash

if condition:
    statement
else:
    statement

```
<br>

<b>Example:</b>

```bash
age = 10

if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")

```
<br>

3.<b>If-elif-else :</b> This Statements is used when there are multiple condition.
<br>
important point about elif:
<br>
1. There can be any number of elif statements.
<br><br>
2. Last else is executed only if all the conditions inside elifs fail.
<br>

<b>Syntax:</b>

```bash
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```
<br>

<b>Example:</b>

```bash

# if-elif-else:

age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")
   
```

4.<b>Nested if statement:</b> An if statement inside another if statement in this condition we can say that it is a Nested if statement.
<br>

<b>Syntax:</b>

```bash

if condition1:
     statement

      if condition2:
          statement

      else:

else:

```
<br>

<b>Example:</b>

```bash

age = int(input("Enter Your Age :"))
salary= int(input("Enter Your Salary :"))

if(age >=18):
    {
           print("Eligible")
    }

    if(salary >=40000):
        {
            print("You are Eligible for Loan ")
        }
    else:
        {
            print("Not Eligible for Loan")
        }
else:
    print("Your Not Eligible")

```
5.<b>Short-hand if (One-line if)</b>

```bash
a = 10
if a > 5: print("Greater than 5")
```
<br>

6. <b>Short-hand if-else (Ternary Operator):</b>

```bash
a = 3
print("Even") if a % 2 == 0 else print("Odd")

# Better way
result = "Even" if a % 2 == 0 else "Odd"
print(result)

```

# Loops:
Loops in Python are used to repeat a block of code multiple times until a condition is met or satisfied.
<br>

<b>Types of Loops :</b>
<br>
There are mainly two types of loops:
<br>

1. while Loop
<br><br>
2. for Loop
<br>

1. <b>while loop:</b> This loop is used when the number of iterations is not known.
<br>

<b>Syntax:</b>

```bash
while (condition):   # The block keeps executing until the condition is true
    statement


```
<br>
In while loops, the condition is checked first. If it evaluates to true, the body of the loop
is executed otherwise not!
<br><br>
If the loop is entered, the process of [condition check & execution] is continued until
the condition becomes False

<b>Example:</b>

```bash

# print 1 to 20 

i = 0
while(i<=20):
    print(i)
    i = i+1
    
```

<b>Infinite Loop Warning:</b>

```bash
# Be careful - this will run forever!
# while True:
#     print("This runs forever")

# Use Ctrl+C to stop infinite loops
```

2. <b>For Loop :</b> This loop is used when the number of iterations is known. For loops is used to iterate over a sequence such as a list, tuple, string or range.
<br>

<b>Syntax:</b>

```bash
for variable in sequence:
    statements
```
<br>

<b>Example:</b>

```bash

fruits = ["apple","mango","banana","papaya","pineapple"]

for fruit in fruits:
    print(fruit)

# Looping with index using enumerate()
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

# Range function in python:
The range() function is used to generate a sequence of numbers.It is mainly used with for loops.
<br>
range() returns a sequence of numbers starting from a given value up to (but ending value not including) the ending value.
<br>

<b>Syntax:</b>

```bash
range(start, stop, step)           # Meaning
                                   start -> Starting value (default = 0)

                                   stop -> Ending value (not included)

                                   step -> Difference between numbers (default = 1)

```
<br>

<b>Example:</b>

```bash
for num in range(1 ,10):

    print(num)   # prints 1 to 9

# Range with step
for num in range(0, 10, 2):
    print(num)  # prints 0, 2, 4, 6, 8

# Reverse range
for num in range(10, 0, -1):
    print(num)  # prints 10 to 1

```

# FOR LOOP WITH ELSE :
An optional else can be used with a for loop if the code is to be executed when the
loops exhausts.
<br>

<b>Example:</b>

```bash

l= [1,7,8]

for item in l:
print(item)

else:
print("done") # this is printed when the loop exhausts!


                  Output:
                  1
                  7
                  8
                  done

```

<b>WHILE LOOP WITH ELSE:</b>

```bash
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("While loop completed")

# else block is skipped if loop is broken
```

# Break statements :
The break statement is a loop control statement used to terminate (stop) a loop immediately, even if the loop condition is still true.
<br>

Example:

```bash
# break in for Loop

for i in range(1,8):
    if i==5:
        break
    print(i)

# break in while loop
num = 0
while num < 10:
    if num == 5:
        break
    print(num)
    num += 1

```

# continue statements:
The continue statement is a loop control statement used to skip the current iteration of a loop and move to the next iteration.
<br>

<b>Example:</b>

```bash
   
for i in range(1,8):
    if i==5:
        continue     # by using this statements it skip 5 
    print(i)
 

               output :
               it print 1 ,2 ,3 ,4 ,6 ,7

# Practical use - skip negative numbers
numbers = [1, -2, 3, -4, 5]
for num in numbers:
    if num < 0:
        continue
    print(num)  # Only prints positive numbers
               
```
# Pass statement :
The pass statement is used as a placeholder where a statement is required but no operation is to be performed.
<br>

<b>Example:</b>

```bash

for i in range(5):
    pass

           # loop run but does nothing

# Useful for creating empty function/class structures
def future_function():
    pass  # Will implement later

class FutureClass:
    pass  # Will add methods later

```

# Function in Python:
A function in Python is a block of reusable code that performs a specific task. Functions help break a large program into smaller, manageable parts, making the code modular, readable, and easy to maintain. Instead of writing the same code repeatedly, you can define a function once and call it whenever needed.In Simple Word we can say that a function is a block of code that perform a specific task.
<br>

<b>Creating a function:</b>
<br>
In Python, a function is defined by using "def" keyword and function name  and paranthesis.
<br>

```bash
# function definition
def my_function():
    print("Hello from a function")

# function call
my_function()


#The code inside the function must be indented. Python uses indentation to define code blocks.

```
<br>

<b>Why we use Function:</b>

```bash

Reuse code

Reduce repetition

Make programs easy to understand

Improve modularity

Easy to maintain and debug

```
<br>

<b>Function Name Rules:</b>

```bash
Function names follow the same rules as variable names in Python:

    1. A function name must start with a letter or underscore.
    2. A function name can only contain letters, numbers, and underscores.
    3. Function names are case-sensitive (myFunction and myfunction are different).

```
<br>

<b>Types Of Function :</b>
<br>
There are two types of function:
<br>
<br>
1. <b>Built-in function :</b> print() , len() , input().
<br><br>
2. <b>User-defined function :</b> This type of function is created by programmers.
<br>

<b>FUNCTION DEFINITION :</b>
The part containing the exact set of instructions which are executed during the function call.
<br>

<b> FUNCTION CALL :</b>
Whenever we want to call a function, we put the name of the function followed by parentheses as follows:
<br>

```bash
func1() # This is called function call

```
<br>

<b>Function with Parameters:</b>

```bash
# Function with single parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Rakesh")

# Function with multiple parameters
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # 8
```

<b>Defalut parameters value :</b>
A default parameter value is a value given to a function parameter at the time of function definition.
<br>
If no argument is passed during the function call, the default value is used automatically.
<br>

```bash
def greet(name="Guest"):
    print("Hello", name)

greet("Rakesh")
greet()


                    output:
                    Hello Rakesh
                    Hello Guest


```

<b>Return Statement:</b>

```bash
# Function that returns a value
def square(num):
    return num ** 2

result = square(5)
print(result)  # 25

# Function returning multiple values
def get_info():
    name = "Rakesh"
    age = 21
    return name, age

n, a = get_info()
print(n, a)  # Rakesh 21
```

<b>Keyword Arguments:</b>

```bash
# Using keyword arguments
def student_info(name, age, course):
    print(f"{name} is {age} years old and studies {course}")

# Order doesn't matter with keyword arguments
student_info(age=21, name="Rakesh", course="BCA")
```

<b>*args and **kwargs:</b>

```bash
# *args - for variable number of arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs - for variable number of keyword arguments
def student_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_details(name="Rakesh", age=21, course="BCA")
```

# Recursion in Python:
Recursion is a technique in which a function calls itself to solve a problem by breaking it into smaller subproblems.
<br>
In Simple world we can say that Recursion is a process where a function calls itself until a base condition is met.
<br>

<b>Every recursive function have two parts:</b>
<br>

```bash

1. Base Case => Condition where the function stops calling itself.

2. Recursive case => The function calls itself with a smaller problem.

It is used to directly use a mathematical formula as function. 

Example of using mathematical formula:

factorial(n) = n x factorial (n-1)
```
<br>

<b>Example of recursion</b>

```bash

def factorial(n):    

    if(n==0 or n==1 ):          # Base case 
        return 1
    return n * factorial(n-1)   # recursive case because it call itself .

n = int(input("Enter a Number :"))

print(" Factorial of given numbers is ",factorial(n))

```
<br>

<b>How factorial(5) works (Step by Step) :</b>

```bash

factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1
= 120

```
<br>

<b>fibonacci series :</b> The Fibonacci series is a sequence of numbers where each number is the sum of the previous two numbers.
<br>

```bash

Series:
0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Formula:

F(n) = F(n-1) + F(n-2)

```
<br>

<b>Example:</b>

```bash

def fibonacci(n):
      
      if( n==0):  # base case
            return 0
      elif(n==1):  # base case
            return 1
      else:
        return fibonacci(n-1) + fibonacci(n-2)   # recursive case

n = int(input("Enter a Number :"))

for i in range(n):

 print(fibonacci(i) , end=" ")

```
<br>

<b>Dry run of this code:</b>

```bash

Assume input :

Enter Number : 5

range(n) -> range(5) -> i = 0, 1, 2, 3, 4


Iteration 1 :

i = 0
fibonacci(0) -> base case -> return 0
Printed: 0

Iteration 2 :

i = 1
fibonacci(1) -> base case -> return 1
Printed: 1

Iteration 3 :

i = 2
fibonacci(2)
= fibonacci(n-1) + (n-2)
= fibonacci(2-1) + (2-2)
= fibonacci(1) + fibonacci(0)
= 1 + 0
= 1
Printed: 1

Iteration 4 :

i = 3
fibonacci(3)
= fibonacci(n-1) + (n-2)
= fibonacci(3-1) + (3-2)
= fibonacci(2) + fibonacci(1)
= 1 + 1
= 2
Printed: 2

Iteration 5 :

i = 4
fibonacci(4)
= fibonacci(n-1) + (n-2)
= fibonacci(4-1) + (4-2)
= fibonacci(3) + fibonacci(2)
= 2 + 1
= 3
Printed: 3


                            output :
                            0 1 1 2 3

```

<b>More Recursion Examples:</b>

```bash
# Sum of natural numbers
def sum_natural(n):
    if n == 1:
        return 1
    return n + sum_natural(n-1)

print(sum_natural(5))  # 15 (1+2+3+4+5)

# Power function
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp-1)

print(power(2, 3))  # 8 (2^3)
```

<b>Important Notes about Recursion:</b>

```bash
1. Always define a base case to avoid infinite recursion

2. Recursion can be slower than loops due to function call overhead

3. Too many recursive calls can cause stack overflow

4. Some problems are naturally recursive (tree traversal, factorial)

5. Use recursion when problem can be broken into smaller similar problems
```
