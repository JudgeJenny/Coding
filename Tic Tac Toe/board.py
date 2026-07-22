class Board():
    """ Create a class to make the game board, manipulate it, and check for a win """
    
    def __init__(self):
        """ Set up the values of the squares the players will put X's or O's.
            Begins with an empty set because the game board begins empty. """
        self.squares = {
            "A1": " ",
            "A2": " ",
            "A3": " ",
            "B1": " ",
            "B2": " ",
            "B3": " ",
            "C1": " ",
            "C2": " ",
            "C3": " "
        }

    def check_win(self):
        """ Check if there's a win either across, down or diagonal. """
        win = False
        if self.squares["A1"] == self.squares["A2"] == self.squares["A3"] and self.squares["A1"] != " ":
            win = True
        elif self.squares["B1"] == self.squares["B2"] == self.squares["B3"] and self.squares["B1"] != " ":
            win = True
        elif self.squares["C1"] == self.squares["C2"] == self.squares["C3"] and self.squares["C1"] != " ":
            win = True
        elif self.squares["A1"] == self.squares["B1"] == self.squares["C1"] and self.squares["A1"] != " ":
            win = True
        elif self.squares["A2"] == self.squares["B2"] == self.squares["C2"] and self.squares["A2"] != " ":
            win = True
        elif self.squares["A3"] == self.squares["B3"] == self.squares["C3"] and self.squares["A3"] != " ":
            win = True
        elif self.squares["A1"] == self.squares["B2"] == self.squares["C3"] and self.squares["A1"] != " ":
            win = True
        elif self.squares["A3"] == self.squares["B2"] == self.squares["C1"] and self.squares["A3"] != " ":
            win = True
        return win
        
    def display_board(self):
        """ Displays the game board with each X/O that has been entered. """
        print(
            "\n   A   B   C \n" \
            f"1  {self.squares['A1']} | {self.squares['B1']} | {self.squares['C1']} \n" \
            "  ---+---+---\n" \
            f"2  {self.squares['A2']} | {self.squares['B2']} | {self.squares['C2']} \n" \
            "  ---+---+---\n" \
            f"3  {self.squares['A3']} | {self.squares['B3']} | {self.squares['C3']} \n" \
        )
    
    def check_valid_position(self, position):
        """ Checks the entered position matches the dictionary name and does not already have a value. """
        valid = False
        if position in self.squares.keys():
            if self.squares[position] == " ":
                valid = True
        return valid
        
        
