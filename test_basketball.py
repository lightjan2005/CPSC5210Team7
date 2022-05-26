from unittest import TestCase

from basketball import *
from parameterized import parameterized
from unittest.mock import Mock, patch
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
        # to change defence

    def test_start_game(self):
        pass

    def test_ball_passed_back(self):
        pass

    def test_foul_shots(self):
        pass

    def test_halftime(self):
        basketball_obj = Basketball()
        basketball_obj.halftime()
        self.assertEqual(basketball_obj.halftime(), None)

    def test_is_halftime(self):
        basketball_obj = Basketball()
        basketball_obj.is_halftime()
        self.assertEqual(basketball_obj.is_halftime(), False)

    def test_print_score(self):
        pass

    def test_start_of_period(self):
        pass

    def test_two_minute_warning(self):
        basketball_obj = Basketball()
        basketball_obj.two_minute_warning()
        self.assertEqual("   *** Two minutes left in the game ***", basketball_obj.two_minute_warning_message)

    def test_dartmouth_jump_shot(self):
        basketball_obj = Basketball()
        # set defense choice
        mock_defense_choice = Mock(get_defense_choice, return_value=6)
        basketball_obj.defense = mock_defense_choice()
        # set opponents name
        mock_get_opponents_name = Mock(get_opponents_name, return_value="mock opponent")
        basketball_obj.opponent = mock_get_opponents_name()
        # set to be opponents ball
        # basketball_obj.dartmouth_ball()

        self.assertEqual(6, basketball_obj.defense)
        self.assertEqual("mock opponent", basketball_obj.opponent)

        pass

    """
        This is a test for when the ball is dartmouth's possession.
        Still configuring the settings before it's dathmouth's possession.
    """

    def test_dartmouth_ball(self):
        basketball_obj = Basketball()
        # set defense choice
        mock_defense_choice = Mock(get_defense_choice, return_value=6)
        basketball_obj.defense = mock_defense_choice()
        # set opponents name
        mock_get_opponents_name = Mock(get_opponents_name, return_value="mock opponent")
        basketball_obj.opponent = mock_get_opponents_name()
        # set to be dartmouth ball

        # set shot for dartmouth
        mock_get_darthmouth_ball_choice = Mock(get_dartmouth_ball_choice, return_value=1)
        basketball_obj.shot = mock_get_darthmouth_ball_choice()
        self.assertEqual(1, basketball_obj.shot)


def test_dartmouth_non_jump_shot():
    pass


def test_opponent_jumpshot():
    pass


def test_opponent_non_jumpshot():
    pass


def test_opponent_ball():
    pass


def test_print_intro(capfd):
    print_intro()
    out, err = capfd.readouterr()
    assert out == "\t\t\t Basketball\n\t Creative Computing  Morristown, New Jersey\n\n\n\nThis is Dartmouth College " \
                  "basketball. \nΥou will be Dartmouth captain and playmaker.\nCall shots as follows:\n1. Long (" \
                  "30ft.) Jump Shot; \n2. Short (15 ft.) Jump Shot; \n3. Lay up; 4. Set Shot\nBoth teams will use the " \
                  "same defense. Call Defense as follows:\n6. Press; 6.5 Man-to-Man; 7. Zone; 7.5 None.\nTo change " \
                  "defense, just type 0 as your next shot.\nYour starting defense will be?\n"


@patch('basketball.set_defense_choice', return_value=6.0)
@patch('basketball.set_opponents_name', return_value="SU")
class Test_Input_Defense_choice(TestCase):

    def test_start_game(self, input, input2):
        basketball_obj = Basketball()
        basketball_obj.startGame()
        self.assertEqual(get_defense_choice(basketball_obj.defense_choices), 6)
        self.assertEqual(get_opponents_name(), "SU")


class Test_DartMouth_Jump_Shot(TestCase):

    @patch('basketball.Basketball.set_random_number', return_value=0.342)
    @patch('basketball.get_dartmouth_ball_choice', return_value=1)
    def test_dartmouth_jump_shot_two_minute_warning(self, input,input2):
        basketball_obj = Basketball()
        basketball_obj.time = 2
        basketball_obj.defense = 6
        basketball_obj.dartmouth_jump_shot()

    @patch('basketball.Basketball.set_random_number', return_value=0.4)
    @patch('basketball.get_dartmouth_ball_choice', return_value=1)
    def test_dartmouth_jump_shot_halftime(self, input, input2):
        basketball_obj = Basketball()
        basketball_obj.time = 0
        basketball_obj.defense = 6
        basketball_obj.dartmouth_jump_shot()





