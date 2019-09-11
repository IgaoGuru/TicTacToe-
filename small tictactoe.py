import numpy as np

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


def generate_game_tree(marker):
    board = [""] * 4
    played_square = -1
    root = GameTree(board, played_square)
    return expand_game_tree(root, marker)


def expand_game_tree(gametree, marker):

    new_m = switch_marker(marker)
    subtrees = []

    for i, square in enumerate(gametree.board):
        if square == "":
            winner_marker = winner(gametree.board)

            board = gametree.board.copy()
            board[i] = marker


            if winner_marker == "":
                subtree = expand_game_tree(GameTree(board, i), new_m)
                subtrees.append(subtree)
            else:
                gametree.winner = winner_marker
                return gametree


    gametree.subtrees = subtrees
    return gametree


def print_tree(tree, tabs = ""): #-> (just prints)
    print(tabs + str(tree.board) + "  " + tree.winner)
    tabs += "    "
    for subtree in tree.subtrees:
        print_tree(subtree, tabs)
    return


def switch_marker(marker):
    if marker == "C":
        return "H"
    else:
        return "C"


def winner(board):
    if board[0] == board[3] and board[0] != "":
        return board[0]
    if board[1] == board[2] and board[1] != "":
        return board[2]
    return ""


def minmax(gametree, marker):
    maximize = True
    if gametree.board[gametree.played_square] == marker:
        maximize = False

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


def evaluate_leafs(gametree, marker):

    if len(gametree.subtrees) == 0:
        leaf_value = get_board_value(gametree, marker)
        return leaf_value
    subtree_values = []
    for subtree in gametree.subtrees:
        subtree_value = evaluate_leafs(subtree, marker)
        if subtree_value != None:
            if type(subtree_value) == list:
                for i in range(len(subtree_value)):
                    subtree_values.append(subtree_value[i])
            elif type(subtree_value) == int:
                subtree_values.append(subtree_value)
    return subtree_values


def get_board_value(gametree, marker):
    if gametree.winner == marker:
        return 1
    elif gametree.winner == switch_marker(marker):
        return -1
    return 0







#testing pad
gametree = generate_game_tree("C")

print_tree(gametree.subtrees[3].subtrees[2])

ai_play = minmax(gametree.subtrees[3].subtrees[2], "C")

print(ai_play)