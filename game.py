from board import Board
from player import AIPlayer1
from player import AIPlayer2
from player import OpponentPlayer


def play(playerA,playerB, order):

        s = 12 # enter here the number of holes per player. Finally set to: 12

        if (order=="2"):
            player0=playerB
            player1=playerA
        else:
            player0=playerA
            player1=playerB

        myBoard=Board([4] * (2 * s), 0, 0)
        #myBoard=Board([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 11, 1, 5, 0, 1, 0, 0, 0, 0, 0, 23, 0], 6, 48)  # for setting up again
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
                    move = player0.move(myBoard, playerNumber) - 1   # minus 1 because of array structure
                    init = False
                myBoard.updateBoard(playerNumber,move)
                print()
                print("player", player0.name, "played field")
                print()
                print(move+1)
            elif (playerNumber == 2):
                print("your turn, enter no. ", myBoard.s+1, "to ", myBoard.s*2,": ", player1.name)
                move = 0
                init = True
                while(myBoard.bins[move] == 0 or init):   # mkae sure that no empty field is selected
                    move = player1.move(myBoard, playerNumber) - 1   # minus 1 because of array structure
                    init = False
                myBoard.updateBoard(playerNumber,move)
                print()
                print("player ", player1.name, "played field")
                print()
                print(move+1)

            # print game status:
            print("current game status:")
            myBoard.printBoard(player0.name, player1.name)

            #check end - winner or draw:
            if(myBoard.endGame):
                end=True
                print("Game is over.")

            # change active player
            playerNumber=(playerNumber % 2) +1


def main():

    print()
    print("welcome to new game")
    #gameMode = input("single-Player-Mode: 1; multi-Player-Mode: 2; mode: ") # for test purposes

    # build rest (independent from gameMode) and start:
    opponentName = input("give the name of opponent player: ")
    order = input("who plays first? press 1 for our AIplayer and 2 for OpponentPlayer")

    #create players
    if (order=="1"):
        myAI=AIPlayer1("AI")
    else:
        myAI=AIPlayer2("AI")
    myOpponent=OpponentPlayer(opponentName)

    play(myAI, myOpponent, order)



if __name__ == "__main__":
    main()
    
