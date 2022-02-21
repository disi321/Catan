import handler_manager

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.handler = get_handler_manager().get_auth_handler(self.name)

    def __str__(self):
        return "Player: " + self.name + " Score: " + str(self.score)

    def __repr__(self):
        return "Player: " + self.name + " Score: " + str(self.score)

    def __eq__(self, other):
        return self.name == other.name and self.score == other.score

    def __ne__(self, other):
        return self.name != other.name or self.score != other.score
        


