import numpy as np

NUM_DICE = 5
ROLLS_PER_TURN=3

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
        self.die_count = [0] * 6
        self.dice  = [0] * 5
        self.rolls = ROLLS_PER_TURN
        
    def classifications(self):
        self.classifications = { "chance": sum(self.dice) }
        
        for i in range(1,7):
            if self.die_count[i] > 0:
                key = "main_{}".format(i)
                self.classifications[key] = self.die_count[i] * i

            if self.die_count[i] >= 3:
                key = "three_of_a_kind"
                self.classifications[key] = sum(self.dice)
                for j in range(1,7):
                    if i != j and self.die_count[j] == 2:
                        key = "full_house"
                        self.classifications[key] = 25                        

            if self.die_count[i] >= 4:
                key = "four_of_a_kind"
                self.classifications[key] = sum(self.dice)

            if self.die_count[i] == 5:
                key = "yahtzee"
                self.classifications[key] = 50

        for i in range(1, 4):
            if self.die_count[i] and self.die_count[i+1] and self.die_count[i+2] and self.die_count[i+3]:
                key   = "small_straight"
                self.classifications[key] = 30
                if i < 3 and self.die_count[i+4]:
                    key   = "large_straight"
                    self.classifications[key] = 40
                


        return self.classifications
        
        
    
    # Accepts an array of the form [0,1,1,0,0]
    # which means re-roll dies 1 and 2.
    # Always rolls everything on first move.
    def roll(self, arr):
        if self.rolls == 0:
            return False
        for i in range(NUM_DICE):
            # Ignore arr[i] if this is the first roll.
            if arr[i] or self.rolls == ROLLS_PER_TURN:
              self.dice[i] = np.random.randint(6) + 1
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
        