import numpy as np
from random import randint

class GameTree():

    board = None
    played_square = None
    subtrees = []
    winner = ""

    def __init__(self, board, played_square):
        self.board = board
        self.played_square = played_square

    def count_nodes(self):
        if len(self.subtrees) == 0:
            return 1

        n = 1
        for subtree in self.subtrees:
            n += subtree.count_nodes()
        return n


def minmax(gametree, marker):
    maximize = True
    if gametree.board[gametree.played_square] == marker:
        maximize = False

    if gametree.board == ["_"] * 9:
        corners = [0, 2, 6, 8]
        return 1, corners[randint(0, 3)]

    if len(gametree.subtrees) == 0:
        leaf_value = get_board_value(gametree, marker)
        return leaf_value, None

    subtree_values = []

    for subtree in gametree.subtrees:
        sub_value, _ = minmax(subtree, marker)
        subtree_values.append(sub_value)

    if maximize:
        return np.max(subtree_values), gametree.subtrees[np.argmax(subtree_values)].played_square
    else:
        return np.min(subtree_values), gametree.subtrees[np.argmin(subtree_values)].played_square


def generate_game_tree(marker):
    board = ["_"] * 9
    played_square = -1
    root = GameTree(board, played_square)
    return expand_game_tree(root, marker)


def expand_game_tree(gametree, marker):
    winner_marker = winner(gametree.board)

    if winner_marker != "_":
        return gametree

    new_m = switch_marker(marker)
    subtrees = []

    for i, square in enumerate(gametree.board):
        if square == "_":
            board = gametree.board.copy()
            board[i] = marker
            tree = GameTree(board, i)
            subtree = expand_game_tree(tree, new_m)
            subtrees.append(subtree)

    gametree.subtrees = subtrees
    return gametree


def print_tree(tree, tabs = ""): #-> (just prints)
    print(tabs + str(tree.board) + "  " + str(tree.winner))
    tabs += "    "
    for subtree in tree.subtrees:
        print_tree(subtree, tabs)
    return


def winner_old(board, square):
    # checks column 0
    cat = 0
    if board[square] != "_":
        if square == 0 or square == 3 or square == 6 and board != "_":
            if board[square] == board[square + 1] and board[square] == board[square + 2]:
                return 1
        # checks column 1
        elif square == 1 or square == 4 or square == 7 and square != "_":
            if board[square] == board[square + 1] and board[square] == board[square - 1]:
                return 1
        # checks column 2
        elif square == 2 or square == 5 or square == 8 and square != "_":
            if board[square] == board[square - 1] and board[square] == board[square - 2]:
                return 1
        # checks line 0
        if square == 0 or square == 1 or square == 2 and square != "_":
            if board[square] == board[square + 3] and board[square] == board[square + 6]:
                return 1
        # checks line 1
        elif square == 3 or square == 4 or square == 5 and square != "_":
            if board[square] == board[square - 3] and board[square] == board[square + 3]:
                return 1
        # checks line 2
        elif square == 6 or square == 7 or square == 8 and square != "_":
            if board[square] == board[square - 3] and board[square] == board[square - 6]:
                return 1
        if square == 6 and square != "_":
            if board[square] == board[square - 2] and board[square] == board[square - 4]:
                return 1
        elif square == 4 and square != "_":
            if board[square] == board[square - 2] and board[square] == board[square + 2]:
                return 1
        elif square == 2 and square != "_":
            if board[square] == board[square + 2] and board[square] == board[square + 4]:
                return 1
        elif square == 0 and square != "_":
            if board[square] == board[square + 4] and board[square] == board[square + 8]:
                return 1
        elif square == 4 and square != "_":
            if board[square] == board[square - 4] and board[square] == board[square + 4]:
                return 1
        elif square == 8 and square != "_":
            if board[square] == board[square - 4] and board[square] == board[square - 8]:
                return 1
        for i in range(len(board)):
            if board[i] != "_":
                cat += 1
        if cat == 9:
            return 2
    return False

def winner(board):

    #checks line 1
    if board[0] == board[1] and board[1] == board[2]:
        return board[0]
    if board[3] == board[4] and board[4] == board[5]:
        return board[3]
    if board[6] == board[7] and board[7] == board[8]:
        return board[6]
    if board[0] == board[3] and board[3] == board[6]:
        return board[0]
    if board[1] == board[4] and board[4] == board[7]:
        return board[1]
    if board[2] == board[5] and board[5] == board[8]:
        return board[2]
    if board[0] == board[4] and board[4] == board[8]:
        return board[0]
    if board[2] == board[4] and board[4] == board[6]:
        return board[6]
    return "_"


def switch_marker(marker):
    if marker == "C":
        return "H"
    else:
        return "C"


def get_board_value(gametree, marker):
    if winner(gametree.board) == marker:
        return 1
    elif winner(gametree.board) == switch_marker(marker):
        return -1
    return 0

