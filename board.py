import numpy as np

class Board:
    def __init__(self, dim = (6,7), adjacent = 4):
        self.board = np.zeros(dim, dtype=np.int8)
        self.adjacent = adjacent

    # play in the nth column, playerID = {1, 2}
    # errors if it's an invalid move
    def play(self, n, playerID):
        if n < 0 or n >= self.board.shape[1]:
            raise ValueError('column number is invalid')
        row = int(min(np.argwhere(np.equal(0, self.board[:, n]))))
        if row < self.board.shape[0]: # we can put another one in
            self.board[row, n] = playerID
            return 0
        else:
            raise ValueError('column is full, can\'t put something there')

    # check if a player has won
    # return the lowest ID of the player with # adjacent in a row
    def evaluate(self):
        lines = list(self.board) + list(self.board.T)
        for diagOffset in range(-self.board.shape[0],self.board.shape[1]):
            lines.append(np.diagonal(self.board, offset=diagOffset))
        for playerID in [1,2]:
            run = ','.join(map(str, np.repeat(playerID, self.adjacent)))
            for line in lines:
                line = ','.join(map(str, line))
                if run in line:
                    return playerID
        return 0

    def __repr__(self):
        board = "---\t"*7 + "\n"
        board += "1\t2\t3\t4\t5\t6\t7\n"
        for i in self.board:
            line = ""
            for j in i:
                if j == 0:
                    checker = "-"
                elif j == 1:
                    checker = "x"
                elif j == 2:
                    checker = "o"
                else:
                    checker = " "
                line += checker + "\t"
            board = line + "\n" + board
        return board
