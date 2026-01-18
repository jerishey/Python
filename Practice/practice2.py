# # ========================================
# # PYTHON PRACTICE EXERCISES FOR BEGINNERS
# # ========================================

# # ----------------
# # EXERCISE 1: Calculator
# # ----------------
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print(f"Sum: {num1 + num2}")
# print(f"Difference: {num1 - num2}")
# print(f"Product: {num1 * num2}")
# print(f"Division: {num1 / num2}")


# # ----------------
# # EXERCISE 2: Even or Odd
# # ----------------
# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")


# # ----------------
# # EXERCISE 3: Grade Calculator
# # ----------------
# score = int(input("Enter your score: "))

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print(f"Your grade is: {grade}")


# # ----------------
# # EXERCISE 4: Sum of Numbers
# # ----------------
# n = int(input("Enter a number: "))
# total = 0

# for i in range(1, n + 1):
#     total += i

# print(f"Sum from 1 to {n} is {total}")


# # ----------------
# # EXERCISE 5: Multiplication Table
# # ----------------
# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{num} × {i} = {num * i}")


# # ----------------
# # EXERCISE 6: Factorial Calculator
# # ----------------
# n = int(input("Enter a number: "))
# factorial = 1

# for i in range(1, n + 1):
#     factorial *= i

# print(f"Factorial of {n} is {factorial}")


# # ----------------
# # EXERCISE 7: Reverse a String
# # ----------------
# text = input("Enter a string: ")
# reversed_text = text[::-1]
# print(f"Reversed: {reversed_text}")


# # ----------------
# # EXERCISE 8: Count Vowels
# # ----------------
# text = input("Enter a string: ").lower()
# vowels = "aeiou"
# count = 0

# for char in text:
#     if char in vowels:
#         count += 1

# print(f"Number of vowels: {count}")


# # ----------------
# # EXERCISE 9: Find Maximum in List
# # ----------------
# numbers = [45, 23, 78, 12, 90, 34]
# max_num = numbers[0]

# for num in numbers:
#     if num > max_num:
#         max_num = num

# print(f"Maximum number: {max_num}")


# # ----------------
# # EXERCISE 10: Palindrome Checker
# # ----------------
# word = input("Enter a word: ").lower()

# if word == word[::-1]:
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not a palindrome")


# # ----------------
# # EXERCISE 11: FizzBuzz
# # ----------------
# for i in range(1, 21):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# # ----------------
# # EXERCISE 12: Prime Number Checker
# # ----------------
# num = int(input("Enter a number: "))
# is_prime = True

# if num < 2:
#     is_prime = False
# else:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print(f"{num} is prime")
# else:
#     print(f"{num} is not prime")


# # ----------------
# # EXERCISE 13: Temperature Converter
# # ----------------
# temp = float(input("Enter temperature: "))
# unit = input("Enter unit (C/F): ").upper()

# if unit == "C":
#     fahrenheit = (temp * 9/5) + 32
#     print(f"{temp}°C = {fahrenheit}°F")
# elif unit == "F":
#     celsius = (temp - 32) * 5/9
#     print(f"{temp}°F = {celsius}°C")
# else:
#     print("Invalid unit")


# # ----------------
# # EXERCISE 14: List Reversal (without slicing)
# # ----------------
# numbers = [1, 2, 3, 4, 5]
# reversed_list = []

# for i in range(len(numbers) - 1, -1, -1):
#     reversed_list.append(numbers[i])

# print(f"Original: {numbers}")
# print(f"Reversed: {reversed_list}")


# # ----------------
# # EXERCISE 15: Simple Password Validator
# # ----------------
# password = input("Enter a password: ")
# is_valid = True

# if len(password) < 8:
#     print("Password must be at least 8 characters")
#     is_valid = False

# has_digit = False
# for char in password:
#     if char.isdigit():
#         has_digit = True
#         break

# if not has_digit:
#     print("Password must contain at least one digit")
#     is_valid = False

# if is_valid:
#     print("Password is valid!")


# # ========================================
# # COMMON BEGINNER MISTAKES TO AVOID
# # ========================================

# # ----------------
# # MISTAKE 1: Forgetting Indentation
# # ----------------
# # Wrong ❌
# # if age >= 18:
# # print("Adult")

# # Correct ✅
# age = 20
# if age >= 18:
#     print("Adult")


# # ----------------
# # MISTAKE 2: Using = Instead of ==
# # ----------------
# # Wrong ❌ (assignment, not comparison)
# # if age = 18:
# #     print("18 years old")

# # Correct ✅
# if age == 18:
#     print("18 years old")


# # ----------------
# # MISTAKE 3: Forgetting to Convert input()
# # ----------------
# # Wrong ❌
# # age = input("Enter age: ")
# # if age >= 18:  # Error! Can't compare string to number

# # Correct ✅
# age = int(input("Enter age: "))
# if age >= 18:
#     print("Adult")


# # ----------------
# # MISTAKE 4: Off-by-One Errors
# # ----------------
# # Prints 0-4, not 1-5!
# for i in range(5):
#     print(i)

# # To print 1-5:
# for i in range(1, 6):
#     print(i)


# # ----------------
# # MISTAKE 5: Infinite Loops
# # ----------------
# # Wrong ❌ - Never stops!
# # count = 1
# # while count <= 5:
# #     print(count)
# #     # Forgot to increment count!

# # Correct ✅
# count = 1
# while count <= 5:
#     print(count)
#     count += 1


# # ----------------
# # MISTAKE 6: Modifying List While Iterating
# # ----------------
# # Wrong ❌
# # numbers = [1, 2, 3, 4, 5]
# # for num in numbers:
# #     if num % 2 == 0:
# #         numbers.remove(num)

# # Correct ✅
# numbers = [1, 2, 3, 4, 5]
# numbers = [num for num in numbers if num % 2 != 0]
# print(numbers)


# # ----------------
# # MISTAKE 7: Mutable Default Arguments
# # ----------------
# # Wrong ❌
# # def add_item(item, my_list=[]):
# #     my_list.append(item)
# #     return my_list

# # Correct ✅
# def add_item(item, my_list=None):
#     if my_list is None:
#         my_list = []
#     my_list.append(item)
#     return my_list