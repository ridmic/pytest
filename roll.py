from dice import Dice


class Roll():
    def __init__(self, dice, rolls=5):
        self.dice = dice
        self.rolls = int(rolls)
        self.rolled = {}
        for i in range(0, self.rolls):
            self.rolled['dice_' + str(i + 1)] = {'roll': 0, 'held': False}

    def roll_all(self):
        for i in range(0, self.rolls):
            self.rolled['dice_' + str(i + 1)]['roll'] = self.dice.roll()


dice = Dice()
roll = Roll(dice)
print(roll.rolled)
roll.roll_all()
print(roll.rolled)
