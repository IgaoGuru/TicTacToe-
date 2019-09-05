class GameTree():

    board = None
    played_square = None
    subtrees = []

    def __init__(self, board, played_square):
        self.board = board
        self.played_square = played_square


def generate_game_tree(marker):
    board = [""] * 4
    played_square = -1
    root = GameTree(board, played_square)
    return expand_game_tree(root, marker)


def expand_game_tree(gametree, marker):
    empty_squares = []
    for i, square in enumerate(gametree.board):
        if square == "":
            empty_squares.append(i)

    new_m = switch_marker(marker)
    subtrees = []

    for i in empty_squares:
        board = gametree.board.copy()
        board[i] = marker
        subtree = expand_game_tree(GameTree(board, i), new_m)
        subtrees.append(subtree)

    gametree.subtrees = subtrees
    return gametree


def print_tree(tree, tabs = ""): #-> (just prints)
    print(tabs + str(tree.board))
    tabs += "    "
    for subtree in tree.subtrees:
        print_tree(subtree, tabs)
    return


def switch_marker(marker):
    if marker == "C":
        return "H"
    else:
        return "C"

gametree = generate_game_tree("C")
print_tree(gametree)
