from copy import deepcopy
class Board:
 
    score1=0
    score2=0
    endGame=False
    moveNo=0
    s = 12 # enter here the number of holes per player. Finally set to: 12
    b = 96 # enter here the number of beans in total. Finally set to: 96

    
    def __init__(self, structure, score1, score2):
        self.bins = structure
        self.score1 = score1
        self.score2 = score2
        
    def collectPoints(self,player,lastAffected,tempBins):   
        lastAffected=lastAffected+self.b  # why?!?
#this is ok
#and this
#a new request
#this doesnt affect the code
#python is ok

        i=lastAffected

        if (self.ownBin(player,i%(self.s*2))):
            #print("Step ",i," took to my own house")
            return 0
        
        points=0
        ongoingCollection=True

        while(ongoingCollection):
            if ((not self.ownBin(player,i%(self.s*2))) and ((tempBins[i%(self.s*2)] == 2) or (tempBins[i%(self.s*2)] == 3))):
                points = points + tempBins[i%(self.s*2)]
                tempBins[i%(self.s*2)] = 0
                i=i-1
            else:
                ongoingCollection=False

        if(player==1):
            self.score1=self.score1+points
        else:
            self.score2=self.score2+points
            
        return points


    def updateBoard(self,player,move):  #moves are from 0 to 5 as array index, player is 1 or 2
        
        self.moveNo = self.moveNo+1
        tempBins=deepcopy(self.bins) # copy by value
        
        stones=tempBins[move]
        tempBins[move]=0

        # move the stones:
        index = 1
        while (index<=stones):
            if (((move+index)%(self.s*2))!=(move%(self.s*2))):  # avoid moving stones to house where they came from
                tempBins[(move+index)%(self.s*2)]=tempBins[(move+index)%(self.s*2)]+1
                index = index + 1
            else:               # in case it's the house from move, increase index and stones by one (because of condition)
                stones = stones + 1
                index = index + 1

        earnedPoints = self.collectPoints(player,(stones+move)%(self.s*2),tempBins)

        if (self.validConfiguration(tempBins,player) and stones >0):                              #if valid move, keep it
            self.bins=deepcopy(tempBins)
        

            if(player==1):
                playerBins=deepcopy(tempBins[0:self.s])
            else:
                playerBins=deepcopy(tempBins[self.s:(self.s*2)])
            self.checkStatus(tempBins,player)


    def validConfiguration(self,tempBins,player):   #it should check if we are causing starv in opponent
        if (player==1):
            firstIndex = self.s
        else:
            firstIndex = 0
            
        for i in range (0,self.s):
            if (tempBins[firstIndex+i]>0):  
                return True
        return False


    def ownBin(self,player,ownbin): # returns true/false whether the accessed object is one's own bin
        return(((player==1) and (0<=ownbin) and (ownbin<=(self.s-1))) or ((player==2) and (self.s<=ownbin) and (ownbin<=((self.s*2)-1))))


    def checkStatus(self,tempBins,player): # check whether game is over
        if(self.score1 >(self.b / 2) or self.score2 >(self.b / 2)):   ### add the end of game for non available moves by itself not as result of big slam!!! DISCUSS THIS TYPE OF EVENT
            self.endGame=True
        # check whether there are still possible moves
        if (player==1):
            lastIndex = self.s *2
            firstIndex = self.s
        else:
            lastIndex = self.s
            firstIndex = 0

        opBeans = sum(tempBins[firstIndex:lastIndex])
        if (opBeans == 0):
            i = 1
            while (i <= self.s):
                if (tempBins[lastIndex-i] >= i):  # compare the no. beans in a hole  with distance to opponent's holes, starting with closest to opponent
                    break
                else:
                    i = i+1
            else:
                print("no possible move that doesn't starve the opponent. Game over.")
                self.endGame=True

    def printBoard(self, player1Name, player2Name): # removed: aBoard
        housesP1 = list(range(1, self.s+1))
        housesP2 = list(reversed(range(self.s +1, self.s*2+1)))
        revList = list(reversed(self.bins[self.s:(self.s*2)]))
        print(player1Name, ":    ", housesP1)
        print(player1Name, ": -> ", self.bins[0:self.s], " =>")
        print(player2Name, ": <- ", revList, " <=")
        print(player2Name, ":    ", housesP2)
        print("won beans player ", player1Name, ": ", self.score1)
        print("won beans player ", player2Name, ": ", self.score2)
        print("played moves: ", self.moveNo)


