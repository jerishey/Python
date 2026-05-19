# Python
Python is one of the most popular programming languages. It’s simple to use, packed with features and supported by a wide range of libraries and frameworks. Its clean syntax makes it beginner-friendly.
<br>
Python was created by <b>Guido van Rossum and first released in 1991</b>. It focuses on readability and uses simple, English-like syntax.
Python is a Object Oriented Programming language.


- A high-level language, used in data science, automation, AI, web development and more.
- Known for its readability, which means code is easier to write, understand and maintain.
- Backed by strong library support, we don’t have to build everything from scratch.

## Why Learn Python?
```bash
1. Requires fewer lines of code compared to other programming languages like Java.
2. Provides libraries and frameworks such as Django and Flask for web development and tools like 
Pandas, TensorFlow and Scikit-learn for artificial intelligence, machine learning and data analysis.
3. Cross-platform, works on Windows, Mac and Linux without major changes.
4. Used by top tech companies like Google, Netflix and NASA.
5. Many Python coding job opportunities in Software Development, Data Science and AI/ML.
```

## Advantages of Python
```bash
1. Many Third-Party Modules: Python has many extra libraries and modules that help programmers do different tasks easily.
2. Large Support Libraries: Python provides powerful libraries like NumPy and Pandas for maths, data analysis, and scientific work.
3. Open Source and Big Community: Python is free to use, and many developers around the world help improve it and provide support.
4. Easy to Read and Learn: Python uses simple syntax, so beginners and experienced programmers can learn and write code easily.
5. Dynamically Typed Language: In Python, you do not need to declare the data type of variables, which makes coding flexible.
6. Supports Different Programming Styles: Python supports both object-oriented programming and procedural programming.
7. Portable and Interactive: Python programs can run on different operating systems, and Python allows instant testing of code through its interactive mode.
```

## Disadvantages of Python
```bash
1. Slower Performance: Python is slower than languages like C or Java because it is an interpreted language.
2. Global Interpreter Lock (GIL): Python allows only one thread to execute at a time, which can reduce performance in multi-threaded programs.
3. High Memory Usage: Python may use more memory, especially when handling large data or complex programs.
4. Dynamic Typing Issues: Since variable types can change during execution, errors may be harder to find and debug.
5. Package and Version Problems: Different libraries and package versions can sometimes create compatibility issues.
6. Too Much Flexibility: Python’s flexible syntax can sometimes make code harder to understand and maintain.
7. Not Best for System or Mobile Development: Python is not commonly used for operating systems, embedded systems, mobile apps, or frontend browser development because of performance limitations.
```

## Python Interpreter 
A Python interpreter is a program that reads, translates, and executes Python code line by line. It converts Python source code into bytecode(machine-understandable) instructions and produces output immediately.
<br>
There is no separate compilation step, which makes Python an interpreted language.
<br>

<b>How interpreter Works :</b>

```bash
1. You write Python code.

2. Interpreter reads the code line by line.

3. Code is converted into bytecode.

4. Bytecode is executed by the Python Virtual Machine (PVM).
```

## Python as Calculator 
Python can be used as a powerful calculator to perform basic and advanced mathematical calculations. This is usually done using the Python interpreter in interactive mode.
<br>

<b>How to use python as a calculator:</b>

```bash
1. Open command prompt or Terminal.

2. Type "python" . This open REPL(Read , Evaluate , Print ,Loop) in your cmd or terminal.

3. Type any calculation just like:
   
 2+6 = 8

4. For exit python type:
  
   exit()
```

## Python Shell 
The Python Shell is an interactive environment where you can write and execute Python commands one line at a time and get instant output. Python Shell is also called interactive interpreter.
<br>
It is identified by this :

```bash
>>>
```
<br>

<b>How to open Python shell :</b>

```bash

1. Open terminal or command prompt.

2. Type:
     python

3. You  will see:
    
    >>>
```

Example :

```bash
>>> print("Hello Python")
Hello Python
>>> 10 + 5
15
```

## Python Identifier
Python Identifiers are user-defined names for variables, functions, or classes. Must follow naming rules (no digits at start, only _ allowed).
- User-defined names for variables, functions, classes, modules, etc.
- Can include letters, digits, and underscores (_).
- Case-sensitive → num, Num, and NUM are different identifiers.
- Python provides str.isidentifier() to check if a string is a valid identifier.

### Rules for Naming Python Identifiers
```bash
1. It cannot be a reserved python keyword.
2. It should not contain white space.
3. It can be a combination of A-Z, a-z, 0-9, or underscore.
4. It should start with an alphabet character or an underscore ( _ ).
5. It should not contain any special character other than an underscore ( _ ).
```

`Example : `
```bash
- Valid identifiers:

1. var1
2. _var1
3. _1_var
4. var_1

- Invalid Identifiers

1. !var1
2. 1var
3. 1_var
4. var#1
5. var 1
```

## Python Keywords
Keywords in Python are special reserved words that are part of the language itself. They define the rules and structure of Python programs which means you cannot use them as names for your variables, functions, classes or any other identifiers.

### Features of Keywords
```bash
1. Predefined and reserved words with special meanings.
2. Used to define the syntax and structure of Python code.
3. Cannot be used as identifiers, variables, or function names.
4. Written in lowercase, except True and False.
5. Python 3.11 has 35 keywords.
6. The keyword module provides:
        iskeyword() → checks if a string is a keyword.
        kwlist → returns the list of all keywords.
```

### List of Python Keywords
| Category              | Keywords                                                                                                         |
| --------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Value Keywords        | `True`, `False`, `None`                                                                                          |
| Operator Keywords     | `and`, `or`, `not`, `is`, `in`                                                                                   |
| Control Flow Keywords | `if`, `else`, `elif`, `for`, `while`, `break`, `continue`, `pass`, `try`, `except`, `finally`, `raise`, `assert` |
| Function and Class    | `def`, `return`, `lambda`, `yield`, `class`                                                                      |
| Context Management    | `with`, `as`                                                                                                     |
| Import and Module     | `import`, `from`                                                                                                 |
| Scope and Namespace   | `global`, `nonlocal`                                                                                             |
| Async Programming     | `async`, `await`                                                                                                 |

## Input and Output in Python
The print() function is used for output in various formats and the input() function enables interaction with users.

`Taking Input using input() :` In Python, most programs need to collect information from users, such as their name, age or a number. This is done using the input() function, which:

- Pauses the program and waits for the user to type something.
- Returns the entered value as a string (str).
- Optionally displays a prompt message to guide the user.

```bash
val = input("Enter your value: ")
print(val)

Output:
Enter your value: 123
123
```

`How the input() Function Works`
```bash
- The program pauses until the user provides some input.
- You can optionally provide a prompt message (e.g., "Enter your age:").
- Whether you type letters, numbers, or symbols, Python always stores it as a string by default.
- If you need another data type (like integer or float), you must convert it manually using typecasting.
```

`Printing Output using print() :` The print() function allows us to display text, variables and expressions on the console.
```bash
Example:
print("Hello, World!")

Output:
Hello, World!
```

## Python Literals
Literals in Python are fixed values written directly in the code that represent constant data. They provide a way to store numbers, text, or other essential information that does not change during program execution. Python supports different types of literals, such as numeric literals, string literals, Boolean literals, and special values like None. 
<br>
For Example :
- 10, 3.14, and 5 + 2j are numeric literals.
- 'Hello' and "Python" are string literals.
- True and False are Boolean literals.

### Types of Literals
`1. Numeric Literals :` Numeric literals represent numbers and are classified into three types
```bash
1. Integer Literals – Whole numbers (positive, negative, or zero) without a decimal point. Example: 10, -25, 0

2. Floating-point (Decimal) Literals – Numbers with a decimal point, representing real numbers. Example: 3.14, -0.01, 2.0

3. Complex Number Literals – Numbers in the form a + bj, where a is the real part and b is the imaginary part. Example: 5 + 2j, 7 - 3j

Example:
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

`2. String Literals :` String literals are sequences of characters enclosed in quotes. They are used to represent text in Python.
```bash
Types of String Literals:

1. Single-quoted strings – Enclosed in single quotes (' '). Example: 'Hello, World!'

2. Double-quoted strings – Enclosed in double quotes (" "). Example: "Python is fun!"

3. Triple-quoted strings – Enclosed in triple single (''' ''') or triple double (""" """) quotes, generally used for multi-line strings or docstrings. Example:
'''This is
a multi-line
string'''

4. Raw strings – Prefix with r to ignore escape sequences (\n, \t, etc.). Example: r"C:\Users\Python" (backslashes are treated as normal characters).

Example:
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

`3. Boolean Literals :` Boolean literals represent truth values in Python. They help in decision-making and logical operations. Boolean literals are useful for controlling program flow in conditional statements like if, while, and for loops.
```bash
Types of Boolean Literals:

- True – Represents a positive condition (equivalent to 1).
- False – Represents a negative condition (equivalent to 0).

Example:
# Boolean literals
a = True
b = False

print(a, b)       # Output: True False
print(1 == True)  # Output: True
print(0 == False) # Output: True
print(True + 5)   # Output: 6 (1 + 5)
print(False + 7)  # Output: 7 (0 + 7)

Explanation:
- True is treated as 1, and False is treated as 0 in arithmetic operations.
- Comparing 1 == True and 0 == False returns True because Python considers True as 1 and False as 0.
```

