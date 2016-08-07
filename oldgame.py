
""" This is a game based on the Yatzy die game. """

# import from random and collections
import random
from collections import OrderedDict


class Control(object):

    @staticmethod   # This static method prints the welcome banner
    def welcome():
        print 'Welcome to Yatzy'.upper(), '\n'

    @staticmethod  # This static ask method works as a selection menu
    def ask_action_2():
        # the input it takes is converted to lower() case
        return raw_input('Press R to roll or Q to quit: ').lower()

    @staticmethod
    def ask_action_3():
        return raw_input('Are you sure you want to quit? Y/N: ').lower()

    @staticmethod   # This static method calls and flow controls input from ask_action_2()
    def control():
        ask = Control.ask_action_2() # calls ask_action_2
        if ask == 'r':
            return  # returns to method ??

        elif ask == 'q':
            ask_3 = Control.ask_action_3()
            if ask_3 == 'y':
                print 'Good Bye!!'
                quit()  # quits program
            else:
                return Control.control()
        else:
            return Control.control() # returns to method control

    @staticmethod  # This static method is used in between the other roll rounds
    def control_1():
        raw_input('Press return to roll')


# This class controls the dice object.
class Dice(object): # parent class with no children

    # creating the variables
    def __init__(self):

        # self.roll_number is variable for the dice output as a list
        self.roll_number = list()

        # self.save is a list of the saved dice
        self.save = list()

    # static method that inputs position of the dice to save
    @staticmethod
    def ask_action():  # is called by ??
        return raw_input('Select positions of dice you want to '
                         'save (eg. 13 - for die positions 1 and 3): ')

    # method that outputs the dice roll

    # sets the variable roll_number to random depending on the amount of dice left
    def die_roll(self):
        self.roll_number = [random.randint(1, 6) for _ in range(0, (5-len(self.save)))]

    # flow control method for the dice object
    def operation(self):

        ask = self.ask_action()  # calls ask_action()

        if ask.isdigit() or ask == '':  # is ask a digit or no input?
            # transform input a list of integers
            if ask == '':
                pass

            else:
                ask = [int(i) for i in ask]

                # creates a list from 1 to 5 with no duplicates
                l_no_dub = [i for i in ask if 5 >= i > 0 and ask.count(i) == 1]

                # creates a list that starts with 0
                l_count_zero = [i - 1 for i in ask if 5 >= i > 0 and ask.count(i) == 1]

                # flow control mechanism
                if ask == l_no_dub and len(ask) <= len(self.roll_number) and\
                        max(ask) <= len(self.roll_number):

                    # appends position in self.roll_number to self.save
                    for i in l_count_zero:
                        self.save.append(self.roll_number[i])

                else:
                    print 'Try again'
                    return self.operation()
        else:
            print 'Try again'
            return self.operation()


class Result(object):
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

    @staticmethod
    def ask_action():
        return raw_input('Where do you want to save the dice to?')

    # defines commands for appending the final saved dice to score slot.
    def operations(self):
        ask = self.ask_action()

        if ask in self.result_catalog and ask not in self.menu:
            self.result_catalog[ask] = PLAYER_DICE.save
            self.menu.append(ask)
        else:
            print 'Try again'
            return self.operations()
        return ask

    # creates the menu to choose score slots that are not already filled
    def menu_1_method(self):
        self.menu_1 = list(i for i in self.result_catalog.keys() if i not in self.menu)


