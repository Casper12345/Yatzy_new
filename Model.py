""" This it the model module """

# import standard library
import random
from collections import OrderedDict


class Dices(object):

    """ class containing the dice object"""

    def __init__(self):

        self.roll_number = list()  # variable for the dice output as a list

        self.roll_save = list()  # variable for the saved dice

    def die_roll(self):  # This method creates the dice result
        self.roll_number = [random.randint(1, 6) for _ in range(0, (5 - len(self.roll_save)))]


class ScoreBoard(object):

    """ Class that contains the scoreboard and the scoreboard control variables """

    def __init__(self):
        self.menu = list()
        self.menu_1 = list()
        self.result_catalog = OrderedDict([
            ('Ones', list()),
            ('Twos', list()),
            ('Threes', list()),
            ('Fours', list()),
            ('Fives', list()),
            ('Sixes', list()),
            ('One Pair', list()),
            ('Two Pairs', list()),
            ('Three of a Kind', list()),
            ('Four of a Kind', list()),
            ('Small Straight', list()),
            ('Large Straight', list()),
            ('Full House', list()),
            ('Chance', list()),
            ('Yatzy', list())])


class ScoreCalculator(object):

    """ This class calculates the dice values of the result slots """

    def __init__(self):

        # setting self.cal to player_score.result_catalog

        self.cal = PLAYER_SCORE_BOARD.result_catalog

        # defining the calculate variables as a dict with 17 values

        self.calculate_catalog = {chr(65+i): None for i in range(17)}

    def ones_cal(self):
        ones_list = [i for i in self.cal['Ones'] if i == 1]
        ones_list = sum(ones_list)
        self.calculate_catalog['A'] = ones_list

    def twos_cal(self):
        twos_list = [i for i in self.cal['Twos'] if i == 2]
        twos_list = sum(twos_list)
        self.calculate_catalog['B'] = twos_list

    def threes_cal(self):
        threes_list = [i for i in self.cal['Threes'] if i == 3]
        threes_list = sum(threes_list)
        self.calculate_catalog['C'] = threes_list

    def fours_cal(self):
        fours_list = [i for i in self.cal['Fours'] if i == 4]
        fours_list = sum(fours_list)
        self.calculate_catalog['D'] = fours_list

    def fives_cal(self):
        fives_list = [i for i in self.cal['Fives'] if i == 5]
        fives_list = sum(fives_list)
        self.calculate_catalog['E'] = fives_list

    def sixes_cal(self):
        sixes_list = [i for i in self.cal['Sixes'] if i == 6]
        sixes_list = sum(sixes_list)
        self.calculate_catalog['F'] = sixes_list

    def one_pair_cal(self):
        one_pair_list = sorted([i for i in self.cal['One Pair']
                                if self.cal['One Pair'].count(i) >= 2], reverse=True)[:2]
        if one_pair_list:
            self.calculate_catalog['G'] = sum(one_pair_list)
        else:
            self.calculate_catalog['G'] = 0

    def two_pairs_cal(self):
        two_pairs_list = sorted([i for i in self.cal['Two Pairs'] if
                                 self.cal['Two Pairs'].count(i) >= 2], reverse=True)[:2]
        k = [i for i in self.cal['Two Pairs'] if i not in two_pairs_list]
        two_pairs_list_1 = sorted([i for i in k if k.count(i) >= 2], reverse=True)[:2]
        if two_pairs_list and two_pairs_list_1:
            self.calculate_catalog['H'] = sum(two_pairs_list + two_pairs_list_1)

        else:
            self.calculate_catalog['H'] = 0

    def three_of_a_kind_cal(self):
        three_of_a_kind_list = [i for i in self.cal['Three of a Kind']
                                if self.cal['Three of a Kind'].count(i) >= 3][:3]
        if three_of_a_kind_list:
            self.calculate_catalog['I'] = sum(three_of_a_kind_list)
        else:
            self.calculate_catalog['I'] = 0

    def four_of_a_kind_cal(self):
        four_of_a_kind_list = [i for i in self.cal['Four of a Kind']
                               if self.cal['Four of a Kind'].count(i) >= 4][:4]
        if four_of_a_kind_list:
            self.calculate_catalog['J'] = sum(four_of_a_kind_list)
        else:
            self.calculate_catalog['J'] = 0

    def small_straight_cal(self):
        small_straight_list = list(set(self.cal['Small Straight']))
        small_straight_list = sorted([i for i in small_straight_list if i == 1 or i == 2 or
                                      i == 3 or i == 4 or i == 5])
        if small_straight_list == [1, 2, 3, 4, 5]:
            self.calculate_catalog['K'] = 15
        else:
            self.calculate_catalog['K'] = 0

    def large_straight_cal(self):
        large_straight_list = list(set(self.cal['Large Straight']))
        large_straight_list = sorted([i for i in large_straight_list if i == 2 or i == 3 or
                                      i == 4 or i == 5 or i == 6])
        if large_straight_list == [2, 3, 4, 5, 6]:
            self.calculate_catalog['L'] = 20
        else:
            self.calculate_catalog['L'] = 0

    def full_house_cal(self):
        full_house_list = sorted([i for i in self.cal['Full House'] if
                                  self.cal['Full House'].count(i) >= 3], reverse=True)[:3]
        k = [i for i in self.cal['Full House'] if i not in full_house_list]
        full_house_list_1 = [i for i in k if k.count(i) >= 2][:2]
        if full_house_list and full_house_list_1:
            self.calculate_catalog['M'] = sum(full_house_list + full_house_list_1)
        else:
            self.calculate_catalog['M'] = 0

    def chance_cal(self):
        self.calculate_catalog['N'] = sum(self.cal['Chance'])

    def yatzy_cal(self):
        yatzy_list = [i for i in self.cal['Yatzy'] if self.cal['Yatzy'].count(i) == 5]
        if yatzy_list:
            self.calculate_catalog['O'] = 50
        else:
            self.calculate_catalog['O'] = 0

    # this method calculates the bonus
    def bonus_cal(self):
        bonus_list = self.calculate_catalog['A'] + self.calculate_catalog['B'] +\
                     self.calculate_catalog['C'] + self.calculate_catalog['D'] +\
                     self.calculate_catalog['E'] + self.calculate_catalog['F']
        if bonus_list >= 63:
            self.calculate_catalog['P'] = 50
        else:
            self.calculate_catalog['P'] = 0

    # this method calculates the final score
    def final_score_cal(self):
        self.calculate_catalog['Q'] = self.calculate_catalog['A'] + self.calculate_catalog['B'] +\
                                      self.calculate_catalog['C'] + self.calculate_catalog['D'] +\
                                      self.calculate_catalog['E'] + self.calculate_catalog['F'] +\
                                      self.calculate_catalog['G'] + self.calculate_catalog['H'] +\
                                      self.calculate_catalog['I'] + self.calculate_catalog['J'] +\
                                      self.calculate_catalog['K'] + self.calculate_catalog['L'] +\
                                      self.calculate_catalog['M'] + self.calculate_catalog['N'] +\
                                      self.calculate_catalog['O'] + self.calculate_catalog['P']

""" Creating instances of Model Classes"""

PLAYER_DICE = Dices()
PLAYER_SCORE_BOARD = ScoreBoard()
PLAYER_CALCULATE = ScoreCalculator()


""" Calculates Player Score"""


def player_score_calculation():

    # runs all the calculation functions
    PLAYER_CALCULATE.ones_cal()
    PLAYER_CALCULATE.twos_cal()
    PLAYER_CALCULATE.threes_cal()
    PLAYER_CALCULATE.fours_cal()
    PLAYER_CALCULATE.fives_cal()
    PLAYER_CALCULATE.sixes_cal()
    PLAYER_CALCULATE.bonus_cal()

    PLAYER_CALCULATE.small_straight_cal()
    PLAYER_CALCULATE.large_straight_cal()
    PLAYER_CALCULATE.three_of_a_kind_cal()
    PLAYER_CALCULATE.four_of_a_kind_cal()
    PLAYER_CALCULATE.one_pair_cal()
    PLAYER_CALCULATE.two_pairs_cal()
    PLAYER_CALCULATE.full_house_cal()
    PLAYER_CALCULATE.chance_cal()
    PLAYER_CALCULATE.yatzy_cal()

    PLAYER_CALCULATE.final_score_cal()
