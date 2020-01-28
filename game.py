import sys
from othelloPVP import pvpMode
from othelloRandomComputer import randomComputerMode
from othelloGreedyComputer import greedyComputerMode
from othelloRandomComputerVsRandomComputer import randomComputerVsComputerMode
#This function is used to exit the program. If the user enters in q or Q at any point the program requests input, then the program will exit


print("\nWELCOME TO OTHELLO (Enter 'q' or 'Q' to exit the program)")
print("===========================================================\n")

while(True):
    print("[0] Player vs Player")
    print("[1] Player vs Computer")
    print("[2] Player vs Greedy Computer")
    print("[3] Random Computer vs Random Computer\n")
    choice = input("What mode would you like to play? ")
    if (choice == '0'):
        pvpMode()
    elif (choice == '1'):
        randomComputerMode()
    elif (choice == '2'):
        greedyComputerMode()
    elif (choice == '3'):
        randomComputerVsComputerMode()
    elif(choice == 'q' or choice == 'Q'):
        print("\nEXITING GAME \nTHANK YOU FOR PLAYING")
        sys.exit()
    else:
        print("Invalid choice please select again")