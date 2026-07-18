def updateBoard(grid):

    # Update the board based on the new grid

    board = \
    "   A   B   C \n" \
    f"1  {grid[0][0]} | {grid[0][1]} | {grid[0][2]} \n" \
    "  ---+---+---\n" \
    f"2  {grid[1][0]} | {grid[1][1]} | {grid[1][2]} \n" \
     "  ---+---+---\n" \
    f"3  {grid[2][0]} | {grid[2][1]} | {grid[2][2]} \n"

    return board

def getLocation(coordinate):
    location = ["", ""]
    if coordinate[0] == "A":
        location[1] = 0
    elif coordinate[0] == "B":
        location[1] = 1
    elif coordinate[0] == "C":
        location[1] = 2
    if coordinate[1] == "1":
        location[0] = 0
    elif coordinate[1] == "2":
        location[0] = 1
    elif coordinate[1] == "3":
        location[0] = 2

    return location

def updateGrid(coordinate, grid, turn):

    # Update the grid based on where the player would like to make their move

    location = getLocation(coordinate)

    if turn % 2 == 0:
        grid[location[0]][location[1]] = 'X'
    else: grid[location[0]][location[1]] = 'O'

    return grid

def checkCoordinate(grid, coordinate):
    #Check that a valid coordinate was entered and that it is a blank space.
    if len(coordinate) == 2:
        if coordinate[0] == "A" or coordinate[0] == "B" or coordinate[0] == "C":
            if coordinate[1] == "1" or coordinate[1] == "2" or coordinate[1] == "3":
                location = getLocation(coordinate)
                if grid[location[0]][location[1]] == " ":
                    validCoordinate = True
                else: 
                    validCoordinate = False
            else:
                validCoordinate = False
        else: 
            validCoordinate = False
    else:
        validCoordinate = False

    return validCoordinate
        
def player1Win(player1, player1Wins, win):
    print(f"{player1} wins!")
    player1Wins += 1
    win = True
    return player1Wins, win

def player2Win(player2, player2Wins, win):
    print(f"{player2} wins!")
    player2Wins += 1
    win = True
    return player2Wins, win

def checkWin(grid, win, player1Wins, player2Wins, player1, player2):
    # Check for top row
    if (grid[0][0] == "X" or grid[0][0] == "O") and grid[0][0] == grid[0][1] == grid[0][2]:
        if grid[0][0] == "X":
            player1Wins, win = player1Win(player1, player1Wins, win)
        else:
            player2Wins, win = player2Win(player2, player2Wins, win)

    # Check for middle row
    elif (grid[1][0] == "X" or grid[1][0] == "O") and grid[1][0] == grid[1][1] == grid[1][2]:
        if grid[1][0] == "X":
            player1Wins, win = player1Win(player1, player1Wins, win)
        else:
            player2Wins, win = player2Win(player2, player2Wins, win)

    # Check for last row
    elif (grid[2][0] == "X" or grid[2][0] == "O") and grid[2][0] == grid[2][1] == grid[2][2]:
        if grid[2][0] == "X":
            player1Wins, win = player1Win(player1, player1Wins, win)
        else:
            player2Wins, win = player2Win(player2, player2Wins, win)

    # Check for first column
    elif (grid[0][0] == "X" or grid[0][0] == "O") and grid[0][0] == grid[1][0] == grid[2][0]:
        if grid[0][0] == "X":
            player1Wins, win = player1Win(player1, player1Wins, win)
        else:
            player2Wins, win = player2Win(player2, player2Wins, win)

    # Check for middle column
    elif (grid[0][1] == "X" or grid[0][1] == "O") and grid[0][1] == grid[1][1] == grid[2][1]:
        if grid[0][1] == "X":
            player1Wins, win = player1Win(player1, player1Wins, win)
        else:
            player2Wins, win = player2Win(player2, player2Wins, win)

    # Check for last column
    elif (grid[0][2] == "X" or grid[0][2] == "O") and grid[0][2] == grid[1][2] == grid[2][2]:
        if grid[0][2] == "X":
            player1Wins, win = player1Win(player1, player1Wins, win)
        else:
            player2Wins, win = player2Win(player2, player2Wins, win)

    # Check for first diagonal
    elif (grid[0][0] == "X" or grid[0][0] == "O") and grid[0][0] == grid[1][1] == grid[2][2]:
        if grid[0][0] == "X":
            player1Wins, win = player1Win(player1, player1Wins, win)
        else:
            player2Wins, win = player2Win(player2, player2Wins, win)

    # Check for first diagonal
    elif (grid[0][2] == "X" or grid[0][2] == "O") and grid[0][2] == grid[1][1] == grid[2][0]:
        if grid[0][2] == "X":
            player1Wins, win = player1Win(player1, player1Wins, win)
        else:
            player2Wins, win = player2Win(player2, player2Wins, win)

    else:
        win = False
    
    return win, player1Wins, player2Wins

def rules():
    # Function that explains the rules of the game to the players.
    print("Two players will enter their names and take terms placing an X or O in the grid. \n" \
    "Player 1 is X and goes first on the first game. \n" \
    "Player 2 is O and goes second on the first game. \n" \
    "From there, players will always alternate turns. Loser goes first on the next game. \n" \
    "Indicate using the coordinates which square you would like to place your next move. \n")
    
    # Make sure there's a clear version of the grid
    grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
    ]
    
    # Make sure there's a clear version of the board
    board =  \
    "   A   B   C \n" \
    f"1  {grid[0][0]} | {grid[0][1]} | {grid[0][2]} \n" \
    "  ---+---+---\n" \
    f"2  {grid[1][0]} | {grid[1][1]} | {grid[1][2]} \n" \
     "  ---+---+---\n" \
    f"3  {grid[2][0]} | {grid[2][1]} | {grid[2][2]} \n"
    print(board)
    
    print("For example, when prompted for your move you may enter 'C1' to mark the top right square. \n")
    grid[0][2] = 'X'
    board = updateBoard(grid)
    print(board)
    grid[0][2] = ' '
    board = updateBoard(grid)
    print("Keep taking turns until some gets three in a row in a row, column, or diagonal, then choose if you want to play again! \n")