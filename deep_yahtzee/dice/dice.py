import numpy as np
import deep_yahtzee.constants as const
import sys

class Dice:

    def __init__(self):
        self.reset()

    def set_die_count_sum(self):
        self.die_count = [0] * 7
        self.die_sum   = 0
        for i in self.dice:
            self.die_count[i] += 1 
            self.die_sum += i

    def as_observation(self):
        return self.dice + [ self.rolls ]

    def reset(self):
        self.die_count = [0] * 7
        self.dice  = [0] * 5
        self.rolls = const.ROLLS_PER_TURN
    
    # ACTIONS  
    #MAIN_1          = 0
    #MAIN_2          = 1
    #MAIN_3          = 2
    #MAIN_4          = 3
    #MAIN_5          = 4
    #MAIN_6          = 5
    #THREE_OF_A_KIND = 6
    #FOUR_OF_A_KIND  = 7
    #FULL_HOUSE      = 8
    #SMALL_STRAIGHT  = 9
    #LARGE_STRAIGHT  = 10
    #CHANCE          = 11
    #YAHTZEE         = 12        
    
    def score_for_category(self, category):
        if category <= const.MAIN_6:
            return self.die_count[category+1] * (category + 1)
        
        if category == const.CHANCE:
            return self.die_sum

        if category == const.THREE_OF_A_KIND:
            for i in range(1,7):
                if self.die_count[i] >= 3:
                    return self.die_sum

        if category == const.FOUR_OF_A_KIND:
            for i in range(1,7):
                if self.die_count[i] >= 4:
                    return self.die_sum

        if category == const.YAHTZEE:
            for i in range(1,7):
                if self.die_count[i] == 5:
                    return 50

        
        if category == const.FULL_HOUSE:
            cnt = 0
            for i in range(1,7):
                if self.die_count[i] == 3 or self.die_count[i] == 2:
                    cnt += 1
            if cnt == 2:
                return 25
            else:
                return 0
        
        if category == const.SMALL_STRAIGHT or category == const.LARGE_STRAIGHT:
            for i in range(1, 4):
                if self.die_count[i] and self.die_count[i+1] and self.die_count[i+2] and self.die_count[i+3]:
                    if category == const.SMALL_STRAIGHT:
                        return 30
                    if category == const.LARGE_STRAIGHT and i < 3 and self.die_count[i+4]:
                        return 40
        # Default!
        return 0
                                        
    
    # Accepts an array of the form [0,1,1,0,0]
    # which means re-roll dies 1 and 2.
    # Always rolls everything on first move.
    def roll(self, arr):
        if self.rolls == 0:
            #print("Tried to roll but out of turns")
            return False
        for i in range(const.NUM_DICE):
            # Ignore arr[i] if this is the first roll.
            if arr[i] or self.rolls == const.ROLLS_PER_TURN:
              self.dice[i] = np.random.randint(6) + 1
        #print("The dice are now: {}".format(self.dice))
        self.rolls -= 1
        self.set_die_count_sum()
        return True

    def debug_dice(self, dice):
        self.dice = dice
        self.set_die_count_sum()
    


if __name__ == "__main__":


    d = Dice()
    
    d.debug_dice([1,1,2,3,4])
    print(d.score_for_category(const.MAIN_1))# == 2)

    d.debug_dice([1,1,2,3,4])
    print(d.score_for_category(const.MAIN_4))# == 4)

    d.debug_dice([1,5,3,5,5])
    print(d.score_for_category(const.THREE_OF_A_KIND))# == 19)

    d.debug_dice([4,4,5,4,4])    
    print(d.score_for_category(const.FOUR_OF_A_KIND))# == 21)

    d.debug_dice([3,3,3,4,4])    
    print(d.score_for_category(const.FULL_HOUSE))# == 25)

    d.debug_dice([3,4,5,5,2])    
    print(d.score_for_category(const.SMALL_STRAIGHT))# == 50)

    d.debug_dice([3,4,5,5,2])    
    print(d.score_for_category(const.LARGE_STRAIGHT))# == 0)

    d.debug_dice([1,2,3,4,5])    
    print(d.score_for_category(const.LARGE_STRAIGHT))# == 40)

    d.debug_dice([3,4,5,5,2])    
    print(d.score_for_category(const.CHANCE))# == 19)

    d.debug_dice([5,5,5,5,5])
    print(d.score_for_category(const.YAHTZEE))# == 50)
        