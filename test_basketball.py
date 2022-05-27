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
@patch('basketball.Basketball.set_random_number', return_value=0.7)
@patch('basketball.get_dartmouth_ball_choice', return_value=1)
@patch('basketball.Basketball.set_dartmouth_ball_random_number', return_value=0.6)
class Test_Input_start_game(TestCase):

    def test_start_game(self, input, input2,input3,input4,input5):
        basketball_obj = Basketball()
        basketball_obj.startGame()
        basketball_obj.add_points(0,2)
        self.assertEqual(get_defense_choice(basketball_obj.defense_choices), 6)
        self.assertEqual(get_opponents_name(), "SU")



class Test_DartMouth_Jump_Shot(TestCase):

    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number1', return_value=0.24)
    @patch('basketball.Basketball.set_opponent_ball_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_opponent_non_jump_shot_random_number1', return_value=0.3)
    @patch('basketball.get_dartmouth_ball_choice', return_value=1)
    @patch('basketball.Basketball.set_dartmouth_ball_random_number', return_value=0.6)
    def test_dartmouth_jump_shot_halftime_two_minute_warning(self, input, input2, input3, input4, input5):
        basketball_obj = Basketball()
        basketball_obj.time = 9
        basketball_obj.defense = 6
        basketball_obj.dartmouth_jump_shot()

    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number6', return_value=0.46)
    @patch('basketball.Basketball.set_opponent_ball_random_number1', return_value=0.35)
    @patch('basketball.Basketball.set_opponent_jump_shot_random_number1', return_value=0.3)
    @patch('basketball.get_dartmouth_ball_choice', return_value=3)
    @patch('basketball.Basketball.set_dartmouth_non_jump_shot_random_number1', return_value=0.3)
    @patch('basketball.Basketball.set_opponent_ball_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_opponent_non_jump_shot_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_opponent_non_jump_shot_random_number2', return_value=0.6)
    @patch('basketball.Basketball.set_opponent_non_jump_shot_random_number3', return_value=0.76)
    @patch('basketball.Basketball.set_opponent_ball_random_number1', return_value=0.9)
    @patch('basketball.Basketball.set_opponent_ball_random_number1', return_value=0.4)
    @patch('basketball.get_dartmouth_ball_choice', return_value=1)
    @patch('basketball.Basketball.set_dartmouth_ball_random_number', return_value=0.6)
    def test_dartmouth_jump_shot_halftime_dartmouth_non_jump_shot(self, input, input2, input3, input4, input5,input6,input7,input8,input9,input10,input11,input12,input13,input14):
        basketball_obj = Basketball()
        basketball_obj.time = 0
        basketball_obj.defense = 6
        basketball_obj.dartmouth_jump_shot()

    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number2', return_value=0.52)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number3', return_value=0.6)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number4', return_value=0.65)
    @patch('basketball.Basketball.set_opponent_ball_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_opponent_non_jump_shot_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_opponent_non_jump_shot_random_number2', return_value=0.4)
    @patch('basketball.get_dartmouth_ball_choice', return_value=1)
    @patch('basketball.Basketball.set_dartmouth_ball_random_number', return_value=0.6)
    def test_dartmouth_jump_shot_dartmouth_jump_shot_non_jumpshot_charging_foul(self, input, input2, input3, input4, input5, input6,input7, input8, input9):
        basketball_obj = Basketball()
        basketball_obj.time = 0
        basketball_obj.defense = 6
        # set add points so that one team would win otherwise would be 0 to 0
        basketball_obj.add_points(0,2)
        basketball_obj.dartmouth_jump_shot()

    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number2', return_value=0.52)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number3', return_value=0.6)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number4', return_value=0.5)
    @patch('basketball.Basketball.get_foul_shot_random', return_value=0.8)
    @patch('basketball.Basketball.set_opponent_ball_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_opponent_non_jump_shot_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_opponent_non_jump_shot_random_number2', return_value=0.4)
    @patch('basketball.get_dartmouth_ball_choice', return_value=1)
    @patch('basketball.Basketball.set_dartmouth_ball_random_number', return_value=0.6)
    def test_dartmouth_jump_shot_dartmouth_jump_shot_non_jumpshot_foul_shot(self, input, input2, input3, input4, input5, input6,input7, input8, input9,input10):
        basketball_obj = Basketball()
        basketball_obj.time = 0
        basketball_obj.defense = 6
        # set add points so that one team would win otherwise would be 0 to 0
        basketball_obj.add_points(0,2)
        basketball_obj.dartmouth_jump_shot()

    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number2', return_value=0.52)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number3', return_value=0.4)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number5', return_value=0.6)
    @patch('basketball.Basketball.set_opponent_ball_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_opponent_non_jump_shot_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_opponent_non_jump_shot_random_number2', return_value=0.4)
    @patch('basketball.get_dartmouth_ball_choice', return_value=1)
    @patch('basketball.Basketball.set_dartmouth_ball_random_number', return_value=0.6)
    def test_dartmouth_jump_shot_dartmouth_jump_shot_shot_is_blocked_opponent_ball(self, input, input2, input3, input4, input5,
                                                                            input6, input7, input8, input9):
        basketball_obj = Basketball()
        basketball_obj.time = 0
        basketball_obj.defense = 6
        # set add points so that one team would win otherwise would be 0 to 0
        basketball_obj.add_points(0, 2)
        basketball_obj.dartmouth_jump_shot()

    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number2', return_value=0.52)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number3', return_value=0.4)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number5', return_value=0.4)
    @patch('basketball.get_dartmouth_ball_choice', return_value=1)
    @patch('basketball.Basketball.set_dartmouth_ball_random_number', return_value=0.6)
    def test_dartmouth_jump_shot_dartmouth_jump_shot_shot_is_blocked_dartmouth_ball(self, input, input2, input3, input4, input5,
                                                                            input6):
        basketball_obj = Basketball()
        basketball_obj.time = 0
        basketball_obj.defense = 6
        # set add points so that one team would win otherwise would be 0 to 0
        basketball_obj.add_points(0, 2)
        basketball_obj.dartmouth_jump_shot()

    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number2', return_value=0.4)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number6', return_value=0.4)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number7', return_value=0.5)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number8', return_value=0.7)
    @patch('basketball.get_dartmouth_ball_choice', return_value=1)
    @patch('basketball.Basketball.set_dartmouth_ball_random_number', return_value=0.6)
    def test_dartmouth_jump_shot_dartmouth_jump_shot_shot_off_target_dartmouth_rebound(self, input, input2, input3, input4, input5,
                                                                            input6, input7):
        basketball_obj = Basketball()
        basketball_obj.time = 0
        basketball_obj.defense = 6
        # set add points so that one team would win otherwise would be 0 to 0
        basketball_obj.add_points(0, 2)
        basketball_obj.dartmouth_jump_shot()

    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number2', return_value=0.4)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number6', return_value=0.4)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number7', return_value=0.5)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number8', return_value=0.5)
    @patch('basketball.get_dartmouth_ball_choice', return_value=1)
    @patch('basketball.Basketball.set_dartmouth_ball_random_number', return_value=0.6)
    def test_dartmouth_jump_shot_dartmouth_jump_shot_shot_off_target_dartmouth_rebound_ball_passed_back(self, input, input2, input3,
                                                                                       input4, input5,
                                                                                       input6, input7):
        basketball_obj = Basketball()
        basketball_obj.time = 0
        basketball_obj.defense = 6
        # set add points so that one team would win otherwise would be 0 to 0
        basketball_obj.add_points(0, 2)
        basketball_obj.dartmouth_jump_shot()

    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number2', return_value=0.4)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number6', return_value=0.5)
    @patch('basketball.Basketball.set_opponent_ball_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_opponent_non_jump_shot_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_opponent_non_jump_shot_random_number2', return_value=0.4)
    @patch('basketball.get_dartmouth_ball_choice', return_value=1)
    @patch('basketball.Basketball.set_dartmouth_ball_random_number', return_value=0.6)
    def test_dartmouth_jump_shot_dartmouth_jump_shot_shot_off_target_opponent_rebound(self, input,
                                                                                                        input2, input3,
                                                                                                        input4, input5,
                                                                                                        input6, input7,input8):
        basketball_obj = Basketball()
        basketball_obj.time = 0
        basketball_obj.defense = 6
        # set add points so that one team would win otherwise would be 0 to 0
        basketball_obj.add_points(0, 2)
        basketball_obj.dartmouth_jump_shot()

    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number2', return_value=0.4)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number6', return_value=0.4)
    @patch('basketball.Basketball.set_dartmouth_jump_shot_random_number7', return_value=0.3)
    @patch('basketball.Basketball.set_dartmouth_non_jump_shot_random_number1', return_value=0.3)
    @patch('basketball.Basketball.set_opponent_ball_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_opponent_non_jump_shot_random_number1', return_value=0.5)
    @patch('basketball.Basketball.set_opponent_non_jump_shot_random_number2', return_value=0.4)
    @patch('basketball.get_dartmouth_ball_choice', return_value=1)
    @patch('basketball.Basketball.set_dartmouth_ball_random_number', return_value=0.6)
    def test_dartmouth_jump_shot_dartmouth_jump_shot_shot_off_target_dartmouth_rebound_dartmouth_non_jump_shot(self, input, input2, input3,
                                                                                       input4, input5,
                                                                                       input6, input7,input8,input9,input10):
        basketball_obj = Basketball()
        basketball_obj.time = 0
        basketball_obj.defense = 6
        # set add points so that one team would win otherwise would be 0 to 0
        basketball_obj.add_points(0, 2)
        basketball_obj.dartmouth_jump_shot()


