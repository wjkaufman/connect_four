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
        self.currPlayer = 1
        return self.board.get(1)
    
    def __str__(self):
        string = str(self.board)
        string += "\ncurrent player is " + str(self.currPlayer)
        return string
    
    def switchPlayer(self):
        if self.currPlayer is 1:
            self.currPlayer = 2
        else:
            self.currPlayer = 1
    
    def getState(self, currPlayer = True):
        """
        Get the current board state, but from the perspective of
        the current player. So if it's player 2, then reverse it
        so 1-->2 and 2-->1 (easier to train, more data).
        """
        playerID = (self.currPlayer if currPlayer else
                (1 if self.currPlayer is 2 else 2))
        return self.board.get(playerID)
    
    def isPlayable(self):
        return not self.board.isFull()
    
    def getWinner(self):
        return self.board.evaluate()
        
    
    def play(self, col):
        """
        Play the game by placing a checker in one of the columns
        as the player whose turn it is. Doing so will return the next
        state of the board, as well as the reward and whether the
        game is done or not.
        
        Args:
            col: the column to put a checker into
        
        Returns:
            s1: the next state of the board from the perspective
                of the player that just went
            r: the reward for the state/action pair
            d: boolean, whether the game is done or not
        """
        # try:
        self.board.play(col, self.currPlayer)
        evaluation = self.board.evaluate()
        r = (1 if self.currPlayer == evaluation else
            0 if evaluation is None else -1)
        s1 = self.board.get(self.currPlayer)
        d = True if self.board.evaluate() is not None else False
        self.switchPlayer()
        return s1, r, d
    
    def start(self):
        try:
            while self.board.evaluate() is None and self.status == 0:
                if self.currPlayer == 1:
                    self.p1.play()
                else:
                    self.p2.play()
                self.switchPlayer()
        except KeyboardInterrupt:
            print('Game interrupted, stopping now')
        if self.board.evaluate() is None:
            print('Game is over, but no winner')
        else:
            print("Player {} wins".format(self.board.evaluate()))
            print(self.board)
    
    def stop(self):
        self.status = -1
