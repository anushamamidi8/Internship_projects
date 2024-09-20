# Function to display the Tic Tac Toe board
def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check for a win
def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]  # diagonals
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (draw condition)
def check_draw(board):
    return all(cell != ' ' for cell in board)

# Function to restart the game
def restart_game():
    while True:
        restart = input("Do you want to play again? (y/n): ").lower()
        if restart == 'y':
            return True
        elif restart == 'n':
            return False
        else:
            print("Invalid input, please enter 'y' or 'n'.")

# Main function to play the game
def play_game():
    while True:
        # Initialize the Tic Tac Toe board (3x3 grid)
        board = [' ' for _ in range(9)]
        current_player = 'X'
        game_over = False

        # Loop for the game
        while not game_over:
            display_board(board)
            # Get the player's move
            try:
                move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != ' ':
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Please enter a valid number between 1 and 9.")
                continue

            # Update the board with the player's move
            board[move] = current_player

            # Check if the player won
            if check_win(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                game_over = True

            # Check for a draw
            elif check_draw(board):
                display_board(board)
                print("It's a draw!")
                game_over = True

            # Switch to the other player
            else:
                current_player = 'O' if current_player == 'X' else 'X'

        # Ask if players want to restart or exit the game
        if not restart_game():
            print("Thank you for playing!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
