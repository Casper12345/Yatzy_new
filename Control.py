""" This is the control module """

# import from local scripts
import Model
import View


class Control(object):

    """ Control Methods """

    """ Defining Variables """
    def __init__(self):
        self.menu = list()
        self.menu_1 = list()

    """ Control Methods """

    @staticmethod  # This method is the initial game menu
    def control():
        ask_1 = View.UserInput.ask_action_1()  # calls ask_action_1 from View
        if ask_1 == 'r':
            return

        elif ask_1 == 'q':
            ask_3 = View.UserInput.ask_action_3()  # asks if user is sure about quitting
            if ask_3 == 'y':
                View.ProgramOutput.goodbye()  # prints goodbye
                quit()  # quits program
            else:
                return Control.control()
        else:
            return Control.control()  # returns to method control

    """ Operations Methods """

    def operation_1(self):  # This method lets the users input position of the dice to save
        ask_2 = View.UserInput.ask_action_2()  # calls ask_action_2 form View

        if ask_2.isdigit() or ask_2 == '':  # is ask a digit or no input?
            # transform input a list of integers
            if ask_2 == '':
                pass

            else:
                ask_2 = [int(i) for i in ask_2]

                # creates a list from 1 to 5 with no duplicates
                l_no_dub = [i for i in ask_2 if 5 >= i > 0 and ask_2.count(i) == 1]

                # creates a list that starts with 0
                l_count_zero = [i - 1 for i in ask_2 if 5 >= i > 0 and ask_2.count(i) == 1]

                # flow control mechanism
                if ask_2 == l_no_dub and len(ask_2) <= len(Model.PLAYER_DICE.roll_number) and\
                        max(ask_2) <= len(Model.PLAYER_DICE.roll_number):

                    # appends position in self.roll_number to self.save
                    for i in l_count_zero:
                        Model.PLAYER_DICE.roll_save.append(Model.PLAYER_DICE.roll_number[i])

                else:
                    View.ProgramOutput.try_again()
                    return self.operation_1()
        else:
            View.ProgramOutput.try_again()
            return self.operation_1()

            # defines commands for appending the final saved dice to score slot.

    def operation_2(self):  # This method
        ask_4 = View.UserInput.ask_action_4()

        if ask_4 in PLAYER_CONTROL.menu_1 and ask_4 not in PLAYER_CONTROL.menu:
            Model.PLAYER_SCORE_BOARD.result_catalog[ask_4] = Model.PLAYER_DICE.roll_save
            PLAYER_CONTROL.menu.append(ask_4)
        else:
            View.ProgramOutput.try_again()
            return self.operation_2()
        return ask_4

        # creates the menu to choose score slots that are not already filled

    def menu_1_method(self):
        self.menu_1 = list(i for i in Model.PLAYER_SCORE_BOARD.result_catalog.keys()
                           if i not in self.menu)


""" Creating instances """

PLAYER_CONTROL = Control()

""" Functions for the game """


def player_roll_func():
    # main roll function
    Model.PLAYER_DICE.die_roll()  # calls method that creates the die output

    View.ProgramOutput.dice_are()  # calls the method that outputs dice are:

    PLAYER_CONTROL.operation_1()  # calls method that handles player input and saves dice

    View.ProgramOutput.saved()  # calls method that prints saved:


def player_roll_result():
    # result function when the sequence is finished.

    PLAYER_CONTROL.menu_1_method()  # appends dice to saved slot

    # this prints the result of the save after all the rolls
    View.ProgramOutput.result_is()  # calls function that outputs result is:

    View.ProgramOutput.save_slots()  # printing the slots that are not yet taken.

    operation = PLAYER_CONTROL.operation_2()  # calls operations_2

    View.ProgramOutput.final_slot(operation)  # outputs final_slot

    # resetting PLAYER_DICE.save
    Model.PLAYER_DICE.roll_save = list()


def player_round():
    player_roll_func()
    for _ in range(2):

        if len(Model.PLAYER_DICE.roll_save) == 5:
            break
        else:
            View.UserInput.control_1()  # waits for <return>
            player_roll_func()

    player_roll_result()


def player_loop():
    # while loop that breaks when all slots are filled. When len(PLAYER_RESULT.menu >= 15.

    while len(PLAYER_CONTROL.menu) < 15:  # changed from 15
        Control.control()  # calls control.control that asks if R or Q.
        player_round()


def main():
    View.ProgramOutput.welcome()  # calls welcome() from class Control
    player_loop()  # calls player_loop()
    Model.player_score_calculation() # calls player_statistics
    View.ProgramOutput.result_out() # outputs result
