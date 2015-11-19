import Stack

def minmax(player,state,d):

    nodeStack=Stack()
    nodeStack.push(state)

    if (player==1):
        maxMoves=range(0,6)
        minMoves=range(6,12)
    else:
        maxMoves=range(6,12)
        minMoves=range(0,6)
    
    


    def maxNode(state):
        if(cutOff(state,depth)):
            nodeStack.pull()
            return evalFunction()
        v= -infinity
        while(maxMoves):
            child=updateState(nodeStack.peek(),move,player)
            if (child != nodeStack.peek()):
                nodeStack.push(child)
                v=max(v,minNode(nodeStack.peek())
            move=move+1

        return v

    def minNode(state):
        if(cutOff(state,depth)):
            nodeStack.pull()
            return evalFunction()
        v= infinity
        while(minMoves):
            child=updateState(nodeStack.peek(),move,((player%2)+1))
            if (child != nodeStack.peek()):
                nodeStack.push(child)
                v=min(v,maxNode(nodeStack.peek())
            move=move+1

        return v              


                          
    #start
    results={}
    v= -infinit
    while(maxMoves):
        move=maxMoves
        child=updateState(nodeStack.peek(),move)
        if(child !=nodeStack.peek()):
            nodeStack.push(child)
            v=max(v,minNode(nodeStack.peek()))
            results[move]=v
    return decision(results,v)
                      
                