class Test_Dartmouth_jump_shot_random_numbers(TestCase):
    def test_set_random_number(self):
        basketball_obj = Basketball()

        num1 = basketball_obj.set_dartmouth_jump_shot_random_number1()
        num2 = basketball_obj.set_dartmouth_jump_shot_random_number2()
        num3 = basketball_obj.set_dartmouth_jump_shot_random_number3()
        num4 = basketball_obj.set_dartmouth_jump_shot_random_number4()
        num5 = basketball_obj.set_dartmouth_jump_shot_random_number5()
        num6 = basketball_obj.set_dartmouth_jump_shot_random_number6()
        num7 = basketball_obj.set_dartmouth_jump_shot_random_number7()
        num8 = basketball_obj.set_dartmouth_jump_shot_random_number8()

        num9 = basketball_obj.set_opponent_ball_random_number1()

        num10 = basketball_obj.set_opponent_non_jump_shot_random_number1()
        num11 = basketball_obj.set_opponent_non_jump_shot_random_number2()
        num12 = basketball_obj.set_opponent_non_jump_shot_random_number3()
        num13 = basketball_obj.set_opponent_non_jump_shot_random_number4()
        num14 = basketball_obj.set_opponent_non_jump_shot_random_number5()

        num15 = basketball_obj.set_dartmouth_ball_random_number()

        self.assertTrue(0 < num1 < 1)
        self.assertTrue(0 < num2 < 1)
        self.assertTrue(0 < num3 < 1)
        self.assertTrue(0 < num4 < 1)
        self.assertTrue(0 < num5 < 1)
        self.assertTrue(0 < num6 < 1)
        self.assertTrue(0 < num7 < 1)
        self.assertTrue(0 < num8 < 1)
        self.assertTrue(0 < num9 < 1)
        self.assertTrue(0 < num10 < 1)
        self.assertTrue(0 < num11 < 1)
        self.assertTrue(0 < num12 < 1)
        self.assertTrue(0 < num13 < 1)
        self.assertTrue(0 < num14 < 1)
        self.assertTrue(0 < num15 < 1)
