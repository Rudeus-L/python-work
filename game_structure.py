from game_logic import check_winner, is_draw, convert_input
#Place the game board
def print_board(board):
    print("    1   2   3")          # X coordinate: 1, 2, 3
    print("  ┌───┬───┬───┐")
    row_vertical = 1
    for row in board:               # Y coordinate: 1, 2, 3
        print(f"{row_vertical} │ {row[0]} │ {row[1]} │ {row[2]} │")
        if row_vertical < 3:
            print("  ├───┼───┼───┤")
        else:
            print("  └───┴───┴───┘")
        row_vertical += 1

# Game loop
def tic_tac_toe():
    # input player name
    print("Welcome to tic-tac-toe game!")
    name1 = input("Please enter player1 name: ").strip()
    name2 = input("Please enter player2 name: ").strip()
    print()

    # allocate the symbol for each player
    symbol1 = "X"
    symbol2 = "O"

    #store players info
    players = [
        {"name": name1, "symbol": symbol1},
        {"name": name2, "symbol": symbol2}
    ]

    print(f"{name1} use '{symbol1}'，{name2} use '{symbol2}'")
    print("Please enter coordinate (x y)")

    #fill board with ' ' first
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(" ")
        board.append(row)

    current_player = 0
    print_board(board)

    while True:
        player = players[current_player]
        move = input(f"{player['name']}(symbol {player['symbol']})'s turn, enter(x y): ").strip()
        result = convert_input(move)

        if result is None:
            print("Invalid input! Please enter coordinate between 1-3, like 1 2。")
            continue

        row, col = result
        if board[row][col] != " ":
            print("The place is occupied, please select other coordinate")
            continue

        board[row][col] = player['symbol']
        print_board(board)

        if check_winner(board, player['symbol']):
            print(f" Player {player['name']} win! Congratulations!")
            break
        elif is_draw(board):
            print("Draw! Board if full.")
            break

        current_player = 1 - current_player
