from random import randint


class AI:

    def __init__(self, name, winning_phrase):
        self.name = name
        self.winning_phrase = winning_phrase

    def get_play(self, board, turn, last_play):
        return None


class AI_Jack_the_random(AI):

    def __init__(self, name = "jack_the_random", winning_phrase = "I have absolutely no idea of what I just did!"):
        AI.__init__(self, name, winning_phrase)

    def get_play(self, board, turn, last_play):
        pcmove = randint(0, 8)
        while board[pcmove] != "_":
            pcmove = randint(0, 8)
        return pcmove

class AI_Bob_the_winner(AI):
    # var definition
    wwin = 0
    middleh1 = False
    playerstart = False
    
    def __init__(self, name = "bob_the_random", winning_phrase = "I literally just followed instructions to get here!"):
        AI.__init__(self, name, winning_phrase)

    def get_play(self, board, turn, last_play):

        if board == ["_"] * 9 and turn == 1:
            self.playerstart = False
        elif board != ["_"] * 9 and turn == 1:
            self.playerstart = True

        if self.playerstart == False:
            #1st turn
            if turn == 1:
                return 0
            #second turn
            elif turn == 3:
                if board[4] == "H":
                    self.middleh1 = True
                    return 8
                if board[1] == "H":
                    self.wwin = 1
                    return 6
                elif board[2] == "H":
                    self.wwin = 2
                    return 8
                elif board[3] == "H":
                    self.wwin = 3
                    return 2
                elif board[5] == "H":
                    self.wwin = 5
                    return 2
                elif board[6] == "H":
                    self.wwin = 6
                    return 2
                elif board[7] == "H":
                    self.wwin = 7
                    return 2
                elif board[8] == "H":
                    self.wwin = 8
                    return 6
            # 3rd turn
            elif turn == 5:
                if self.wwin == 1:
                    if board[3] == "H":
                        return 4
                    else:
                        return 3
                elif self.wwin == 2:
                    if board[4] == "H":
                        return 6
                    else:
                        return 4
                elif self.wwin == 3:
                    if board[1] == "H":
                        return 8
                    else:
                        return 1
                elif self.wwin == 5:
                    if board[1] == "H":
                        return 6
                    else:
                        return 1
                elif self.wwin == 6:
                    if board[1] == "H":
                        return 8
                    else:
                        return 1
                elif self.wwin == 7:
                    if board[1] == "H":
                        return 4
                    else:
                        return 1
                elif self.wwin == 8:
                    if board[3] == "H":
                        return 2
                    else:
                        return 3
                if self.middleh1 == True:
                    if board[1] == "H":
                        return 7
                    elif board[2] == "H":
                        return 6
                    elif board[3] == "H":
                        return 5
                    elif board[5] == "H":
                        return 3
                    elif board[6] == "H":
                        return 2
                    elif board[7] == "H":
                        return 1
            #turn 4(final)
            elif turn == 7:
                if self.middleh1 == True:
                    if board[0] == "C" and board[0] == board[1] and board[2] == "_":
                        return 2
                    elif board[1] == "C" and board[2] == board[1] and board[0] == "_":
                        return 0
                    elif board[3] == "C" and board[3] == board[4] and board[5] == "_":
                        return 5
                    elif board[4] == "C" and board[4] == board[5] and board[3] == "_":
                        return 3
                    elif board[6] == "C" and board[6] == board[7] and board[8] == "_":
                        return 8
                    elif board[7] == "C" and board[7] == board[8] and board[6] == "_":
                        return 6
                    elif board[0] == "C" and board[0] == board[3] and board[6] == "_":
                        return 6
                    elif board[3] == "C" and board[3] == board[6] and board[0] == "_":
                        return 0
                    elif board[1] == "C" and board[1] == board[4] and board[7] == "_":
                        return 7
                    elif board[4] == "C" and board[4] == board[7] and board[1] == "_":
                        return 1
                    elif board[2] == "C" and board[2] == board[5] and board[8] == "_":
                        return 8
                    elif board[5] == "C" and board[5] == board[8] and board[2] == "_":
                        return 2
                    elif board[2] == "C" and board[2] == board[4] and board[6] == "_":
                        return 6
                    elif board[4] == "C" and board[4] == board[6 ] and board[2] == "_":
                        return 2

                    if board[0] == "H" and board[0] == board[1] and board[2] == "_":
                        return 2
                    elif board[1] == "H" and board[2] == board[1] and board[0] == "_":
                        return 0
                    elif board[3] == "H" and board[3] == board[4] and board[5] == "_":
                        return 5
                    elif board[4] == "H" and board[4] == board[5] and board[3] == "_":
                        return 3
                    elif board[6] == "H" and board[6] == board[7] and board[8] == "_":
                        return 8
                    elif board[7] == "H" and board[7] == board[8] and board[6] == "_":
                        return 6
                    elif board[0] == "H" and board[0] == board[3] and board[6] == "_":
                        return 6
                    elif board[3] == "H" and board[3] == board[6] and board[0] == "_":
                        return 0
                    elif board[1] == "H" and board[1] == board[4] and board[7] == "_":
                        return 7
                    elif board[4] == "H" and board[4] == board[7] and board[1] == "_":
                        return 1
                    elif board[2] == "H" and board[2] == board[5] and board[8] == "_":
                        return 8
                    elif board[5] == "H" and board[5] == board[8] and board[2] == "_":
                        return 2
                    elif board[2] == "H" and board[2] == board[4] and board[6] == "_":
                        return 6
                    elif board[4] == "H" and board[4] == board[6 ] and board[2] == "_":
                        return 2
                if self.wwin == 1:
                    if board[2] == "H":
                        return 8
                    else:
                        return 2
                if self.wwin == 2:
                    if board[3] == "H":
                        return 7
                    else:
                        return 3
                if self.wwin == 3:
                    if board[4] == "H":
                        return 5
                    else:
                        return 4
                if self.wwin == 5:
                    if board[3] == "H":
                        return 4
                    else:
                        return 3
                if self.wwin == 6:
                    if board[4] == "H":
                        return 5
                    else:
                        return 4
                if self.wwin == 7:
                    if board[6] == "H":
                        return 8
                    else:
                        return 6
                if self.wwin == 8:
                    if board[1] == "H":
                        return 4
                    else:
                        return
            #last turn possible
            elif turn == 9:
                if self.middleh1 == True:
                    if board[0] == "C" and board[0] == board[1] and board[2] == "_":
                        return 2
                    elif board[1] == "C" and board[2] == board[1] and board[0] == "_":
                        return 0
                    elif board[3] == "C" and board[3] == board[4] and board[5] == "_":
                        return 5
                    elif board[4] == "C" and board[4] == board[5] and board[3] == "_":
                        return 3
                    elif board[6] == "C" and board[6] == board[7] and board[8] == "_":
                        return 8
                    elif board[7] == "C" and board[7] == board[8] and board[6] == "_":
                        return 6
                    elif board[0] == "C" and board[0] == board[3] and board[6] == "_":
                        return 6
                    elif board[3] == "C" and board[3] == board[6] and board[0] == "_":
                        return 0
                    elif board[1] == "C" and board[1] == board[4] and board[7] == "_":
                        return 7
                    elif board[4] == "C" and board[4] == board[7] and board[1] == "_":
                        return 1
                    elif board[2] == "C" and board[2] == board[5] and board[8] == "_":
                        return 8
                    elif board[5] == "C" and board[5] == board[8] and board[2] == "_":
                        return 2
                    elif board[2] == "C" and board[2] == board[4] and board[6] == "_":
                        return 6
                    elif board[4] == "C" and board[4] == board[6 ] and board[2] == "_":
                        return 2

                    if board[0] == "H" and board[0] == board[1] and board[2] == "_":
                        return 2
                    elif board[1] == "H" and board[2] == board[1] and board[0] == "_":
                        return 0
                    elif board[3] == "H" and board[3] == board[4] and board[5] == "_":
                        return 5
                    elif board[4] == "H" and board[4] == board[5] and board[3] == "_":
                        return 3
                    elif board[6] == "H" and board[6] == board[7] and board[8] == "_":
                        return 8
                    elif board[7] == "H" and board[7] == board[8] and board[6] == "_":
                        return 6
                    elif board[0] == "H" and board[0] == board[3] and board[6] == "_":
                        return 6
                    elif board[3] == "H" and board[3] == board[6] and board[0] == "_":
                        return 0
                    elif board[1] == "H" and board[1] == board[4] and board[7] == "_":
                        return 7
                    elif board[4] == "H" and board[4] == board[7] and board[1] == "_":
                        return 1
                    elif board[2] == "H" and board[2] == board[5] and board[8] == "_":
                        return 8
                    elif board[5] == "H" and board[5] == board[8] and board[2] == "_":
                        return 2
                    elif board[2] == "H" and board[2] == board[4] and board[6] == "_":
                        return 6
                    elif board[4] == "H" and board[4] == board[6 ] and board[2] == "_":
                        return 2

        elif self.playerstart == True:
            if turn == 1:
                if board[4] == "_":
                    self.wwin = 100
                    return 4
                else:
                    self.wwin = 101
                    return 0
            elif turn == 3:
                if self.wwin == 100 or 101:
                    if board[0] == "C" and board[0] == board[1] and board[2] == "_":
                        return 2
                    elif board[1] == "C" and board[2] == board[1] and board[0] == "_":
                        return 0
                    elif board[3] == "C" and board[3] == board[4] and board[5] == "_":
                        return 5
                    elif board[4] == "C" and board[4] == board[5] and board[3] == "_":
                        return 3
                    elif board[6] == "C" and board[6] == board[7] and board[8] == "_":
                        return 8
                    elif board[7] == "C" and board[7] == board[8] and board[6] == "_":
                        return 6
                    elif board[0] == "C" and board[0] == board[3] and board[6] == "_":
                        return 6
                    elif board[3] == "C" and board[3] == board[6] and board[0] == "_":
                        return 0
                    elif board[1] == "C" and board[1] == board[4] and board[7] == "_":
                        return 7
                    elif board[4] == "C" and board[4] == board[7] and board[1] == "_":
                        return 1
                    elif board[2] == "C" and board[2] == board[5] and board[8] == "_":
                        return 8
                    elif board[5] == "C" and board[5] == board[8] and board[2] == "_":
                        return 2
                    elif board[2] == "C" and board[2] == board[4] and board[6] == "_":
                        return 6
                    elif board[4] == "C" and board[4] == board[6 ] and board[2] == "_":
                        return 2

                    if board[0] == "H" and board[0] == board[1] and board[2] == "_":
                        return 2
                    elif board[1] == "H" and board[2] == board[1] and board[0] == "_":
                        return 0
                    elif board[3] == "H" and board[3] == board[4] and board[5] == "_":
                        return 5
                    elif board[4] == "H" and board[4] == board[5] and board[3] == "_":
                        return 3
                    elif board[6] == "H" and board[6] == board[7] and board[8] == "_":
                        return 8
                    elif board[7] == "H" and board[7] == board[8] and board[6] == "_":
                        return 6
                    elif board[0] == "H" and board[0] == board[3] and board[6] == "_":
                        return 6
                    elif board[3] == "H" and board[3] == board[6] and board[0] == "_":
                        return 0
                    elif board[1] == "H" and board[1] == board[4] and board[7] == "_":
                        return 7
                    elif board[4] == "H" and board[4] == board[7] and board[1] == "_":
                        return 1
                    elif board[2] == "H" and board[2] == board[5] and board[8] == "_":
                        return 8
                    elif board[5] == "H" and board[5] == board[8] and board[2] == "_":
                        return 2
                    elif board[2] == "H" and board[2] == board[4] and board[6] == "_":
                        return 6
                    elif board[4] == "H" and board[4] == board[6 ] and board[2] == "_":
                        return 2
                    elif board[0] == "H" and board[0] == board[4] and board[8] == "_":
                        return 8
                    elif board[4] == "H" and board[4] == board[8] and board[0] == "_":
                        return 0
                    else:
                        return 2

            elif turn == 5:
                if self.wwin == 100 or 101:
                    if board[0] == "C" and board[0] == board[1] and board[2] == "_":
                        return 2
                    elif board[1] == "C" and board[2] == board[1] and board[0] == "_":
                        return 0
                    elif board[3] == "C" and board[3] == board[4] and board[5] == "_":
                        return 5
                    elif board[4] == "C" and board[4] == board[5] and board[3] == "_":
                        return 3
                    elif board[6] == "C" and board[6] == board[7] and board[8] == "_":
                        return 8
                    elif board[7] == "C" and board[7] == board[8] and board[6] == "_":
                        return 6
                    elif board[0] == "C" and board[0] == board[3] and board[6] == "_":
                        return 6
                    elif board[3] == "C" and board[3] == board[6] and board[0] == "_":
                        return 0
                    elif board[1] == "C" and board[1] == board[4] and board[7] == "_":
                        return 7
                    elif board[4] == "C" and board[4] == board[7] and board[1] == "_":
                        return 1
                    elif board[2] == "C" and board[2] == board[5] and board[8] == "_":
                        return 8
                    elif board[5] == "C" and board[5] == board[8] and board[2] == "_":
                        return 2
                    elif board[2] == "C" and board[2] == board[4] and board[6] == "_":
                        return 6
                    elif board[4] == "C" and board[4] == board[6 ] and board[2] == "_":
                        return 2

                    if board[0] == "H" and board[0] == board[1] and board[2] == "_":
                        return 2
                    elif board[1] == "H" and board[2] == board[1] and board[0] == "_":
                        return 0
                    elif board[3] == "H" and board[3] == board[4] and board[5] == "_":
                        return 5
                    elif board[4] == "H" and board[4] == board[5] and board[3] == "_":
                        return 3
                    elif board[6] == "H" and board[6] == board[7] and board[8] == "_":
                        return 8
                    elif board[7] == "H" and board[7] == board[8] and board[6] == "_":
                        return 6
                    elif board[0] == "H" and board[0] == board[3] and board[6] == "_":
                        return 6
                    elif board[3] == "H" and board[3] == board[6] and board[0] == "_":
                        return 0
                    elif board[1] == "H" and board[1] == board[4] and board[7] == "_":
                        return 7
                    elif board[4] == "H" and board[4] == board[7] and board[1] == "_":
                        return 1
                    elif board[2] == "H" and board[2] == board[5] and board[8] == "_":
                        return 8
                    elif board[5] == "H" and board[5] == board[8] and board[2] == "_":
                        return 2
                    elif board[2] == "H" and board[2] == board[4] and board[6] == "_":
                        return 6
                    elif board[4] == "H" and board[4] == board[6 ] and board[2] == "_":
                        return 2
                    else:
                        choice = randint(0,8)
                        while board[choice] != "_":
                            choice = randint(0,8)
                        return choice


            elif turn == 7:
                if self.wwin == 100 or 101:
                    if board[0] == "C" and board[0] == board[1] and board[2] == "_":
                        return 2
                    elif board[1] == "C" and board[2] == board[1] and board[0] == "_":
                        return 0
                    elif board[3] == "C" and board[3] == board[4] and board[5] == "_":
                        return 5
                    elif board[4] == "C" and board[4] == board[5] and board[3] == "_":
                        return 3
                    elif board[6] == "C" and board[6] == board[7] and board[8] == "_":
                        return 8
                    elif board[7] == "C" and board[7] == board[8] and board[6] == "_":
                        return 6
                    elif board[0] == "C" and board[0] == board[3] and board[6] == "_":
                        return 6
                    elif board[3] == "C" and board[3] == board[6] and board[0] == "_":
                        return 0
                    elif board[1] == "C" and board[1] == board[4] and board[7] == "_":
                        return 7
                    elif board[4] == "C" and board[4] == board[7] and board[1] == "_":
                        return 1
                    elif board[2] == "C" and board[2] == board[5] and board[8] == "_":
                        return 8
                    elif board[5] == "C" and board[5] == board[8] and board[2] == "_":
                        return 2
                    elif board[2] == "C" and board[2] == board[4] and board[6] == "_":
                        return 6
                    elif board[4] == "C" and board[4] == board[6 ] and board[2] == "_":
                        return 2

                    if board[0] == "H" and board[0] == board[1] and board[2] == "_":
                        return 2
                    elif board[1] == "H" and board[2] == board[1] and board[0] == "_":
                        return 0
                    elif board[3] == "H" and board[3] == board[4] and board[5] == "_":
                        return 5
                    elif board[4] == "H" and board[4] == board[5] and board[3] == "_":
                        return 3
                    elif board[6] == "H" and board[6] == board[7] and board[8] == "_":
                        return 8
                    elif board[7] == "H" and board[7] == board[8] and board[6] == "_":
                        return 6
                    elif board[0] == "H" and board[0] == board[3] and board[6] == "_":
                        return 6
                    elif board[3] == "H" and board[3] == board[6] and board[0] == "_":
                        return 0
                    elif board[1] == "H" and board[1] == board[4] and board[7] == "_":
                        return 7
                    elif board[4] == "H" and board[4] == board[7] and board[1] == "_":
                        return 1
                    elif board[2] == "H" and board[2] == board[5] and board[8] == "_":
                        return 8
                    elif board[5] == "H" and board[5] == board[8] and board[2] == "_":
                        return 2
                    elif board[2] == "H" and board[2] == board[4] and board[6] == "_":
                        return 6
                    elif board[4] == "H" and board[4] == board[6 ] and board[2] == "_":
                        return 2
                    else:
                        choice = randint(0,8)
                        while board[choice] != "_":
                            choice = randint(0,8)
                        return choice






