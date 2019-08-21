board = ["_"] * 9
from random import randint
from time import sleep
turn = 0
win = False

def print_board(board:list):
      print("_{}_|_{}_|_{}_\n" 
      "_{}_|_{}_|_{}_\n"
      "_{}_|_{}_|_{}_\n".format(board[0], board[1], board[2], board[3], board[4], board[5],
                         board[6], board[7], board[8]))

def play(board, square:int, marker:str):
      if square >= 8 and square < 0:
            print("user input invalid")
            return False
      else:
            board[square] = marker
            print_board(board)
            global win
            win = bool(check_win(board, square))
            if win == True and board[square] == "H":
              print("win!")
            elif win == True and board[square] == "C":
                print("The computer wins :(")

def check_win(board, square):
      #checks column 0
      if square == 0 or square == 3 or square == 6:
            if board[square] == board[square+1] and board[square] == board[square+2]:
                  return True
      #checks column 1
      elif square == 1 or square == 4 or square == 7:
            if board[square] == board[square+1] and board[square] == board[square-1]:
                  return True
      #checks column 2
      elif square == 2 or square == 5 or square == 8:
        if board[square] == board[square-1] and board[square] == board[square-2]:
              return True
      # checks line 0
      if square == 0 or square == 1 or square == 2:
        if board[square] == board[square + 3] and board[square] == board[square + 6]:
          return True
      # checks line 1
      elif square == 3 or square == 4 or square == 5:
        if board[square] == board[square - 3] and board[square] == board[square + 3]:
          return True
      # checks line 2
      elif square == 6 or square == 7 or square == 8:
        if board[square] == board[square - 3] and board[square] == board[square - 6]:
          return True
      if square == 6:
        if board[square] == board[square - 2] and board[square] == board[square - 4]:
            return True
      elif square == 4:
        if board[square] == board[square - 2] and board[square] == board[square + 2]:
            return True
      elif square == 2:
        if board[square] == board[square + 2] and board[square] == board[square + 4]:
            return True
      elif square == 0:
        if board[square] == board[square + 4] and board[square] == board[square + 8]:
            return True
      elif square == 4:
        if board[square] == board[square - 4] and board[square] == board[square + 4]:
            return True
      elif square == 8:
        if board[square] == board[square - 4] and board[square] == board[square - 8]:
            return True
      else:
          return False


#----------------------[GAME INIT]-------------------------

print("Welcome to tic tac toe!")

play_first = (input("Do you wanna play first? [Y/n]")).lower()
while play_first != "y" and play_first != "n":
      play_first = (input("Do you wanna play first? [Y/n]")).lower()

if play_first == "n":
    turn = 1

while win == False:
    if (turn % 2) == 0:
        turn += 1
        print("your turn!")
        sleep(1)
        playermove = int(input("Choose a space[0-8]:"))
        while (playermove > 8 or playermove < 0) or board[playermove] != "_":
            print("user input invalid")
            playermove = int(input("Choose a space[0-8]:"))
        play(board, playermove, "H")
    else:
        turn += 1
        print("The computer plays now!")
        sleep(1)
        pcmove = randint(0, 8)
        while board[pcmove] != "_":
            pcmove = randint(0, 8)
        play(board, pcmove, "C")


