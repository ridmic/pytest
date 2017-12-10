import unittest
from dice import Dice


class TestDice(unittest.TestCase):

    def setUp(self):
        self.dice2 = Dice(2)
        self.dice6 = Dice(6)
        self.dice50 = Dice(50)

        self.all_dice = (self.dice2, self.dice6, self.dice50)

    # Test our rolls are in bounds (try 1000 times each so we have high prob of out-of-bounds)
    def test_dice_rolls_inbound(self):
        for dice in self.all_dice:
            for i in range(0, 1000):
                roll = dice.roll()
                self.assertTrue(roll in range(1,dice.sides+1))          # Test rolls are in bounds

    # Test our return roll matches our dice.rolled try 100 times each so we have high prob of mismatch)
    def test_dice_rolls_match_rolled(self):
        for dice in self.all_dice:
            for i in range(0, 100):
                roll = dice.roll()
                self.assertTrue(roll == dice.rolled)                    # Test roll == dice.rolled

    # Test our return default string matches our expected result
    def test_dice_rolls_match_string(self):
        for dice in self.all_dice:
            for i in range(0, 100):
                roll = dice.roll()
                self.assertTrue(str(dice) == "{}".format(dice.rolled))  # Test str(dice) == "rolled'


if __name__ == '__main__':
    unittest.main()
