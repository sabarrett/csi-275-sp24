
print("Hello world!")
print("This is on its own line")
print("And so is this!")

# Declare `someVar` and initialize to 23.
someVar = 23
print(someVar)

someVar = "now this is a string!"
print(someVar)

print("Boolean values:", True, False)
print("Float values  :", 1.0, 3.14)
print("Int values    :", 65, 97)

f = 3.0
i = 3
print(f, i)
print(f == i)

# turn i into a float
print(f, float(i))
# turn f into an int
print(int(f), i)
# as in C++, when converting to an integer,
# floats are _truncated_ rather than _rounded_.
# Can use the built-in `round()` function to
# round floats to ints instead.

# i++ # Not allowed!
i += 1  # This is how you increment.
print(i)
# 2 raised to the power of i
print(2 ** i)
# int / int -> float
print(7 / 2)

# strings can be declared with either '' or ""
my_string = "Hello there"
my_string = 'Hello there'
# ^^^ These two statements are functionally identical

escaped_string = 'Andy\\ Warhol\tcoined the term \'fifteen minutes of fame\'\nI think that\'s neat!'
print(escaped_string)

print("escaped_string has", len(escaped_string), "characters")

substr = "inut"
print("escaped_string has", substr, "appearing", escaped_string.count(substr), "times")
print("escaped_string has", substr, "at index", escaped_string.index(substr))

print(escaped_string)
print(escaped_string[0])
print(escaped_string[8])
print(escaped_string[0:15])
print(escaped_string[10:25])
print(escaped_string[10:])
print(escaped_string[:25])
print(escaped_string[0:30])
print(escaped_string[0:30:2])
print(escaped_string[:30:2])
print(escaped_string[::2])
print(escaped_string[::-1])
print(escaped_string[5:-5])
print(f"'{escaped_string[20:0]}'")
print(escaped_string[20:0:-1])

my_list = [1, 2, 3]
print(my_list)
my_list.append(4)
print(my_list)

# lists are mutable (changeable) -- you can
# add and remove objects from them.
# strings are immutable (unchangeable) -- you
# cannot modify a string once it's created.
# string.append() does not exist.
# escaped_string.append("------")

print(my_list[1:3])
print(my_list.index(2))

print(f'The value of my_list is: {my_list}')
print(f'{20} times {43} is {20 * 43}')


def sort_list(unordered_list):
    print(unordered_list)
    print("Another line!")


sort_list([1, 2, 3])

user_input = input('Enter a number: ')
print(user_input)
user_input_as_int = int(user_input)
print(user_input_as_int)
