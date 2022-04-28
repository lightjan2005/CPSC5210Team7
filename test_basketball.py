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

    def test_shot_choice(self):
        basketballObj = basketball.Basketball()
        basketball.print_intro()
        shot = basketball.get_dartmouth_ball_choice(basketballObj.shot_choices)
        self.assertEqual(3, shot)


    def test_check_print_score_should_return_true(self):
        basketballObj = basketball.Basketball()
        basketballObj.add_points(0, 2)
        self.assertEqual("Score:  0 to 2", basketballObj.print_score())








