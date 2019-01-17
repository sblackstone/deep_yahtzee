#!/usr/bin/env python3.6

import numpy as np
import yahtzee_env
import sys
from tensorforce.execution import Runner
from tensorforce.contrib.openai_gym import OpenAIGym
from agent import create_agent

environment = OpenAIGym('YahtzeeEnv-v0', visualize=False)
environment.gym.reset()
#sys.exit()


agent       = create_agent(environment=environment)
runner      = Runner(agent=agent, environment=environment)


def episode_finished(r):
    if runner.episode % 50 == 0:
      print("Total episodes: {ep}. Average reward of last 1000 episodes: {ar}.".format(
        ep=runner.episode,
        ar=np.mean(runner.episode_rewards[-50:]))
        )   
    print
    return True


runner.run(episodes=10000, max_episode_timesteps=200, episode_finished=episode_finished)
runner.close()

print("Learning finished. Total episodes: {ep}. Average reward of last 100 episodes: {ar}.".format(
    ep=runner.episode,
    ar=round(np.mean(runner.episode_rewards[-100:])))
)

