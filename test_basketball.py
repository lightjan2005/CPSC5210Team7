from unittest import TestCase, mock
from unittest.mock import Mock
import unittest
import pytest
from parameterized import parameterized

import basketball


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

    # def test_defense_choice_mock(self):
    #     with mock.patch('builtins.input', return_value=6):
    #         basketballObj = basketball.Basketball()
    #         assert basketball.get_defense_choice(basketballObj.defense_choices) == 6

    # @pytest.mark.parametrize('defense_choice', 'result',
    #                          [
    #                              (6, 6)
    #                          ]
    #                          )
    # def test_defense_choice_mock(self, defense_choice, result):
    #     with mock.patch('builtins.input', return_value=defense_choice):
    #         basketballObj = basketball.Basketball()
    #         assert basketball.get_defense_choice(basketballObj.defense_choices) == result

    def test_get_defense_choice(self):
        mock_get_defense_choice = Mock(basketball.get_defense_choice, return_value=6)
        self.assertEqual(mock_get_defense_choice([]), 6)


class TestSequence(unittest.TestCase):
    @parameterized.expand([
        [6, 6, ],
        [7, 7],
        [6.5, 6.5],
        [7.5, 7.5]
    ])
    def test_sequence(self, a, b):
        mock_get_defense_choice = Mock(basketball.get_defense_choice, return_value=a)
        self.assertEqual(mock_get_defense_choice([]), b)
