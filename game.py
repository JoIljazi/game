from board import Board
from player import AIPlayer
from player import OpponentPlayer


def play(playerA,playerB):

        order = input("who plays first? press 1 for our AIplayer and 2 for OpponentPlayer")
        if (order=="2"):
            player0=playerB
            player1=playerA
        else:
            player0=playerA
            player1=playerB

        myBoard=Board(player0,player1)
        myBoard.printBoard(player0.name, player1.name)
        playerNumber = 1
        end=False
        while (not end):
            print()
            if (playerNumber == 1):
                print("your turn, enter no. 1 to ", myBoard.s, ": ", player0.name)
                move = 0
                init = True
                while(myBoard.bins[move] == 0 or init):     # mkae sure that no empty field is selected
                    move = player0.move(myBoard, player0) - 1   # minus 1 because of array structure
                    init = False
                myBoard.updateBoard(playerNumber,move)
            elif (playerNumber == 2):
                print("your turn, enter no. ", myBoard.s+1, "to ", myBoard.s*2,": ", player1.name)
                move = 0
                init = True
                while(myBoard.bins[move] == 0 or init):   # mkae sure that no empty field is selected
                    move = player1.move(myBoard, player1) - 1   # minus 1 because of array structure
                    init = False
                myBoard.updateBoard(playerNumber,move)

            # print game status:
            print("current game status:")
            myBoard.printBoard(player0.name, player1.name)
            #print("beens player ", player0.name, ": ", myBoard.getScoreStatus(1))
            #print("beens player ", player1.name, ": ", myBoard.getScoreStatus(2))

            #check end - winner or draw:
            if(myBoard.endGame):
                end=True

            # change active player
            playerNumber=(playerNumber % 2) +1


def main():

    print()
    print("welcome to new game")
    gameMode = input("single-Player-Mode: 1; multi-Player-Mode: 2; mode: ") # for test purposes

    # built instance of AI player, as this is different dep. on gameMode:
    if (gameMode=="1"):
        myAI=AIPlayer("AI")
    elif (gameMode=="2"):
        aiName = input("give the name of one player (AIPlayer): ")
        myAI=OpponentPlayer(aiName)
    # build rest (independent from gameMode) and start:
    opponentName = input("give the name of opponent player: ")
    myOpponent=OpponentPlayer(opponentName)
    play(myAI, myOpponent)



if __name__ == "__main__":
    main()
    
