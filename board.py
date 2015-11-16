from copy import deepcopy
class Board:

    score1=0
    score2=0
    
    def __init__(self,player1,player2):
        self.player1=player1
        self.player2=player2
        # self.bins=[1, 3, 2, 4, 0, 6, 0, 0, 0, 0, 3, 7] For testing
        self.bins=[4,4,4,4,4,4,4,4,4,4,4,4]
        
    def collectPoints(self,player,lastAffected,tempBins):   #TO TEST keep track of how much in all
        lastAffected=lastAffected+48

        i=lastAffected
        # while(self.ownBin(player,i%12)): #This would be OK if you could capture from opponent even if you end up in your own hause
        #           print("Step ",i," backward")
        #           i=i-1

        if (self.ownBin(player,i%12)):
            print("Step ",i," took to my own house")
            return 0
        
        points=0
        ongoingCollection=True

        while(ongoingCollection):
            print("Considering bin ", i%12)
            if ((not self.ownBin(player,i%12)) and ((tempBins[i%12] == 2) or (tempBins[i%12] == 3))):
                points = points + tempBins[i%12]
                print("Earning ", tempBins[i%12])
                tempBins[i%12] = 0
                print("Now I have ",points, " and the board is ", tempBins)
                i=i-1
            else:
                print("Stopping!")
                ongoingCollection=False
                if (self.ownBin(player,i%12)):
                    print("Ended up in own houses ", i%12)
                elif ((tempBins[i%12] != 2) and (tempBins[i%12] != 3)):
                    print("Stones neither 2 nor 3", tempBins[i%12])

        if(player==1):
            self.score1=self.score1+points
        else:
            self.score2=self.score2+points
            
        return points


    def updateBoard(self,player,move):  #moves are from 0 to 5 as array index, player is 1 or 2
        
        tempBins=deepcopy(self.bins)
        
        if(player==2):
            move=move+6

        stones=tempBins[move]
        tempBins[move]=0

        index = 1
        while (index<=stones):
            if (((move+index)%12)!=(move%12)):
                tempBins[(move+index)%12]=tempBins[(move+index)%12]+1
                index = index + 1
            else:
                stones = stones + 1
                index = index + 1

        earnedPoints = self.collectPoints(player,(stones+move)%12,tempBins)

        if (self.validConfiguration(tempBins,player)):
            print("Valid configuration found. Changing from ", self.bins, " to ", tempBins)
            self.bins=deepcopy(tempBins)
            print("Earned point ",earnedPoints)
            print("Player 1 score", self.score1)
            print("Player 2 score", self.score2)
        else:
            print("Invalid configuration", tempBins)
            print("Original configuration unchanged", self.bins)

    def validConfiguration(self,tempBins,player):   #to be tested
        if (player==1):
            firstIndex = 0
        else:
            firstIndex = 6
            
        for i in range (0,6):
            if (tempBins[firstIndex+i]>0):
                return True
        return False


    def ownBin(self,player,ownbin):
        return(((player==1) and (0<=ownbin) and (ownbin<=5)) or ((player==2) and (6<=ownbin) and (ownbin<=11)))


    def printBoard():
        return True    # implement later
