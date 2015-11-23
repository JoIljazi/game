from stack import Stack
from board import Board
from copy import deepcopy
#from timeit import default_timer as timer

def alphabeta(player,state, score1, score2):

    d = 4  # definition of depth of search
    s = 6 # enter here the number of holes per player. Finally set to: 12


    #start = timer()


    nodeStack=Stack()
    orig=Board(state, score1, score2)
    nodeStack.push(orig)


    if (player==1):
        maxMoves=s
        minMoves=s*2
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
        if (nodeStack.size() == d or state.endGame):  # add time constraint
            return True
        else:
            return False

    # update state and create new child
    def updateState(board,move, player):
        tempBoard = Board(board.bins, board.score1, board.score2)
        tempBoard.updateBoard(player, move)
        return tempBoard


    def maxNode(state,alpha,beta):
        if(cutOff(state)):
            st=nodeStack.pop()
            return evalFunction(st)
        v= -1000
        o = maxMoves-s
        while(o < maxMoves):
            child=updateState(nodeStack.peek(),o,player)
            if (child.bins != nodeStack.peek().bins):
                nodeStack.push(child)
                v=max(v,minNode(nodeStack.peek(),alpha,beta))
                if v >= beta:
                    nodeStack.pop()
                    return v
                alpha = max(alpha, v)
            o=o+1

        nodeStack.pop()
        return v

    def minNode(state,alpha,beta):
        if(cutOff(state)):
            st=nodeStack.pop()
            res = evalFunction(st)
            return res
        v= 1000
        n = minMoves-s
        while(n < minMoves):
            child=updateState(nodeStack.peek(),n,((player%2)+1))
            print("from minNode Child is created as:",child.bins)
            if (child.bins != nodeStack.peek().bins):
                nodeStack.push(child)
                v=min(v,maxNode(nodeStack.peek(),alpha,beta))
                if v >= beta:
                    nodeStack.pop()  ### for same reasons
                    return v
                alpha = min(alpha, v)
            n=n+1
        nodeStack.pop()  ### taking out the node that generated already all its children
        return v              


                          
    #start
    
    v= -1000
    alpha= -1000
    beta= 1000
    
    m=maxMoves-s
    while(m < maxMoves):
        child = updateState(nodeStack.peek(),m, player)
        if(child.bins != orig.bins):
            nodeStack.push(child)
            temp=v
            v=max(v,minNode(nodeStack.peek(),alpha,beta))
            if (v != temp):
 
                bestMove=m
        m = m+1
    return bestMove
                      
                
