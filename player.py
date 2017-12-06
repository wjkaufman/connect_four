from ConnectFour import *

class Player:
    
    checker = ["x", "o"]
    
    def __init__(self, id, isHuman, game):
        self.id = id
        self.isHuman = isHuman
        self.game = game
    
    def play(self):
        if self.isHuman:
            print("Player {}, make a move:".format(self.id))
            print(self.game.board)
            playerInput = raw_input("column: ")
            if playerInput == 'q':
                self.game.stop()
            elif playerInput.isdigit():
                try:
                    self.game.board.play(int(playerInput) - 1, self.id)
                except:
                    print("Invalid move, please try again")
                    self.play()
            else:
                print("Invalid input, please try again")
                self.play()
        else:
            # do some fancy AI trick
            return 0
    
    def __repr__(self):
        if self.id == 1:
            return checker[0]
        else:
            return checker[1]
