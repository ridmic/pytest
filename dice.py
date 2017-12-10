from random import randint


class Dice:

    def __init__(self, sides=6):
        self.sides = int(sides)
        self.rolled = None

    def roll(self):
        self.rolled = randint(1, self.sides)
        return self.rolled

    def __str__(self):
        return str(self.rolled)