`4. Collection Literals :` Python provides four different types of literal collections:
```bash
1. List literals: [1, 2, 3]
2. Tuple literals: (1, 2, 3)
3. Dictionary literals: {"key": "value"}
4. Set literals: {1, 2, 3}
```
`Example:`
```bash
Rank = ["First", "Second", "Third"]  # List
colors = ("Red", "Blue", "Green")  # Tuple
Class = { "Jai": 10, "Anaya": 12 }  # Dictionary
unique_num = {1, 2, 3}  # Set

print(Rank, colors, Class, unique_num)

Output:
['First', 'Second', 'Third'] ('Red', 'Blue', 'Green') {'Jai': 10, 'Anaya': 12} {1, 2, 3}

Explanation:

1. ["First", "Second", "Third"] is a list (rank of students).
2. ("Red", "Blue", "Green") is a tuple (like a set of crayons you can’t change).
3. {"Jai": 10, "Anaya": 12} is a dictionary (storing names and ages).
4. {1, 2, 3} is a set (a bag where every item is unique).
```
`5. Special Literal :` Python contains one special literal (None). 'None' is used to define a null variable. If 'None' is compared with anything else other than a 'None', it will return false.
```bash
Example:
res = None
print(res)

Output:
None

Explanation: None represents "nothing" or "empty value."
```
### Difference between Literals
| Type of Literals   | Description                                         | Example                                                       | Mutable/Immutable |
| ------------------ | --------------------------------------------------- | ------------------------------------------------------------- | ----------------- |
| Integer literals   | Whole numbers (without decimals).                   | `a = 77`                                                      | Immutable         |
| Float literals     | Numbers with a decimal point.                       | `b = 3.144`                                                   | Immutable         |
| Complex literals   | Numbers with real and imaginary parts.              | `c = 7 + 5j`                                                  | Immutable         |
| String literals    | Stores text using single, double, or triple quotes. | `greeting = "Bonjour"`<br>`story = """Once upon a time..."""` | Immutable         |
| Boolean literals   | Represents `True` or `False`.                       | `a = (1 == True) → True`<br>`b = (1 == False) → False`        | Immutable         |
| Boolean as Number  | Boolean values can act as numbers (`1` or `0`).     | `c = True + 3 → 4`<br>`d = False + 7 → 7`                     | Immutable         |
| List literal       | Stores multiple values and can be changed.          | `Rank = ["First", "Second", "Third"]`                         | Mutable           |
| Tuple literal      | Like a list but cannot be changed.                  | `colors = ("Red", "Blue", "Green")`                           | Immutable         |
| Dictionary literal | Stores data in key-value pairs.                     | `Class = {"Jai": 10, "Anaya": 12}`                            | Mutable           |
| Set literal        | Stores unique unordered values.                     | `unique_num = {1, 2, 3}`                                      | Mutable           |
| Special literal    | Represents no value or empty value.                 | `water_remain = None`                                         | Immutable         |


## indentation in Python
Indentation means the spaces or tabs at the beginning of a line of code. In Python, indentation is very important because it is used to define blocks of code.
<br>
Unlike C, C++ or Java (which use { }), Python uses indentation to show structure or define the block of code.
<br>

<b>Why Indentation is important :</b>

```bash
1.It tells Python which statements belong together.

2.Controls the flow of:
- if-else
- for and while loops
- functions
- classes

3.Wrong indentation causes an Indentation error
```
Example :

```bash
num = 8

if num%2==0:
    print("even number")
else:
    print(" odd number")    
```
## Comments in Python
Comments are lines in a program that are ignored by the Python interpreter.
<br>
They are used to explain code, make programs easy to understand, and improve readability.
<br>

<b>Types of comments:</b>
<br>
There are Two types of comments in python:
<br>

