
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







