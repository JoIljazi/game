class Board:

    
    
    def __init__(self,player1,player2):
        self.player1=player1
        self.player2=player2
        self.bins=[4,4,4,4,4,4,4,4,4,4,4,4]
        

    def updateBoard(self,player,move):  #moves are from 0 to 5 as array index, player is 1 or 2 */
        
        tempBins=self.bins
        if(player==2):
            move=move+6

        stones=tempBins[move]
        tempBins[move]=0

        for i in range(1,stones+1):
            tempBins[(move+i)%12]=tempBins[(move+i)%12]+1

        earnedPoints = collectPoints(player,(stones+move)%12,tempBins)

        if (self.validConfiguration(tempBins)==True):
            self.bins=tempBins
            print(self.bins)

    def validConfiguration(self,tempBins,player):   #to be tested
        if (player==1):
            firstIndex = 0
            else:
                firstIndex = 6
        for i in range (0,5)
            if (tempBins[firstIndex+i]>0):
                return True
        return False

    def collectPoints(player,lastAffected,tempBins):   #TO TEST keep track of how much in all
        lastAffected=lastAffected+12

        i=lastAffected
        while(ownBin(player,i%12)):
            i=i-1

        points=0
        ongoingCollection=True

        while(ongoingCollection):
            if (!ownBin(player,i%12)) && ((tempBins[i] == 2) || (tempBins[i] == 3)):
                points = points + tempBins[i]
                tempBins[i] = 0
                i=i+1
                else:
                    ongoingCollection=False

        return points


    def ownBin(player,ownbin):
        return(((player==1) && (0<=ownbin) && (ownbin<=5)) || ((player==2) && (6<=ownbin) && (ownbin<=11)))

    


    def printBoard():
        return True    # implement later
