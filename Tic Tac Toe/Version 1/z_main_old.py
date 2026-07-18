# Make a two player tic tac toe game. Easy, right?
# Let's make a board, take player input, and update the board until the win condition is met.

# To fix: alternate who goes first after every game

import numpy as np
from functions import *

# --------------------------------------------------
# S E T U P

# Let's set up a blank grid for our new game. First let's store the X's and O's in an easier to parse list.
grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

board =  \
    "   A   B   C \n" \
    f"1  {grid[0][0]} | {grid[0][1]} | {grid[0][2]} \n" \
    "  ---+---+---\n" \
    f"2  {grid[1][0]} | {grid[1][1]} | {grid[1][2]} \n" \
     "  ---+---+---\n" \
    f"3  {grid[2][0]} | {grid[2][1]} | {grid[2][2]} \n"

# Set this boolean keepGoing to true as long as the game is playing with an exit to change to false at the end
keepPlaying = True

#Set initial win condition to False so the game will keep going
win = False

# Set the first turn number as 0, and the number of wins for each player as 0
turn = 0
player1Wins = 0
player2Wins = 0

# --------------------------------------------------
# T H E  G A M E

print("Welcome to Tic Tac Toe! \n------------------")
viewRules = input("Would you like to learn how to play? Enter 'yes' if so. Enter anything else to skip. ")

if viewRules == 'yes':
    rules()

# Grab the player names
player1 = input("Please enter a name for player 1: ")
player2 = input("Please enter a name for player 2: ")

# Begin the loop to keep playing until the players choose to exit 
while keepPlaying == True:

    # Set up the blank board and print it to start the game and show the players the grid
    grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
    ]

    print(updateBoard(grid))

    while win == False:

        # Reset the number of turns
        turn = 0

        # Keep taking turns while there are under 9 turns. At 9 turns, there are no more moves.
        while turn <= 8:
            if turn % 2 == 0:
                coordinate = input(f"You're up, {player1}. Where do you want to make your move? (eg. A1) ")
            else:
                coordinate = input(f"Your turn, {player2}. What's your move? (eg. A1) ")
            validCoordinate = False
            while validCoordinate == False:
                validCoordinate = checkCoordinate(grid, coordinate)
                if validCoordinate == False:
                    coordinate = input("That's not a valid move, try entering a coordinate again: ")
                else:
                    exit
            grid = updateGrid(coordinate, grid, turn)
            board = updateBoard(grid)
            print(board)
            win, player1Wins, player2Wins = checkWin(grid, win, player1Wins, player2Wins, player1, player2)
            turn += 1
        

        if turn == 9 and win == False:
            print("It's a draw. \n ----------------------------")
            # I know a draw is not a "win" but this will exit the while loop. Should be named gameOver = False
            win = True
    
    # Display the ongoing score for each player
    print("Here's the score \n" \
          f"{player1}: {player1Wins} \n" \
          f"{player2}: {player2Wins} \n"
          )
    
    # Play again logic - make sure user has inputted yes or no and then have the option to exit or start a new game.
    playAgain = input("Do you want to play again? (yes/no) ")
    while playAgain != "yes" and playAgain != "no":
        playAgain = input("Not sure what you mean, enter yes or no. ")
    if playAgain == "yes":
        win = False
    elif playAgain == "no":
        print("See you next time!")
        keepPlaying = False