import numpy as np

ROLLS_PER_TURN=3

class Dice:

    def __init__(self):
        self.reset()

    def reset(self):
        self.dice  = [0, 0, 0, 0, 0]
        self.rolls = ROLLS_PER_TURN
    
    # Accepts an array of the form [0,1,1,0,0]
    # which means re-roll dies 1 and 2.
    # Always rolls everything on first move.
    def roll(self, arr):
        if self.rolls == 0:
            return False

        for i in range(5):

            # Ignore arr[i] if this is the first roll.
            if arr[i] or self.rolls == ROLLS_PER_TURN:
              self.dice[i] = np.random.randint(6) + 1

        self.rolls -= 1
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

        