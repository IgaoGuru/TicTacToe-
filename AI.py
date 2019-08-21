from random import randint

class AI:

    def __init__(self, name, winning_phrase):
        self.name = name
        self.winning_phrase = winning_phrase

    def get_play(self, board):
        return None


class AI_Jack_the_random(AI):

    def __init__(self, name = "jack_the_random", winning_phrase = "I have absolutely no idea of what I just did!"):
        AI.__init__(self, name, winning_phrase)

    def get_play(self, board):
        pcmove = randint(0, 8)
        while board[pcmove] != "_":
            pcmove = randint(0, 8)
        return pcmove