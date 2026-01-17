"""Floating Point"""

# x = 0
# for i in range(10):
#     x += 0.1
# print(x == 1)
# print(x, 'is the same as?', 10*0.1)

"""Guessing Perfect Square Roots"""

# # guessing perfect square roots

# x = int(input("Enter an integer: "))
# guess = 0
# while guess**2 < x:
#     guess += 1
# if guess**2 == x:
#     print(f'Square root of {x} is {guess}')
# else:
#     print(f'{x} is not a perfect square')

# # finding square root with negative flag

# guess = 0
# neg_flag = False
# x = int(input("Enter a positive integer: "))
# if x < 0:
#     neg_flag = True
# while guess**2 < x:
#     guess = guess + 1
# if guess**2 == x:
#     print(f'Square root of {x} is {guess}')
# else:
#     print(f'{x} is not a perfect square')
#     if neg_flag:
#         print(f'Just checking... did you mean {-x} ?')

"""Guessing Cube Root"""

# # cube root

# # finding a perfect cube of positive numbers
# cube = int(input("Enter an integer: "))
# for guess in range(cube+1):
#     if guess**3 == cube:
#         print(f'Cube root of {cube} is {guess}')



# #finding perfect cube with negative numbers
# cube = int(input("Enter an integer: "))
# for guess in range(abs(cube)+1):
#     if guess**3 == abs(cube):
#         if cube < 0:
#             guess = -guess
#         print(f'Cube root of {str(cube)} is {str(guess)}')



# # finding cube root with error message
# cube = int(input("Enter an integer: "))
# for guess in range(abs(cube)+1):
#     if guess**3 >= abs(cube):
#         break
# if guess**3 != abs(cube):
#     print(f'{cube} is not a perfect cube')
# else:
#     if cube < 0:
#         guess = -guess
#     print(f'Cube root of {str(cube)} is {str(guess)}')

"""Convert To Binary"""

# # Only positive numbers
# num = 1507
# result = ''
# if num == 0:
#     result = '0'
# while num > 0:
#     result = str(num%2) + result
#     num = num//2

# # Can handle negative numbers
# num = -15
# if num < 0:
#     is_neg = True
#     num = abs(num)
# else:
#     is_neg = False
# result = ''
# if num == 0:
#     result = '0'
# while num > 0:
#     result = str(num%2) + result
#     num = num//2
# if is_neg:
#     result = '-' + result

# # Can handle decimal number between 0 and 1
# x = float(input('Enter a decimal number between 0 and 1: '))

# p = 0
# while ((2**p)*x)%1 != 0:
#     print(f'Remainder = {str((2**p)*x - int((2**p)*x))}')
#     p += 1

# num = int(x*(2**p))

# result = ''
# if num == 0:
#     result = '0'
# while num > 0:
#     result = str(num%2) + result
#     num = num//2

# for i in range(p - len(result)):
#     result = '0' + result

# result = result[0:-p] + '.' + result[-p:]
# print(f'The binary representation of the decimal {str(x)} is {str(result)}')