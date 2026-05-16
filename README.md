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