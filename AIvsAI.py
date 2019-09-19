from time import sleep
from AI import *
from universals import *

board = ["_"] * 9

ai_list = [AI_Jack_the_random(), AI_Bob_the_winner(), AI_Max_the_Min()]

turn = 1

print("Welcome to tic tac toe!")
sleep(1)

print("choose first A.I:")
for ai_idx, ai in enumerate(ai_list):
    print("\t- {} | index:{}\n".format(ai.name, ai_idx))
ai_index = int(input("type index here:"))
while ai_index not in range(len(ai_list)):
    print("invalid input!")
    ai_index = int(input("type index here:"))
ai1 = ai_list[ai_index]

print("ok, choose your second A.I:")
for ai_idx, ai in enumerate(ai_list):
    print("\t- {} | index:{}\n".format(ai.name, ai_idx))
ai_index = int(input("type index here:"))
while ai_index not in range(len(ai_list)):
    print("invalid input!")
    ai_index = int(input("type index here:"))
ai2 = ai_list[ai_index]

#executing A.Is:

pcmove1 = 0
pcmove2 = 0

ai1.prepare()
ai2.prepare()

win = 0

while win == 0:
        print(f"{ai1.name} plays!")
        sleep(1)
        pcmove1 = ai1.get_play(board, turn, pcmove2)
        win = play(board, pcmove1, "C", ai1)
        turn += 1

        if win == 1 or win == 2:
            break

        print(f"{ai2.name} plays!")
        sleep(1)
        pcmove2 = ai2.get_play(board, turn, pcmove1)
        win = play(board, pcmove2, "H", ai2)
        turn += 1