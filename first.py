# ========== VARIABLES ==========
# x, y, z = 100, 200, 300

# studentName = "Rakesh"
# print(studentName)

# num1 = 50

# num2 = 75

# print(num1 + num2)


# import keyword

# print(keyword.kwlist)

# ========== OPERATORS ==========

# Arithmetic operator
# p = 45

# q = 9

# print(p + q)  # Addition
# print(p - q)  # Subtraction
# print(p * q)  # Multiplication
# print(p / q)  # Division
# print(p % q)  # Modulus
# print(p // q) # Floor Division
# print(p ** q) # Exponentiation


# # Bitwise operator
# m = 15
# n = 6

# print(m & n)   # AND
# print(m | n)   # OR
# print(~m)      # NOT
# print(m ^ n)   # XOR
# print(m >> 2)  # Right Shift
# print(m << 2)  # Left Shift

# ========== INPUT AND OUTPUT ==========
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# print("Sum is:", num1 + num2)


# # Average of given numbers
# sub1 = int(input("Enter marks in subject 1: "))
# sub2 = int(input("Enter marks in subject 2: "))
# sub3 = int(input("Enter marks in subject 3: "))
# sub4 = int(input("Enter marks in subject 4: "))

# print("Average marks:", (sub1 + sub2 + sub3 + sub4) / 4)


# # Power calculation

# base = int(input("Enter base: "))
# power = int(input("Enter power: "))

# print("Result:", base ** power)


# ========== STRINGS ==========

# firstName = "Rakesh"
# surName = "Kumar"

# print(firstName + " " + surName)

# # Indexing

# word = "Python"

# print(word[3])  # h

# # Slicing:

# message = "Welcome to Python"

# print(message[0:7])  # Welcome

# firstName = "Rakesh"
# surName = "Kumar"

# print(firstName + " " + surName)  # Concatenation

# print(firstName * 4)     # Repetition

# print("R" in firstName)   # Membership


# ========== STRING METHODS ==========

# text = " learn python programming "

# print(text.upper())  # upper()

# print(text.lower())  # lower()

# print(len(text))  # len()

# print(text.title())  # title()

# print(text.capitalize())  # capitalize()

# print(text.strip())  # strip()

# print(text.find("python"))  # find()


# userName = str(input("Enter your name: "))

# greeting = "Hello" + " " + userName + "!"

# print(greeting)

# # Slicing:

# sentence = "Python Programming"

# print(sentence[0:6])  # Python (start from index 0 to 5)



# ========== LISTS ==========

# marks = [85, 92, 78, 88, 95, 73, 81]

# # print(marks[2:6])  # [78, 88, 95, 73]

# # print(marks[0:3])  # [85, 92, 78]

# marks.append(90)  # append()
# marks.insert(1, 100)  # insert()
# marks.extend([65, 77])  # extend()
# print(marks)



# ========== TUPLE ==========

# scores = (45, 67, 89, 32, 78, 56, 90, 23, 45, "End")

# print(scores[0])

# # Tuple slicing

# print(scores[3:7])

# numbers = (10, 20, 30, 30, 30, 40, 50, 50, 50, 50, 60, 70, 80, 90, "Done")

# occurrences = numbers.count(50)

# print(occurrences)



# ========== DICTIONARY ==========

# employee = {
#     "name": "Priya",
#     "age": 28,
#     "department": "IT",
#     "empID": 1045
# }

# print(employee["name"])  # Accessing name

# print(employee.get("age"))  # Accessing dictionary by using get method

# # How to add elements in dictionary
# employee["city"] = "Mumbai"
# print(employee)

# # How to update elements in dictionary

# employee["age"] = 29
# print(employee)



# ========== SETS ==========

# # How to create sets:
# myNumbers = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110}
# print(myNumbers)

# # How to create an empty set:
# emptySet = set()
# print(type(emptySet))

# # How to add an element:
# myNumbers.add(120)
# print(myNumbers)

# # Add multiple elements in set:

# myNumbers.update([130, 140, 150, 160])
# print(myNumbers)


# ========== OPERATIONS ON SETS ==========

# # Union -> It combines both sets in single one.

# groupA = {5, 10, 15, 20, 25}

# groupB = {15, 20, 25, 30, 35, 40, 45}

# print(groupA | groupB)


# # Intersection -> It searches common elements in both sets

# groupA = {5, 10, 15, 20, 25, 30}

