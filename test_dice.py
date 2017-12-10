import unittest
from dice import Dice


class TestDice(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()
        self.dice2 = Dice(2)

    def test_dice_roll(self):
        for i in range(1, 1000):
            rolled = self.dice.roll()
            self.assertTrue(rolled in range(1, self.dice.sides + 1))
            self.assertTrue(rolled == self.dice.rolled)

        for i in range(1, 1000):
            rolled = self.dice2.roll()
            self.assertTrue(rolled in range(1, self.dice2.sides + 1))
            self.assertTrue(rolled == self.dice2.rolled)


if __name__ == '__main__':
    unittest.main()
