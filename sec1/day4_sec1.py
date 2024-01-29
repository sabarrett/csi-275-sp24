import random

def function(param1, param2=0):
    pass


# Do this:
arg1 = 5
arg2 = 3
function(arg1, arg2)

# Not this:
function( arg1, arg2 )

list = [0, 1, 2]

# Do this:
list[1:2]

# Not this:
list[ 1 : 2 ]

random.randint()

def is_odd(number):
    return number % 2


if is_odd(3):
    print("This will run -- but is_even returned 1")

str1 = """abcdefg
ghijkl"""



# prints the newline embedded in str1
print(str1)

str2 = "abcdefg \
        sadflk"

print(str2)
