from Game2048 import (
    initialize_board, print_board, add_new_tile,
    move, check_win, check_game_over
)
import copy

def main():
    board = initialize_board()
    while True:
        print_board(board)
        
        # 检查胜利条件
        if check_win(board):
            print("恭喜你达到了2048！你赢了！")
            choice = input("输入 r 重新开始，或 q 退出游戏：").strip().lower()
            if choice == 'r':
                board = initialize_board()
                continue
            elif choice == 'q':
                break
        
        # 检查是否无法进行任何移动
        if check_game_over(board):
            print("游戏结束，没有更多合法移动。")
            choice = input("输入 r 重新开始，或 q 退出游戏：").strip().lower()
            if choice == 'r':
                board = initialize_board()
                continue
            elif choice == 'q':
                break
        
        # 获取用户输入，并处理异常输入
        try:
            user_input = input("请输入移动方向 (w=上, s=下, a=左, d=右)：").strip().lower()
            if user_input not in ['w', 'a', 's', 'd']:
                raise ValueError("无效输入")
        except ValueError as e:
            print("错误：请输入 w, a, s 或 d。")
            continue
        
        # 使用深拷贝检测移动是否改变棋盘状态
        board_copy = copy.deepcopy(board)
        try:
            new_board = move(board_copy, user_input)
        except Exception as e:
            print("移动过程中出错：", e)
            continue
        
        if new_board == board:
            print("该方向无法移动，请尝试其他方向。")
            continue
        else:
            board = new_board
            board = add_new_tile(board)

if __name__ == "__main__":
    main()
    
# GitHub: 请将你的代码 push 到你的 GitHub 账号，并在此处留下你的 GitHub 链接。
# 例如: # GitHub: https://github.com/yourusername/2048-game