class Calculate(object):
    # this class calculates the dice values of the result slots
    def __init__(self):

        # setting self.cal to player_score.result_catalog
        self.cal = PLAYER_RESULT.result_catalog

        # defining the calculate variables
        self.ones = None
        self.twos = None
        self.threes = None
        self.fours = None
        self.fives = None
        self.sixes = None
        self.one_pair = None
        self.two_pairs = None
        self.three_of_a_kind = None
        self.four_of_a_kind = None
        self.small_straight = None
        self.large_straight = None
        self.full_house = None
        self.chance = None
        self.yatzy = None
        self.bonus = None
        self.final_score = None

    def ones_cal(self):
        ones_list = [i for i in self.cal['Ones'] if i == 1]
        ones_list = sum(ones_list)
        self.ones = ones_list

    def twos_cal(self):
        twos_list = [i for i in self.cal['Twos'] if i == 2]
        twos_list = sum(twos_list)
        self.twos = twos_list

    def threes_cal(self):
        threes_list = [i for i in self.cal['Threes'] if i == 3]
        threes_list = sum(threes_list)
        self.threes = threes_list

    def fours_cal(self):
        fours_list = [i for i in self.cal['Fours'] if i == 4]
        fours_list = sum(fours_list)
        self.fours = fours_list

    def fives_cal(self):
        fives_list = [i for i in self.cal['Fives'] if i == 5]
        fives_list = sum(fives_list)
        self.fives = fives_list

    def sixes_cal(self):
        sixes_list = [i for i in self.cal['Sixes'] if i == 6]
        sixes_list = sum(sixes_list)
        self.sixes = sixes_list

    def one_pair_cal(self):
        one_pair_list = sorted([i for i in self.cal['One Pair']
                                if self.cal['One Pair'].count(i) >= 2], reverse=True)[:2]
        if one_pair_list:
            self.one_pair = sum(one_pair_list)
        else:
            self.one_pair = 0

    def two_pairs_cal(self):
        two_pairs_list = sorted([i for i in self.cal['Two Pairs'] if
                                 self.cal['Two Pairs'].count(i) >= 2], reverse=True)[:2]
        m = [i for i in self.cal['Two Pairs'] if i not in two_pairs_list]
        two_pairs_list_1 = sorted([i for i in m if m.count(i) >= 2], reverse=True)[:2]
        if two_pairs_list and two_pairs_list_1:
            self.two_pairs = sum(two_pairs_list + two_pairs_list_1)

        else:
            self.two_pairs = 0

    def three_of_a_kind_cal(self):
        three_of_a_kind_list = [i for i in self.cal['Three of a Kind']
                                if self.cal['Three of a Kind'].count(i) >= 3][:3]
        if three_of_a_kind_list:
            self.three_of_a_kind = sum(three_of_a_kind_list)
        else:
            self.three_of_a_kind = 0

    def four_of_a_kind_cal(self):
        four_of_a_kind_list = [i for i in self.cal['Four of a Kind']
                               if self.cal['Four of a Kind'].count(i) >= 4][:4]
        if four_of_a_kind_list:
            self.four_of_a_kind = sum(four_of_a_kind_list)
        else:
            self.four_of_a_kind = 0

    def small_straight_cal(self):
        small_straight_list = list(set(self.cal['Small Straight']))
        small_straight_list = sorted([i for i in small_straight_list if i == 1 or i == 2 or
                                      i == 3 or i == 4 or i == 5])
        if small_straight_list == [1, 2, 3, 4, 5]:
            self.small_straight = 15
        else:
            self.small_straight = 0

    def large_straight_cal(self):
        large_straight_list = list(set(self.cal['Large Straight']))
        large_straight_list = sorted([i for i in large_straight_list if i == 2 or i == 3 or
                                      i == 4 or i == 5 or i == 6])
        if large_straight_list == [2, 3, 4, 5, 6]:
            self.large_straight = 20
        else:
            self.large_straight = 0

    def full_house_cal(self):
        full_house_list = sorted([i for i in self.cal['Full House'] if
                                  self.cal['Full House'].count(i) >= 3], reverse=True)[:3]
        m = [i for i in self.cal['Full House'] if i not in full_house_list]
        full_house_list_1 = [i for i in m if m.count(i) >= 2][:2]
        if full_house_list and full_house_list_1:
            self.full_house = sum(full_house_list + full_house_list_1)
        else:
            self.full_house = 0

    def chance_cal(self):
        self.chance = sum(self.cal['Chance'])

    def yatzy_cal(self):
        yatzy_list = [i for i in self.cal['Yatzy'] if self.cal['Yatzy'].count(i) == 5]
        if yatzy_list:
            self.yatzy = 50
        else:
            self.yatzy = 0

    # this method calculates the bonus
    def bonus_cal(self):
        bonus_list = self.ones + self.twos + self.threes + self.fours + self.fives + self.sixes
        if bonus_list >= 63:
            self.bonus = 50
        else:
            self.bonus = 0

    # this method calculates the final score
    def final_score_cal(self):
        self.final_score = self.ones + self.twos + self.threes + \
                           self.fours + self.fives + self.sixes +\
                           self.bonus + self.one_pair + self.two_pairs + self.three_of_a_kind +\
                           self.four_of_a_kind + self.small_straight + self.large_straight +\
                           self.full_house + self.chance + self.yatzy


