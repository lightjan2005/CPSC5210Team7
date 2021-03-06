"""
The basketball class is a computer game that allows you to play as
Dartmouth College's captain and playmaker
The game uses set probabilites to simulate outcomes of each posession
You are able to choose your shot types as well as defensive formations
"""

import random
from typing import List, Literal, Optional


def print_intro() -> None:
    print(
        "\t\t\t Basketball\n\t Creative Computing  Morristown, New Jersey\n\n\n\nThis is Dartmouth College "
        "basketball. \nΥou will be Dartmouth captain and playmaker.\nCall shots as follows:\n1. Long (30ft.) Jump "
        "Shot; \n2. Short (15 ft.) Jump Shot; \n3. Lay up; 4. Set Shot\nBoth teams will use the same defense. Call "
        "Defense as follows:\n6. Press; 6.5 Man-to-Man; 7. Zone; 7.5 None.\nTo change defense, just type 0 as your "
        "next shot.\nYour starting defense will be?")


class Basketball:
    def __init__(self) -> None:
        self.time = 0
        self.score = [0, 0]  # first value is opponents score, second is home
        self.defense_choices: List[float] = [6, 6.5, 7, 7.5]
        self.shot: Optional[int] = None
        self.shot_choices: List[Literal[0, 1, 2, 3, 4]] = [0, 1, 2, 3, 4]
        self.z1: Optional[float] = None
        self.defense = 0
        self.opponent = ""
        self.two_minute_warning_message = ""
        self.random_number = 0.0

    def startGame(self):
        print_intro()
        self.defense = get_defense_choice(self.defense_choices)
        self.opponent = get_opponents_name()
        self.start_of_period()

    def add_points(self, team: Literal[0, 1], points: Literal[0, 1, 2]) -> None:
        """
        Add points to the score.

        Team can take 0 or 1, for opponent or Dartmouth, respectively
        """
        self.score[team] += points
        self.print_score()

    def ball_passed_back(self) -> None:
        print("Ball passed back to you. ", end="")
        self.dartmouth_ball()

    def change_defense(self) -> None:
        """change defense, called when the user enters 0 for their shot"""
        defense = None

        defense = get_new_defense_choice(defense, self.defense_choices)
        assert isinstance(defense, float)
        self.defense = defense
        self.dartmouth_ball()

    def foul_shots(self, team: Literal[0, 1]) -> None:
        """Simulate two foul shots for a player and adds the points."""
        print("Shooter fouled.  Two shots.")
        random_num = self.get_foul_shot_random()

        if random_num > 0.49:
            if random_num > 0.75:
                print("Both shots missed.")
            else:
                print("Shooter makes one shot and misses one.")
                self.score[team] += 1
        else:
            print("Shooter makes both shots.")
            self.score[team] += 2

        self.print_score()

    def halftime(self) -> None:
        """called when t = 50, starts a new period"""
        print("End of first half")
        self.is_halftime()
        # self.print_score()
        # self.start_of_period()

    def is_halftime(self) -> bool:
        if self.time == 12:
            return True
        else:
            return False

    def print_score(self) -> None:
        """Print the current score"""
        print(f"Score:  {self.score[1]} to {self.score[0]}\n")

    # def start_of_period(self) -> None:
    #     """Simulate a center jump for posession at the beginning of a period"""
    #     print("Center jump")
    #     random = self.set_random_number()
    #     if random > 0.6:
    #         print("Dartmouth controls the tap.\n")
    #         self.dartmouth_ball()
    #     else:
    #         print(self.opponent + " controls the tap.\n")
    #         self.opponent_ball()


    """new version of start_of_period that supports mocking"""
    def start_of_period(self) -> None:
        """Simulate a center jump for posession at the beginning of a period"""
        print("Center jump")
        randomNum = self.get_random_number_for_starting()
        if randomNum > 0.6:
            print("Dartmouth controls the tap.\n")
            self.dartmouth_ball()
        else:
            print(self.opponent + " controls the tap.\n")
            self.opponent_ball()


    def two_minute_warning(self) -> None:
        """called when t = 3"""
        self.two_minute_warning_message = "   *** Two minutes left in the game ***"
        print(self.two_minute_warning_message)

    def dartmouth_jump_shot(self) -> None:
        """called when the user enters 1 or 2 for their shot"""
        self.time += 1
        if self.time == 12:
            self.halftime()
        elif self.time == 22:
            self.two_minute_warning()
        print("Jump Shot.")
        # simulates chances of different possible outcomes
        random_number1 = self.set_dartmouth_jump_shot_random_number1()
        random_number2 = self.set_dartmouth_jump_shot_random_number2()
        random_number_3 = self.set_dartmouth_jump_shot_random_number3()
        random_number_4 = self.set_dartmouth_jump_shot_random_number4()
        random_number_5 = self.set_dartmouth_jump_shot_random_number5()
        random_number_6 = self.set_dartmouth_jump_shot_random_number6()
        random_number_7 = self.set_dartmouth_jump_shot_random_number7()
        random_number_8 = self.set_dartmouth_jump_shot_random_number8()

        if random_number1 > 0.341 * self.defense / 8:  # 0.25575
            if random_number2 > 0.682 * self.defense / 8:  # 0.5115
                if random_number_3 > 0.782 * self.defense / 8:  # 0.5865
                    if random_number_4 > 0.843 * self.defense / 8:  # 0.63225
                        print("Charging foul. Dartmouth loses ball.\n")
                        self.opponent_ball()
                    else:
                        # player is fouled
                        self.foul_shots(1)
                        self.opponent_ball()
                else:
                    if random_number_5 > 0.5:
                        print(
                            "Shot is blocked. Ball controlled by "
                            + self.opponent
                            + ".\n"
                        )
                        self.opponent_ball()
                    else:
                        print("Shot is blocked. Ball controlled by Dartmouth.")
                        self.dartmouth_ball()
            else:
                print("Shot is off target.")
                if self.defense / 6 * random_number_6 > 0.45:
                    print("Rebound to " + self.opponent + "\n")
                    self.opponent_ball()
                else:
                    print("Dartmouth controls the rebound.")
                    if random_number_7 > 0.4:
                        if self.defense == 6 and random_number_8 > 0.6:
                            print("Pass stolen by " + self.opponent + ", easy lay up")
                            self.add_points(0, 2)
                            self.dartmouth_ball()
                        else:
                            # ball is passed back to you
                            self.ball_passed_back()
                    else:
                        print()
                        self.dartmouth_non_jump_shot()
        else:
            print("Shot is good.")
            self.add_points(1, 2)
            self.opponent_ball()

    def dartmouth_non_jump_shot(self, counter=0) -> None:
        """
        Lay up, set shot, or defense change

        called when the user enters 0, 3, or 4
        """

        self.time += 1
        if self.time == 12:
            self.halftime()
        elif self.time == 22:
            self.two_minute_warning()

        if self.shot == 4:
            print("Set shot.")
        elif self.shot == 3:
            print("Lay up.")
        elif self.shot == 0:
            self.change_defense()

        random_number_1 = self.set_dartmouth_non_jump_shot_random_number1()
        random_number_2 = self.set_dartmouth_non_jump_shot_random_number2()
        random_number_3 = self.set_dartmouth_non_jump_shot_random_number3()
        random_number_4 = self.set_dartmouth_non_jump_shot_random_number4()
        random_number_5 = self.set_dartmouth_non_jump_shot_random_number5()
        random_number_6 = self.set_dartmouth_non_jump_shot_random_number6()

        # simulates different outcomes after a lay up or set shot
        if 7 / self.defense * random_number_1 > 0.4:
            if 7 / self.defense * random_number_2 > 0.7:
                if 7 / self.defense * random_number_3 > 0.875:
                    if 7 / self.defense * random_number_4 > 0.925:
                        print("Charging foul. Dartmouth loses the ball.\n")
                        self.opponent_ball()
                    else:
                        print("Shot blocked. " + self.opponent + "'s ball.\n")
                        self.opponent_ball()
                else:
                    self.foul_shots(1)
                    self.opponent_ball()
            else:
                print("Shot is off the rim.")
                if random_number_5 > 2 / 3:
                    print("Dartmouth controls the rebound.")
                    if random_number_6 > 0.4:
                        print("Ball passed back to you.\n")
                        self.dartmouth_ball()
                    else:
                        if counter == 3:
                            print("ball stolen. Opponents Ball")
                            self.opponent_ball()
                        else:
                            self.dartmouth_non_jump_shot(counter + 1)
                else:
                    print(self.opponent + " controls the rebound.\n")
                    self.opponent_ball()
        else:
            print("Shot is good. Two points.")
            self.add_points(1, 2)
            self.opponent_ball()

    def dartmouth_ball(self) -> None:
        """plays out a Dartmouth posession, starting with your choice of shot"""
        shot = get_dartmouth_ball_choice(self.shot_choices)
        self.shot = shot

        random_number1 = self.set_dartmouth_ball_random_number()
        if self.time < 24 or random_number1 < 0.5:
            if self.shot == 1 or self.shot == 2:
                self.dartmouth_jump_shot()
            else:
                self.dartmouth_non_jump_shot()
        else:
            if self.score[0] != self.score[1]:
                print("\n   ***** End Of Game *****")
                print(
                    "Final Score: Dartmouth: "
                    + str(self.score[1])
                    + "  "
                    + self.opponent
                    + ": "
                    + str(self.score[0])
                )
            else:
                print("\n   ***** End Of Second Half *****")
                print("Score at end of regulation time:")
                print(
                    "     Dartmouth: "
                    + str(self.score[1])
                    + " "
                    + self.opponent
                    + ": "
                    + str(self.score[0])
                )
                print("Begin two minute overtime period")
                self.time = 22
                self.start_of_period()

    def opponent_jumpshot(self) -> None:
        """Simulate the opponents jumpshot"""
        random_number1 = self.set_opponent_jump_shot_random_number1()
        random_number2 = self.set_opponent_jump_shot_random_number2()
        random_number_3 = self.set_opponent_jump_shot_random_number3()
        random_number_4 = self.set_opponent_jump_shot_random_number4()
        random_number_5 = self.set_opponent_jump_shot_random_number5()
        random_number_6 = self.set_opponent_jump_shot_random_number6()
        random_number_7 = self.set_opponent_jump_shot_random_number7()

        print("Jump Shot.")
        if 8 / self.defense * random_number1 > 0.35:
            if 8 / self.defense * random_number2 > 0.75:
                if 8 / self.defense * random_number_3 > 0.9:
                    print("Offensive foul. Dartmouth's ball.\n")
                    self.dartmouth_ball()
                else:
                    self.foul_shots(0)
                    self.dartmouth_ball()
            else:
                print("Shot is off the rim.")
                if self.defense / 6 * random_number_4 > 0.5:
                    print(self.opponent + " controls the rebound.")
                    if self.defense == 6:
                        if random_number_5 > 0.75:
                            print("Ball stolen. Easy lay up for Dartmouth.")
                            self.add_points(1, 2)
                            self.opponent_ball()
                        else:
                            if random_number_6 > 0.5:
                                print()
                                self.opponent_non_jumpshot()
                            else:
                                print("Pass back to " + self.opponent + " guard.\n")
                                self.opponent_ball()
                    else:
                        if random_number_7 > 0.5:
                            self.opponent_non_jumpshot()
                        else:
                            print("Pass back to " + self.opponent + " guard.\n")
                            self.opponent_ball()
                else:
                    print("Dartmouth controls the rebound.\n")
                    self.dartmouth_ball()
        else:
            print("Shot is good.")
            self.add_points(0, 2)
            self.dartmouth_ball()

    def opponent_non_jumpshot(self, counter=0) -> None:
        """Simulate opponents lay up or set shot."""
        if self.z1 > 3:  # type: ignore
            print("Set shot.")
        else:
            print("Lay up")
        random_number1 = self.set_opponent_non_jump_shot_random_number1()
        random_number2 = self.set_opponent_non_jump_shot_random_number2()
        random_number3 = self.set_opponent_non_jump_shot_random_number3()
        random_number4 = self.set_opponent_non_jump_shot_random_number4()
        random_number5 = self.set_opponent_non_jump_shot_random_number5()

        if 7 / self.defense * random_number1 > 0.413:
            print("Shot is missed.")
            if self.defense / 6 * random_number2 > 0.5:
                print(self.opponent + " controls the rebound.")
                if self.defense == 6:
                    if random_number3 > 0.75:
                        print("Ball stolen. Easy lay up for Dartmouth.")
                        self.add_points(1, 2)
                        self.opponent_ball()
                    else:
                        if random_number4 > 0.5:
                            print()
                            if counter == 3:
                                print("Ball stolen. Dartmouth ball.")
                                self.dartmouth_ball()
                            else:
                                self.opponent_non_jumpshot(counter + 1)
                        else:
                            print("Pass back to " + self.opponent + " guard.\n")
                            self.opponent_ball()
                else:
                    if random_number5 > 0.5:
                        print()
                        if counter == 3:
                            print("Ball stolen. Dartmouth ball.")
                            self.dartmouth_ball()
                        else:
                            self.opponent_non_jumpshot(counter + 1)
                    else:
                        print("Pass back to " + self.opponent + " guard\n")
                        self.opponent_ball()
            else:
                print("Dartmouth controls the rebound.\n")
                self.dartmouth_ball()
        else:
            print("Shot is good.")
            self.add_points(0, 2)
            self.dartmouth_ball()

    def opponent_ball(self) -> None:
        """
        Simulate an opponents possesion

        Randomly picks jump shot or lay up / set shot.
        """
        random_number_1 = self.set_opponent_ball_random_number1()

        self.time += 1
        if self.time == 12:
            self.halftime()
        self.z1 = 10 / 4 * random_number_1 + 1
        if self.z1 > 2:
            self.opponent_non_jumpshot()
        else:
            self.opponent_jumpshot()

    def set_random_number(self) -> float:
        num = random.random()
        return num

    def set_dartmouth_jump_shot_random_number1(self) -> float:
        num = random.random()
        return num

    def set_dartmouth_jump_shot_random_number2(self) -> float:
        num = random.random()
        return num

    def set_dartmouth_jump_shot_random_number3(self) -> float:
        num = random.random()
        return num

    def set_dartmouth_jump_shot_random_number4(self) -> float:
        num = random.random()
        return num

    def set_dartmouth_jump_shot_random_number5(self) -> float:
        num = random.random()
        return num

    def set_dartmouth_jump_shot_random_number6(self) -> float:
        num = random.random()
        return num

    def set_dartmouth_jump_shot_random_number7(self) -> float:
        num = random.random()
        return num

    def set_dartmouth_jump_shot_random_number8(self) -> float:
        num = random.random()
        return num

    def set_opponent_ball_random_number1(self) -> float:
        num = random.random()
        return num

    def set_opponent_non_jump_shot_random_number1(self) -> float:
        num = random.random()
        return num

    def set_opponent_non_jump_shot_random_number2(self) -> float:
        num = random.random()
        return num

    def set_opponent_non_jump_shot_random_number3(self) -> float:
        num = random.random()
        return num

    def set_opponent_non_jump_shot_random_number4(self) -> float:
        num = random.random()
        return num

    def set_opponent_non_jump_shot_random_number5(self) -> float:
        num = random.random()
        return num

    def set_dartmouth_ball_random_number(self) -> float:
        num = random.random()
        return num

    def set_opponent_jump_shot_random_number1(self) -> float:
        return random.random()

    def set_opponent_jump_shot_random_number2(self) -> float:
        return random.random()

    def set_opponent_jump_shot_random_number3(self) -> float:
        return random.random()

    def set_opponent_jump_shot_random_number4(self) -> float:
        return random.random()

    def set_opponent_jump_shot_random_number5(self) -> float:
        return random.random()

    def set_opponent_jump_shot_random_number6(self) -> float:
        return random.random()

    def set_opponent_jump_shot_random_number7(self) -> float:
        return random.random()

    def set_dartmouth_non_jump_shot_random_number1(self) -> float:
        return random.random()

    def set_dartmouth_non_jump_shot_random_number2(self) -> float:
        return random.random()

    def set_dartmouth_non_jump_shot_random_number3(self) -> float:
        return random.random()

    def set_dartmouth_non_jump_shot_random_number4(self) -> float:
        return random.random()

    def set_dartmouth_non_jump_shot_random_number5(self) -> float:
        return random.random()

    def set_dartmouth_non_jump_shot_random_number6(self) -> float:
        return random.random()

    def get_foul_shot_random(self) -> float:
        return random.random()
    
    def get_random_number_for_starting(self) -> float:
        num = random.random()
        return num


