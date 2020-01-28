class Grid:
    
    #This initializes the class and creates the grid. The grid is full of X's and we assign the middle pieces with W and B
    # X represents blank space and W represents white tokens and B represents black tokens
    def __init__(self):
        self.grid = [['X' for x in range(8)] for y in range(8)] 
        self.grid[3][3] = 'W'
        self.grid[4][3] = 'B'
        self.grid[3][4] = 'B'
        self.grid[4][4] = 'W'
    
    #This displays the current grid and dipslays coordinate markers on the edge -> (0,1,2,3,4...)
    def printGrid(self):
        print("\nTHE GRID ")
        print("==================")
        print("  0 1 2 3 4 5 6 7")
        for y in range (len(self.grid)):
            row = str(y) + ' '
            for x in range(len(self.grid[0])):
                row += self.grid[x][y] + ' '
            print(row)
            row = ''
        print("")




    #This method is used to check if we are going out of the boundaries of the matrix/grid 
    def inBounds(self,xVal,yVal):
        if (xVal) < 0 or (yVal) < 0 or (xVal) >= len(self.grid) or (yVal) >= len(self.grid):
            return False
        else:
            return True


    #This method is used to place the token on the coordinate provided by the user and then flip all corresponding tokens on the grid. It also prints the grid on the console
    def place(self,xCor,yCor,opColor,color):
            self.grid[xCor][yCor] = color
            self.flip(xCor,yCor,opColor,color)
            self.printGrid()


    def checkPoints(self,opColor,color):
        possiblePoints = [] #This list keep tracks of the the possible coordinates where the user can place tokens on 
        tokenFlips = [] #This keeps track of the number of token flips for each corresponding point in possiblePoints. So the coordinate in "possiblePoint[n]"" will flip "tokenFlips[n]"" tokens

        #Step 1 we need to iterate through the grid and look for tokens of the opposite colour
        for xCor in range (len(self.grid)):
            for yCor in range(len(self.grid[0])): 
                if self.grid[xCor][yCor] == opColor:

                    #Step 2 we need to check the surrounding spaces of the token we found and see if we can find any blank spaces left in the grid. 'X' means it's blank
                    for i in range(-1,2):
                        for j in range(-1,2):
                                xAdj = xCor + i
                                yAdj = yCor + j
                                if self.inBounds(xAdj,yAdj) and self.grid[xAdj][yAdj] == 'X':
                                
                                #Step 3 Once we have found a blank space we need to see if there is a token of the SAME colour on the opposite side of this current token. If we find a token of the same colour we add this coordinate to the possiblePoints list
                                    xOpp = xCor + i * -1
                                    yOpp = yCor + j * -1
                                    numFlips = 1

                                    if self.inBounds(xOpp,yOpp):
                                        if self.grid[xOpp][yOpp] == color:  #If we find that the token on the opposite side is color(same colour), then we know that we know that [xAdj,yAdj] is a possible point to place a token. (This also means that we'll only be flipping one token)
                                            if [xAdj,yAdj] not in possiblePoints:
                                                possiblePoints.append([xAdj,yAdj])
                                                tokenFlips.append(numFlips)
                                        elif self.grid[xOpp][yOpp] == opColor: #If we find that the token on the opposite side is opColor(opposite colour), then it it still possible that [xAdj,yAdj] is a possible point. We need to continue traversing in this direction until we find a token with color in order for it to be a possible point.
                                            while(True):
                                                xOpp += i * -1 
                                                yOpp += j * -1
                                                numFlips += 1
                                                if self.inBounds(xOpp,yOpp):
                                                    if self.grid[xOpp][yOpp] == color:  #If we get to this if statement then that means that after traversing for a little while, we managed to find a token of the same color. Which means [xAdj,yAdj] is a possible point.
                                                        if [xAdj,yAdj] not in possiblePoints:
                                                            possiblePoints.append([xAdj,yAdj])
                                                            tokenFlips.append(numFlips)
                                                        break
                                                    elif self.grid[xOpp][yOpp] == opColor:  #If we get to this if statement then that means we need to keep traversing.
                                                        continue
                                                    else: #If we get to this else statement, then that means that we ran into an empty space meaning that [xAdj,yAdj] is not a possible point
                                                        break
                                                else: #This means we are out of bounds and [xAdj,yAdj] is not a possible point
                                                    break
                                                
        return [possiblePoints,tokenFlips]
                                




    #After placing a token we call this method to check for tokens that need to be flipped
    def flip(self,xCor,yCor,opColor,color):
        for i in range(-1,2):
            for j in range(-1,2):
                if self.inBounds(xCor + i,yCor + j) == False:
                   
                    continue

                if self.grid[xCor + i][yCor + j] == opColor:
                    xTraverse = xCor + i
                    yTraverse = yCor + j
                    coords = [[xTraverse,yTraverse]] #This list keeps track of all the coordinates of the tokens that we need to flip if we do indeed need to flip them
                    while(True): 
                  #This while loop is designed to traverse the grid in the same direction of the opposite token we found. It will keep searching until it goes out of bounds or it finds a same colour token
                        xTraverse += i
                        yTraverse += j
                        if self.inBounds(xTraverse,yTraverse):
                            if (self.grid[xTraverse][yTraverse] == opColor): #This if statement searches for tokens of the opposite colour. If we find one we append that coordinate to the coords list
                                coords.append([xTraverse,yTraverse])
                            elif(self.grid[xTraverse][yTraverse] == color): #This if statment searches for a token of the same colour. If we find then we need to flip all the token in the coords list.
                                for point in coords: 
                                    #This for loop iterates through all the points in coords, flips them to the appropriate colour and then clears the coords list
                                    self.grid[point[0]][point[1]] = color
                                coords.clear()
                                break
                            else: #If we get to this else statement then we know that we have found an empty space, which means we can't flip any token so we clear the coords list and exit the while loop
                                coords.clear()
                                break
                        else: #This means we've gone out of bounds so we need to also clear the coords list and exit the while loop
                            coords.clear()
                            break
                    

    #This method iterates through the contents of the grid and counts the number of white and black tokens
    #It then prints out on the console, who won the game. (Whoever has more tokens wins)               
    def whoWon(self,p1,p2):
        whiteTokens = 0
        blackTokens = 0
        for x in range (len(self.grid)):
            for y in range(len(self.grid[0])):
                if self.grid[x][y] == 'W':
                    whiteTokens += 1
                elif self.grid[x][y] == 'B':
                    blackTokens += 1

        if whiteTokens > blackTokens:
            print("Congratulations %s you have won the game :D (%d White Tokens)" % (p2,whiteTokens))
        elif whiteTokens < blackTokens:
            print("Congratulations %s you have won the game :D (%d Black Tokens)" % (p1,blackTokens))
        else:
            print("WOW IT'S A TIE THIS IS INCREDIBLE")
   

