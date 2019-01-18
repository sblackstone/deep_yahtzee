import deep_yahtzee.constants
from tabulate import tabulate
import deep_yahtzee.constants as const

class ScorePad:
    def __init__(self):
        self.reset()
    
    def dump(self):
        data = []
        for i in const.SCORE_TYPES:
            if i in self.scores:
                score = self.scores[i]
            else:
                score = ""    
            data.append([i, score])         
        data.append(["SubTotal", self.main_total])
        data.append(["Bonus", self.bonus])
        data.append(["Score", self.score()])
        print(tabulate(data))
        print("\n\n")
        
        
    def reset(self):
        self.scores     = {}
        self.total      = 0.0
        self.main_total = 0.0
        self.bonus      = 0.0
    
    
    def score(self):
        return self.total + self.bonus
        
    def as_observation(self):
        res = []
        for i in const.SCORE_TYPES:
            if i in self.scores.keys():
                res.append(self.scores[i])
            else:
                res.append(-1)
        return(res + [ self.total ])

    def unscored_types(self):
        return [x for x in const.SCORE_TYPES if not x in self.scores.keys()]
    
    def take_score(self, score_type, value):
        #import code; code.interact(local=dict(globals(), **locals()))
        #if score_type == 'yahtzee':
            #import code; code.interact(local=dict(globals(), **locals()))
            
        if score_type in self.unscored_types():
            #print("Taking {} for {}".format(score_type, value))
            self.scores[score_type] = value
            self.total += value
            if score_type[:4] == 'main':
                self.main_total += value
                if self.main_total > 62:
                    self.bonus = 35

            return(True)
        else:
            return(False)
            
    def game_over(self):
        return len(self.unscored_types()) == 0
        
        
if __name__ == "__main__":
    s = ScorePad()
    print(s.unscored_types())
    s.take_score('main_6', 24)
    s.take_score('full_house', 25)
    print(s.unscored_types())
    print(s.scores)
    print(s.as_observation())
    print(len(const.SCORE_TYPES))
    print(len(s.as_observation()))