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

gametree = generate_game_tree("H")

print_tree(gametree)

num_nodes = gametree.count_nodes()
print(num_nodes)