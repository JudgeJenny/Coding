class Player:
    def __init__(self, name):
        self.name = name
        self.symbol = ""
        self.wins = 0

    def update_symbol(self, symbol):
        self.symbol = symbol

    def show_wins(self):
        print(self.wins)