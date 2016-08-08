""" This is the view module """

# import from local scripts

import Model
import Control


class UserInput(object):

    """ Static class that takes user input """

    """ Control Methods """

    @staticmethod  # This  method is used in between the other roll rounds
    def control_1():
        raw_input('Press return to roll')

    """ Ask Methods """

    @staticmethod  # This ask method works as a selection menu
    def ask_action_1():
        return raw_input('Press R to roll or Q to quit: ').lower()  # converted to lower()

    @staticmethod # This ask method inputs position of the dice to save
    def ask_action_2():
        return raw_input('Select positions of dice you want to '
                         'save (eg. 13 - for die positions 1 and 3): ')

    @staticmethod  # This ask method verifies if user wants to quit
    def ask_action_3():
        return raw_input('Are you sure you want to quit? Y/N: ').lower()  # converted to lower()

    @staticmethod
    def ask_action_4():  # This ask method inputs what slot to save result dice to
        return raw_input('Where do you want to save the dice to?')


class ProgramOutput(object):

    """ Static class that outputs to the console """

    """ Graphic Output Methods """

    @staticmethod  # This method prints the welcome banner
    def welcome():
        print 'Welcome to Yatzy'.upper(), '\n'  # prints in upper()

    """ Score Output Methods """

    @staticmethod  # This method outputs the result of the dice
    def dice_are():
        print '\n', 'Dice are:', Model.PLAYER_DICE.roll_number, '\n'

    @staticmethod  # This method outputs the saved dice
    def saved():
        print '\n', Model.PLAYER_DICE.roll_save, 'saved', '\n'

    @staticmethod  # This method outputs the result of the round
    def result_is():
        print 'Result is:', Model.PLAYER_DICE.roll_save, '\n'

    @staticmethod  # This method outputs the empty slots to save to
    def save_slots():
        for i in Control.PLAYER_CONTROL.menu_1:
            print i
        print '\n'

    @staticmethod  # This method outputs the final save in the slot
    def final_slot(k):
        print '\n', '{}:{}'.format(k, Model.PLAYER_SCORE_BOARD.result_catalog[k]), '\n'

    @staticmethod  # This method outputs the final score result
    def result_out():

        # prints the result of the first part of the score
        print 'Ones score:', Model.PLAYER_CALCULATE.calculate_catalog['A']
        print 'Twos score:', Model.PLAYER_CALCULATE.calculate_catalog['B']
        print 'Threes score:', Model.PLAYER_CALCULATE.calculate_catalog['C']
        print 'Fours score:', Model.PLAYER_CALCULATE.calculate_catalog['D']
        print 'Fives score:', Model.PLAYER_CALCULATE.calculate_catalog['E']
        print 'Sixes score:', Model.PLAYER_CALCULATE.calculate_catalog['F'], '\n'

        # prints the result of the bonus
        print 'Bonus:', Model.PLAYER_CALCULATE.calculate_catalog['P'], '\n'

        # prints the result og the second part of the score
        print 'One Pair:', Model.PLAYER_CALCULATE.calculate_catalog['G']
        print 'Two Pairs:', Model.PLAYER_CALCULATE.calculate_catalog['H']
        print 'Three of a Kind:', Model.PLAYER_CALCULATE.calculate_catalog['I']
        print 'Four of a Kind:', Model.PLAYER_CALCULATE.calculate_catalog['J']
        print 'Small Straight:', Model.PLAYER_CALCULATE.calculate_catalog['K']
        print 'Large Straight', Model.PLAYER_CALCULATE.calculate_catalog['L']
        print 'Full House', Model.PLAYER_CALCULATE.calculate_catalog['M']
        print 'Chance:', Model.PLAYER_CALCULATE.calculate_catalog['N']
        print 'Yatzy:', Model.PLAYER_CALCULATE.calculate_catalog['O'], '\n'

        # prints the final score
        print 'Final score:', Model.PLAYER_CALCULATE.calculate_catalog['Q']

    """ Auxiliary Output Methods"""

    @staticmethod  # This method print good bye
    def goodbye():
        print 'Good Bye!!'

    @staticmethod  # This method prints try again
    def try_again():
        print 'Try again'
