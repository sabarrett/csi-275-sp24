import random

class Rectangle:

    def __init__(self, width: int | float = 0, height: int | float = 0):
        self.width = width
        self.height = height

    @staticmethod
    def num_sides():
        return 4

    def area(self):
        return self.width * self.height

    def print(self):
        print(f'{self.width}, {self.height}: {self.area()}')


class SecondRectangle:
    def __init__(self):
        self.width = 2
        self.height = 5

rect = Rectangle(4, 5)
rect.print()

rand_rect = Rectangle(random.randint(1, 10), random.randint(1, 10))
rand_rect.print()

float_rect = Rectangle(random.random(), random.random())
float_rect.print()

options = ["rock", "paper", "scissors"]
user_pick = None
while user_pick not in options:
    user_pick = input("Choose your weapon: ")
opponent_pick = random.choice(options)
print(f"You threw {user_pick} and opponent threw {opponent_pick}")

# FORBIDDEN ARTS
# print(f'{rect.width}, {rect.height}: {Rectangle.area(rect2)}')

