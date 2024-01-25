print("Hello world!")

# This assigns 23 to a variable
someVar = 23

# print("someVar's value is", someVar)

someVar = "this is someVar"

# print("someVar's value is", someVar, sep='_')

myVar = int(7.0)
myVar = float(7)

myVar += 1

# print(myVar ** 3)
# print(7 / 2)

my_string = "This is a string"
# Demo escape sequences
my_string = 'This is a\tstring\nAnd that\'s cool!'
# print(my_string)

new_string = f'my_string: "{my_string}". myVar: {myVar}'
# print(new_string)

print(f'new_string is {len(new_string)} characters long')

# indexing a substring that doesn't exist will crash your program
# print(new_string.index("asgsdaserahgsdf"))

fox = 'the quick brown fox jumped over the lazy dog'

my_list = [1, 2, 3, 4, 5, 6]
print(my_list[0:6:2])
print(my_list[-1])

my_list.append(20)
print(my_list)

# main difference between strings and lists -- strings are
# immutable (meaning "unchangeable") and can't be modified.
# There is no 'append' function on strings.
#fox.append('---------')
#print(fox)

# Get user input and store it in the variable `user_input`:
user_input = input('Enter a number: ')
user_input_as_int = int(user_input)


# Define a function named 'sort_list' that takes one parameter:
def sort_list(unsorted_list):
    print(unsorted_list)
    print("This is another line of the function")

def another_fn():
    return None


sort_list([1, 2, 3])


