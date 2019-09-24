from AI import AI_Max_the_Min
import maxthemin
import numpy as np

def tree_export(gametree, filepath):
    filehandler = open(filepath, "w+")
    filehandler.write("S0,S1,S2,S3,S4,S5,S6,S7,S8,value,optimal_play\n")

    tree_export_(gametree, filehandler)

    filehandler.close()

def tree_export_(gametree, file):

    if gametree == []:
        return

    new_board = ""

    for i_idx, i in enumerate(gametree.board):
        if i == "_":
            i = 0
        elif i == "C":
            i = 1
        elif i == "H":
            i = 2

        new_board += str(i)
        if i_idx != (len(gametree.board) - 1):
            new_board += ", "

    file.write(new_board + ", " + str(gametree.value) + ", " + str(gametree.optimal_play) + "\n")

    for subtree in gametree.subtrees:
        tree_export_(subtree, file)


def minmax_modded(gametree, marker):
    maximize = True
    if gametree.board[gametree.played_square] == marker:
        maximize = False

    if len(gametree.subtrees) == 0:
        leaf_value = maxthemin.get_board_value(gametree, marker)
        return leaf_value, None

    subtree_values = []

    for subtree in gametree.subtrees:
        sub_value, _ = minmax_modded(subtree, marker)
        subtree_values.append(sub_value)

    if maximize:
        gametree.value = np.max(subtree_values)
        gametree.optimal_play = gametree.subtrees[np.argmax(subtree_values)].played_square
        return np.max(subtree_values), gametree.subtrees[np.argmax(subtree_values)].played_square
    else:
        gametree.value = np.min(subtree_values)
        gametree.optimal_play = gametree.subtrees[np.argmin(subtree_values)].played_square
        return np.min(subtree_values), gametree.subtrees[np.argmin(subtree_values)].played_square

ai = AI_Max_the_Min()

ai.play_first = "n"
ai.prepare()

minmax_modded(ai.gametree, "C")

tree_export(ai.gametree, "tree_exported.txt")