# modify try except to defense input and use for loop to convert each char to float, if contain non-changeable char,
# set defense to none
def get_defense_choice2() -> float:
    try:
        defense = float(input())
    except ValueError:
        defense = None

    return defense


def get_new_defense_choice(defense, defense_choices: List[float], counter=0) -> float:
    # if the input wasn't a valid defense, takes input again
    while defense not in defense_choices:
        print("Your new defensive alignment is? ", end="")
        try:
            defense = float(input())
        except ValueError:
            if counter != 3:
                counter += 1
                continue
            else:
                defense = 6
    return defense


def get_defense_choice(defense_choices: List[float]) -> float:
    """Takes input for a defense"""

    defense = get_defense_choice2()
    defense = get_new_defense_choice(defense, defense_choices)

    assert isinstance(defense, float)
    return defense


def set_and_return_shot() -> int:
    try:
        shot = int(input())
    except ValueError:
        shot = None
    return shot

def get_new_shot_choice(shot, shot_choices: List[Literal[0, 1, 2, 3, 4]], counter=0) -> float:
    # if the input wasn't a valid defense, takes input again
    while shot not in shot_choices:
        print("Incorrect answer. Retype it. Your shot? ", end="")
        try:
            shot = int(input())
        except Exception:
            if counter != 3:
                counter += 1
                continue
            else:
                shot = 1
    return shot

def get_dartmouth_ball_choice(shot_choices: List[Literal[0, 1, 2, 3, 4]]) -> int:
    print("Your shot? ", end="")
    shot = None

    shot = set_and_return_shot()

    shot = get_new_shot_choice(shot,shot_choices)
    assert isinstance(shot, int)
    return shot


def set_opponents_name() -> str:
    opponent = input()
    return opponent


def get_opponents_name() -> str:
    """Take input for opponent's name"""
    print("\nChoose your opponent? ", end="")

    return set_opponents_name()


if __name__ == "__main__":
    Basketball().startGame()
