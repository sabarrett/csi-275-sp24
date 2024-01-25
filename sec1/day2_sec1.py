enemy_health = 15

if enemy_health < 20:
    print("The enemy looks weak!")
elif enemy_health < 40:
    print("The enemy is damaged!")
elif enemy_health < 45:
    print("The enemy is mostly healthy!")
else:
    print("The enemy is completely healthy!")

print("Select your battle command!")

ll = [90, 23, 76, -45, 0.001, "Hello world!"]
for number in ll:
    print(number)

# Ok, Scott, what if I want to do the "normal" C++
# for loop? Say, loop from 0 to 20.

print(list(range(0, 20)))

# range(min, max_excl) produces a generator (which is like
# a list -- just think of it as a list) that yields the numbers
# min to (max_excl - 1).

# range(20) == range(0, 20)
# This loop is like C++ for (int i = 0; i < 20; i++)
for i in range(20):
    print(i)

for i in range(20):
    # Skip even numbers
    if i % 2 == 0:
        continue
    # Only process numbers up to 10
    if i > 10:
        break
    print(i)

gpr_faculty_names = ["Scott", "Eric", "Dean", "Alex"]

if "David" in gpr_faculty_names:
    print("David is one of the GPR faculty!")

if "Scott" in gpr_faculty_names:
    print("Scott is one of the GPR faculty!")

test_names = ["David", "Dean", "Wei", "Eric"]

result_names = []
for name in test_names:
    if name in gpr_faculty_names:
        result_names.append(name)

print(result_names)

user_input = None
while user_input != "Done":
    user_input = input("Enter a number: ")
    as_int = None
    # Should clean this up -- this will yell
    # when the user enters "Done", which is
    # totally valid input!
    try:
        as_int = int(user_input)
        # This is a ZeroDivisionError -- our
        # except block won't catch this
        # 10 / 0
        print(as_int)
    except ValueError:
        print(user_input, "is not an integer!")


def print_enemy_health(health):
    if enemy_health < 20:
        print("The enemy looks weak!")
    elif enemy_health < 40:
        print("The enemy is damaged!")
    elif enemy_health < 45:
        print("The enemy is mostly healthy!")
    else:
        print("The enemy is completely healthy!")
    return 300


value = print_enemy_health(30)
print(value)


def main():
    print("This is my main function!")
    print("Please run me!")
    print("I'm used to being the center of attention")
    print("Pls text back")
    print(":((((")


if __name__ == "__main__":
    main()



def change_list(input):
    input.append(2)
    input[0] = 3

var = [0, 1]
# change_list(var) -- inlined
input = var
input.append(2)
input[0] = 3
print(var)		# prints [3, 1, 2]!


def change_list_2(input):
    input = [2, 3]

var = [0, 1]
# change_list(var) -- inlined
input = var
input = [2, 3]
print(var)		# still prints [0, 1]!


def change_num(value):
    value += 1


var = 4
# change_num(var) (inlined)
value = var
value += 1
print(var)
