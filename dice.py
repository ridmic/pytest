from random import randint


class Dice():
    def __init__(self, sides=6):
        self.sides = int(sides)
        self.__rolled = 0

    @property
    def rolled(self):
        return self.__rolled

    def roll(self):
        self.__rolled = randint(1, self.sides)
        return self.__rolled
