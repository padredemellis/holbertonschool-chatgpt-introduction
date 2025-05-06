#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Filas
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):
            return True
    # Columnas
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return True
    # Diagonales
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        # Pedir coordenadas con validación
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {current_player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {current_player}: "))
        except ValueError:
            print("Invalid input. Please enter numbers 0, 1, or 2.")
            continue
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Coordinates out of range. Must be 0, 1, or 2.")
            continue
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Colocar ficha
        board[row][col] = current_player

        # Comprobar ganador
        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Cambiar jugador
        current_player = "O" if current_player == "X" else "X"

    print("Game over.")

if __name__ == "__main__":
    tic_tac_toe()

