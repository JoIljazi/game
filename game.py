import Board
import AIPlayer
import OpponentPlayer

def mainGame():

    print()
    opponentName=raw_input("welcome to new game, give the name of opponent player")

    myAI=AIPlayer()
    myOpponent=OpponentPlayer()
    play(myAI,myOpponent)

    def play(player0,player1):
        
        order = input("who plays first? press 0 for our AIplayer and 1 for OpponentPlayer")
        if (order==1):
                  tempPlayer0=player1
                  tempPlayer1=player0
              else:
                  tempPlayer0=player0
                  tempPlayer1=player1
              
        myBoard=Board(tempPlayer0,tempPlayer1)
        playerNumber = 0
        while (!end)
            move=tempPlayer0.move()
            myBoard.updateBord(playerNumber,move)
            playerNumber=(playerNumber+1)%2
            temp=tempPlayer0
            tempPlayer0 = tempPlayer1
            tempPlayer1 = temp
            #check end - winner or draw 

            
    
