import random

def function(param1, param2=0):
    pass


arg1 = 5
arg2 = 3

# Do this:
function(arg1, arg2)

# Don't do this:
function ( arg1, arg2 )


list = [1, 2, 3, 4, 5]

# Do this:
sublist_1 = list[1:4]

# Not this:
sublist_2 = list [ 1 : 4 ]

def is_odd(number):
    """Returns 1 if number is odd; else 0."""
    return number % 2

if is_odd(3):
    print("We're in this branch even though is_odd() returned a non-boolean value")

str1 = """abcdef
ghijk"""

# str1 has newline embedded in it
print(str1)

str2 = "abcdef \
ghijk"

# str2 has no newline
print(str2)
