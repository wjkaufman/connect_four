from board import *
from player import *

class Game:
    
    def __init__(self):
        self.board = Board((6,7), 4)
        self.p1 = Player(1, True, self)
        self.p2 = Player(2, True, self)
        self.status = 0
    
    def start(self):
        currPlayer = 1
        try:
            while self.board.evaluate() == 0 and self.status == 0:
                if currPlayer == 1:
                    self.p1.play()
                    currPlayer = 2
                else:
                    self.p2.play()
                    currPlayer = 1
        except KeyboardInterrupt:
            print('Game interrupted, stopping now')
        if self.board.evaluate() is 0:
            print('Game is over, but no winner')
        else:
            print("Player {} wins".format(self.board.evaluate()))
    
    def stop(self):
        self.status = -1
