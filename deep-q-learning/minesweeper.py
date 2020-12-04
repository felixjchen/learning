import numpy as np

MINE = -1
COVER = -2


class Minesweeper():

    def __init__(self, n, m, reward_profile):
        """
        An nxn minesweeper board with m mines

        n -- length of side
        m -- number of mines
        """
        self.size = n
        self.mines = m
        self.reward_profile = reward_profile

        # Largest number tile
        self.maxTile = min(m, 8)
        self.numStates = (3 + self.maxTile) ** (n ** 2)
        self.numMoves = n ** 2

        # Create game
        self.newGame()

    def newGame(self):
        """ Starts a new game of minesweeper """
        n = self.size
        m = self.mines

        self.covers = [[1 for _ in range(n)] for _ in range(n)]
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.squaresLeft = (n**2) - m

        # Place mines
        for i in np.random.choice(n**2, m, replace=False):
            self.board[i // n][i % n] = MINE

        # Paint numbers
        for i in range(n):
            for j in range(n):

                if self.board[i][j] != MINE:
                    count = 0

                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if 0 <= i + di <= n - 1 and 0 <= j + dj <= n-1:

                                if self.board[i+di][j+dj] == MINE:
                                    count += 1

                    self.board[i][j] = count

        return self.getState()

    def getState(self):
        n = self.size

        observed = np.zeros((n, n))

        for i in range(n):
            for j in range(n):
                if self.covers[i][j] == 1:
                    observed[i][j] = COVER
                else:
                    observed[i][j] = self.board[i][j]
        return observed.flatten()

    def move(self, action):
        """ 
        Takes action and returns new state number, reward and if the game is finished

        action -- uncover board at row (action//2) and column (action%2)
        """
        n = self.size
        reward_profile = self.reward_profile

        i, j = action // n, action % n

        # Already uncovered...
        if self.covers[i][j] == 0:
            # penalty for wasting time
            reward = reward_profile['resweep']
            done = False
        else:
            # Sweep
            self.covers[i][j] = 0

            # Lose
            if self.board[i][j] == MINE:
                reward = reward_profile['lose']
                done = True
            else:
                reward = reward_profile['sweep']
                done = False
                self.squaresLeft -= 1

                # Win
                if self.squaresLeft == 0:
                    reward = reward_profile['win']
                    done = True

        # New enumerated state, reward for move, game done
        return self.getState(), reward, done

    def __str__(self):
        """ Returns a str representation of the board """
        r = ''

        n = self.size

        for i in range(n):
            for j in range(n):
                if self.covers[i][j]:
                    r += 'X  '
                else:
                    t = str(self.board[i][j])
                    t = t+' ' if len(t) == 2 else t + '  '
                    r += f'{t}'
            r += '\n'
        return r


if __name__ == "__main__":
    n = 3
    m = 1
    reward_profile = {
        'sweep': 1,
        'resweep': -2,
        'win': n ** 2,
        'lose': -n ** 2
    }
    m = Minesweeper(3, 1, reward_profile)
    print('# of states:', m.numStates)

    print(m.getState())
    print(m.move(0))
    print(m.move(1))
    print(m.move(2))
    print(m.move(3))
    print(m.move(4))
    print(m.move(5))
    print(m.move(6))
    print(m.move(8))
