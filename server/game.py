import player
import board as b

class Game:
    def __init__(self, name, score):
        self.players = []
        self.board = Board()
        turn = 0
    
    def add(player):
        self.players.append(player)

    def remove(player):
        self.players.remove(player)

    def start(self):
        pass

    def play(self):
        pass
        turn = (turn + 1) % len(self.players)

    
