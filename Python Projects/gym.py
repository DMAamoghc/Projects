import gym
env = gym.make('FrozenLake-v0')
# env.reset()
# env.render()
# print(env.action_space)
env,reset()
for _ in range(10):
    obs, rew, done, info = env.step(env.action_space.sample())
    env.render()
    if rew == 1:
        print("WINNER")
    if done:
        break