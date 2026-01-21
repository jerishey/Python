#A very simple example of a function that has one
#argument and returns one value
def is_even(i):   
    """Assumes: i, a positive int
    Returns True if i is even, otherwise False"""
    if i%2 == 0:
        return True
    else:
        return False

# is_even(3) # <- returns False
# is_even(8) # <- returns True

# print(is_even(3)) # <- prints False
# print(is_even(8)) # <- prints True

def is_even_without_return( i ):
    """ 
    Input: i, a positive int
    Returns None
    """
    print('without return')
    remainder = i % 2
    has_rem = (remainder == 0)
    print(has_rem)
    ##return None

#is_even_without_return(3)          # -> None
#print(is_even_without_return(3))  # -> print(None)

def is_even_with_return( i ):
    """ 
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    print('with return')
    remainder = i % 2
    return remainder == 0

#is_even_with_return(3)          # -> False
#print(is_even_with_return(3))  # -> print(False)

# # Using the is_even function later on in the code
# print("Numbers between 1 and 10: even or odd")

# for i in range(1,10):
#     if is_even(i):
#         print(i, "even")
#     else:
#         print(i, "odd")

###########################
### EXAMPLE: sum of all odd numbers between (including) a and b
###########################
## with a for loop
def sum_odd(a, b):
    sum_of_odds = 0
    for i in range(a, b+1):
        if i%2 == 0:
            sum_of_odds += i
            print(i, sum_of_odds)
    return sum_of_odds

# print(sum_odd(2,4)) 
# print(sum_odd(2,7)) 

# # with a while loop
def sum_odd(a, b):
    sum_of_odds = 0
    i = a
    while i <= b:
        if i%2 == 1:
            sum_of_odds += i
        i += 1
    return sum_of_odds

# print(sum_odd(2,4)) 
# print(sum_odd(2,7)) 

# def div_by(n, d):
#     """ n and d are ints > 0
#         Returns True if d divides n evenly and False otherwise 
#     """
#     # your code here
#     # one way
#     if n%d==0:
#         return True
#     else:
#         return False
#     # another way: 
#     # return n%d==0
    
# print(div_by(10,3))    
# print(div_by(195,13))    


# def is_palindrome(s):
#     """ s is a string
#     Returns True if s is a palindrome and False otherwise
#     """
#     # your code here
#     for i in range(len(s)//2):
#         if s[i] != s[len(s)-i-1]:
#             return False
#     return True        

# s="2222"
# print(is_palindrome(s))

# s="222"
# print(is_palindrome(s))

# s="abc"
# print(is_palindrome(s))

def keep_consonants(word):
    """ word is a string of lowercase letters
        Returns a string containing only the consonants 
        of word in the order they appear
    """
    vowels = "aeiou"
    ans = ""
    for char in word:
        if char not in vowels:
            ans += char
    return ans

# For example:
# print(keep_consonants("abcd"))  # prints bcd
# print(keep_consonants("aaa"))  # prints an empty string
# print(keep_consonants("babas"))  # prints bbs


def first_to_last_diff(s, c):
    """ s is a string, c is single character string
        Returns the difference between the index where c first
        occurs and the index where c last occurs. If c does not 
        occur in s, returns -1. 
    """
    if c not in s:
        return -1
    # if reach here, c is in s
    for i in range(len(s)):
        if s[i]==c:
            # break here to save i as the first instance of c in s
            break
    # loop through s backwards
    for j in range(len(s)-1,-1,-1):
        if s[j]==c:
            # break here to save j as the last instance of c in s
            break
    # this return is ok becasue the loops iterated through indices not chars of s
    return j-i

# For example
# print(first_to_last_diff('aaaa', 'a'))  # prints 3
# print(first_to_last_diff('abcabcabc', 'b'))  # prints 6
# print(first_to_last_diff('xyz', 'b'))  # prints -1

# Fix this buggy code so it works according to the specification:
def is_triangular(n):
    """ n is an int > 0 
        Returns True if n is triangular, i.e. equals a continued
        summation of natural numbers (1+2+3+...+k) 
    """
    total = 0
    for i in range(n):
        total += i
        if total == n:
            print(True)
    print(False)

# # start by runing it on simple test cases
# print(is_triangular(4))  # print False
# print(is_triangular(6))  # print True
# print(is_triangular(1))  # print True

# bisection square root as a function

def bisection_root(x):
    epsilon = 0.01
    low = 0
    high = x
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x: 
            low = ans
        else: 
            high = ans
        ans = (high + low)/2.0
#    print(ans, 'is close to the root of', x)
    return ans

# print(bisection_root(4))
# print(bisection_root(123))

def is_palindrome(s):
    """ s is a string
    Returns True if s is a palindrome and False otherwise. 
    A palindrome is a string that contains the same 
    sequence of characters forward and backward """
    # your code here
    for i in range(len(s)):
        if s[i] != s[len(s)-i-1]:
            # returning here essentially breaks the loop
            # as soon as we find an inconsistency
            return False
    return True

# For example:
# print(is_palindrome("222"))   # prints True
# print(is_palindrome("2222"))   # prints True
# print(is_palindrome("abc"))   # prints False



def f_yields_palindrome(n, f):
    """ n is a positive int
        f is a function that takes in an int and returns an int
    Returns True if applying f on n returns a number that is a
    palindrome and False otherwise.  """
    # your code here
    f_on_n = f(n)
    return is_palindrome(str(f_on_n))

# For example:
def f(x):
    return x+1

def g(x):
    return x*2

def h(x):
    return x//2

# print(f_yields_palindrome(2, f))   # prints True
# print(f_yields_palindrome(76, f))   # prints True
# print(f_yields_palindrome(11, g))   # prints True
# print(f_yields_palindrome(123, h))   # prints False