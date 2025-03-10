import random
import copy

def initialize_board():
    """初始化4×4棋盘，填入两个随机的2，其余为0"""
    board = [[0] * 4 for _ in range(4)]
    board = add_new_tile(board)
    board = add_new_tile(board)
    return board

def print_board(board):
    """美化输出棋盘"""
    print("-" * 25)
    for row in board:
        # 每个数字占宽度4，不足的空格补充，0显示为空格
        print("|", end="")
        for num in row:
            cell = f"{num}" if num != 0 else " "
            print(f"{cell:^4}|", end="")
        print("\n" + "-" * 25)
        
def add_new_tile(board):
    """在空位置随机生成一个新的数字2"""
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if not empty_cells:
        return board
    i, j = random.choice(empty_cells)
    board[i][j] = 2
    return board

def move_row_left(row):
    """对一行数据进行左移，合并相邻相同数字"""
    # 去掉0
    new_row = [num for num in row if num != 0]
    merged_row = []
    skip = False
    i = 0
    while i < len(new_row):
        if skip:
            skip = False
            i += 1
            continue
        # 如果下一个数字相同，则合并
        if i + 1 < len(new_row) and new_row[i] == new_row[i+1]:
            merged_row.append(new_row[i] * 2)
            skip = True
        else:
            merged_row.append(new_row[i])
        i += 1
    # 补全0，使长度为4
    merged_row += [0] * (4 - len(merged_row))
    return merged_row

def move_left(board):
    """左移整个棋盘"""
    new_board = []
    for row in board:
        new_board.append(move_row_left(row))
    return new_board

def move_right(board):
    """右移：反转每一行，左移后再反转回来"""
    new_board = []
    for row in board:
        reversed_row = row[::-1]
        new_reversed = move_row_left(reversed_row)
        new_board.append(new_reversed[::-1])
    return new_board

def transpose(board):
    """转置矩阵"""
    return [list(row) for row in zip(*board)]

def move_up(board):
    """上移：先转置，左移，再转置回来"""
    transposed = transpose(board)
    moved = move_left(transposed)
    return transpose(moved)

def move_down(board):
    """下移：先转置，右移，再转置回来"""
    transposed = transpose(board)
    moved = move_right(transposed)
    return transpose(moved)

def move(board, direction):
    """
    根据输入的方向进行移动：
    'w' => 上移, 's' => 下移, 'a' => 左移, 'd' => 右移.
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
        raise ValueError("无效的移动方向，请输入 w, a, s 或 d。")

def check_win(board):
    """检测是否有数字达到2048"""
    for row in board:
        if 2048 in row:
            return True
    return False

def check_game_over(board):
    """
    检查是否没有空格且无法进行任何合并操作，
    若所有单元格均非0且相邻数字没有相等的情况，则游戏结束。
    """
    # 存在空格，游戏未结束
    for row in board:
        if 0 in row:
            return False
    # 检查行和列中相邻元素是否可合并
    for i in range(4):
        for j in range(4):
            if i < 3 and board[i][j] == board[i+1][j]:
                return False
            if j < 3 and board[i][j] == board[i][j+1]:
                return False
    return True
