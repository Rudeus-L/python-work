from game_structure import tic_tac_toe

# Start game and ask for restart after game over
def start_game():
    while True:
        print("=== Tic-Tac-Toe game start! ===")
        print()
        tic_tac_toe()
        print()
        choice = input("Do you want to restart? Please enter 'restart' to play again, or any other key to exit the game:")
        if choice.lower() != "restart":
            print("Game over! Thanks for playing!")
            break

if __name__ == "__main__":
    start_game()