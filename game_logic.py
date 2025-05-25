# Check who wins
def check_winner(board, player):
    # check if wins by line
    for row in board:
        row_win = True
        for cell in row:
            if cell != player:      #if the cell input in line is not current player, no win
                row_win = False
                break
        if row_win:
            return True

    # check if wins by columns
    for column in range(3):
        column_win = True
        for row in range(3):
            if board[row][column] != player:
                column_win = False
                break
        if column_win:
            return True

    # check diagonal1 (from left top to right bottom)
    diagonal1_win = True
    for i in range(3):
        if board[i][i] != player:
            diagonal1_win = False
            break
    if diagonal1_win:
        return True

    # check diagonal2 (from right top to left bottom)
    diagonal2_win = True
    for j in range(3):
        if board[j][2 - j] != player:
            diagonal2_win = False
            break
    if diagonal2_win:
        return True

    return False


# Check if the board is full. If it's full, game is draw.
def is_draw(board):
    for row in board:   # check every line
        for cell in row:    # check cells in each line
            if cell == " ":     # if remain space, game continue
                return False
    return True

# Convert input into valid input
def convert_input(move):
    command = move.strip().split()
    if len(command) != 2:        #input must be (x y)
        return None

    if not command[0].isdigit() or not command[1].isdigit():        #input must be int
        return None

    #ensure the coordinate displays horizontal axis then vertical
    column = int(command[0]) - 1
    row = int(command[1]) - 1

    if row < 0 or row > 2 or column < 0 or column > 2:      #input must be valid within board size
        return None
    return row, column