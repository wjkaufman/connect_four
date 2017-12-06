import numpy as np

class Board:
    def __init__(self, dim = (6,7), adjacent = 4):
        self.board = np.zeros(dim, dtype=np.int8)
        self.adjacent = adjacent
    
    def get(self, playerID):
        """
        Get a tensor representation of the board, whic would be
        row x col x 2 (for 2 players). First slice is for the
        current player (based on playerID), second slice is for
        opposing player
        """
        b = np.zeros([2, self.board.shape[0], self.board.shape[1]])
        b[0,:,:] = self.board == playerID
        b[1,:,:] = self.board == (1 if playerID is 2 else 2)
        return b
    
    def isFull(self):
        return not (self.board == 0).any()

    # play in the nth column, playerID = {1, 2}
    # errors if it's an invalid move
    def play(self, n, playerID):
        if n < 0 or n >= self.board.shape[1]:
            raise ValueError('column number is invalid')
        try:
            row = int(min(np.argwhere(np.equal(0, self.board[:, n]))))
            self.board[row, n] = playerID
            return
        except:
            raise ValueError('column is full, cannot put something there')

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
        return None

    def __repr__(self):
        board = "---\t"*self.board.shape[1] + "\n"
        board += "\t".join(map(str, [i+1 for i in range(self.board.shape[1])]))
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