`1. Single-Line comments :`
<br>
Single-Line commnets starts with hash sign (#). Anything written after hash sign is consider as comments and that line id ignored by python interpreter.
<br>
Example:

```bash
# This is a single-line comment
x = 10  # variable storing value
```
`2. Multi-Line Comments :`
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

## Python Variables
Variables are used to store data that can be referenced and manipulated during program execution. A variable is essentially a name that is assigned to a value.

- Unlike Java and many other languages, Python variables do not require explicit declaration of type.
- Type of the variable is inferred based on the value assigned.

### Rules for Naming Variables
```bash
1. Variable names can only contain letters, digits and underscores (_).
2. A variable name cannot start with a digit.
3. Variable names are case-sensitive like myVar and myvar are different.
4. Avoid using Keywords like if, else, for as variable names.
```
Example :
```bash
1. Valid Variables
age = 21
_colour = "lilac"
total_score = 90

2. Invalid Variables
1name = "Error"  # Starts with a digit
class = 10       # 'class' is a reserved keyword
user-name = "Doe"  # Contains a hyphen
```

### Assigning Values to Variables
```bash
1. Basic Assignment: Variables are assigned values using the = operator.
x = 5
y = 3.14
z = "Hi"

2. Dynamic Typing: variables are dynamically typed, meaning the same variable can hold different types of values during execution.
x = 10
x = "Now a string"

- Multiple Assignments
3. Assigning Same Value: allows assigning the same value to multiple variables in a single line, which can be useful for initializing variables with the same value.
a = b = c = 100
print(a, b, c)

4. Assigning Different Values: we can assign different values to multiple variables simultaneously, making the code concise and easier to read.
x, y, z = 1, 2.5, "Python"
print(x, y, z)
```

## Python Data Types
Data types in Python are a way to classify data items. They represent the kind of value which determines what operations can be performed on that data. Since everything is an object in Python programming, Python data types are classes and variables are instances (objects) of these classes.

<b>`1. Numeric Data Types :`</b> Python numbers represent data that has a numeric value. A numeric value can be an integer, a floating number or even a complex number. These values are defined as int, float and complex classes.

```bash
1. Integers: value is represented by int class. It contains positive or negative whole numbers (without fractions or decimals). There is no limit to how long an integer value can be.

2. Float: value is represented by float class. It is a real number with a floating-point representation. It is specified by a decimal point. Optionally, character e or E followed by a positive or negative integer may be appended to specify scientific notation.

3. Complex Numbers: It is represented by a complex class. It is specified as (real part) + (imaginary part)j. For example - 2+3j

Example:
a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))
```

<b>`2. Sequence Data Types :`</b> A sequence is an ordered collection of items, which can be of similar or different data types. Sequences allow storing of multiple values in an organized and efficient fashion. There are several sequence data types of Python:

`1. String Data Type :` Python Strings are arrays of bytes representing Unicode characters. In Python, there is no character data type, a character is a string of length one. It is represented by str class.
<br>
Strings in Python can be created using single quotes, double quotes or even triple quotes. We can access individual characters of a String using index.
```bash
s = 'Hello World!'
print(s)

# check data type 
print(type(s))

# access string with index
print(s[1])
print(s[2])
print(s[-1]) # -1 refers to the last character, -2 is second last, and so on
```

`2. List Data Type :` Lists are similar to arrays found in other languages. They are an ordered and mutable collection of items. It is very flexible as items in a list do not need to be of the same type.
```bash
- Creating a List in Python: Lists can be created by just placing sequence inside the square brackets[].

Example:
# Empty list
a = []

# list with int values
a = [1, 2, 3]
print(a)

# list with mixed values int and String
b = ["Nitish", "Shivam", "Rakesh", 4, 5]
print(b)
```

`3. Tuple Data Type :` Tuple is an ordered collection of Python objects. The only difference between a tuple and a list is that tuples are immutable. Tuples cannot be modified after it is created.
```bash
# initiate empty tuple
tup1 = ()

tup2 = ('Nistish', 'Rakesh')
print("\nTuple with the use of String: ", tup2)
```

<b>`3. Boolean Data Type :`</b> The Boolean data type in Python represents one of two values: True or False. It is used to store logical values and is denoted by the class bool.

- Boolean values are commonly used in conditions, comparisons and decision-making statements.
```bash
print(type(True))
print(type(False))
print(type(true))

Output:
<class 'bool'>
<class 'bool'>

Hangup (SIGHUP)
Traceback (most recent call last):
  File "/home/guest/sandbox/Solution.py", line 3, in <module>
    print(type(true))
               ^^^^
NameError: name 'true' is not defined. Did you mean: 'True'?
```
`Truthy and Falsy Values :` truthy and falsy values are values that evaluate to True or False in a Boolean context. Truthy values behave like True, while falsy values behave like False when used in conditions.

```bash
1. Truthy Values
- Non-empty sequences or collections: [ 1 ], ( 0, ), "Hello", { 1:2 }
- Numeric values not equal to zero: 1, -4, 3.5
- Constant: True

2. Falsy Values
- Empty sequences and collections: [ ], ( ), { }, set( ), " ", range(0)
- Numbers: 0 (integer), 0.0 (float), 0j (complex)
- Constants: None, False

Example:
if 1:
    print("1 is truthy")

if not 0:
    print("0 is falsy")

Output:
1 is truthy
0 is falsy
```

<b>`4. Set Data Type :`</b> Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements.
```bash
numbers = {1, 2, 3, 4}

print(numbers)
print(type(numbers))

Output:
{1, 2, 3, 4}
<class 'set'>
```

`5. Dictionary Data Type :` A dictionary in Python is a collection of data values used to store information in the form of key-value pairs. It works like a map where each key is associated with a specific value, allowing fast access and retrieval of data.
- Each key is unique.
- A colon (:) separates a key and its value.
- Multiple key-value pairs are separated by commas.
```bash
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print(student)
print(type(student))

Output:
{'name': 'Rahul', 'age': 20, 'course': 'Python'}
<class 'dict'>
```
## Python Operators
Python operators are fundamental for performing mathematical calculations. In Python programming, Operators in general are used to perform operations on values and variables.
- Operators: Special symbols like -, + , * , /, etc.
- Operands: Value on which the operator is applied.

### `Types of Operators in Python`

#### <b>`Arithmetic Operators :`</b> 
Arithmetic operators are symbols used to perform mathematical operations on numerical values. Arithmetic operators include addition (+), subtraction (-), multiplication (*), division (/), and modulus (%).

`1. Addition Operator :` In Python, + is the addition operator. It is used to add 2 values.
```bash
 val1 = 2
val2 = 3

# using the addition operator
res = val1 + val2
print(res)
```

`2. Subtraction Operator :` In Python, - is the subtraction operator. It is used to subtract the second value from the first value.
```bash
val1 = 2
val2 = 3

# using the subtraction operator
res = val1 - val2
print(res)
```

`3. Multiplication Operator :` Python * operator is the multiplication operator. It is used to find the product of 2 values.
```bash
val1 = 2
val2 = 3

# using the multiplication operator
res = val1 * val2
print(res)
```
`4. Division Operator :` In Python programming language Division Operators allow us to divide two numbers and return a quotient, i.e., the first number or number at the left is divided by the second number or number at the right and returns the quotient. 

- There are two types of division operators: 
```bash
1. Float division : The quotient returned by this operator is always a float number, no matter if two numbers are integers.

Example:
print(5/5)
print(10/2)
print(-10/2)
print(20.0/2)

Output:
1.0
5.0
-5.0
10.0

2. Floor division : The quotient returned by this operator is dependent on the argument being passed. If any of the numbers is float, it returns output in float. 
- It is also known as Floor division because, if any number is negative, then the output will be floored.

Example:
print(10//3)
print (-5//2)
print (5.0//2)
print (-5.0//2)

Output:
3
-3
2.0
-3.0
```

`5. Modulus Operator :` The % in Python is the modulus operator. It is used to find the remainder when the first operand is divided by the second. 
```bash
val1 = 3
val2 = 2

# using the modulus operator
res = val1 % val2
print(res)
```

`6. Exponentiation Operator :` In Python, ** is the exponentiation operator. It is used to raise the first operand to the power of the second.
```bash
val1 = 2
val2 = 3

# using the exponentiation operator
res = val1 ** val2
print(res)
```
<b>`Precedence of Arithmetic Operators in Python`</b>
| Operators           | Description                                           | Associativity |
| ------------------- | ----------------------------------------------------- | ------------- |
| `**`                | Exponentiation Operator                               | Right-to-Left |
| `%`, `*`, `/`, `//` | Modulus, Multiplication, Division, and Floor Division | Left-to-Right |
| `+`, `-`            | Addition and Subtraction Operators                    | Left-to-Right |
<br>

#### <b>`Comparison Operators`</b>
Comparison operators (or Relational) in Python allow you to compare two values and return a Boolean result: either True or False. 
<br>
Python supports comparison across different data types, such as numbers, strings and booleans. For strings, the comparison is based on lexicographic (alphabetical) order.

`1. Equality Operator (==) :` The equality operator checks if two values are exactly the same.
```bash
Example:
a = 9
b = 5
c = 9

print(a == b)
print(a == c)

Output:
False
True

Explanation: a == b is False because 9 is not equal to 5 and a == c is True because both values are 9.
```

`2. Inequality Operator (!=) :` The inequality operator checks if two values are not equal.
```bash
Example:
a = 9
b = 5
c = 9

print(a != b)
print(a != c)

Output:
True
False

Explanation: a != b is True because 9 and 5 are different and a != c is False because both are 9.
```

`3. Greater Than Operator (>) :` Checks if the left operand is larger than the right.
```bash
Example: Comparing two numbers with the greater-than operator.
a = 9
b = 5
​
print(a > b)
print(b > a)

Output:
True
False
```

`4. Less Than Operator (<) :` Checks if the left operand is smaller than the right.
```bash
Example: Comparing two numbers with the less-than operator.
a = 9
b = 5

print(a < b)
print(b < a)

Output:
False
True
```

`5. Greater Than or Equal To Operator (>=) :` Checks if the left operand is greater than or equal to the right.
```bash
Example: Using >= to check greater than or equal conditions.
a = 9
b = 5
c = 9

print(a >= b)
print(a >= c)
print(b >= a)

Output:
True
True
False
```

`6. Less Than or Equal To Operator (<=) :` Checks if the left operand is less than or equal to the right.
```bash
Example: Using <= to check less than or equal conditions.
a = 9
b = 5
c = 9

print(a <= b)
print(a <= c)
print(b <= a)

Output:
False
True
True
```

`7. Chaining Comparison Operators :` Python allows you to chain multiple comparisons in a single statement. This makes conditions more compact and readable.
```bash
Example: Using chained operators to evaluate multiple conditions together.
a = 5

print(1 < a < 10)
print(10 > a <= 9)
print(5 != a > 4)
print(a < 10 < a*10 == 50)

Output:
True
True
False
True

Explanation:
- 1 < a < 10: True because 5 is between 1 and 10.
- 10 > a <= 9: True because 5 < 10 and 5 <= 9.
- 5 != a > 4: False because a equals 5.
- a < 10 < a*10 == 50: True because 5 < 10 and 5*10 = 50.
```

#### `Logical Operators :` 
Python logical operators are used to combine or modify conditions and return a Boolean result (True or False). They are commonly used in conditional statements to control the flow of a program based on multiple logical conditions.
```bash
1. AND Operator : The Boolean AND operator returns True if both the operands are True else it returns False.

2. OR Operator : The Boolean OR operator returns True if either of the operands is True.

3. NOT Operator : The Boolean NOT operator works with a single boolean value. If the boolean value is True it returns False and vice-versa.
```
<br>

<b>`Truth Table for Logical Operators`</b>
| A     | B     | A and B | A or B | not A |
| ----- | ----- | ------- | ------ | ----- |
| True  | True  | True    | True   | False |
| True  | False | False   | True   | False |
| False | True  | False   | True   | True  |
| False | False | False   | False  | True  |

<br>

<b>`Example:`</b>
```bash
a, b, c = True, False, True

# AND: Both conditions must be True
if a and c:
    print("Both a and c are True (AND condition).")

# OR: At least one condition must be True
if b or c:
    print("Either b or c is True (OR condition).")

# NOT: Reverses the condition
if not b:
    print("b is False (NOT condition).")

Output:
- Both a and c are True (AND condition).
- Either b or c is True (OR condition).
- b is False (NOT condition).

Explanation:
- a and c returns True because both values are True.
- b or c returns True because at least one value is True.
- not b reverses False to True, so the condition executes.
```

#### <b>`Bitwise Operators :`</b> 
Python bitwise operators are used to perform bitwise calculations on integers. The integers are first converted into binary and then operations are performed on each bit or corresponding pair of bits and the result is then returned in decimal format.

```bash
1. Bitwise AND Operator : Python Bitwise AND (&) operator takes two equal-length bit patterns as parameters. The two-bit integers are compared. If the bits in the compared positions of the bit patterns are 1, then the resulting bit is 1. If not, it is 0.

2. Bitwise OR Operator : Python Bitwise OR (|) Operator takes two equivalent length bit designs as boundaries, if the two bits in the looked-at position are 0, the next bit is zero. If not, it is 1.

3. Bitwise XOR Operator : Python Bitwise XOR (^) Operator also known as the exclusive OR operator, is used to perform the XOR operation on two operands, i.e., it compares corresponding bits of two operands and returns true if and only if exactly one of the operands is true.

4. Bitwise NOT Operator : Python Bitwise Not (~) is a unary operator that returns one's complement of the operand. This means it toggles all bits in the value, transforming 0 bits to 1 and 1 bits to 0.
```

`Bitwise Shift :` These operators are used to shift the bits of a number left or right thereby multiplying or dividing the number by two respectively. They can be used when we have to multiply or divide a number by two.
```bash
1. Bitwise Right Shift : Shifts the bits of the number to the right and fills 0 on voids left(fills 1 in the case of a negative number) as a result. Similar effect as of dividing the number with some power of two.

Example 1: Right shifting a positive integer

a = 10 = 0000 1010 (Binary)
a >> 1 = 0000 0101 = 5

2. Bitwise Left Shift : Shifts the bits of the number to the left and fills 0 on voids right as a result. Similar effect as of multiplying the number with some power of two.

Example 1: Left shifting a positive integer

a = 5 = 0000 0101 (Binary)
a << 1 = 0000 1010 = 10
```

#### <b>`Assignment Operators :`</b> 
Assignment Operators are used to assign values to variables. This operator is used to assign the value of the right side of the expression to the left side operand.
```bash
# Assigning values using 
# Assignment Operator 
a = 3
b = 5

c = a + b 

# Output 
print(c)
```

`1. Addition Assignment Operator :` The Addition Assignment Operator is used to add the right-hand side operand with the left-hand side operand and then assigning the result to the left operand.
```bash
a = 3
b = 5

# a = a + b
a += b

# Output
print(a)
```

`2. Subtraction Assignment Operator :` The Subtraction Assignment Operator is used to subtract the right-hand side operand from the left-hand side operand and then assigning the result to the left-hand side operand.
```bash
a = 3
b = 5

# a = a - b
a -= b

# Output
print(a)
```

`3. Multiplication Assignment Operator :` The Multiplication Assignment Operator is used to multiply the right-hand side operand with the left-hand side operand and then assigning the result to the left-hand side operand.
```bash
a = 3
b = 5

# a = a * b
a *= b

# Output
print(a)
```

`4. Division Assignment Operator :` The Division Assignment Operator is used to divide the left-hand side operand with the right-hand side operand and then assigning the result to the left operand.
```bash
Syntax: a /= b

Example:
a = 3
b = 5

# a = a / b
a /= b

# Output
print(a)
```

`5. Modulus Assignment Operator :` The Modulus Assignment Operator is used to take the modulus, that is, it first divides the operands and then takes the remainder and assigns it to the left operand.
```bash
Syntax: a %= b

Example:
a = 3
b = 5

# a = a % b
a %= b

# Output
print(a)
```

`6. Floor Division Assignment Operator :` The Floor Division Assignment Operator is used to divide the left operand with the right operand and then assigs the result(floor value) to the left operand.
```bash
Syntax: a //= b

Example:
a = 3
b = 5

# a = a // b
a //= b

# Output
print(a)
```

`7. Exponentiation Assignment Operator :` The Exponentiation Assignment Operator is used to calculate the exponent(raise power) value using operands and then assigning the result to the left operand.
```bash
Syntax: a **= b

Example:
a = 3
b = 5

# a = a ** b
a **= b

# Output
print(a)
```

`8. Bitwise AND Assignment Operator :` The Bitwise AND Assignment Operator is used to perform Bitwise AND operation on both operands and then assigning the result to the left operand.
```bash
Syntax: a &= b

Example:
a = 3
b = 5

# a = a & b
a &= b

# Output
print(a)
```

`9. Bitwise OR Assignment Operator :` The Bitwise OR Assignment Operator is used to perform Bitwise OR operation on the operands and then assigning result to the left operand.
```bash
Syntax: a |= b

Example:
a = 3
b = 5

# a = a | b
a |= b

# Output
print(a)
```

`10. Bitwise XOR Assignment Operator :` The Bitwise XOR Assignment Operator is used to perform Bitwise XOR operation on the operands and then assigning result to the left operand.
```bash
Syntax: a ^= b

Example:
a = 3
b = 5

# a = a ^ b
a ^= b

# Output
print(a)
```

`11. Bitwise Right Shift Assignment Operator :` The Bitwise Right Shift Assignment Operator is used to perform Bitwise Right Shift Operation on the operands and then assign result to the left operand.
```bash
Syntax: a >>= b

Example:
a = 3
b = 5

# a = a >> b
a >>= b

# Output
print(a)
```

`12. Bitwise Left Shift Assignment Operator :` The Bitwise Left Shift Assignment Operator is used to perform Bitwise Left Shift Opertator on the operands and then assign result to the left operand.
```bash
Syntax: a <<= b

Example:
a = 3
b = 5

# a = a << b
a <<= b

# Output
print(a)
```

`13. Walrus Operator :` The Walrus Operator (:=), introduced in Python 3.8, allows you to assign a value to a variable as part of an expression. It helps avoid redundant code when a value needs to be both used and tested in the same expression — especially in loops or conditional statements.
```bash
Syntax: variable := expression
- The expression on the right-hand side is evaluated, assigned to the variable, and then returned.

Example:
num = [1, 2, 3, 4, 5]

while (n := len(num)) > 0:
    print(num.pop())

Output:
5
4
3
2
1

Explanation:
- len(numbers) is assigned to n inside the loop condition.
- The loop continues while n > 0, printing and removing elements until the list is empty.
- This avoids calling len(numbers) repeatedly in separate statements.
```

#### <b>`Python Membership and Identity Operators`</b>
In Python, Membership and Identity operators help us check relationships between values and objects. They are mainly used to test whether a value exists within a sequence or whether two variables refer to same object in memory.

`1. Membership Operators :` The Membership operators test for the membership of an object in a sequence, such as strings, lists or tuples. Python offers two membership operators to check or validate the membership of a value.
```bash
1. IN Operator : The "in" operator returns True if the given element exists inside a sequence, otherwise it returns False.

Example:
l = [1, 2, 3, 4, 5]
s = "Hello World"

print(2 in l)
print('O' in s)

Output:
True
False

Explanation:
- 2 in l: True because 2 exists in the list.
- 'O' in s: False because Python is case-sensitive ('O' ≠ 'o').

2. NOT IN Operator : The "not in" operator works the opposite of "in" operator, it returns True if the element is not found in a sequence.

Example:
l = [1, 2, 3, 4, 5]
s = "Hello World"

print(2 not in l)
print('O' not in s)

Output:
False
True

Explanation:
- 2 not in l: False because 2 exists.
- 'O' not in s: True because 'O' is missing.

3. operator.contains() Method : Python also provides a function from the operator module called contains() that works like in.

Syntax: operator.contains(sequence, value)

Example:
import operator

print(operator.contains([1, 2, 3, 4, 5], 2))         # list
print(operator.contains("Hello World", 'O'))         # string
print(operator.contains({1, 2, 3, 4, 5}, 6))         # set
print(operator.contains({1: "Ram", 2:"Son"}, 3))   # dictionary key
print(operator.contains((1, 2, 3, 4, 5), 9))         # tuple

Output:
True
False
False
False
False

Explanation: Works the same as in, but in function form (useful in functional programming).
```

`2. Identity Operators :` The Identity Operators are used to compare the objects if both objects are actually of same data type and share same memory location.
```bash
1. IS Operator : The "is" operator checks if two variables point to the same object (same memory location).

Example:
n1 = 5
n2 = 5

a = [1, 2, 3]
b = [1, 2, 3]
c = a

s1 = "hello world"
s2 = "hello world"

print(n1 is n2)  # integers
print(a is b)        # lists
print(a is c)        # reference
print(s1 is s2)      # strings

Output:
True
False
True
True

Explanation:
- n1 is n2: True because small integers are cached by Python.
- a is b: False because even though the lists look the same, they are stored at different memory locations.
- a is c: True because c directly refers to a.
- s1 is s2: True because Python reuses identical string objects.

2. IS NOT Operator : The "is not" operator checks if two variables point to different objects.

Example:
n1 = 5
n2 = 5

a = [1, 2, 3]
b = [1, 2, 3]
c = a

s1 = "hello world"
s2 = "hello world"

print(n1 is not n2)
print(a is not b)
print(a is not c)
print(s1 is not s2)

Output:
False
True
False
False

Explanation:
- a is not b: True because they are different objects.
- a is not c: False because they point to the same object.
```

`Difference Between == and is :` The equality operator (==) is used to compare value of two variables, whereas identity operator (is) is used to compare memory location of two variables.
```bash
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)   # identity check
print(a == b)   # value check

Output:
False
True

Explanation:
- a == b: True because the contents are the same.
- a is b: False because they are stored as separate list objects.
```
#### `Ternary Operator`
Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false.
- It simply allows testing a condition in a single line replacing the multiline if-else, making the code compact.
```bash
Syntax :  [on_true] if [expression] else [on_false] 

Example:
a = 10
b = 20

result = "a is greater" if a > b else "b is greater"

print(result)

Output:
b is greater
```

## Precedence and Associativity of Operators in Python
In Python, operators have different precedence levels, which determine order in which expressions are evaluated. If operators have same precedence, associativity decides whether they are evaluated left-to-right or right-to-left.

```bash
1. Operators Precedence : Operator precedence defines order in which Python evaluates different operators in an expression. When an expression has multiple operators, Python follows precedence rules to decide order of evaluation.

2. Operators Associativity : If an expression contains two or more operators with same precedence then Operator Associativity is used. It can either be Left to Right or from Right to Left.
```

<b>`Operator Precedence and Associativity List in Python`</b>

<i>

|      | Operator | Description | Associativity |
|---|---|---|---|
| 1 | `()` | Parentheses (highest precedence) | Left to right |
| 2 | `x[index]`, `x[index:index]` | Subscription, slicing | Left to right |
| 3 | `await x` | Await expression | — |
| 4 | `**` | Exponentiation | Right to left |
| 5 | `+x`, `-x`, `~x` | Unary plus, unary minus, bitwise NOT | Right to left |
| 6 | `*`, `@`, `/`, `//`, `%` | Multiplication, matrix multiplication, division, floor division, remainder | Left to right |
| 7 | `+`, `-` | Addition and subtraction | Left to right |
| 8 | `<<`, `>>` | Bitwise shifts | Left to right |
| 9 | `&` | Bitwise AND | Left to right |
| 10 | `^` | Bitwise XOR | Left to right |
| 11 | `\|` | Bitwise OR | Left to right |
| 12 | `in`, `not in`, `is`, `is not`, `<`, `<=`, `>`, `>=`, `!=`, `==` | Comparisons, membership, identity tests | Left to right |
| 13 | `not x` | Boolean NOT | Right to left |
| 14 | `and` | Boolean AND | Left to right |
| 15 | `or` | Boolean OR | Left to right |
| 16 | `if-else` | Conditional expression | Right to left |
| 17 | `lambda` | Lambda expression | — |
| 18 | `:=` | Assignment expression (Walrus operator) | Right to left |

</i>
<br>

## Conditional Statements in Python
Conditional statements are used to control the flow of execution in a program based on specific conditions. They allow programs to execute different blocks of code depending on whether a condition evaluates to True or False.

`1. If Statement :` If statement is used to execute a block of code only when a specified condition evaluates to True.

```bash
Syntax:
if(Condition) {
    // Code Block
}

Example:
age = 20
if age >= 18:
    print("Eligible to vote.")

Output:
Eligible to vote.
```

`2. Short Hand if :` Short-hand if is used to write if statements in a single line. It is useful when only one statement needs to be executed.
```bash
Example:
age = 19
if age > 18: print("Eligible to Vote.")

Output:
Eligible to vote.
```

`3. If else Statement :` In Python, If-Else is a fundamental conditional statement used for decision-making in programming. If...Else statement allows to execution of specific blocks of code depending on the condition is True or False.
<br>
When the if condition is False. If the condition in the if statement is not true, the else block will be executed.
```bash
Syntax:
if condition:
    # code executes if condition is True
else:
    # code executes if condition is False

Example:
age = 25
exp = 10

# Using '>' operator & 'and' with if-else
if age > 23 and exp > 8:
    print("Eligible.")
else:
    print("Not eligible.")

Output:
Eligible.
```

`4. Nested If Else Statement :` Nested if...else statement occurs when if...else structure is placed inside another if or else block. Nested If..else allows the execution of specific code blocks based on a series of conditional checks.
```bash
Syntax:
if condition1:
    # code executes if condition1 is True

    if condition2:
        # code executes if condition2 is also True
    else:
        # code executes if condition2 is False

else:
    # code executes if condition1 is False

Example:
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")

Output:
You can drive
```

`5. if…elif…else Statement :` if-elif-else statement in Python is used for multi-way decision-making. This allows us to check multiple conditions sequentially and execute a specific block of code when a condition is True. If none of the conditions are true, the else block is executed.
```bash
Syntax:
if condition1:
    # code executes if condition1 is True

elif condition2:
    # code executes if condition2 is True

else:
    # code executes if all conditions are False

Example:
marks = 75

if marks >= 90:
    print("Grade A")

elif marks >= 60:
    print("Grade B")

else:
    print("Grade C")

Output:
Grade B
```

`6. Ternary Conditional Statement or Ternary Operator :` Ternary conditional statement is a short way to write an if-else statement in a single line. It is used when choosing between two values based on a condition.
```bash
Syntax:
value_if_true if condition else value_if_false

Example:
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)

Output:
Adult
```

`7. Match-Case Statement :` Match-Case statement is used to compare a value against multiple patterns and execute the matching block of code. It is similar to the switch-case statement available in other programming languages.
```bash
Syntax:
match variable:
    case value1:
        # code block

    case value2:
        # code block

    case _:
        # default block

Explanation:
1. match checks the value.
2. case defines possible matches.
3. _ works like a default case.
4. Makes multiple condition checking cleaner and easier to read.

Example:
day = 2

match day:
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case _:
        print("Invalid day")

Output:
Tuesday
```

## Loops in Python
Loops are used to execute a block of code repeatedly until a condition is met or all items in a sequence are processed. The main types are For loops (iterating over sequences) and While loops (executing code based on a condition).

### `1. For Loop :` 
Python for loops are used to iterate over sequences such as lists, tuples, strings and ranges.

- Allows the same operation to be applied to every item in a sequence.
- Avoids the need to manage loop indices manually.
```bash
Syntax:
for variable in sequence:
    # code block

Example: Loop through a list
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

`range() Method :` The range() function in Python is used to generate a sequence of integers within a specified range. It is most commonly used in loops to control how many times a block of code runs.
- range(stop) generates numbers from 0 to stop-1.
- range(start, stop) generates numbers from start to stop-1.
- range(start, stop, step) generates numbers from start to stop-1, incrementing by step.
```bash
Syntax:
range(start, stop, step)

Parameters:
1. start (optional): Starting number of the sequence (default is 0)
2. stop: Number at which the sequence stops (not included)
3. step (optional): Difference between consecutive numbers (default is 1)

Return: A range object representing the sequence

Example:
for n in range(5, 10):
    print(n, end=" ")

Output:
5 6 7 8 9 

Explanation:
- range(5, 10) starts at 5 and stops before 10
- Numbers increase by the default step of 1
```

### `2. While Loop :`
While Loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop in the program is executed.
```bash
while condition:
    statement(s)

Parameter:
1. condition: This is a boolean expression. If it evaluates to True, the code inside the loop will execute.
2. statement(s): These are the statements that will be executed during each iteration of the loop.

Example:
i = 1

while i <= 5:
    print(i)
    i += 1

Output:
1
2
3
4
5
```

### `Control Statements :` 
These statements are used to change the normal flow of loop execution in Python. They help control loop behavior by skipping iterations, stopping loops or acting as placeholders inside loops and conditional blocks.

`1. Continue Statement :` The continue statement in Python is a loop control statement that skips the rest of the code inside the loop for the current iteration and moves to the next iteration immediately.
```bash
Example:
for i in range(1, 11):
    if i == 6:
        continue
    print(i, end=" ")

Output:
1 2 3 4 5 7 8 9 10 

Explanation: When i == 6, the continue statement executes, skipping the print operation for 6.

Example: 
i = 0
while i < 10:
    if i == 5:
        i += 1  # ensure the loop variable is incremented to avoid infinite loop
        continue
    print(i)
    i += 1

Explanation : When i == 5, the continue statement skips printing and jumps to the next iteration.
```

`2. break statement :` The break statement in Python is used to exit or "break" out of a loop (either for or while loop) prematurely, before the loop has iterated through all its items or reached its condition. 
<br>
When the break statement is executed, the program immediately exits the loop, and the control moves to the next line of code after the loop.
```bash
Example:
a = [1, 3, 5, 7, 9, 11]
val = 7

for i in a:
    if i == val:
        print(f"Found at {i}!")
        break
else:
    print(f"not found")

Output:
Found at 7!

Explanation:
- The loop iterates through each number in the list.
- When the number 7 is found, it prints a confirmation message and executes break, exiting the loop immediately.
- If the loop completes without finding the number, the else block is executed.

Example: while Loop with break
i = 1

while i <= 5:
    if i == 4:
        break
    print(i)
    i += 1

Explanation : The loop stops when i becomes 4.
```

`3. pass Statement :` The pass statement in Python is a placeholder that does nothing when executed.

- It is used to keep code blocks valid where a statement is required but no logic is needed yet.
- Examples situations where pass is used are empty functions, classes, loops or conditional blocks.
```bash
1. In Functions : The pass keyword in a function is used when we define a function but don't want to implement its logic immediately. It allows the function to be syntactically valid, even though it doesn't perform any actions yet.

Example:
def fun():
    pass

fun() # Call the function

Explanation: fun() is defined but contains pass statement, so it does nothing when called and program continues execution without any errors.

2. In Conditional Statements : In conditional statements, when no action is needed but a block is still required, pass statement acts as a placeholder to keep the code syntactically valid.

Example:
x = 10

if x > 5:
    pass  # Placeholder for future logic
else:
    print("x is 5 or less")

Explanation:
- When x > 5, the pass statement runs, so nothing happens.
- If x <= 5, else block executes and prints the message.

3. In Loops : In loops, pass can be used to skip writing any action during a specific iteration while still keeping the loop structure correct.

Example:
for i in range(5):
    if i == 3:
        pass  # Do nothing when i is 3
    else:
        print(i)

Explanation:
- For i == 3, the pass statement ensures nothing happens.
- For other values, the loop prints the number.

4. In Classes : The pass statement allows defining empty classes or methods that act as placeholders until actual functionality is added later.

Example:
class EmptyClass:
    pass  # No methods or attributes yet

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        pass  # Placeholder for greet method

# Creating an instance of the class
p = Person("Emily", 30)

Explanation:
- EmptyClass is valid even without methods or attributes because of pass.
- greet() method exists but does nothing yet, letting us build the structure first.
```

### `Advanced Loop Features :`
`1. Else Statement :` else block with a loop executes only when the loop completes normally without a break statement.
```bash
Example:
for i in range(1, 4):
    print(i)
else:  
    print("No Break\n")

Output:
1
2
3
No Break

Explanation:
- for i in range(1, 4): iterates from 1 to 3.
- else: executes after loop completion.
- "No Break" is printed because loop ends normally without break.
```

`2. Enumerate :` The enumerate() function in Python is used to iterate over an iterable while keeping track of both the index and the value. 
<br>
It returns pairs in the form (index, element). This removes the need to manually maintain a counter variable during iteration.
```bash
Syntax:
enumerate(iterable, start=0) 

Parameters:
1. iterable: sequence or collection to iterate over.
2. start (optional): starting value of the index. Default is 0.

Example:
a = ["A", "B", "C"]
r = list(enumerate(a))
print(r)

Output:
[(0, 'A'), (1, 'B'), (2, 'C')]

Explanation: list(enumerate(a)) converts index-element pairs into a list of tuples.
```

`3. Nested Loops :` In Python, there are two types of loops: for loop and while loop. Using these loops, we can create nested loops, which means loops inside a loop. For example, a while loop inside a for loop, or a for loop inside another for loop.
```bash
Syntax:
Outer_loop Expression:
    Inner_loop Expression:
        Statement inside inner_loop
    Statement inside Outer_loop

Example: Nested for Loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

Output:
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3

Example: Nested while Loop
i = 1

while i <= 3:
    j = 1

    while j <= 3:
        print(i, j)
        j += 1

    i += 1
```

## Python Functions 
Python functions are reusable blocks of code used to perform a specific task. They help organize programs into smaller sections and execute the same logic whenever needed by calling the function.

### `Why Use Functions`
```bash
1. Code Reusability : Write code once and use many times.
2. Reduces code duplication : Avoid writing the same code again and again.
3. Makes code easy to understand : Programs become more organized and readable.
4. Easier debugging : Errors can be found and fixed easily.
5. Improves program structure : Large programs can be divided into smaller parts.
```

### `1. Defining a Function`
A function can be defined using def keyword. 
<br>
The def keyword in Python is used to define a function. Functions are logical blocks of code that can be reused multiple times.
```bash
Syntax:
def function_name(parameters):
    # Code to execute
    return value  # Optional

Explanation:
1. def: Keyword to define a function
2. function_name: Name of the function
3. parameters: Optional input values (can be empty)
4. return: Optional, sends a value back from the function
5. The indented block is executed when the function is called
```

### `2. Calling a Function`
After creating a function, call it by using the name of the functions followed by parenthesis containing parameters of that particular function.
```bash
Example:
def func():
    print("Hello")

func()

Explanation:
- def func(): Defines a function named func.
- print("Hello"): Code inside the function that runs when called.
- func(): Calls the function, printing Hello to the output.
```

### `3. Function Arguments`
Arguments are values passed to a function when it is called. They allow functions to receive input data and perform operations using those values.
```bash
Syntax:
def function_name(arguments):
    # function body
    return value

Explanation:
1. def function_name(arguments): defines a function with optional arguments.
2. # function body contains the statements to be executed.
3. return value returns a result from the function. If no return statement is used, it returns None by default.

Example:
def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))
```

#### `Types of Function Arguments` 
Python supports different types of arguments that can be passed during a function call.

`1. Default argument :` In Python, functions can have default arguments, which are parameters with predefined values. This means you don’t always need to pass every argument while calling a function.
- If you provide a value, Python uses it.
- If you skip it, the default value is used automatically.

```bash
Syntax of Default Arguments
def function_name(param1=value1, param2=value2, ...):
    # function body

