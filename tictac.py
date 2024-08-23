import queue
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False
def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True
def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "
def bfs_ai_move(board, player):
    q = queue.Queue()
    q.put(board)

    while not q.empty():
        current_board = q.get()

        for row in range(3):
            for col in range(3):
                if current_board[row][col] == " ":
                    new_board = [row[:] for row in current_board]
                    new_board[row][col] = player
                    if is_winner(new_board, player):
                        return row, col
                    q.put(new_board)

    return None  # If no winning move is found, return None
# main game loop
def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = players[0]

    while True:
        print_board(board)

        if current_player == "X":
            row = int(input(f"Enter row (0-2) for player X: "))
            col = int(input(f"Enter column (0-2) for player X: "))
        else:
            print("Player O (AI) is making a move...")
            ai_move = bfs_ai_move(board, current_player)
            if ai_move:
                row, col = ai_move
            else:
                print("AI couldn't find a winning move, making a random move.")
                # Implement a more advanced AI algorithm here.
                row, col = 0, 0  # For simplicity, making a random move.

        if is_valid_move(board, row, col):
            board[row][col] = current_player

            if is_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = players[1] if current_player == players[0] else players[0]

        else:
            print("Invalid move. Please try again.")
# main Function
if __name__ == "__main__":
    play_tic_tac_toe()
