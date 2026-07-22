from game_controller import Game_Controller

input("Welcome to Tic Tac Toe! Press enter to set up your players. ")

if __name__ == "__main__":
    game = Game_Controller()
    game.play_game()