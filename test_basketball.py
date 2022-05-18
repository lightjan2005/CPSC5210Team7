from basketball import *
from parameterized import parameterized
from unittest.mock import Mock
import unittest


class Test_BasketBall(unittest.TestCase):
    @parameterized.expand([
        [0, 2, ],
        [0, 1],
        [0, 0],
        [1, 2],
        [1, 1],
        [1, 0]

    ])
    def test_add_points_return_equal(self, team, score):
        basketball_obj = Basketball()
        basketball_obj.add_points(team, score)
        if team == 0:
            self.assertEqual(score, basketball_obj.score[0])
        else:
            self.assertEqual(score, basketball_obj.score[1])

    @parameterized.expand([
        ["Name", "Name"],

    ])
    def test_shot_choice(self, shot_choice, expected_Value):
        mock_shot_choice = Mock(get_dartmouth_ball_choice, return_value=shot_choice)
        self.assertEqual(mock_shot_choice([]), expected_Value)

    @parameterized.expand([
        [0, 0, ],
        [1, 1],
        [2, 2],
        [3, 3],
        [4, 4]
    ])
    def test_shot_choice(self, shot_choice, expected_Value):
        mock_shot_choice = Mock(get_dartmouth_ball_choice, return_value=shot_choice)
        self.assertEqual(mock_shot_choice([]), expected_Value)

    @parameterized.expand([
        [6, 6, ],
        [7, 7],
        [6.5, 6.5],
        [7.5, 7.5]
    ])
    def test_get_defense_choice(self, defense_choice, expected_Value):
        mock_get_defense_choice = Mock(get_defense_choice, return_value=defense_choice)
        self.assertEqual(mock_get_defense_choice([]), expected_Value)

    def test_two_minute_warning(self):
        basketball_obj = Basketball()
        basketball_obj.two_minute_warning()
        self.assertEqual("   *** Two minutes left in the game ***", basketball_obj.two_minute_warning_message)


def test_start_game():
    assert False


def test_add_points():
    assert False


def test_ball_passed_back():
    assert False


def test_change_defense():
    assert False


def test_foul_shots():
    assert False


def test_halftime():
    assert False


def test_is_halftime():
    assert False


def test_print_score():
    assert False


def test_start_of_period():
    assert False


def test_two_minute_warning():
    assert False


def test_dartmouth_jump_shot():
    assert False


def test_dartmouth_non_jump_shot():
    assert False


def test_dartmouth_ball():
    assert False


def test_opponent_jumpshot():
    assert False


def test_opponent_non_jumpshot():
    assert False


def test_opponent_ball():
    assert False
