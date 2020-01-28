import time
import sys
import random
from gridClass import Grid


def quitFunction(userInput):
    if userInput == 'q' or userInput == 'Q':
        print("\nEXITING GAME \nTHANK YOU FOR PLAYING")
        sys.exit(0)


def randomComputerMode():
    nameInput = input("What is your name? ")
    quitFunction(nameInput)
    if (random.randint(1,2) == 1):  #When we are playing against the computer I want to randomize who will go first. Someitmes the computer will go first and sometimes the player will go first
        playerOne = nameInput
        playerTwo = "CPU"
        print("\n%s you will go first and use BLACK Tokens\n"  % (nameInput))
        print("The CPU will go second and use WHITE Tokens\n")
    else:
        playerOne = "CPU"
        playerTwo = nameInput
        print("\nThe CPU will go first and use BLACK Tokens\n")
        print("%s you will go second and use WHITE Tokens\n" % (nameInput))

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
        
        #Whenever it is the CPU's Turn we will run this block of code so the CPU will place a token on the board
        if pInfo[2] == "CPU":
            selection = random.randint(0,len(possiblePoints) - 1) #Here we select a random index in the possiblePoints list
            coordinate = possiblePoints[selection] #Here we actually get the coordinate from the possiblePoints list
            theBoard.place(coordinate[0],coordinate[1],pInfo[0],pInfo[1]) #Here we place a token on the board based on the random coordinate selected
            turnFlag = not turnFlag
            skipCounter = 0

        
        #When it is the player's turn. We run the same code where we ask the user for coordinate input
        else:
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
