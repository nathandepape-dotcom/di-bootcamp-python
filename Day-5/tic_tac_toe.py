# Mini-Project - Tic Tac Toe (Day 5)
#
# Goal: Create a Tic Tac Toe game in Python where two players
# play against each other on a 3x3 grid.
#
# Players take turns marking empty squares with 'X' or 'O'.
# First to get 3 in a row (horizontal, vertical, diagonal) wins.
# If the grid fills up with no winner, it's a tie.

# Step 1: Represent the game board (3x3 grid, empty cells = ' ')
board = []
for i in range(3):
    ligne = []
    for j in range(3):
        ligne.append(' ')
    board.append(ligne)

# Step 2: display_board() - print the current state of the grid
def display_board():
    for ligne in board:
        print(ligne)

# Step 3: player_input(player) - get the player's move, validate it, place it
def player_input(player):
    while True:
        line = int(input("Ligne (1-3): "))
        colonne = int(input("Colonne (1-3) : "))

        # validation 1 : dans la plage 1-3
        if not (1 <= line <= 3 and 1 <= colonne <= 3):
            print("Position invalide (entre 1 et 3).")
            continue

        # validation 2 : la case doit être vide
        if board[line - 1][colonne - 1] != ' ':
            print("Case déjà occupée, choisis-en une autre.")
            continue

        break

    board[line - 1][colonne - 1] = player

# Step 4: check_win(board, player) - return True if player has 3 in a row
def check_win(board, player):
    # 3 lignes
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True

    # 3 colonnes
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True

    # 2 diagonales
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

# Step 5: check_tie(board) - return True if grid is full with no winner
def check_tie(board):
    for ligne in board:
        for case in ligne:
            if case == ' ':
                return False
    return True

# Step 6: play() - main game loop (display -> input -> update -> check -> switch)
def play():
    current_player = 'X'
    while True:
        display_board()
        player_input(current_player)
        if check_win(board, current_player):
            display_board()
            print(f"{current_player} a gagné !")
            break
        if check_tie(board):
            display_board()
            print("Égalité !")
            break
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

play()
