from dice import Dice


class Roll:

    def __init__(self, dice, dice_count=5):
        self.dice = dice
        self.dice_count = int(dice_count)
        self.rolls = {}
        for i in range(0,self.dice_count):
            self.rolls['dice_'+str(i+1)] = {'rolled': 0, 'held': False}

    # Get all dice rolls
    def get_all_dice_rolls(self):
        rolls = []
        for i in range(0,self.dice_count):
            rolls.append(self.get_dice_roll('dice_'+str(i+1)))
        return rolls

    # Get a dice roll
    def get_dice_roll(self, dice_name):
        if dice_name in self.rolls:
            return self.rolls[dice_name]['rolled']
        return None

    # Roll all our dice
    def roll_all_dice(self):
        for i in range(0,self.dice_count):
            self.roll_dice('dice_'+str(i+1))

    # Roll a dice (unless held)
    def roll_dice(self, dice_name ):
        if dice_name in  self.rolls:
            if not self.rolls[dice_name]['held']:
                self.rolls[dice_name]['rolled'] = self.dice.roll()
            return self.rolls[dice_name]['rolled']
        return None

    def hold_dice(self, dice_name ):
        if dice_name in  self.rolls:
            self.rolls[dice_name]['held'] = True

    def release_dice(self, dice_name ):
        if dice_name in  self.rolls:
            self.rolls[dice_name]['held'] = False

    def __str__(self):
        return str(self.rolls)


dice = Dice(6)
roll = Roll(dice)

roll.roll_all_dice()
print(roll.get_all_dice_rolls())
print(roll)

roll.roll_all_dice()
print(roll)
