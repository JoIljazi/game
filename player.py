class AbstractPlayer():

    def __init__(self,name):
        self.name=name

    def move(boardState,player):

        throw("method not implemented")


class AIPlayer(AbstractPlayer):

    def move(boardState,player):
        newmove=minmax()
        return newmove


class OpponentPlayer(AbstractPlayer):

    def move(boardState,player):
        newmove=int(input())
        return newmove



