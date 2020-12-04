import numpy as np

from minesweeper import Minesweeper

from neural_network import NeuralNetwork
from loss_function import CrossEntropy, Quadratic
from activation_function import *

np.random.seed(0)


class DQN():

    def __init__(self, size, mines, reward_profile, alpha=0.2, gamma=0.1, epsilon=0.1):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

        self.reward_profile = reward_profile

        self.env = Minesweeper(size, mines, reward_profile)
        self.q_model = NeuralNetwork(
            size=[self.env.numMoves, 30, 30, self.env.numMoves],
            activation=[ReLU6(), ReLU6(), Linear()],
            loss=Quadratic(),
            regression=True)

    def train(self, episodes=100):
        alpha = self.alpha
        gamma = self.gamma
        epsilon = self.epsilon
        env = self.env
        q_model = self.q_model

        wins = 0

        for e in range(episodes):

            state = env.newGame()
            episodeDone = False
            while not episodeDone:
                if np.random.uniform(0, 1) < epsilon:
                    action = np.random.randint(0, env.numMoves)
                else:
                    action = q_model.predict(state)[0]

                newState, reward, episodeDone = env.move(action)

                oldActivations = q_model.feedforward(state)
                oldReward = oldActivations[0][action]
                nextMax = np.max(q_model.feedforward(newState))

                update = (1-alpha) * oldReward + \
                    alpha * (reward + gamma*nextMax)
                oldActivations[0][action] = update

                train_X = state[None, :]
                train_y = oldActivations

                q_model.SGD(train_X, train_y, batch_percent=1)

            print(self.test())

    def test(self, trials=100):

        env = self.env
        q_model = self.q_model
        reward_profile = self.reward_profile

        wins = 0
        penalties = 0
        instantLoses = 0
        for _ in range(trials):
            state = env.newGame()
            done = False
            moves = 0
            while not done:
                # print(env)
                action = q_model.predict(state)[0]
                newState, reward, done = env.move(action)

                # Repeat action autofail
                if (state == newState).all():
                    reward = -999
                    penalties += 1
                    done = True

                # First turn lose
                if done and moves == 0 and reward == reward_profile['lose']:
                    instantLoses += 1

                # Win
                if done and reward == reward_profile['win']:
                    wins += 1

                # print(env)
                moves += 1
                state = newState

        return wins / (trials - instantLoses) * 100, penalties

    def demo(self):
        env = self.env
        q_model = self.q_model

        state = env.newGame()
        done = False
        while not done:
            action = q_model.predict(state)[0]

            newState, reward, done = env.move(action)

            # Repeat action autofail
            if (state == newState).all():
                reward = -999
                done = True

            state = newState

            print(env)
            if done and reward > 0:
                print('WIN')
            elif done:
                print('LOSE')


if __name__ == "__main__":
    size = 3
    mines = 1
    reward_profile = {
        'sweep': 1,
        'resweep': -size,
        'win': size ** 2,
        'lose': -size ** 2
    }
    model = DQN(size, mines, reward_profile)
    model.train(100)
