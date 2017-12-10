import unittest
from dice import Dice
from roll import Roll


class TestRoll(unittest.TestCase):

    def setUp(self):
        self.dice = Dice(2)                 # Pulled in from Roll
        self.roll = Roll(self.dice)

    # Test our rolls are in bounds (try 1000 times each so we have high prob of out-of-bounds)
    def test_roll(self):
        for i in range(0, 1000):
            self.roll.roll_all_dice()
            rolled = self.roll.get_all_dice_rolls()
            for j in range(0, len(rolled)):
                self.assertTrue(rolled[j] in range(1, self.dice.sides+1))


if __name__ == '__main__':
    unittest.main()