# groupB = {15, 20, 25, 30, 35, 40, 45}

# print(groupA & groupB)


# # Difference -> Elements in first set but not in second

# groupA = {5, 10, 15, 20, 25, 30}

# groupB = {15, 20, 25, 30, 35, 40, 45}

# print(groupA - groupB)


# myNumbers = {10, 20, 30, 40, 50, 60, 70, 80, 90}
# print(myNumbers.pop())

# # Question:
# testSet = set()
# testSet.add(50)
# testSet.add(50.0)
# testSet.add("50")
# testSet.add(0.50)

# print(testSet)





# ========== FUNCTIONS ==========

# def greet():
#     print("Welcome to Python functions!")
# greet()


# # Function definition
# def multiply(x, y):       # x and y are parameters
#     return x * y
# answer = multiply(8, 12)


# print(answer)   # Function call


# ========== CONDITIONAL STATEMENTS ==========

# # if statement
# temperature = 35
# if temperature > 30:
#     print("It's a hot day!")

# # if-else statement
# number = 47
# if number % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# # if-elif-else statement
# percentage = 78
# if percentage >= 90:
#     print("Grade: A+")
# elif percentage >= 75:
#     print("Grade: A")
# elif percentage >= 60:
#     print("Grade: B")
# elif percentage >= 50:
#     print("Grade: C")
# else:
#     print("Grade: F")

# # nested if
# value = 42
# if value > 0:
#     if value % 2 == 0:
#         print("Positive even number")
#     else:
#         print("Positive odd number")


# ========== LOOPS ==========

# # for loop with range
# for counter in range(1, 6):
#     print(counter)  # prints 1 to 5

# # for loop with list
# colors = ["red", "green", "blue", "yellow"]
# for color in colors:
#     print(color)

# # for loop with string
# language = "JavaScript"
# for letter in language:
#     print(letter)

# # while loop
# num = 10
# while num >= 1:
#     print(num)
#     num -= 1

# # break statement - exits the loop
# for j in range(1, 20):
#     if j == 8:
#         break
#     print(j)  # prints 1 to 7

# # continue statement - skips current iteration
# for k in range(1, 8):
#     if k == 4:
#         continue
#     print(k)  # prints 1,2,3,5,6,7 (skips 4)

# # else with loop - executes when loop completes normally
# for idx in range(5):
#     print(idx)
# else:
#     print("Loop finished without break")


# ========== LIST COMPREHENSION ==========

# # basic list comprehension
# cubes = [num**3 for num in range(1, 6)]
# print(cubes)  # [1, 8, 27, 64, 125]

# # list comprehension with condition
# multiples_of_3 = [val for val in range(1, 31) if val % 3 == 0]
# print(multiples_of_3)  # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# # list comprehension with if-else
# status = ["Positive" if digit > 0 else "Zero or Negative" for digit in range(-2, 4)]
# print(status)


# ========== LAMBDA FUNCTIONS ==========

# # lambda function - single line anonymous function
# cube = lambda a: a**3
# print(cube(4))  # 64

# # lambda with multiple arguments
# subtract = lambda p, q: p - q
# print(subtract(20, 7))  # 13

# # lambda with map() - applies function to all items
# values = [2, 4, 6, 8, 10]
# tripled = list(map(lambda v: v * 3, values))
# print(tripled)  # [6, 12, 18, 24, 30]

# # lambda with filter() - filters items based on condition
# integers = [5, 12, 18, 23, 30, 41, 56, 67, 72, 85]
# divisible_by_5 = list(filter(lambda d: d % 5 == 0, integers))
# print(divisible_by_5)  # [5, 30, 85]


# ========== EXCEPTION HANDLING ==========

# # try-except block
# try:
#     userInput = int(input("Enter a divisor: "))
#     output = 100 / userInput
#     print(f"Result: {output}")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")
# except ValueError:
#     print("Error: Invalid input! Please enter a valid number")

# # try-except-else-finally
# try:
#     val1 = 50
#     val2 = 5
#     quotient = val1 / val2
# except ZeroDivisionError:
#     print("Division by zero error occurred")
# else:
#     print(f"Quotient: {quotient}")  # executes if no exception
# finally:
#     print("Execution completed")  # always executes


# ========== FILE HANDLING ==========

# # writing to a file
# myFile = open("sample.txt", "w")  # w = write mode
# myFile.write("Python is awesome!\n")
# myFile.write("File operations are simple.")
# myFile.close()

