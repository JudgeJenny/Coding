from player import Player
from board import Board

input("Welcome to Tic Tac Toe! Press enter to set up your players. ")

##############################################
# Player set up

print("\n---Player 1 set up---")

# Name and validation
player_1_name = input("What is player 1's name? (max 20 characters) ").strip()
while len(player_1_name) >= 20:
    player_1_name = input("That's not valid. Please choose a name using 20 characters or less. ").strip()

# Symbol and validation
player_1_symbol = input(f"Hey {player_1_name}! Choose your one-character symbol. We recommend X or O. ").strip()
while len(player_1_symbol) != 1:
    player_1_symbol = input("That's not valid. Please choose only one character as your symbol: ").strip()

# Instantiate and set player 1 to go first
player1 = Player(player_1_name, player_1_symbol)
player1.go_first = True
print(f"Awesome, welcome {player1.name}! Your symbol is {player1.symbol}.")

print("\n---Player 2 set up---")

# Name and validation
player_2_name = input("What is player 2's name? (max 50 characters) ").strip()
while len(player_2_name) >= 50:
    player_2_name = input("That's not valid. Please choose a name using 50 characters or less. ").strip()

# Symbol and validation
player_2_symbol = input(f"Hey {player_2_name}! Choose your one-character symbol. We recommend X or O. ").strip()
while len(player_2_symbol) != 1 or player_1_symbol == player_2_symbol:
    player_2_symbol = input("That's not valid. Please choose only one unique character as your symbol: ").strip()

# Instantiate
player2 = Player(player_2_name, player_2_symbol)
print(f"Awesome, welcome {player2.name}! Your symbol is {player2.symbol}.")

print(f"\nPlayer 1 always goes first. You're up, {player1.name}.\n")

##################################
# Gameplay

# Set initial variables to keep playing, alternating turns, and calculations for a later table.
keep_playing = True
turn_order = [0,1,0,1,0,1,0,1,0]
name_length = max(len(player1.name), len(player2.name))

while keep_playing == True:

    # Initiate a new board, show the blank board, and reset which turn we're on
    board = Board()
    board.display_board()
    turn_number = 0

    # Logic to alternate who goes first depending on results of previous game.
    if player1.go_first == True:
        players = [player1, player2]
    elif player2.go_first == True:
        players = [player2, player1]

    # Game machine. This depends on which player is going first and alternates.
    for turn in turn_order:

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
            players[turn_order[turn_number - 1]].go_first = True
            players[turn_order[turn_number - 1]].loses += 1
            print(f"{players[turn].name} wins!\n")
            break
        
        # Count which turn we are on. If no winner at 9 turns, it's a draw. No winner.
        turn_number += 1
        if turn_number == 9:
            print("It's a draw.\n")

    # Display the scoreboard
    print("The current score is: \n")
    print(f"{'Player':<{max(6, name_length)}} | {'Wins':<5} | {'Loses':<5}")
    print("-" * 23)
    print(f"{player1.name:<{max(6, name_length)}} | {player1.wins:<5} | {player1.loses} \n"
          f"{player2.name:<{max(6, name_length)}} | {player2.wins:<5} | {player2.loses} \n")

    # Determine if players want to play another round
    play_again = input("Would you like to play again? (Y/N) ").strip().lower()
    while play_again not in ["y", "n"]:
        play_again = input("That's not a valid input. Would you like to play again? (Y/N) ").strip().lower()
    if play_again == "y":
        if player1.go_first == True:
            print(f"You got it! {player1.name}, you're up first.")
        elif player2.go_first == True:
            print(f"You got it! {player2.name}, you're up first.")
    elif play_again == "n":
        print("No problem, see you next time!")
        keep_playing = False

    