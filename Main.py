board = ["_"] * 9

from time import sleep
from AI import AI_Jack_the_random
from AI import AI_Bob_the_winner
from AI import AI_Max_the_Min
from universals import *

turn = 0
ai_list = [AI_Jack_the_random(), AI_Bob_the_winner(), AI_Max_the_Min()]

#----------------------[GAME INIT]-------------------------

print("Welcome to tic tac toe!")
sleep(1)

print("choose an A.I:")
for ai_idx, ai in enumerate(ai_list):
    print("\t- {} | index:{}\n".format(ai.name, ai_idx))
ai_index = int(input("type index here:"))
while ai_index not in range(len(ai_list)):
    print("invalid input!")
    ai_index = int(input("type index here:"))
ai = ai_list[ai_index]
playermove = 0
play_first = (input("Do you wanna play first? [Y/n]")).lower()
while play_first != "y" and play_first != "n":
      play_first = (input("Do you wanna play first? [Y/n]")).lower()

if play_first == "n":
    turn = 1

ai.play_first = play_first
ai.prepare()

ai.tree_export()

win = 0

while win == 0:
    if (turn % 2) == 0:
        print("your turn!")
        sleep(1)
        playermove = int(input("Choose a space[0-8]:"))
        while (playermove > 8 or playermove < 0) or board[playermove] != "_":
            print("user input invalid")
            playermove = int(input("Choose a space[0-8]:"))
        win = play(board, playermove, "H", ai)
        turn += 1
    else:
        print("The computer plays now!")
        sleep(1)
        pcmove = ai.get_play(board, turn, playermove)
        win = play(board, pcmove, "C", ai)
        turn += 1


