import time
import sys
from gridClass import Grid


def quitFunction(userInput):
    if userInput == 'q' or userInput == 'Q':
        print("\nEXITING GAME \nTHANK YOU FOR PLAYING")
        sys.exit(0)


def pvpMode():
    playerOne = input("What is the name of Player One? (This player will use Black Tokens) ")
    quitFunction(playerOne)
    playerTwo = input("What is the name of Player Two? (This player will use White Tokens) ")
    quitFunction(playerTwo)

    def turnOperations(flag):
        if (flag == True):
            pInfo = ['W','B',playerOne] #The first element is opColor, the second element is color, and the third element is the name of player
            return pInfo
        else:
            pInfo = ['B','W',playerTwo]
            return pInfo


    theBoard = Grid()
    turnFlag = True
    skipCounter = 0 #If the skip counter becomes 2 then that means there are no possible spaces to put tokens on the grid and the game is over

    theBoard.printGrid()


    while (True):
        pInfo = turnOperations(turnFlag) #playerInfo keeps tracks of the opColor, color, and the name of the player who's turn it is

        if skipCounter == 2:
            print("THE GAME IS OVER")
            break

        print("Player %s it is your turn" % (pInfo[2]))
        possiblePoints = theBoard.checkPoints(pInfo[0],pInfo[1])[0]
        print("Possible Coordinates: " + str(possiblePoints))
        if len(possiblePoints) == 0:
            print("Oops, there are no moves available for your turn Player %s\n" % (pInfo[2]))
            time.sleep(2)
            skipCounter += 1
            turnFlag = not turnFlag #Flips the flag to switch to the next player
            continue
        
        while(True):
            xCor = input("Please enter the X value of your coordinate ")
            quitFunction(xCor)
            yCor = input("Please enter the Y value of your coordinate ")
            quitFunction(yCor)
            if xCor.isdigit() and yCor.isdigit() and ([int(xCor),int(yCor)] in possiblePoints):
                theBoard.place(int(xCor),int(yCor),pInfo[0],pInfo[1])
                turnFlag = not turnFlag
                skipCounter = 0
                break
            else:
                print("Invalid coordinate please try again")
        

    theBoard.whoWon(playerOne,playerTwo)
    input("Press any key to exit the program")
    sys.exit(0)





