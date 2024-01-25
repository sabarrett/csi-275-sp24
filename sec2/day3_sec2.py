import random


class Rectangle:
    width = None
    height = None

    def __init__(self, width=3, height=3):
        self.width = width
        self.height = height

    @staticmethod
    def num_sides():
        return 4

    def area(self):
        return self.width * self.height


rect = Rectangle(6, 4)
print(f'{rect.width}, {rect.height}: {rect.area()}')
print(Rectangle.num_sides())

print(random.randint(1, 10))
print(random.uniform(1, 10))

options = ["rock", "paper", "scissors"]
user_pick = None
while user_pick not in options:
    user_pick = input("Choose your weapon: ")
enemy_pick = random.choice(options)
print(f'You threw {user_pick} and enemy threw {enemy_pick}')

