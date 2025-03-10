from Game2048 import (
    initialize_board, print_board, add_new_tile,
    move, check_win, check_game_over
)
import copy

def main():
    board = initialize_board()
    while True:
        print_board(board)
        
        # Check if the win condition is met.
        if check_win(board):
            print("Congratulations, you've reached 2048! You win!")
            choice = input("Enter 'r' to restart or 'q' to quit: ").strip().lower()
            if choice == 'r':
                board = initialize_board()
                continue
            elif choice == 'q':
                break
        
        # Check if there are no more valid moves.
        if check_game_over(board):
            print("Game over! No more valid moves available.")
            choice = input("Enter 'r' to restart or 'q' to quit: ").strip().lower()
            if choice == 'r':
                board = initialize_board()
                continue
            elif choice == 'q':
                break
        
        # Get user input and handle any invalid inputs.
        try:
            user_input = input("Enter move direction (w=up, s=down, a=left, d=right): ").strip().lower()
            if user_input not in ['w', 'a', 's', 'd']:
                raise ValueError("Invalid input")
        except ValueError as e:
            print("Error: Please enter 'w', 'a', 's', or 'd'.")
            continue
        
        # Use a deep copy to verify if the move changes the board state.
        board_copy = copy.deepcopy(board)
        try:
            new_board = move(board_copy, user_input)
        except Exception as e:
            print("Error during move:", e)
            continue
        
        if new_board == board:
            print("No tiles moved in that direction. Please try a different move.")
            continue
        else:
            board = new_board
            board = add_new_tile(board)

if __name__ == "__main__":
    main()
    
# GitHub: Please push your code to your GitHub account and include your GitHub link here.
# Example: # GitHub: https://github.com/yourusername/2048-game
