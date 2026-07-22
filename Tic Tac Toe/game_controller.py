from player import Player
from board import Board

class Game_Controller():

    def __init__(self):
        """ Start it up with two players. Difficulty to be a future feature when playing against an AI. """
        self.player1 = None
        self.player2 = None
        self.difficulty = None
        self.keep_playing = True
        self.turn_order = [0,1,0,1,0,1,0,1,0]

    def play_game(self):
        """ Starts and plays the game """
        self.game_setup()
        self.game()

    def game(self):
        """ The game machine """
        while self.keep_playing == True:

            # Initiate a new board, show the blank board, and reset which turn we're on
            board = Board()
            turn_number = 0

            # Logic to alternate who goes first depending on results of previous game.
            if self.player1.go_first == True:
                players = [self.player1, self.player2]
            elif self.player2.go_first == True:
                players = [self.player2, self.player1]

            # Set up the first move
            print(f"{players[0].name}, you're up first!")
            board.display_board()

            # Game machine. This depends on which player is going first and alternates.
            for turn in self.turn_order:

                # Player who is up chooses which box to place their symbol
                position = input(f"Alright {players[turn].name}, where do you want to make your move? ")
                while board.check_valid_position(position) == False: # Confirm valid entry
                    position = input("That's not a valid position, please try again: ").strip()
                board.squares[position] = players[turn].symbol # Places player's symbol in board location
                board.display_board()
                
                # Check for win conditions. If met, set win & loss count, and set who goes first next round.
                if board.check_win() == True:
                    players[turn].go_first = False
                    players[turn].wins += 1
                    players[self.turn_order[turn_number - 1]].go_first = True
                    players[self.turn_order[turn_number - 1]].loses += 1
                    print(f"{players[turn].name} wins!\n")
                    break
                
                # Count which turn we are on. If no winner at 9 turns, it's a draw. No winner.
                turn_number += 1
                if turn_number == 9:
                    print("It's a draw.\n")
            
            self.display_score()
            self.play_again()

    def play_again(self):
        """ Determines if a new game will begin """

        play_again = input("Would you like to play again? (Y/N) ").strip().lower()
        while play_again not in ["y", "n"]:
            play_again = input("That's not a valid input. Would you like to play again? (Y/N) ").strip().lower()
        if play_again == "n":
            print("No problem, see you next time!")
            self.keep_playing = False

    def display_score(self):
        """ Displays the scoreboard for the players """
        name_length = max(len(self.player1.name), len(self.player2.name))

        print("The current score is: \n")
        print(f"{'Player':<{max(6, name_length)}} | {'Wins':<5} | {'Loses':<5}")
        print("-" * 23)
        print(f"{self.player1.name:<{max(6, name_length)}} | {self.player1.wins:<5} | {self.player1.loses} \n"
              f"{self.player2.name:<{max(6, name_length)}} | {self.player2.wins:<5} | {self.player2.loses} \n")
    
    def game_setup(self):
        """ Set up both players """

        print(" === Player 1 setup === ")
        self.player1 = self.player_setup()
        self.player1.go_first = True

        print(" === Player 2 setup === ")
        self.player2 = self.player_setup(self.player1.symbol, self.player1.name)

    def player_setup(self, opponent_symbol = None, opponent_name = None):
        """ Players input their name and symbol to create their player """
        player_name = input("\nWhat is your name? (max 20 characters) ").strip()
        while len(player_name) >= 20 or player_name == opponent_name:
            player_name = input("That's not valid. Please choose a name using 20 characters or less. ").strip()

        # Symbol and validation
        player_symbol = input(f"Hey {player_name}! Choose your one-character symbol. We recommend X or O. ").strip()
        while len(player_symbol) != 1 or player_symbol == opponent_symbol:
            player_symbol = input("That's not valid. Please choose only one character as your symbol: ").strip()

        # Instantiate and set player 1 to go first
        self.player = Player(player_name, player_symbol)
        print(f"\nAwesome, welcome {self.player.name}! Your symbol is {self.player.symbol}.\n================================================\n")

        return self.player
    
