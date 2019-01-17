
SCORE_TYPES = ['main_1', 'main_2', 'main_3', 'main_4', 'main_5', 'main_6', 'three_of_a_kind', 'four_of_a_kind', 'full_house', 'small_straight', 'large_straight', 'chance', 'yahtzee' ]

class ScorePad:
    def __init__(self):
        self.reset()

    def reset(self):
        self.scores = {}
    
    def unscored_types(self):
        return [x for x in SCORE_TYPES if not x in self.scores.keys()]
    
    def take_score(self, type, value):
        if not type in self.unscored_types():
            raise Exception('Score Already Taken') 
        self.scores[type] = value
        
if __name__ == "__main__":
    s = ScorePad()
    print(s.unscored_types())
    s.take_score('main_6', 24)
    s.take_score('full_house', 25)
    print(s.unscored_types())
    print(s.scores)