# # reading from a file
# myFile = open("sample.txt", "r")  # r = read mode
# data = myFile.read()
# print(data)
# myFile.close()

# # using with statement (automatically closes file)
# with open("sample.txt", "w") as f:
#     f.write("Using context manager\n")
#     f.write("No need to close manually")

# with open("sample.txt", "r") as f:
#     print(f.read())

# # reading file line by line
# with open("sample.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# # append mode - adds to existing file
# with open("sample.txt", "a") as f:
#     f.write("\nNew line appended here")


# ========== CLASSES AND OBJECTS (OOP) ==========

# # creating a class
# class Employee:
#     # constructor
#     def __init__(self, empName, empAge, empSalary):
#         self.empName = empName
#         self.empAge = empAge
#         self.empSalary = empSalary

#     # method
#     def showDetails(self):
#         print(f"Name: {self.empName}, Age: {self.empAge}, Salary: {self.empSalary}")

#     def work(self, task):
#         print(f"{self.empName} is working on {task}")

# # creating objects
# emp1 = Employee("Vikram", 32, 75000)
# emp2 = Employee("Sneha", 28, 68000)

# emp1.showDetails()
# emp2.showDetails()
# emp1.work("Database Management")


# # Inheritance
# class Animal:
#     def __init__(self, species, age):
#         self.species = species
#         self.age = age

#     def display(self):
#         print(f"Species: {self.species}, Age: {self.age}")

# class Dog(Animal):  # Dog inherits from Animal
#     def __init__(self, species, age, breed):
#         super().__init__(species, age)  # calling parent constructor
#         self.breed = breed

#     def showInfo(self):
#         self.display()
#         print(f"Breed: {self.breed}")

# myDog = Dog("Canine", 3, "Golden Retriever")
# myDog.showInfo()


# ========== MODULES AND IMPORTS ==========

# # importing built-in modules
# import math
# print(math.sqrt(64))  # 8.0
# print(math.pi)  # 3.141592653589793

# # importing specific functions
# from random import randint, choice
# print(randint(10, 50))  # random number between 10 and 50
# print(choice(['mango', 'orange', 'grape']))  # random choice

# # importing with alias
# import datetime as dt
# currentTime = dt.datetime.now()
# print(currentTime)


# ========== USEFUL BUILT-IN FUNCTIONS ==========

# # enumerate() - gets index and value
# cars = ['BMW', 'Audi', 'Tesla']
# for position, car in enumerate(cars):
#     print(f"{position}: {car}")

# # zip() - combines multiple iterables
# employees = ['Vikram', 'Sneha', 'Rohan']
# salaries = [75000, 68000, 82000]
# for emp, sal in zip(employees, salaries):
#     print(f"{emp} earns {sal}")

# # sorted() - returns sorted list
# scores = [88, 45, 92, 67, 73]
# print(sorted(scores))  # [45, 67, 73, 88, 92]
# print(sorted(scores, reverse=True))  # [92, 88, 73, 67, 45]

# # any() and all()
# grades = [85, 90, 78, 92, 88]
# print(any(g > 95 for g in grades))  # False
# print(all(g >= 70 for g in grades))  # True

# # reversed() - reverses an iterable
# digits = [3, 6, 9, 12, 15]
# print(list(reversed(digits)))  # [15, 12, 9, 6, 3]


# ========== PRACTICE PROBLEMS ==========

# # 1. Find factorial of a number
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)
# print(factorial(6))  # 720

# # 2. Check if string is palindrome
# def check_palindrome(text):
#     return text == text[::-1]
# print(check_palindrome("level"))  # True
# print(check_palindrome("python"))  # False

# # 3. Count vowels in a string
# def vowel_counter(text):
#     vowels = "aeiouAEIOU"
#     return sum(1 for char in text if char in vowels)
# print(vowel_counter("Python Programming"))  # 4

# # 4. Fibonacci series
# def generate_fibonacci(limit):
#     first, second = 0, 1
#     for i in range(limit):
#         print(first, end=" ")
#         first, second = second, first + second
# generate_fibonacci(12)  # 0 1 1 2 3 5 8 13 21 34 55 89

# # 5. Remove duplicates from list
# def unique_elements(lst):
#     return list(set(lst))
# items = [5, 10, 5, 20, 10, 30, 20, 40]
# print(unique_elements(items))  # [40, 10, 20, 5, 30]