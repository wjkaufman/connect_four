from Board import *
from Player import *

class Game:
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.board = Board((6,7), 4)
        self.p1 = Player(1, True, self)
        self.p2 = Player(2, True, self)
        self.status = 0
    
    def getState(self, playerID):
        """
        Get the current board state, but from the perspective of
        the current player. So if it's player 2, then reverse it
        so 1-->2 and 2-->1 (easier to train, more data).
        """
        return self.board.get(playerID)
        
    
    def play(self, playerID, col):
        """
        Play the game by placing a checker in one of the columns
        as either player 1 or 2. Doing so will return the next
        state of the board, as well as the reward and whether the
        game is done or not.
        """
        try:
            self.board.play(col, playerID)
            r = (1 if playerID == self.board.evaluate() else
                0 if self.board.evaluate() is None else
                -1)
            s1 = self.board.get(playerID)
            d = True if self.board.evaluate() is not None else False
            return r, s1, d
        except ValueError:
            # do something probably
            pass
    
    def start(self):
        currPlayer = 1
        try:
            while self.board.evaluate() is None and self.status == 0:
                if currPlayer == 1:
                    self.p1.play()
                    currPlayer = 2
                else:
                    self.p2.play()
                    currPlayer = 1
        except KeyboardInterrupt:
            print('Game interrupted, stopping now')
        if self.board.evaluate() is None:
            print('Game is over, but no winner')
        else:
            print("Player {} wins".format(self.board.evaluate()))
    
    def stop(self):
        self.status = -1
