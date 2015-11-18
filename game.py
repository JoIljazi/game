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
        playerNumber = 1
        end=False
        while (not end):
# to be done:
            if (playerNumber == 1):
                print("your turn, enter no. 1 to 6:", player0.name)
                move = player0.move(myBoard, player0) - 1   # minus 1 because of array structure
                myBoard.updateBoard(playerNumber,move)
            elif (playerNumber == 2):
                print("your turn, enter no. 1 to 6:", player1.name)
                move = player1.move(myBoard, player1) - 1   # minus 1 because of array structure
                myBoard.updateBoard(playerNumber,move)
            playerNumber=(playerNumber % 2) +1      # change active player
            #temp=tempPlayer0   # what is this for?
            #tempPlayer0 = tempPlayer1   # what is this for?
            #tempPlayer1 = temp   # what is this for?

            #check end - winner or draw:
            if(myBoard.endGame):
                end=True


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
    
