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
        basketball.print_intro()
        defense = basketball.get_defense_choice(basketballObj.defense_choices)
        self.assertEqual(6, defense)

    def test_opponents_name(self):
        basketball.print_intro()
        opponents_name = basketball.get_opponents_name()
        self.assertEqual("SeattleU", opponents_name)






