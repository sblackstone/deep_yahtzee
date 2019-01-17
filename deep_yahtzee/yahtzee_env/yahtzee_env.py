import gym
from gym import spaces
from gym import wrappers

import numpy as np
import sys

from scorepad import ScorePad
from dice     import Dice

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
ROLL_DICE            = 13

SCORE_TYPES = ['main_1', 'main_2', 'main_3', 'main_4', 'main_5', 'main_6', 'three_of_a_kind', 'four_of_a_kind', 'full_house', 'small_straight', 'large_straight', 'chance', 'yahtzee' ]


class YahtzeeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):        
        self.scorepad          = ScorePad()
        self.dice              = Dice()
        self.action_space      = spaces.Tuple([spaces.Discrete(2), 
                                               spaces.Discrete(2), 
                                               spaces.Discrete(2), 
                                               spaces.Discrete(2), 
                                               spaces.Discrete(2),
                                               spaces.Discrete(14)])

        self.observation_space = spaces.Box(low=np.array([1.0, 1.0, 1.0, 1.0, 1.0,  # Dice
                                                  0, #rolls left
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
                                                  400.0, # Score                                                                                            
                                                  100 #step count
                                              ]), dtype=np.float32)

                                           
    def seed(self, seed=None):
        pass

    def step(self, action):
        self.take_action(action)
        return self.observe(), self.scorepad.total - self.step_count, self.scorepad.game_over(), {}


    def take_action(self, action):
        self.step_count += 1
        #print(action)
        action_id = action[5]
        print("Action_id = {}".format(action_id))
        if action_id == ROLL_DICE:
            print("Rolling")
            self.dice.roll(action[0:5])
        else:
            key = SCORE_TYPES[action_id]
            classifications = self.dice.classifications()
            if key in classifications:
                print("Trying to take {}".format(key))
                if self.scorepad.take_score(key, classifications[key]):
                    print("SUCCESS!")
                    self.dice.reset()

    def reset(self):
        # Reset VArs
        # Set current observation and return it.
        print("Resetting")
        self.scorepad.reset()
        self.dice.reset()
        self.step_count = 0
        return self.observe()
    
    def observe(self):
        obs = self.dice.as_observation() + self.scorepad.as_observation() + [  self.step_count ]
        return(obs)
        
    def render(self, mode='human'):
      print("HI")
      pass
