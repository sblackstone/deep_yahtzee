print("Importing Constants")
#class Constants:
SCORE_TYPES = ['main_1', 'main_2', 'main_3', 'main_4', 'main_5', 'main_6', 'three_of_a_kind', 'four_of_a_kind', 'full_house', 'small_straight', 'large_straight', 'chance', 'yahtzee' ]
MAX_MONTHS=5
DEFAULT_CASH=1e5

# ACTIONS  
MAIN_1          = 0
MAIN_2          = 1
MAIN_3          = 2
MAIN_4          = 3
MAIN_5          = 4
MAIN_6          = 5
THREE_OF_A_KIND = 6
FOUR_OF_A_KIND  = 7
FULL_HOUSE      = 8
SMALL_STRAIGHT  = 9
LARGE_STRAIGHT  = 10
CHANCE          = 11
YAHTZEE         = 12
# 13-45 are for die rolls.

SCORE_TYPE_COUNT = len(SCORE_TYPES)

NUM_DICE = 5
ROLLS_PER_TURN=3
