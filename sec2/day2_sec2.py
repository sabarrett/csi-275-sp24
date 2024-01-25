import random

enemy_health = 35

if enemy_health < 20:
    print("The enemy is heavily damaged!")
elif enemy_health < 40:
    print("The enemy looks hurt!")
elif enemy_health < 45:
    print("The enemy looks slightly hurt!")
else:
    print("The enemy looks healthy!")

print("Select your combat action: ")

numbers = [20, 30, -40, 0.75, 2]
total = 0
for number in numbers:
    print(number)
    total += number
print(total)

print(random.randint(0, 20))

# But Scott! I like the counting-based loop
# sometimes! If Python only has a range-based
# loop, how can I do something N times (for
# example, generate 20 random numbers)?

# print(list(range(0, 20)))

# range(first, last_excl) generates a list (actually
# it's not a list, it's a thing that produces numbers
# on-demand, but you can think of it like a list, and
# can turn it into a list with list()) of integers
# in the range [first, last_excl)

# We can combine this with the range-based for loop
# to count from, say, 0 to 19!
rand_ints = []

# range(20) is exactly the same as range(0, 20)
for i in range(20):
    rand_ints.append(random.randint(1, 100))
print(rand_ints)

for i in range(20):
    # skip even numbers
    if i % 2 == 0:
        continue
    if i > 10:
        break
    print(i)

gpr_faculty_names = ["Scott", "Dean", "Eric", "Alex"]
if "Scott" in gpr_faculty_names:
    print("Scott is in the GPR faculty!")

if "David" in gpr_faculty_names:
    print("David is in the GPR faculty!")

test_names = ["Wei", "Brian", "Eric", "Melanie", "Dean"]
result_list = []
for name in test_names:
    if name in gpr_faculty_names:
        result_list.append(name)
print(result_list)

user_input = input("Enter an integer: ")
try:
    as_int = int(user_input)
    print(as_int)
except ValueError:
    print(user_input, "is not an integer")


def print_enemy_status(health):
    if enemy_health < 20:
        print("The enemy is heavily damaged!")
    elif enemy_health < 40:
        print("The enemy looks hurt!")
    elif enemy_health < 45:
        print("The enemy looks slightly hurt!")
    else:
        print("The enemy looks healthy!")


print_enemy_status(12)


def change_num(value):
    value += 1

var = 4
# change_num(var) -- inline
value = var
value += 1
print(var)		# still prints 4

def change_list(input):
    input.append(2)
    input[0] = 3

var = [0, 1]
change_list(var) # -- inlined
# input = var
# input.append(2)
# input[0] = 3
print(var)		# prints [3, 1, 2]!

def change_list_2(input):
    input = [2, 3]

var = [0, 1]
# change_list_2(var) #-- inlined
input = var
input = [2, 3]
print(var)		# still prints [0, 1]!

def main():
    print("I'm the main function!")

if __name__ == "__main__":
    main()