Parameters:
1. param1, param2, ...: Names of the parameters.
2. value1, value2, ...: Default values assigned using =.
3. function_name: The name of the function.

Example:
def greet(name="Guest"):
    print("Hello,", name)

greet()          
greet("Nitish")

Output:
Hello, Guest
Hello, Nitish
```

`Rules to Keep in Mind :`
```bash
1. Non-default parameters must come before default parameters in the function definition.
2. Positional arguments must come before keyword arguments when calling a function.
3. If using keyword arguments, order does not matter.
4. Each parameter must have only one value.
5. Keyword name must match exactly with the function definition.
6. For positional (non-keyword) arguments, order matters strictly.
```

`2. Keyword Arguments :` pass values using parameter names, so argument order does not matter.
```bash
def student(fname, lname):
    print(fname, lname)

student(fname='Nitish', lname='Kumar')
student(lname='Yadav', fname='Shivam')

Output:
Nitish Kumar
Shivam Yadav

Explanation: fname and lname are passed using parameter names and arguments can be provided in any order
```

`3. Positional Arguments :` values are assigned to parameters based on their order in the function call.
```bash
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Rakesh", 21)

print("Case-2:")
nameAge(21, "Rakesh")

Output:
Case-1:
Hi, I am Rakesh
My age is  21
Case-2:
Hi, I am 21
My age is  Rakesh

