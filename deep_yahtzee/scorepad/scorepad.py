import deep_yahtzee.constants
from tabulate import tabulate
import deep_yahtzee.constants as const

class ScorePad:
    def __init__(self):
        self.reset()
    
    def dump(self):
        data = []
        for i in range(const.SCORE_TYPE_COUNT):
            if self.scores[i] > -1:
                score = self.scores[i]
            else:
                score = ""    
            data.append([const.SCORE_TYPES[i], score])         
        data.append(["Main Total", self.main_total])
        data.append(["Bonus", self.bonus])
        data.append(["Score", self.score()])
        print(tabulate(data))
        print("\n\n")
        
        
    def reset(self):
        self.scores     = [-1] * const.SCORE_TYPE_COUNT
        self.total      = 0.0
        self.main_total = 0.0
        self.bonus      = 0.0
    
    
    def score(self):
        return self.total + self.bonus
        
    def as_observation(self):
        return(self.scores + [ self.total ])

    def unscored_types(self):
        return [x for x in range(const.SCORE_TYPE_COUNT) if self.scores[x] == -1]
    
    def take_score(self, score_type, value):
        #import code; code.interact(local=dict(globals(), **locals()))
        #if score_type == 'yahtzee':
            #import code; code.interact(local=dict(globals(), **locals()))
            
        if score_type in self.unscored_types():
            #print("Taking {} for {}".format(score_type, value))
            self.scores[score_type] = value
            self.total += value
            if score_type < 6:
                self.main_total += value
                if self.main_total > 62:
                    print("Bonus Unlocked")
                    self.bonus = 35

            return(True)
        else:
            return(False)
            
    def game_over(self):
        return len(self.unscored_types()) == 0
        
        
if __name__ == "__main__":
    s = ScorePad()
    print(s.unscored_types())
    s.take_score(const.MAIN_1, 24)
    s.take_score(const.MAIN_2, 24)
    s.take_score(const.MAIN_3, 24)
    s.take_score(const.MAIN_4, 24)
    s.take_score(const.MAIN_5, 24)
    s.take_score(const.MAIN_5, 24)

    s.take_score(const.FULL_HOUSE, 25)
    print(s.unscored_types())
    print(s.scores)
    s.dump()
    print(s.as_observation())
    print(len(const.SCORE_TYPES))
    print(len(s.as_observation()))