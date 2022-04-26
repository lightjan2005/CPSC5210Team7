from unittest import TestCase

import basketball
import sys


class TestBasketball(TestCase):
    def test_add_points(self):
        BasketballObj = basketball.Basketball()
        BasketballObj.add_points(0, 2)
        self.assertEqual(2, BasketballObj.score[0])

    def test_defense_choice(self):
        basketballObj = basketball.Basketball()
        basketball.get_defense_choice(basketballObj.defense_choices)
        self.assertEqual(6, basketballObj.get_defense())