Explanation:
- In Case-1, values match the correct parameters.
- In Case-2, values are swapped because the order changed.
```

`4. Arbitrary Arguments :` Allow functions to accept multiple values. This is done using two special symbols:
- *args collects extra positional arguments as a tuple.
- **kwargs collects extra keyword arguments as a dictionary.

<br>

`1. Non-Keyword Arguments (*args) :` The special syntax *args allows us to pass any number of positional (non-keyword) arguments to a function. 
<br>
These arguments are collected into a tuple, which means we can loop through them or use them with built-in functions.
<br>
This is useful when you don’t know in advance how many values will be passed.
```bash
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2, 3, 4))

Output:
24

Explanation:
1. def multiply(*args): accepts multiple numbers as input.
2. result = 1: initialize result to 1 (since we are multiplying).
3. for num in args: loop through all arguments.
4. result *= num: multiply each number with result.
```

`2. Keyword Arguments (**kwargs) :` The special syntax **kwargs allows us to pass any number of keyword arguments (arguments in the form key=value). These arguments are collected into a dictionary, where:
- Keys = argument names
- Values = argument values
```bash
def introduce(**kwargs):
    details = []
    for k, v in kwargs.items():
        details.append(k + ": " + str(v))
    return ", ".join(details)

print(introduce(Name="Alice", Age=25, City="New York"))

