import gym
env = gym.make('FrozenLake-v0')
print(env.action_space)
print(env.observation_space)

score = 0

for _ in range(1000):
    env.reset()
    # obs, rew, done, info = env.step(1)
    # obs, rew, done, info = env.step(1)
    # obs, rew, done, info = env.step(2)
    # obs, rew, done, info = env.step(2)
    # obs, rew, done, info = env.step(2)
    # obs, rew, done, info = env.step(1)
    # obs, rew, done, info = env.step(2)
    for _ in range(100):
        obs, rew, done, info = env.step(1)
        obs, rew, done, info = env.step(1)
        obs, rew, done, info = env.step(2)
        obs, rew, done, info = env.step(2)
        obs, rew, done, info = env.step(2)
        obs, rew, done, info = env.step(1)
        obs, rew, done, info = env.step(2)
        # 0 for left, down is 1, 2 is right
        # env.action_space.sample() makes random

        if done:
            score += rew

            break
print(score)