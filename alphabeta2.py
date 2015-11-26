from stack import Stack
from board import Board
from copy import deepcopy
#from time import localtime


def alphabeta(player,state, score1, score2):

    #d = 7  # definition of depth of search
    s = 12 # enter here the number of holes per player. Finally set to: 12

    fullHouses=2*s
    sumHouse=0
    for i in range(0,2*s):
        if (state[i] == 0):
            fullHouses=fullHouses-1
        else:
            sumHouse = sumHouse+1
    if (fullHouses<14 and sumHouse < 49):
        d=8
    else:
        d=7


    #current_time = localtime()  # set timer for calculation
    #start = current_time.tm_sec
    #if (start>52):
    #    start = start-60
    #end=(start+8)%60


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
            if (state.score2 > (s*4)):  # means: we lost
                delta=-96
            elif (state.score1 > (s*4)):  # means: we won
                delta=96
            else:
                delta = (state.score1 - state.score2)+(state.bins[13] + state.bins[14]+state.bins[15]+state.bins[16])*0.5 #get delta between our score and opponent's score
        else:
            if (state.score1 > (s*4)):  # means: we lost
                delta=-96
            elif (state.score2 > (s*4)):  # means: we won
                delta=96
            else:
                delta = (state.score2 - state.score1)+(state.bins[0] + state.bins[1]+state.bins[2]+state.bins[3])*0.5 #get delta between our score and opponent's score
        return delta

    
    # when to stop going down in tree, returns true or false
    def cutOff(state):
        #current_time2=localtime()
        #tm=current_time2.tm_sec
        #if (tm > 52):
        #    tm=tm-60
        #if (nodeStack.size() == d or state.endGame or tm > end):  # stop when depth-level reached, or game over, or taking too much time
        if (nodeStack.size() == d or state.endGame):
            #if (tm > end):
            #    print("timout rerached")
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
            if (child.bins != nodeStack.peek().bins):
                nodeStack.push(child)
                v=min(v,maxNode(nodeStack.peek(),alpha,beta))
                if v <= alpha:
                    nodeStack.pop()
                    return v
                beta = min(beta, v)
            n=n+1
        nodeStack.pop()  ### taking out the node that generated already all its children
        return v              


                          
    #start
    
    v= -1000
    
    
    m=maxMoves-s
    while(m < maxMoves):
        child = updateState(nodeStack.peek(),m, player)
        if(child.bins != orig.bins):
            nodeStack.push(child)
            temp=v
            v=max(v,minNode(nodeStack.peek(),-1000,1000))
            if (v != temp):
 
                bestMove=m
        m = m+1
    return bestMove
                      
                