Output:
Name: Alice, Age: 25, City: New York

Explanation:
1. def introduce(**kwargs): accepts flexible keyword arguments.
2. for k, v in kwargs.items(): loop through each key-value pair.
3. details.append(k + ": " + str(v)): format each pair as key: value and add to list.
4. ", ".join(details): join list items into a single string separated by commas.
```

## Python String
Strings are sequence of characters written inside quotes. It can include letters, numbers, symbols and spaces. Python does not have a separate character type.
- A single character is treated as a string of length one.
- Strings are commonly used for text handling and manipulation.

### How to Create a String

`1. Creating a String :` Strings can be created using either single ('...') or double ("...") quotes. Both behave the same.
```bash
s1 = 'Nitish'  
s2 = "Rakesh"  
print(s1)
print(s2)

Output:
Nitish
Rakesh
```

`2. Multi-line Strings :` Use triple quotes ('''...''' ) or ( """...""") for strings that span multiple lines. Newlines are preserved.
```bash
s = """I am Learning
Python String."""
print(s)

s = '''I'm a 
BCA Student.'''
print(s)

Output:
I am Learning
Python String.
I'm a 
BCA Student.
```

### `Accessing characters in String :` 
Strings are indexed sequences. Positive indices start at 0 from the left, negative indices start at -1 from the right.
```bash
s = "Nitish"
print(s[0])   
print(s[4])

Output:
N
s

- Accessing an index out of range will cause an IndexError. Only integers are allowed as indices and using a float or other types will result in a TypeError.
```

### `String Slicing :` 
String slicing in Python is a way to get specific parts of a string by using start, end and step values. It’s especially useful for text manipulation and data parsing.
```bash
Syntax:
        substring = s[start : end : step]

Parameters:
1. s: The original string.
2. start (optional): Starting index (inclusive). Defaults to 0 if omitted.
3. end (optional): Stopping index (exclusive). Defaults to the end of the string if omitted.
4. step (optional): Interval between indices. A positive value slices from left to right, while a negative value slices from right to left. If omitted, it defaults to 1 (no skipping of characters).
```

`Negative Indexing in Slicing :` Negative indexing is useful for accessing elements from the end of the String. The last element has an index of -1, the second last element -2 and so on.
```bash
s = "abcdefghijklmno"

print(s[-4:])

print(s[:-3])

print(s[-5:-2])

print(s[-8:-1:2])

Output:
lmno
abcdefghijkl
klm
hjln

Explanation:
1. s[-4:] slices the string starting from the 4th character from the end ('m') to the end of the string.
2. s[:-3] slices the string from the beginning up to the 3rd character from the end ('k'), excluding it.
3. s[-5:-2] slices the string from the 5th character from the end ('l') to the 2nd character from the end ('n'), excluding the last character.
4. s[-8:-1:2] slices the string from the 8th character from the end ('g') to the 2nd character from the end ('n'), with a step of 2, taking every second character.
```

`Reverse a String Using Slicing :` To reverse a string, use a negative step value of -1, which moves from the end of the string to the beginning.
```bash
s = "Python"

# Reverse the string
print(s[::-1])

Output:
nohtyP

Explanation: The slice s[::-1] starts from the end and steps backward through the string, which effectively reversing it. This method does not alter the original string.
```

### `String Iteration :` 
Strings are iterable, one can loop through characters one by one.
```bash
s = "Python"
for char in s:
    print(char)

Output:
P
y
t
h
o
n

Explanation: for loop pulls characters in order and each iteration prints the next character.
```
### `String Immutability :` 
Strings are immutable, which means that they cannot be changed after they are created. If we need to manipulate strings then we can use methods like concatenation, slicing or formatting to create new strings based on original.
```bash
Example : Trying to Change a Character

text = "Python"
text[0] = "J"

Output:
TypeError: 'str' object does not support item assignment

Explanation : Strings do not allow direct modification using indexes.

Example : Creating a New String

text = "Python"
new_text = "J" + text[1:]
print(new_text)

Output:
Jython

Explanation : Instead of changing the original string, a new string is created.
```

### `Deleting a String :` 
It's not possible to delete individual characters from a string since strings are immutable. However, we can delete an entire string variable using the del keyword.
```bash
text = "Python Programming"
del text

print(text)

Output:
NameError: name 'text' is not defined

Explanation : After deleting the variable, it no longer exists in memory.
```
### `Updating a String :` 
As strings are immutable, “updates” create new strings using slicing or methods such as replace().
```bash
text = "Hello World"
new_text = text.replace("World", "Python")
print(new_text)

Output:
Hello Python
```
### `Common String Methods :` 
Python provides various built-in methods to manipulate strings.

`1. len() :` returns the total number of characters in a string (including spaces and punctuation).
```bash
s = "Python"
print(len(s))

Output:
6
```

`2. upper() and lower() :` upper() method converts all characters to uppercase whereas, lower() method converts all characters to lowercase.
```bash
s = "Hello World"
print(s.upper())
print(s.lower())

Output:
HELLO WORLD
hello world
```

`3. strip() and replace() :` strip() removes leading and trailing whitespace from the string and replace() replaces all occurrences of a specified substring with another.
```bash
s = "   BCA   "
print(s.strip())    

s = "Python is fun"
print(s.replace("fun", "awesome"))

Output:
BCA
Python is awesome
```

### `Concatenating and Repeating Strings :` 
We can concatenate strings using + operator and repeat them using * operator.

`1. Strings can be combined by using + operator.`
```bash
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

Output:
Hello World
```

`2. We can repeat a string multiple times using * operator.`
```bash
s = "Hello "
print(s * 3)

Output:
Hello Hello Hello 
```

### `Formatting Strings`

`1. Using f-strings :` f-strings (formatted string literals) were introduced in Python 3.6 to make string formatting easier and more readable. They allow variables and expressions to be directly embedded inside strings using curly braces {}.
```bash
Syntax: f"{variable/expression}"

- An f-string is created by adding f before the string and placing variables or expressions inside {}.

Example:
name = "Emily"
age = 20
print(f"My name is {name} and I am {age} years old")

Output:
My name is Emily and I am 20 years old
```

`2. Using format() :`
format() method in Python is a tool used to create formatted strings. By embedding variables or values into placeholders within a template string, we can construct dynamic, well-organized output. It replaces the outdated % formatting method, making string interpolation more readable and efficient. 
```bash
Syntax: string.format(value1, value2, ...)

Parameter: values (such as integers, strings, or variables) to be inserted into the placeholders in the string.

Returns: a string with the provided values embedded in the placeholders.

Example:
a = "shakshi" # name 
b = 22 # age

msg = "My name is {0} and I am {1} years old.".format(a,b)
print(msg)

Output:
My name is shakshi and I am 22 years old.

Explanation: format(a, b) method replaces {0} with the first argument (a = "shakshi") and {1} with the second argument (b = 22).
```

## Python Lists
List is a built-in data structure used to store an ordered collection of items. They are dynamic, resizable and capable of storing multiple data types.
- Mutable: list elements can be changed, updated, added, or removed after the list is created.
- Ordered: elements maintain the order in which they are inserted.
- Index-based: elements are accessed using their position, starting from index 0.

### `Creating a List :` 
Lists can be created in several ways, such as using square brackets [] , the list() constructor or by repeating elements.

`1. Using Square Brackets :` Square brackets [] are used to create a list directly.
```bash
a = [1, 2, 3]
print(a)

b = ["apple", "banana"]
print(b)

Output:
[1, 2, 3]
['apple', 'banana']
```

`2. Using list() Constructor :` A list can also be created by passing an iterable (such as tuple, string or another list) to the list() constructor.
```bash
a = list((1, 2, 3, 'apple', 4.5))  
print(a)

b = list("RAM")
print(b)

Output:
[1, 2, 3, 'apple', 4.5]
['R', 'A', 'M']
```

`3. Creating List with Repeated Elements :` A list with repeated elements can be created using the multiplication (*) operator.
```bash
a = [2] * 5
b = [0] * 7

print(a)
print(b)

Output:
[2, 2, 2, 2, 2]
[0, 0, 0, 0, 0, 0, 0]
```

`Internal Representation of Lists`

Python list stores references to objects, not the actual values directly.

- The list keeps memory addresses of objects like integers, strings or booleans.
- Actual objects exist separately in memory.
- Modifying a mutable object inside a list changes the original object.
- Reassigning an immutable object creates a new object instead of changing the old one.
```bash
a = [1, 2, 2, "Python"]
print(a[0])   # index-based
print(a)

