class AbstractPlayer():

    def __init__(self,name):
        self.name=name

    def move(self,boardState,player):

        throw("method not implemented")


class AIPlayer(AbstractPlayer):

    def move(self,boardState,player):
        newmove=minmax()
        return newmove


class OpponentPlayer(AbstractPlayer):

    def move(self,boardState,player):
        newmove = 0
        while(not (1 <= newmove <= 6)):
            newmove=int(input())
        return newmove




