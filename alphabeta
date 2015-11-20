from stack import Stack
from board import Board
from copy import deepcopy

def alphabeta(player,state, score1, score2):

    d = 2   # definition of depth of search
    s = 6 # enter here the number of holes per player. Finally set to: 12


    if (player==1):
        maxMoves=s
        minMoves=2*s
    else:
        maxMoves=2*s
        minMoves=s

    ## evalFunctions
    def evalFunction(state):
        if (player==1):
            delta = state.score1 - state.score2
        else:
            delta = state.score2 - state.score1
        return delta

    
    # when to stop going down in tree, returns true or false
    def cutOff(state):
        if (nodeStack.size() == d or state.endGame):
            return True
        else:
            return False

    # update state and create new child
    def updateState(board,move, player):
        tempBoard = Board(board.bins, board.score1, board.score2)
        tempBoard.updateBoard(player, move)
        return tempBoard


    def maxNode(state, alpha, beta):
        if(cutOff(state)):
            st=nodeStack.pop()
            return evalFunction(st)
        v= -1000
        o = 0
        while(o < maxMoves):
            child=updateState(nodeStack.peek(),o,player)
            if (child.bins != nodeStack.peek().bins):
                nodeStack.push(child)
                v = max(v, minNode(updateState(state, a), alpha, beta, depth+1))
                if v >= beta:
                    return v
                alpha = max(alpha, v)
        return v

    def minNode(state, alpha, beta, depth):
        if(cutOff(state)):
            st=nodeStack.pop()
            return evalFunction(st)
        v= -1000
        o = 0
        while(o < maxMoves):
            child=updateState(nodeStack.peek(),o,player)
            if (child.bins != nodeStack.peek().bins):
                nodeStack.push(child)
                v = min(v, minNode(updateState(state, a), alpha, beta, depth+1))
                if v >= beta:
                    return v
                alpha = min(alpha, v)
        return v

    

#start
    results={}
    v= -1000
    nodeStack=Stack()
    orig=Board(state, score1, score2)
    nodeStack.push(orig)
    m=0
    while(m < maxMoves):
        child = updateState(nodeStack.peek(),m, player)
        if(child.bins != orig.bins):
            nodeStack.push(child)
            temp=v
            v=max(v,minNode(nodeStack.peek()))
            if (v != temp):
                results["value"]=v
                results["move"]=m
        m = m+1
    return results["move"]
       


