from player import Player
from board import Board

input("Welcome to Tic Tac Toe! Press enter to set up your players. ")

##############################################
# Player set up

print("\n---Player 1 set up---")
player_1_name = input("What is player 1's name? ").strip()
player1 = Player(player_1_name)
# Add while loop to confirm valid name

player_1_symbol = input(f"Hey {player1.name}! Choose your one-character symbol. We recommend X or O. ")
player1.symbol = player_1_symbol
# Add while loop to confirm valid symbol

print("\n---Player 2 set up---")
player_2_name = input("What is player 2's name? ").strip()
player2 = Player(player_2_name)
# Add while loop to confirm valid name

player_2_symbol = input(f"Hey {player2.name}! Choose your one-character symbol. We recommend X or O. ")
player2.symbol = player_2_symbol
# Add while loop to confirm valid symbol
# Add while loop to prevent player 1 and player 2 from having the same symbol

##################################
# Board set up

board = Board()
board.display_board()

turn = 1

while True:
    position = input(f"Alright {player1.name}, where do you want to make your move? ")
    while board.check_valid_position(position) == False:
        position = input("That's not a valid position, please try again: ").strip()
    board.squares[position] = player1.symbol
    if board.check_win() == True:
        break
    board.display_board()
    turn += 1

    position = input(f"Your turn, {player2.name}. Where would you like to go? ")
    while board.check_valid_position(position) == False:
        position = input("That's not a valid position, please try again: ").strip()
    board.squares[position] = player2.symbol
    if board.check_win() == True:
        break
    board.display_board()
    turn += 1

print("Game over")