Output:
1
[1, 10, 2, 'Python']

Explanation:
- The list a contains an integer (10, 20 and 40), a string ("GfG") and a boolean (True).
- Elements are accessed using indexing (a[0], a[1], etc.).
- Each element keeps its original type.
```

### `Accessing List Elements :` 
Elements in a list are accessed using indexing. Python uses zero-based indexing, meaning a[0] represents the first element. Negative indexing is also supported, where -1 accesses the last element.
```bash
a = [10, 20, 30]
print(a[0])
print(a[-1])

Output:
10
30
```

### `Adding Elements into List :` 
Elements can be added to a list using the following methods:

`1. append() :` Adds an element at the end of the list.
```bash
Syntax: list_name.append(element)

a = [1, 2]
a.append(3)
print(a)

Output:
[1, 2, 3]
```

`2. insert() :` Adds an element at a specific position.
```bash
Syntax: list_name.insert(index, element)

a = [1, 3]
a.insert(1, 2)
print(a)

Output:
[1, 2, 3]
```

`3. extend() :` Adds multiple elements to the end of the list.
```bash
Syntax: list_name.extend(iterable)

numbers = [1, 2, 3]
numbers.extend([4, 5, 6])
print(numbers)

Output:
[1, 2, 3, 4, 5, 6]
```

### `Updating Elements into List `

`1. Updating a Single Element :` You can update an element using its index number.
```bash
Syntax: list_name[index] = new_value

numbers = [10, 20, 30, 40]
numbers[1] = 25
print(numbers)

Output:
[10, 25, 30, 40]
```

`2. Updating Multiple Elements :` You can update multiple elements using slicing.
```bash
Syntax: list_name[start:end] = [new_values]

numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [20, 30, 40]
print(numbers)

Output:
[1, 20, 30, 40, 5]
```

`3. Updating All Elements Using Loop :` You can update all elements using a loop.
```bash
numbers = [1, 2, 3, 4]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)

Output:
[2, 4, 6, 8]
```

`4. Updating Nested List Elements :` Lists inside another list are called nested lists.
```bash
matrix = [[1, 2], [3, 4]]

matrix[0][1] = 10

print(matrix)

Output:
[[1, 10], [3, 4]]
```

### `Removing Elements from List`

`1. remove() :` Removes the first occurrence of an element.
```bash
Syntax: list_name.remove(element)

a = [1, 2, 3]
a.remove(2)
print(a)

Output:
[1, 3]
```

`2. pop() Method :` Removes an element using its index or the last element if no index is specified and returns the removed element.
```bash
Syntax: list_name.pop(index)

a = [1, 2, 3]
a.pop()
print(a)

Output:
[1, 2]
```

`3. del Statement :` Deletes an element at a specified index or entire list.
```bash
Syntax: del list_name[index]

a = [1, 2, 3]
del a[1]
print(a)

Output:
[1, 3]
```

`4. clear() :` Removes all elements from the list.
```bash
Syntax: list_name.clear()

a = [1, 2, 3]
a.clear()
print(a)

Output:
[]
```

### `Nested Lists :` 
A nested list is a list that contains another list as its element. It is commonly used to represent matrices or tabular data. Nested elements can be accessed by chaining multiple indexes.
```bash
a = [[1, 2], [3, 4]]
print(a[0])
print(a[1][0])

Output:
[1, 2]
3
```
### Iterate over a list
Python provides several ways to iterate over list. The simplest and the most common way to iterate over a list is to use a for loop. This method allows us to access each element in the list directly.

`1. Using for Loop and in :` We can access all elements using for loop and in keyword to traverse all elements.
```bash
a = [1, 3, 5, 7, 9]

# On each iteration val
# represents the current item/element
for val in a:
    print(val)

Output:
1
3
5
7
9
```
`2. Using while Loop :` A while loop is used to repeat a block of code as long as a condition is True. 
- We can use it to access list elements one by one using an index.
```bash
Syntax:
index = 0

while index < len(list_name):
    # code
    index += 1

Example:
a = [1, 3, 5, 7, 9]
 
# Start from the first index
i = 0
 
# The loop runs till the last index (i.e., 4)
while i < len(a):
    print(a[i])
    i += 1

Output:
1
3
5
7
9
```
`3. Using enumerate() :` We can also use the enumerate() function to iterate through the list. This method provides both the index (i) and the value (val) of each element during the loop.
```bash
a = [1, 3, 5, 7, 9]

# Here, i and val reprsents index and value respectively
for i, val in enumerate(a):
    print (i, val)

Output:
0 1
1 3
2 5
3 7
4 9
```
`4. Using for Loop with range() :` We can use the range() method with for loop to traverse the list. This method allow us to access elements by their index, which is useful if we need to know the position of an element or modify the list in place.
```bash
a = [1, 3, 5, 7, 9]
 
# Calculate the length of the list
n = len(a)
 
# Iterates over the indices from 0 to n-1 (i.e., 0 to 4)
for i in range(n):
    print(a[i])

Output:
1
3
5
7
9
```

### List Comprehension
List comprehension is a concise way to create new lists by applying an expression to each item in an existing iterable like a list, tuple or range. It helps to write clean, readable and efficient code compared to traditional loops.
```bash
Syntax:
[expression for item in iterable if condition]

Parameters:
1. expression: operation or value to include in the new list.
2. item: current element from the iterable.
3. iterable: sequence like a list, tuple or range.
4. if condition (optional): filter to include only items that satisfy the condition.
```
<b>`Example`</b>
```bash
a = [2, 3, 4, 5]
res = [val ** 2 for val in a]
print(res)

Output:
[4, 9, 16, 25]

Explanation: res = [val ** 2 for val in a] use list comprehension to create a new list by squaring each number in a.
```

## Python Tuples
A tuple is an immutable ordered collection of elements.

- Tuples are similar to lists, but unlike lists, they cannot be changed after their creation.
- Can hold elements of different data types.
- These are ordered, heterogeneous and immutable.

### `Creating a Tuple`
A tuple is created by placing all the items inside parentheses (), separated by commas. A tuple can have any number of items.
```bash
tup = ()
print(tup)

# Using String
tup = ('Nitish', 'Rakesh')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Shivam')
print(tup)

Output:
()
('Nitish', 'Rakesh')
(1, 2, 4, 5, 6)
('S', 'h', 'i', 'v', 'a', 'm')
```

`Creating a Tuple with Mixed Datatypes :` Tuples can store elements of different data types, such as integers, strings, lists and dictionaries, within a single structure.
```bash
tup = (5, 'Welcome', 7.5, True, [1, 2, 3], {'key': 'value'})
print(tup)

Output:
(5, 'Welcome', 7.5, True, [1, 2, 3], {'key': 'value'})
```
### Tuple Basic Operations

`1. Accessing of Tuples :` We can access the elements of a tuple by using indexing and slicing, similar to how we access elements in a list. 
<br>
Indexing starts at 0 for the first element and goes up to n-1, where n is the number of elements in the tuple. Negative indexing starts from -1 for the last element and goes backward.
```bash
tup = tuple("Rakesh")
print(tup[0])
print(tup[1:4])  
print(tup[:3])

# Tuple unpacking
tup = ("Pytan", "For", "AI")

# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)

Output:
R
('a', 'k', 'e')
('R', 'a', 'k')
Python
For
AI
```

`2. Concatenation of Tuples :` Tuples can be concatenated using the + operator. This operation combines two or more tuples to create a new tuple.
<br>
Only tuples can be concatenated with tuples. Combining a tuple with other types like lists will raise an error. Tuples themselves can contain mixed datatypes.
```bash
tup1 = (0, 1, 2, 3)
tup2 = ('Python', 'For', 'ML')
tup3 = tup1 + tup2
print(tup3)

Output:
(0, 1, 2, 3, 'Python', 'For', 'ML')
```

`3. Slicing of Tuple :` Tuple slicing is a technique to extract a sub-part of a tuple. It uses a range of indices to create a new tuple from the original tuple.
```bash
Syntax: tuple[start:stop:step]

Parameter:
1. start: The starting index from where the slice begins (inclusive). Default is 0.
2. stop: The ending index where the slice ends (exclusive).
3. step: The step size or stride. Default is 1
```
<b>`Example:` </b>
```bash
# Define a tuple
tup = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Slice from index 2 to 5
s1 = tup[2:6]
print(s1)  

# Slice from the beginning to index 3
s2 = tup[:4]
print(s2)  

# Slice from index 5 to the end
s3 = tup[5:]
print(s3)  

# Slice the entire tuple
s4 = tup[:]
print(s4)

Output:
(2, 3, 4, 5)
(0, 1, 2, 3)
(5, 6, 7, 8, 9)
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```

`Using Negative Indices :` Negative indices can be used to slice tuples from the end.
```bash
# Define a tuple
tup = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Slice from the third last to the end
s1 = tup[-3:]
print(s1)  

# Slice from the beginning to the third last
s2 = tup[:-3]
print(s2)  

# Slice from the third last to the second last
s3 = tup[-3:-1]
print(s3)

Output:
(7, 8, 9)
(0, 1, 2, 3, 4, 5, 6)
(7, 8)
```

`Using Step in Slicing :` The step parameter allows us to define the increment between indices for the slice.
```bash
# Define a tuple
tup = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Slice with a step of 2
s1 = tup[1:8:2]
print(s1)  

# Slice with a negative step (reverse the tuple)
s2 = tup[::-1]
print(s2)

