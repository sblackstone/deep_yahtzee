from gym.envs.registration import register

# This throws an error if run more than once..
# So we just deal with it.
try:
    register(
        id="YahtzeeEnv-v0",
        entry_point='yahtzee_env.yahtzee_env:YahtzeeEnv'
    )
except:
    print