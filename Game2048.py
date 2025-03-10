import random
import copy

def initialize_board():
    """Initialize a 4x4 board with two random tiles set to 2, and the rest as 0."""
    board = [[0] * 4 for _ in range(4)]
    board = add_new_tile(board)
    board = add_new_tile(board)
    return board

def print_board(board):
    """Print the board in a formatted style."""
    print("-" * 25)
    for row in board:
        print("|", end="")
        for num in row:
            cell = f"{num}" if num != 0 else " "
            print(f"{cell:^4}|", end="")
        print("\n" + "-" * 25)

def add_new_tile(board):
    """Place a new tile (with the value 2) at a random empty position on the board."""
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if not empty_cells:
        return board
    i, j = random.choice(empty_cells)
    board[i][j] = 2
    return board

def move_row_left(row):
    """Slide a row to the left and merge adjacent tiles with the same number."""
    # Remove zeros from the row.
    new_row = [num for num in row if num != 0]
    merged_row = []
    skip = False
    i = 0
    while i < len(new_row):
        if skip:
            skip = False
            i += 1
            continue
        # Merge with the next tile if they are the same.
        if i + 1 < len(new_row) and new_row[i] == new_row[i+1]:
            merged_row.append(new_row[i] * 2)
            skip = True
        else:
            merged_row.append(new_row[i])
        i += 1
    # Append zeros to fill the row back to length 4.
    merged_row += [0] * (4 - len(merged_row))
    return merged_row

def move_left(board):
    """Move all tiles on the board to the left."""
    new_board = []
    for row in board:
        new_board.append(move_row_left(row))
    return new_board

def move_right(board):
    """Move all tiles to the right by reversing each row, moving left, then reversing back."""
    new_board = []
    for row in board:
        reversed_row = row[::-1]
        new_reversed = move_row_left(reversed_row)
        new_board.append(new_reversed[::-1])
    return new_board

def transpose(board):
    """Transpose the board (swap rows and columns)."""
    return [list(row) for row in zip(*board)]

def move_up(board):
    """Move all tiles up by transposing, moving left, and transposing back."""
    transposed = transpose(board)
    moved = move_left(transposed)
    return transpose(moved)

def move_down(board):
    """Move all tiles down by transposing, moving right, and transposing back."""
    transposed = transpose(board)
    moved = move_right(transposed)
    return transpose(moved)

def move(board, direction):
    """
    Move the board in the given direction:
    'w' -> Up, 's' -> Down, 'a' -> Left, 'd' -> Right.
    """
    if direction == 'w':
        return move_up(board)
    elif direction == 's':
        return move_down(board)
    elif direction == 'a':
        return move_left(board)
    elif direction == 'd':
        return move_right(board)
    else:
        raise ValueError("Invalid move direction. Please enter 'w', 'a', 's', or 'd'.")

def check_win(board):
    """Check if any tile has reached 2048."""
    for row in board:
        if 2048 in row:
            return True
    return False

def check_game_over(board):
    """
    Check if the game is over:
    The game ends if there are no empty cells and no adjacent tiles that can be merged.
    """
    # If there is any empty cell, the game is not over.
    for row in board:
        if 0 in row:
            return False
    # Check for possible merges in rows and columns.
    for i in range(4):
        for j in range(4):
            if i < 3 and board[i][j] == board[i+1][j]:
                return False
            if j < 3 and board[i][j] == board[i][j+1]:
                return False
    return True
