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



def display_board():
    for ligne in board:
        print(ligne)

# Step 3: player_input(player) - get the player's move (row, column), validate it
def player_input(player):
    display_board()
    line = int(input("Ligne (1-3): "))
    colonne = int(input("Colonne (1-3) : "))

    board[line - 1][colonne - 1] = player

   
   

    
        


# Step 4: check_win(board, player) - return True if player has 3 in a row
def check_win(board, player):
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    if board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    if board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True

    # --- 3 colonnes (verticales) ---
    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    if board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    if board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True

    # --- 2 diagonales ---
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
    current_player = 'X'                 # AVANT la boucle
    while True:                          # indenté sous le def
        display_board()
        player_input(current_player)
        if check_win(board, current_player):
            print(f"{current_player} a gagné !")
            print(board)
            break
        if check_tie(board):
            print("Égalité !")
            print(board)
            break
        if current_player == 'X':        # bascule en fin de boucle
            current_player = 'O'
        else:
            current_player = 'X'
    
    
 
   
    


play()
