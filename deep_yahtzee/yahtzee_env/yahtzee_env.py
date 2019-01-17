import gym
import numpy as np
import sys

MAX_MONTHS=5
DEFAULT_CASH=1e5
    
      
class YahtzeeGym(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):        
        # Setup Action Space
        # Setup Observation Space
                                           
    def seed(self, seed=None):
        pass

    def step(self, action):
        reward, done = self.take_action(action)
        return self.obs, reward, done, {}

    def take_action(self, action):
        return 10, false

    def calc_reward(self, action): 
         reward = 10.0             
         return(reward)

    def reset(self):
        # Reset VArs
        # Set current observation and return it.
        self.obs = [1,2,3]           
        return self.obs

    def render(self, mode='human'):
      print("HI")
      pass