# Variables set to create instances of the three classes.
PLAYER_DICE = Dice()
PLAYER_RESULT = Result()
PLAYER_CALCULATE = Calculate()


# functions that define the game for the player.

def player_roll_func():
    # main roll function
    PLAYER_DICE.die_roll()  # calls method that creates the die output
    print '\n', 'Dice are:', PLAYER_DICE.roll_number, '\n'
    PLAYER_DICE.operation()  # calls method that handles player input and saves dice
    print '\n', PLAYER_DICE.save, 'saved', '\n'


def player_roll_result():
    # result function when the sequence is finished.
    # refreshes menu_1
    PLAYER_RESULT.menu_1_method() # appends dice to saved slot

    # this prints the result of the save after all the rolls
    print 'Result is:', PLAYER_DICE.save, '\n'

    # printing the slots that are not yet taken.
    for i in PLAYER_RESULT.menu_1:
        print i
    print '\n'

    # prints the name of the slot where the result is saved to and the result
    m = PLAYER_RESULT.operations()
    print '\n', '{}:{}'.format(m, PLAYER_RESULT.result_catalog[m]), '\n'

    # resetting PLAYER_DICE.save
    PLAYER_DICE.save = list()


def player_round():

    player_roll_func()
    for _ in range(2):

        if len(PLAYER_DICE.save) == 5:
            break
        else:
            Control.control_1()  # waits for <return>
            player_roll_func()

    player_roll_result()


def player_loop():

    # while loop that breaks when all slots are filled. When len(PLAYER_RESULT.menu >= 15.

    while len(PLAYER_RESULT.menu) < 15: # changed from 15
        Control.control()  # calls control.control that asks if R or Q.
        player_round()


def player_statistics():

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

    # prints the result of the first part of the score
    print 'Ones score:', PLAYER_CALCULATE.ones
    print 'Twos score:', PLAYER_CALCULATE.twos
    print 'Threes score:', PLAYER_CALCULATE.threes
    print 'Fours score:', PLAYER_CALCULATE.fours
    print 'Fives score:', PLAYER_CALCULATE.fives
    print 'Sixes score:', PLAYER_CALCULATE.sixes, '\n'
    # prints the result of the bonus
    print 'Bonus:', PLAYER_CALCULATE.bonus, '\n'

    # prints the result og the second part of the score
    print 'Small Straight:', PLAYER_CALCULATE.small_straight
    print 'Large Straight:', PLAYER_CALCULATE.large_straight
    print 'Three of a Kind:', PLAYER_CALCULATE.three_of_a_kind
    print 'Four of a Kind:', PLAYER_CALCULATE.four_of_a_kind
    print 'One Pair:', PLAYER_CALCULATE.one_pair
    print 'Two Pairs', PLAYER_CALCULATE.two_pairs
    print 'Full House', PLAYER_CALCULATE.full_house
    print 'Chance:', PLAYER_CALCULATE.chance
    print 'Yatzy:', PLAYER_CALCULATE.yatzy, '\n'

    # prints the final score
    print 'Final score:', PLAYER_CALCULATE.final_score


def main():
    Control.welcome()  # calls welcome() from class Control
    player_loop()  # calls player_round()
    player_statistics() # calls player_statistics


if __name__ == '__main__':
    main()
