import minmaxCut
import alphabeta
import alphabeta2
class AbstractPlayer():

    def __init__(self,name):
        self.name=name

    def move(self,boardState,player):

        print("method not implemented")


class AIPlayer1(AbstractPlayer):

    def move(self,boardState,player):
        newmove=alphabeta.alphabeta(player, boardState.bins, boardState.score1, boardState.score2)
        return (newmove+1)

class AIPlayer2(AbstractPlayer):

    def move(self,boardState,player):
        newmove=alphabeta2.alphabeta(player, boardState.bins, boardState.score1, boardState.score2)
        return (newmove+1)


class OpponentPlayer(AbstractPlayer):

    def move(self,boardState,player):
        newmove=int(input())
        return newmove




