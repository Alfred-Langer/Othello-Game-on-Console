import time
import sys
import random
from gridClass import Grid


def quitFunction(userInput):
    if userInput == 'q' or userInput == 'Q':
        print("\nEXITING GAME \nTHANK YOU FOR PLAYING")
        sys.exit(0)


def randomComputerVsComputerMode():
    if (random.randint(1,2) == 1):  #When we are playing against the computer I want to randomize who will go first. Someitmes the computer will go first and sometimes the player will go first
        playerOne = "CPU 1"
        playerTwo = "CPU 2"
        print("CPU 1 will go first and use BLACK Tokens\n")
        print("CPU 2 will go second and use WHITE Tokens\n")
    else:
        playerOne = "CPU 2"
        playerTwo = "CPU 1"
        print("CPU 2 will go first and use BLACK Tokens\n")
        print("CPU 1 will go second and use WHITE Tokens\n")

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

    print("LET THE GAME BEGIN!!!!!")
    print("==================================================")
    theBoard.printGrid()


    while (True):
        pInfo = turnOperations(turnFlag) #playerInfo keeps tracks of the opColor, color, and the name of the player who's turn it is

        if skipCounter == 2:
            print("THE GAME IS OVER")
            break

        print("%s it is your turn" % (pInfo[2]))
        possiblePoints = theBoard.checkPoints(pInfo[0],pInfo[1])[0]
        print("Possible Coordinates: " + str(possiblePoints))
        if len(possiblePoints) == 0:
            print("Oops, there are no moves available for your turn, %s\n" % (pInfo[2]))
            time.sleep(2)
            skipCounter += 1
            turnFlag = not turnFlag #Flips the flag to switch to the next player
            continue
        
        
        #This block of code is the CPU code 

        selection = random.randint(0,len(possiblePoints) - 1) #Here we select a random index in the possiblePoints list
        coordinate = possiblePoints[selection] #Here we actually get the coordinate from the possiblePoints list
        theBoard.place(coordinate[0],coordinate[1],pInfo[0],pInfo[1]) #Here we place a token on the board based on the random coordinate selected
        turnFlag = not turnFlag
        skipCounter = 0

        

    theBoard.whoWon(playerOne,playerTwo)
    input("Press any key to exit the program")
    sys.exit(0)
