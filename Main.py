board = ["_"] * 9

from time import sleep
from AI import AI_Jack_the_random
from AI import AI_Bob_the_winner
turn = 0
win = 0
ai_list = [AI_Jack_the_random(), AI_Bob_the_winner()]

def print_board(board:list):
      print("_{}_|_{}_|_{}_\n" 
      "_{}_|_{}_|_{}_\n"
      "_{}_|_{}_|_{}_\n".format(board[0], board[1], board[2], board[3], board[4], board[5],
                         board[6], board[7], board[8]))

def play(board, square:int, marker:str, ai):
      if square > 8 and square < 0:
            print("user input invalid")
            return False
      else:
            board[square] = marker
            print_board(board)
            global win
            win = check_win(board, square)
            if win == 1 and board[square] == "H":
              print("win!")
            elif win == 1 and board[square] == "C":
                print("The computer wins :(")
                print("Computer says: {}".format(ai.winning_phrase))
            elif win == 2:
                print("Cat")

def check_win(board, square):
      #checks column 0
      cat = 0
      if square == 0 or square == 3 or square == 6:
            if board[square] == board[square+1] and board[square] == board[square+2]:
                  return 1
      #checks column 1
      elif square == 1 or square == 4 or square == 7:
            if board[square] == board[square+1] and board[square] == board[square-1]:
                  return 1
      #checks column 2
      elif square == 2 or square == 5 or square == 8:
        if board[square] == board[square-1] and board[square] == board[square-2]:
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

while win == 0:
    if (turn % 2) == 0:
        print("your turn!")
        sleep(1)
        playermove = int(input("Choose a space[0-8]:"))
        while (playermove > 8 or playermove < 0) or board[playermove] != "_":
            print("user input invalid")
            playermove = int(input("Choose a space[0-8]:"))
        play(board, playermove, "H", ai)
        turn += 1
    else:
        print("The computer plays now!")
        sleep(1)
        pcmove = ai.get_play(board, turn, playermove)
        play(board, pcmove, "C", ai)
        turn += 1


