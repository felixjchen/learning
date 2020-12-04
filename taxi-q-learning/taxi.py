import gym
import random
import pickle
from IPython.display import clear_output
import numpy as np
# https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/

env = gym.make("Taxi-v3").env

# (taxi row, taxi column, passenger index, destination index)
# state = env.encode(0, 1, 0, 0)
# print("State:", state)
# env.s = 1
# env.render()

# env.render()

# print("Action Space {}".format(env.action_space))
# print("State Space {}".format(env.observation_space))

# 500 x 6 q table
q_table = np.zeros([env.observation_space.n, env.action_space.n])

def train():
    # Q(state, action) = (1-a)Q(state,action) + a(reward + g*max(Q(next state, all actions)))
    # 0 < a <= 1 learning rate, how much our q value is being udpated every iteration
    alpha = 0.1
    # 0 <= g <= 1 discount factor, how much importance given to future rewards, higher captures the long term effective award, lower is greedier
    gamma = 0.6
    # 0 <= eps <= 1 exploration or exploit
    epsilon = 1

    for i in range(1, 100001):
        state = env.reset()

        done = False

        while not done:
            
            # Actions 1...6, random action or explot q_table at this state
            if random.uniform(0,1) < epsilon:
                action = env.action_space.sample() 
            else:
                action = np.argmax(q_table[state])

            next_state, reward, done, info = env.step(action)
            # Q(state, action) = (1-a)Q(state,action) + a(reward + g*max(Q(next state, all actions)))
            q_table[state, action] = (1-alpha) * q_table[state, action] + alpha*(reward + gamma * np.max(q_table[next_state]))

            state = next_state

        if i % 100 == 0:
            clear_output(wait=True)
            print(f"Episode: {i}")



def test():
    total_epochs, total_penalties = 0, 0
    episodes = 1000

    for _ in range(episodes):
        state = env.reset()
        epochs, penalties, reward = 0, 0, 0
        
        done = False
        
        while not done:
            # print(q_table)
            action = np.argmax(q_table[state])
            state, reward, done, info = env.step(action)

            if reward == -10:
                penalties += 1

            epochs += 1

        total_penalties += penalties
        total_epochs += epochs

    print(f"Results after {episodes} episodes:")
    print(f"Average timesteps per episode: {total_epochs / episodes}")
    print(f"Average penalties per episode: {total_penalties / episodes}")

def single_test():
    state = env.reset()
    done = False
    
    while not done:
        env.render()
        action = np.argmax(q_table[state])
        state, reward, done, info = env.step(action)

    

def save_q_table():
    with open('q_table.pkl', 'wb') as f:
        pickle.dump(q_table, f)

def read_q_table():
    global q_table
    with open('q_table.pkl', 'rb') as f:
        q_table = pickle.load(f)

read_q_table()
single_test()
# test()
# train()
# save_q_table()