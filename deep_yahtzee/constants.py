print("Importing Constants")
#class Constants:
SCORE_TYPES = ['main_1', 'main_2', 'main_3', 'main_4', 'main_5', 'main_6', 'three_of_a_kind', 'four_of_a_kind', 'full_house', 'small_straight', 'large_straight', 'chance', 'yahtzee' ]
MAX_MONTHS=5
DEFAULT_CASH=1e5

# ACTIONS  
TAKE_MAIN_1          = 0
TAKE_MAIN_2          = 1
TAKE_MAIN_3          = 2
TAKE_MAIN_4          = 3
TAKE_MAIN_5          = 4
TAKE_MAIN_6          = 5
TAKE_THREE_OF_A_KIND = 6
TAKE_FOUR_OF_A_KIND  = 7
TAKE_FULL_HOUSE      = 8
TAKE_SMALL_STRAIGHT  = 9
TAKE_LARGE_STRAIGHT  = 10
TAKE_CHANCE          = 11
TAKE_YAHTZEE         = 12
# 13-45 are for die rolls.

NUM_DICE = 5
ROLLS_PER_TURN=3
