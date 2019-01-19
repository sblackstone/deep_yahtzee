import numpy as np
import deep_yahtzee.constants as const

class Dice:

    def __init__(self):
        self.reset()

    def set_die_count(self):
        self.die_count = [0] * 7
        for i in self.dice:
            self.die_count[i] += 1 
        return(self.die_count)

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
    
    def classifications(self):
        self.klassifications = [ -1 ] * const.SCORE_TYPE_COUNT
        self.klassifications[const.CHANCE] = 
        
        for i in range(1,7):
            if self.die_count[i] > 0:
                self.klassifications[i-1] = self.die_count[i] * i

            if self.die_count[i] >= 3:
                key = const.THREE_OF_A_KIND
                self.klassifications[key] = sum(self.dice)
                for j in range(1,7):
                    if i != j and self.die_count[j] == 2:
                        self.klassifications[const.FULL_HOUSE] = 25                        

            if self.die_count[i] >= 4:
                self.klassifications[const.FOUR_OF_A_KIND] = sum(self.dice)

            if self.die_count[i] == 5:
                key = const.YAHTZEE
                self.klassifications[key] = 50

        for i in range(1, 4):
            if self.die_count[i] and self.die_count[i+1] and self.die_count[i+2] and self.die_count[i+3]:
                key   = const.SMALL_STRAIGHT
                self.klassifications[key] = 30
                if i < 3 and self.die_count[i+4]:
                    key   = const.LARGE_STRAIGHT    
                    self.klassifications[key] = 40
                


        return self.klassifications
        
        
    
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
        self.set_die_count()
        return True



if __name__ == "__main__":
    d = Dice()
    print(d.roll([1,0,1,0,1]))
    print(d.dice)
    print(d.roll([1,0,1,0,1]))
    print(d.dice)
    print(d.roll([1,0,1,0,1]))
    print(d.dice)
    print(d.roll([1,0,1,0,1]))
    print(d.dice)
    print(d.die_count[1:6])
    print(d.classifications())
        