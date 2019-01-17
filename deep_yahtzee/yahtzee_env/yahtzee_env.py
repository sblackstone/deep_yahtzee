import gym
import numpy as np
import sys

from scorepad import scorepad
from dice     import dice
from gym import spaces

MAX_MONTHS=5
DEFAULT_CASH=1e5
    
      
class YahtzeeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):        
        self.action_space      = spaces.Tuple((spaces.Discrete(1), 
                                               spaces.Discrete(1), 
                                               spaces.Discrete(1), 
                                               spaces.Discrete(1), 
                                               spaces.Discrete(1),
                                               spaces.Discrete(10)))

        self.observation_space = spaces.Tuple((spaces.Discrete(2), spaces.Discrete(3)))


        pass
        # Setup Action Space
        # Setup Observation Space
                                           
    def seed(self, seed=None):
        pass

    def step(self, action):
        reward, done = self.take_action(action)
        return self.observe(), reward, done, {}

    def take_action(self, action):
        return 10, false

    def calc_reward(self, action): 
         reward = 10.0             
         return(reward)

    def reset(self):
        # Reset VArs
        # Set current observation and return it.
        self.scorepad = ScorePad()
        self.dice     = Dice()
        return self.observe()
    
    def observe(self):
        obs = list(self.dice.as_observation(), self.scorepad.as_observation())
        pass
        
    def render(self, mode='human'):
      print("HI")
      pass
