def print_board(board: list):
    print("_{}_|_{}_|_{}_\n"
          "_{}_|_{}_|_{}_\n"
          "_{}_|_{}_|_{}_\n".format(board[0], board[1], board[2], board[3], board[4], board[5],
                                    board[6], board[7], board[8]))


def play(board, square: int, marker: str, ai):
    if square > 8 and square < 0:
        print("user input invalid")
        return False
    else:
        board[square] = marker
        print_board(board)
        win = check_win(board, square)
        if win == 1 and board[square] == "H":
            print("win!")
        elif win == 1 and board[square] == "C":
            print("The computer wins :(")
            print("Computer says: {}".format(ai.winning_phrase))
        elif win == 2:
            print("Cat")
    return win


def check_win(board, square):
    # checks column 0
    cat = 0
    if square == 0 or square == 3 or square == 6:
        if board[square] == board[square + 1] and board[square] == board[square + 2]:
            return 1
    # checks column 1
    elif square == 1 or square == 4 or square == 7:
        if board[square] == board[square + 1] and board[square] == board[square - 1]:
            return 1
    # checks column 2
    elif square == 2 or square == 5 or square == 8:
        if board[square] == board[square - 1] and board[square] == board[square - 2]:
            return 1
    # checks line 0
    if square == 0 or square == 1 or square == 2:
        if board[square] == board[square + 3] and board[square] == board[square + 6]:
            return 1
    # checks line 1
    elif square == 3 or square == 4 or square == 5:
        if board[square] == board[square - 3] and board[square] == board[square + 3]:
            return 1
    # checks line 2
    elif square == 6 or square == 7 or square == 8:
        if board[square] == board[square - 3] and board[square] == board[square - 6]:
            return 1
    if square == 6:
        if board[square] == board[square - 2] and board[square] == board[square - 4]:
            return 1
    elif square == 4:
        if board[square] == board[square - 2] and board[square] == board[square + 2]:
            return 1
    elif square == 2:
        if board[square] == board[square + 2] and board[square] == board[square + 4]:
            return 1
    elif square == 0:
        if board[square] == board[square + 4] and board[square] == board[square + 8]:
            return 1
    elif square == 4:
        if board[square] == board[square - 4] and board[square] == board[square + 4]:
            return 1
    elif square == 8:
        if board[square] == board[square - 4] and board[square] == board[square - 8]:
            return 1
    for i in range(len(board)):
        if board[i] != "_":
            cat += 1
    if cat == 9:
        return 2
    else:
        return False