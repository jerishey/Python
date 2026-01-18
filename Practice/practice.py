"""FIRST USE REPL (Read , Evaluate , Print ,Loop) IN TERMINAL"""

## TYPE THIS IN THE CONSOLE -- STRINGS ##
a = 'me'
b = "myself"
c = a + b
d = a + " " + b
silly = a * 3

s = "abc"
len(s)

## TYPE THIS IN THE CONSOLE -- INDEXING ##
s = "abc"
s[0]
s[1]
s[2]
#s[3]  # this is an error
s[-1]
s[-2]
s[-3]

## TYPE THIS IN THE CONSOLE -- SLICING ##
s = "abcdefgh"
s[3:6]
s[3:6:2]
s[:]
s[::-1]
s[4:1:-2]

## TYPE THIS IN THE CONSOLE - MANIPULATION ##
s = "car"
#s[0] = 'b'  # this is an error
s = 'b'+s[1:len(s)]

"""STRINGS, INPUT/OUTPUT, AND BRANCHING"""

# ## USER INPUT ##
#Example 1
# text = input("Type anything... ")
# print(5*text)

# #Example 2
# num1 = input("Type a number: ")
# print(5*num1)
# num2 = int(input("Type a number: "))
# print(5*num2)

# #Example 3 - Newton's Method for cube root
# x = int(input('What x to find the cube root of? '))
# g = int(input('What guess to start with? '))

# print('Current estimate cubed = ', g**3)
# next_g = g - ((g**3 - x)/(3*g**2))
# print('Next guess to try = ', next_g)


# ## F-STRINGS ##
# num = 3000
# fraction = 1/3
# print(num*fraction, 'is', fraction*100, '% of', num)
# print(num*fraction, 'is', str(fraction*100) + '% of', num)
# print(f'{num*fraction} is {fraction*100}% of {num}')

# print(f'{num*fraction:,.0f} is {fraction*100:,.2f}% of {num:,}')


# pset_time = 15
# sleep_time = 8
# print(sleep_time > pset_time)
# derive = True
# drink = False
# both = drink and derive
# print(both)

"""CONDITIONAL STATEMENTS ( IF-ELIF-ELSE )"""

# ## BRANCHING ##
# #Example 1
# pset_time = 22
# sleep_time = 8
# if (pset_time + sleep_time) > 24:
#     print("impossible!")
# elif (pset_time + sleep_time) >= 24:
#     print("full schedule!")
# else:
#     leftover = abs(24-pset_time-sleep_time)
#     print(leftover,"h of free time!")
# print("end of day")

# ## NESTED BRANCHING ##
# #Example 1
# x = float(input("Enter a number for x: "))
# y = float(input("Enter a number for y: "))
# if x == y:
#     print("x and y are equal")
#     if y != 0:
#         print("therefore, x / y is", x/y)
# elif x < y:
#     print("x is smaller")
# else:
#     print("y is smaller")
# print("thanks!")

"""ITERATION :- FOR AND WHERE LOOP"""

# # while loops

# n = int(input('Please enter a non-negative integer: '))
# while n > 0:
#     print('x')
#     n = n-1  # the same as n -= 1


# where = input("You are in the Lost Forest. Go left or right? ")
# while where == "right":
#     where = input("You are in the Lost Forest. Go left or right? ")
# print("You got out of the Lost Forest! \o/")


################ YOU TRY IT ###################
## EXAMPLE: infinite loop, be careful!
# To stop it, click the shell and hit CTRL+c 
##############################################
# while True:
#     print("noooooooo")

#############
## EXAMPLE: counter
#############

## With while loop
# n = 0
# while n < 5:
#     print(n)
#     n = n+1

###########
## EXAMPLE: factorial
###########

## With while loops
# x = 6
# i = 1
# factorial = 1
# while i <= x:
#     factorial *= i
#     i += 1
# print(f'{x} factorial is {factorial}')

#BASIC EXAMPLE:
for i in range(1,4,1):
    print(i)
for j in range(1,4,2):
    print(j*2)
for me in range(4,0,-1):
    print("$"*me)


###############
## EXAMPLE: sum
###############

#mysum = 0
#for i in range(10):
#    mysum += i
#print(mysum)

######

#mysum = 0
#for i in range(7, 10):
#    mysum += i
#print(mysum)

######

#mysum = 0
#for i in range(5, 11, 2):
#    mysum += i
#    if mysum == 5:
#        break
#        mysum += 1
#print(mysum)

#############
## EXAMPLE: counter
#############

## With for loop
#for n in range(5):
#    print(n)

###########
## EXAMPLE: factorial
###########

## With for loops
# factorial = 1
# for i in range(1, x+1, 1):
#     factorial *= i
# print(f'{x} factorial is {factorial}')

#FOR PRACTICE

# Practice 1:
# Declare a variable x that stores an int > 0. Print all ints, one on each
# line, between 1 (inclusive) and x (inclusive) that are divisible by 5.
# For ex. if x = 15, it prints 5, 10, and 15. If x = 14, it prints 5 and 10.

# x = 15
# for i in range(1,x+1):
#     if i%5 == 0:
#         print(i)


# Practice 2:
# Declare a variable n that stores an int. Print the sum of all digits
# in n. Hint: you can get a digit at a time looking at the remainder
# when you divide n by 10.
# For ex. If x = 1234, print 10

# n = 1234
# total = 0
# while True:
#     r = n%10
#     total += r
#     n = n//10
#     if n == 0:
#         break
# print(total)

"""LOOPING OVER CHRARCTER"""

####################
## EXAMPLE: looping over characters
## These 3 code snippets do the same thing
####################

# s = "demo loops - fruit loops"
# for index in range(len(s)):
#     if s[index] == 'i' or s[index] == 'u':
#         print("There is an i or u")

######

# s = "demo loops - fruit loops"
# for char in s:
#     if char == 'i' or char == 'u':
#         print("There is an i or u")

#####

# s = "demo loops - fruit loops"
# for char in s:
#     if char in 'iu':
#         print("There is an i or u")

#####

####################
## EXAMPLE:  robot cheerleaders
####################

# an_letters = "aefhilmnorsxAEFHILMNORSX"
# word = input("I will cheer for you! Enter a word: ")
# times = int(input("Enthusiasm level (1-10): "))

# for w in word:
#     if w in an_letters:
#         #print(f'Give me an {c}: {c}') # with f-strings
#         print("Give me an " + w + ": " + w)
#     else:
#         #print(f'Give me a {c}: {c}') # with f-strings
#         print("Give me a " + w + ": " + w)
# print("What does that spell?")
# for i in range(times):
#     print(word, "!!!")

#####

###################
# EXAMPLE: word problems
###################

# this code is very slow for large numbers!
# for alyssa in range(11):
#     for ben in range(11):
#         for cindy in range(11):
#             total = (alyssa + ben + cindy == 10)
#             two_less = (ben == alyssa-2)
#             twice = (cindy == 2*alyssa)
#             if total and two_less and twice:
#                 print(f"Alyssa sold {alyssa} tickets")
#                 print(f"Ben sold {ben} tickets")
#                 print(f"Cindy sold {cindy} tickets")

# this code is better -- only one loop!
# for alyssa in range(1001):
#     ben = max(alyssa-20,0)
#     cindy = alyssa*2
#     if ben + cindy + alyssa == 1000:
#         print(f'Alyssa sold {alyssa} tickets')
#         print(f'Ben sold {ben} tickets')
#         print(f'Cindy sold {cindy} tickets')