Output:
(1, 3, 5, 7)
(9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
```

`4. Deleting a Tuple :` Since tuples are immutable, we cannot delete individual elements of a tuple. However, we can delete an entire tuple using del statement.
<br>
Printing of Tuple after deletion results in an Error. 
```bash
tup = (0, 1, 2, 3, 4)
del tup
print(tup)

Output:
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 6, in <module>
NameError: name 'tup' is not defined
```

`5. Tuple Unpacking with Asterisk (*) :` *operator is used in tuple unpacking to grab multiple items into a list. This is useful to extract just a few specific elements and collect the rest together.
```bash
tup = (1, 2, 3, 4, 5)
a, *b, c = tup
print(a) 
print(b) 
print(c)

Output:
1
[2, 3, 4]
5

Explanation: a gets the first item, c gets the last item and *b collects everything in between into a list.
```

## Python Dictionary
Dictionary is a data structure that stores information in key-value pairs. While keys must be unique and immutable (like strings or numbers), values can be of any data type, whether mutable or immutable. 
<br>
This makes dictionaries ideal for accessing data by a specific name rather than a numeric position like in list.

### `Features of Dictionary`
```bash
1. Stores Data in Key–Value Pairs : A dictionary stores information in the form of `key : value`, making data easy to organize and access.

2. Mutable (Changeable) : Dictionaries can be modified after creation, allowing users to add, update, or remove items whenever needed.

3. Keys are Unique : Each key in a dictionary must be unique. If the same key is used again, the old value gets replaced by the new one.

4. Values Can Be Any Data Type : Dictionary values can store integers, strings, lists, tuples, or even another dictionary.

5. Fast Access to Data : Dictionaries provide quick and efficient access to values using their keys instead of searching through the entire collection.

6. Dynamic Size : The size of a dictionary can grow or shrink during program execution because items can be added or deleted anytime.
```

### `Creating a Dictionary`
A dictionary is created by writing key-value pairs inside { }, where each key is connected to a value using colon (:). 
```bash
a = {"x": 1, "y": 2}
print(a)

Output:
{'x': 1, 'y': 2}
```

`Using dict() :` dict() function in Python is a built-in constructor used to create dictionaries.
```bash
# passing keyword arguments
d = dict(a=1, b=2, c=3, d=4)

print(d)

Output:
{'a': 1, 'b': 2, 'c': 3, 'd': 4}

- Explanation: dict() allows direct key-value pair assignment using the key=value syntax, where each key must be a valid Python identifier i.e., a string without quotes that follows variable naming rules.
```

### `Accessing Dictionary Items`
A value in a dictionary is accessed by using its key. This can be done either with square brackets [ ].
```bash
d = {"name": "Kat", "age": 21}
print(d["name"])     # Access using key

Output:
Kat

- Accessing a missing key with [ ] raises a KeyError.
```

`Using get() :` The dict.get() method in Python returns the value associated with a given key. If the key is not present, it returns None by default or a specified default value if provided. It allows safe access to dictionary keys without raising a KeyError.
```bash
Syntax: dict_name.get(key, default_value)

Parameters:
- key: The key whose value needs to be retrieved.
-default_value (optional): Value returned if the key is not found. Default is None.

Return Value:
- Returns the value of the specified key.
- Returns default_value (or None) if the key does not exist.

Example:
d = {'coding': 'good', 'thinking': 'better'}
print(d.get('coding'))

Output:
good

Explanation: d.get('coding') returns the value linked to 'coding'. Since the key exists, its value is returned.
```
### `Adding and Updating Dictionary Items`
New items are added to a dictionary using the assignment operator (=) by giving a new key a value. If an existing key is used with the assignment operator, its value is updated with the new one.
```bash
d = {"name": "Sam"}

d["age"] = 21        # Adding a new key-value pair
d["name"] = "Alex"   # Updating an existing value
print(d)

Output:
{'name': 'Alex', 'age': 21}
```

### `Removing Dictionary Items`
Dictionary items can be removed using built-in deletion methods that work on keys:

`1. del :` removes an item using its key
```bash
d = {"a": 1, "b": 2}
del d["a"]
print(d)

Output:
{'b': 2}
```

`2. pop() :` removes the item with the given key and returns its value
```bash
d = {"a": 1, "b": 2}

val = d.pop("a")
print(val)
print(d)

Output:
1
{'b': 2}
```

`3. popitem() :` removes and returns the last inserted key-value pair
```bash
d = {"a": 1, "b": 2}
print(d.popitem())

Output:
('b', 2)
```

`4. clear() :` removes all items from the dictionary
```bash
d = {"a": 1, "b": 2}
d.clear()
print(d)

Output:
{}
```

### `Iterating Through a Dictionary`
A dictionary can be traversed using a for loop to access its keys, values or both key-value pairs by using the built-in methods keys(), values() and items().

`1. Iterate keys :` Returns all keys from the dictionary.
```bash
Syntax: dict_name.keys()

1. Parameters: No parameter required.
2. Return Type: Returns a dynamic view object containing dictionary keys.

Example:
d = {"a": 1, "b": 2}
for key in d:
    print(key)

Output:
a
b
```

`2. Iterate values :` Returns all values from the dictionary.
```bash
Syntax: dict_name.values()

1. Parameters: No parameters are required.
2. Returns: Returns a dynamic view object containing all dictionary values.

Example:
d = {"a": 1, "b": 2}
for value in d.values():
    print(value)

Output:
1
2
```
`3. Iterate key-value pairs :` Returns all key-value pairs as tuples.
```bash
Syntax: dict.items()

1. Parameters: No parameters are required.
2. Return value: Returns a dict_items view object containing (key, value) tuples.

Example:
d = {"a": 1, "b": 2}
for key, value in d.items():
    print(key, value)

Output:
a 1
b 2
```

### `Nested Dictionary`
A nested dictionary is a dictionary that contains another dictionary as a value. It helps organize complex or grouped data, like student details or product info in a clean and structured way.

`1. Creating a Nested Dictionary :` Creating a Nested Dictionary means placing dictionaries as values inside an outer dictionary using curly braces {}. 
```bash
students = {}

students['student1'] = {'name': 'Drake', 'age': 20, 'grade': 'A'}
students['student2'] = {'name': 'Travis', 'age': 22, 'grade': 'B'}
students['student3'] = {'name': 'Charlie', 'age': 21, 'grade': 'A+'}

print("Student Details:")
print(students)

Output:
Student Details:
{'student1': {'name': 'Drake', 'age': 20, 'grade': 'A'}, 'student2': {'name': 'Travis', 'age': 22, 'grade': 'B'}, 'student3': {'name': 'Charlie', 'age': 21, 'grade': 'A+'}}
```

`2. Adding Elements to a Nested Dictionary :` Adding elements to a nested dictionary means inserting new key-value pairs into inner dictionaries or adding new inner dictionaries using normal assignment.
```bash
person = {'employee1': {'name': 'Nitish', 'age': 25}}

# Adding a new key-value pair to existing inner dictionary
person['employee1']['department'] = 'HR'

# Adding a new inner dictionary
person['employee2'] = {'name': 'Shivam', 'age': 30, 'department': 'IT'}

print("Updated Nested Dictionary:")
print(person)

Output:
Updated Nested Dictionary:
{'employee1': {'name': 'Nitish', 'age': 25, 'department': 'HR'}, 'employee2': {'name': 'Shivam', 'age': 30, 'department': 'IT'}}
```

`3. Accessing Elements in a Nested Dictionary :` Accessing elements in a nested dictionary means using outer and inner keys to retrieve specific values from structured data.
```bash
student = {'student1': {'name': 'Taniya', 'age': 20, 'grade': 'A'}}

# Accessing elements
print("Name:", student['student1']['name'])
print("Grade:", student['student1']['grade'])

Output:
Name: Taniya
Grade: A
```

`4. Deleting from a Nested Dictionary :` Deleting from a Nested Dictionary means removing items from a nested dictionary using del or .pop(), either from inner dictionary or whole entry.
```bash
employee = {'emp1': {'name': 'John', 'age': 28, 'dept': 'Sales'},
            'emp2': {'name': 'Sara', 'age': 32, 'dept': 'HR'} }

# Deleting a key from inner dictionary
del employee['emp1']['dept']

# Deleting an entire inner dictionary
del employee['emp2']

print("Updated Nested Dictionary:")
print(employee)

Output:
Updated Nested Dictionary:
{'emp1': {'name': 'John', 'age': 28}}
```

### `Dictionary Comprehension`
Dictionary comprehension is used to create a dictionary in a short and clear way. It allows keys and values to be generated from a loop in one line. This helps in building dictionaries directly without writing multiple statements.
```bash
Syntax : {key: value for (key, value) in iterable if condition}

Parameter:
1. key: The item to use as the dictionary key.
2. value: The item to use as the dictionary value.
3. iterable: Any sequence or collection to loop through.
4. condition (optional): Lets you include only certain items

Example:
sq = {x: x**2 for x in range(1, 6)}
print(sq)

Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

`Creating a Dictionary from Two Lists :` This method creates a dictionary by pairing each item from one list with the matching item from another list using zip().
```bash
keys = ['a','b','c','d','e']
values = [1, 2, 3, 4, 5]  

d = {k:v for (k,v) in zip(keys, values)}  
print (d)

Output:
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
```

`Using fromkeys() Method :` The fromkeys() method creates a dictionary by taking a group of keys and assigning the same value to all of them.
```bash
Syntax : fromkeys(seq, val)

Parameters :
1. seq : The sequence to be transformed into a dictionary.
2. val : Initial values that need to be assigned to the generated keys. Defaults to None.

Returns : A dictionary with keys mapped to None if no value is provided, else to the value provided in the field. 

Example:
d = dict.fromkeys(range(5), True)
print(d)

Output:
{0: True, 1: True, 2: True, 3: True, 4: True}
```

`Dictionary Comprehension with Conditional Statements :` We can include conditions in a dictionary comprehension to filter items or apply logic only to specific values. This allows us to create dictionaries more selectively.
```bash
d = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(d)

Output:
{0: 0, 8: 512, 2: 8, 4: 64, 6: 216}
```

`Nested Dictionary Comprehension :` We can also create dictionaries within dictionaries using nested dictionary comprehensions. This is useful when each key maps to another dictionary of related values.
```bash
Syntax:
{
    key: {subkey: value for subkey in iterable}
    for key in iterable
}

Example:
table = {
    x: {y: x * y for y in range(1, 6)}
    for x in range(1, 6)
}

print(table)

Output:
{
  1: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
  2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10},
  3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15},
  4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20},
  5: {1: 5, 2: 10, 3: 15, 4: 20, 5: 25}
}
```