import random

board = ["-"] * 9

def print_board():
    print()
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("--+---+--")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("--+---+--")
    print(board[6]+" | "+board[7]+" | "+board[8])
    print()

def take_turn(player):
    if player == "X":
        position = input("Your turn (choose position 1-9): ")
        while position not in [str(i) for i in range(1, 10)]:
            position = input("Invalid input. Choose a position from 1-9: ")
        position = int(position) - 1
        while board[position] != "-":
            position = int(input("Position already taken. Choose a different position: ")) - 1
        board[position] = "X"
    else:
        print("Bot's turn...")
        position = bot_move()
        board[position] = "O"
    print_board()

def bot_move():
    # Basic bot: choose random empty cell
    empty_positions = [i for i in range(9) if board[i] == "-"]
    return random.choice(empty_positions)

def check_game_over():
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for condition in win_conditions:
        a, b, c = condition
        if board[a] == board[b] == board[c] and board[a] != "-":
            return board[a]  # 'X' or 'O'
    if "-" not in board:
        return "tie"
    return "play"

def play_game():
    print("Welcome to Tic-Tac-Toe: You vs Bot 🤖")
    print_board()
    current_player = "X"
    while True:
        take_turn(current_player)
        result = check_game_over()
        if result == "X":
            print("🎉 You win!")
            break
        elif result == "O":
            print("🤖 Bot wins!")
            break
        elif result == "tie":
            print("It's a tie!")
            break
        current_player = "O" if current_player == "X" else "X"

play_game()
