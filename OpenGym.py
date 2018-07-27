import gym
env = gym.make('FrozenLake-v0')

env = gym.make('FrozenLake-v0')
print()

env.reset()
for _ in range(60):
    obs, rew,  done, info = env.step(2)  # random step taken (info)
    print("observation is")
    print(obs)
    print("reward is")
    print(rew)
    print("done is")
    print(done)
    print(info)
    print(obs)
    if done:
        break


print("action space is")
print("env.action_space")

env.render()









# k map&centroids
