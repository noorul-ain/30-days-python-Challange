# Tic Tac Toe Game - Noor ul Ain

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

# Initialize the game
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

print("Welcome to Tic Tac Toe!")
print_board(board)

# Game loop
while True:
    try:
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter column (0-2): "))

        if board[row][col] != " ":
            print("Cell already taken. Try again.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins! 🎉")
            break
        elif is_full(board):
            print("It's a tie! 🤝")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"
    except (ValueError, IndexError):
        print("Invalid input. Please enter numbers between 0 and 2.")
