class Board:

    
    
    def __init__(self,player1,player2):
        self.player1=player1
        self.player2=player2
        self.bins=[4,4,4,4,4,4,4,4,4,4,4,4]
        

    def updateBoard(self,player,move):  #moves are from 0 to 5 as array index, player is 1 or 2 */
        
        tempBins=self.bins
        print(tempBins)
        if(player==2):
            move=move+6

        stones=tempBins[move]
        print(move)
        print(stones)
        tempBins[move]=0

        for i in range(1,stones+1):
            print(i)
            print(tempBins[(move+i)%12])
            print(tempBins[(move+i)%12]+1)
            tempBins[(move+i)%12]=tempBins[(move+i)%12]+1
            

        if (self.validConfiguration(tempBins)==True):
            self.bins=tempBins
            print(tempBins)
            print(self.bins)

    def validConfiguration(self,tempBins,player):   #implement later
        if (player==1):
            firstIndex = 0
            else:
                firstIndex = 6
        for i in range (0,5)
            if (tempBins[firstIndex+i]>0):
                return True
        return False
