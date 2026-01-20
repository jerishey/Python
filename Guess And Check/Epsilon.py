################
## EXAMPLE: Approximation by epsilon increments
## Incrementally fixing code as we find issues with approximation
################

# try with 36, 24, 2, 12345
# x = 36
# epsilon = 0.01
# num_guesses = 0
# guess = 0.0
# increment = 0.0001
# while abs(guess**2 - x) >= epsilon:
#     guess += increment
#     num_guesses += 1
# print(f'num_guesses = {num_guesses}')
# print(f'{guess} is close to square root of {x}')

###########

# Caution, you'll need to "Restart Kernel" in the shell if you run this code
# x = 54321
# epsilon = 0.01
# num_guesses = 0
# guess = 0.0
# increment = 0.0001
# while abs(guess**2 - x) >= epsilon:
#     guess += increment
#     num_guesses += 1
#     if num_guesses%100000 == 0:
#         print(f'Current guess = {guess}')
#         print(f'Current guess**2 - x = {abs(guess*guess - x)}')
#     if num_guesses%1000000 == 0:
#         input('continue?')
# print(f'num_guesses = {num_guesses}')
# print(f'{guess} is close to square root of {x}')

##########

# Add an extra stopping condition 
# and check for why the loop terminated
# x = 54321
# epsilon = 0.01
# num_guesses = 0
# guess = 0.0
# increment = 0.0001  # try with 0.00001
# while abs(guess**2 - x) >= epsilon and guess**2 <= x:
#     guess += increment
#     num_guesses += 1
# print(f'num_guesses = {num_guesses}')
# if abs(guess**2 - x) >= epsilon:
#     print(f'Failed on square root of {x}')
#     print(f'Last guess was {guess}')
#     print(f'Last guess squared is {guess*guess}')
# else:
#     print(f'{guess} is close to square root of {x}')
    
#######

#####################
## EXAMPLE: fast square root using bisection search
#####################

# x = 54321  # try 0.5
# epsilon = 0.01
# num_guesses = 0
# low = 0.0
# high = x
# guess = (high + low)/2

# while abs(guess**2 - x) >= epsilon:
#     # uncomment to see each step's guess, high, and low 
#     #print(f'low = {str(low)} high = {str(high)} guess = {str(guess)}')
#     if guess**2 < x:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
#     num_guesses += 1
# print(f'num_guesses = {str(num_guesses)}')
# print(f'{str(guess)} is close to square root of {str(x)}')

############### YOU TRY IT ###################
# x = 0.5
# epsilon = 0.01
# # choose the low endpoint
# low = ???
# # choose the high endpopint
# high = ???

# guess = (high + low)/2

# while abs(guess**2 - x) >= epsilon:
#     #print(f'low = {str(low)} high = {str(high)} guess = {str(guess)}')
#     if guess**2 < x:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
# print(f'{str(guess)} is close to square root of {str(x)}')

#####################################################


#####################
## Code for square root with all x values
#####################
#x = 0.5
#epsilon = 0.01
#if x >= 1:
#    low = 1.0
#    high = x
#else:
#    low = x
#    high = 1.0
#guess = (high + low)/2
#
#while abs(guess**2 - x) >= epsilon:
#    print(f'low = {str(low)} high {str(high)} guess = {str(guess)}')
#    if guess**2 < x:
#        low = guess
#    else:
#        high = guess
#    guess = (high + low)/2.0
#print(f'{str(guess)} is close to square root of {str(x)}')

######## Cube root for all cubes ############
# cube = -27
# neg = False
# if cube < 0:
#     neg = True
# cube = abs(cube)
# epsilon = 0.01
# low = 0
# high = cube
# guess = (high + low)/2.0
# while abs(guess**3 - cube) >= epsilon:
#     if guess**3 < cube :
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
# if neg == True:
#     guess = -guess
# print(f'{guess} is close to the cube root of {cube}')


########################
## EXAMPLE: Newton-Raphson to find roots
######################
# epsilon = 0.01
# k = 24  # try 54321
# guess = k/2.0
# num_guesses = 0

# while abs(guess*guess - k) >= epsilon:
#     num_guesses += 1
#     guess = guess - (((guess**2) - k)/(2*guess))
# print(f'num_guesses = {str(num_guesses)}')
# print(f'Square root of {str(k)} is about {str(guess)}')

# Write code to use bisection search to find the cube 
# root of positive cubes to within some epsilon

# cube = 27
# epsilon = 0.01
# low = 0
# high = cube
# guess = (high + low)/2.0
# while abs(guess**3 - cube) >= epsilon:
#     if guess**3 < cube :
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
#     numGuesses += 1
# print('numGuesses =', numGuesses)
# print(guess, 'is close to the cube root of', cube)