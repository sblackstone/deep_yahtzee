import deep_yahtzee.constants as const
import gym
from gym import spaces
from gym import wrappers

import numpy as np
import sys

from scorepad import ScorePad
from dice     import Dice


class YahtzeeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):        
        self.scorepad          = ScorePad()
        self.dice              = Dice()
        self.episode_count     = 0
        self.top_score         = 0.0
        self.action_space      = spaces.Discrete(46)
        self.observation_space = spaces.Box(low=np.array([1.0, 1.0, 1.0, 1.0, 1.0,  # Dice
                                                  0, #rolls left
                                                  0, # Main 1...
                                                  0,
                                                  0,
                                                  0,
                                                  0,
                                                  0, # Main 6
                                                  0, # TOK
                                                  0, # FOK
                                                  0, # FH
                                                  0, # SS
                                                  0, # LS
                                                  0, # CHC
                                                  0, # Yahtzee
                                                 -1, # Main 1
                                                 -1, # Main 2
                                                 -1, # Main 3
                                                 -1, # Main 4
                                                 -1, # Main 5
                                                 -1, # Main 6
                                                 -1, # three_of_a_kind
                                                 -1, # four_of_a_kind
                                                 -1, # full_house
                                                 -1, # small_straight
                                                 -1, # large_straight
                                                 -1, # chance
                                                 -1, # yahtzee
                                                  0, # Score
                                                  0, # STEP COUNT
                                            ]),
                                            high=np.array([6.0, 6.0, 6.0, 6.0, 6.0, # Dice
                                                  3.0, # Rolls Left
                                                  5.0, # Main 1
                                                  10.0,# Main 2
                                                  15.0,# Main 3
                                                  20.0,# Main 4
                                                  25.0,# Main 5
                                                  30.0,# Main 6
                                                  30.0,#three of kind
                                                  30.0,#four of kind
                                                  25.0,#full house
                                                  30.0,#small straight
                                                  40.0,#large straight
                                                  30.0, #chance,
                                                  50.0, #Yahtzee
                                                  5.0, # Main 1
                                                  10.0,# Main 2
                                                  15.0,# Main 3
                                                  20.0,# Main 4
                                                  25.0,# Main 5
                                                  30.0,# Main 6
                                                  30.0,#three of kind
                                                  30.0,#four of kind
                                                  25.0,#full house
                                                  30.0,#small straight
                                                  40.0,#large straight
                                                  30.0, #chance,
                                                  50.0, #Yahtzee
                                                  400.0, # Score                                                                                            
                                                  100 #step count
                                              ]), dtype=np.float32)

                                           
    def seed(self, seed=None):
        pass

    def step(self, action):
        self.take_action(action)
        reward = self.calc_reward()
        #print("Reward = {}".format(reward))
        #print("*" * 50)
        #if self.scorepad.game_over():
        #    print("Gamee Over!")
        #    self.scorepad.dump()
        #    sys.exit()
        return self.observe(), self.calc_reward(), self.scorepad.game_over(), {}

    def calc_reward(self):
        return self.scorepad.score() + (3 - self.dice.rolls) - self.bad_move_count + ((self.scorepad.main_total / 63.0)*35)

    def take_action(self, action_id):
        self.step_count += 1
        #print("Action_id = {}".format(action_id))
        if action_id > 12:
            # We represent the pattern of which die to roll as the binary
            # representation of the action chosen.  They map to 0-31
            val = action_id - 13
            result = []
            while val > 0:
                result.append(val & 1)
                val = val >> 1
            while(len(result) < 5):
                result.append(0)                    
            #print("Roll Array: {}".format(result))
            if not self.dice.roll(result):
                self.bad_move_count += 1

        else:
            if self.dice.rolls == 3:
                self.bad_move_count += 1
                return

            if self.scorepad.take_score(action_id, self.dice.score_for_category(action_id)):
                #print("Took {}".format(action_id))
                #self.scorepad.dump()
                self.dice.reset()
            else:
                #print("Unable to take {}".format(key))
                self.bad_move_count += 1

    def reset(self):
        # Reset VArs
        # Set current observation and return it.
        if self.scorepad.score() > self.top_score:
            self.scorepad.dump()
            self.top_score = self.scorepad.score() 

        self.episode_count += 1 
        self.scorepad.reset()
        self.dice.reset()
        self.episode_count = 0
        self.step_count = 0
        self.bad_move_count = 0
        return self.observe()
    
    def observe(self):
        obs = self.dice.as_observation() + self.scorepad.as_observation() + [  self.step_count ]
        return(obs)
        
    def render(self, mode='human'):
      print("HI")
      pass
