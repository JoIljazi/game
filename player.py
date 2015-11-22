import minmaxCut
class AbstractPlayer():

    def __init__(self,name):
        self.name=name

    def move(self,boardState,player):

        throw("method not implemented")


class AIPlayer(AbstractPlayer):

    def move(self,boardState,player):
        #print("TEST *************** ", boardState.score1, boardState.score2)
        newmove=minmaxCut.minmax(player, boardState.bins, boardState.score1, boardState.score2)
        return (newmove+1)


class OpponentPlayer(AbstractPlayer):

    def move(self,boardState,player):
        newmove=int(input())
        return newmove




