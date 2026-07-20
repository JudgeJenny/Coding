class Player:
    """ Create a player with stored name and symbol for the board.
        Keeps track of player wins. """
    
    def __init__(self, name, symbol):
        """ Construct with the player's inputted name and symbol.
            Also stores number of wins and whether the player will go first in the next game. """
        self.name = name
        self.symbol = symbol
        self.wins = 0
        self.loses = 0
        self.go_first = False