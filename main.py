import random

ttboard = ["-", "-", "-",
           "-", "-", "-",
           "-", "-", "-"]

winner = None
GameRunning = True
c_player = "X"

def printdis(ttboard):
    print(ttboard[0], "|", ttboard[1],"|", ttboard[2])
    print("_________")
    print(ttboard[3], "|",ttboard[4], "|",ttboard[5])
    print("_________")
    print(ttboard[6],"|", ttboard[7],"|", ttboard[8])

def playerInput(ttboard):
    tt_input = int(input("Enter a number a 1-9: "))
    if tt_input >= 1 and tt_input<=9 and ttboard[tt_input-1]=="-":
        ttboard[tt_input-1]=c_player
    elif tt_input >= 1 and tt_input<=9 and ttboard[tt_input-1] !="-":
        print("Choose a different number! The space is already Occupied.")
    else:
        print("Error!!! Please enter a number 1 through 9: ")

def WinHorizontal(ttboard):
    global winner
    if ttboard[0] == ttboard[1] == ttboard[2] and ttboard[1] != "-":
        winner = ttboard[1]
        return True
    elif ttboard[3] == ttboard[4] == ttboard[5] and ttboard[3] != "-":
        winner = ttboard[3]
        return True
    elif ttboard[6] == ttboard[7]==ttboard[8] and ttboard[6] != "-":
        winner = ttboard[6]
        return True
    
def WinVertical(ttboard):
    global winner
    if ttboard[0] == ttboard[3] == ttboard[6] and ttboard[0] != "-":
        winner = ttboard[0]
        return True
    elif ttboard[1] == ttboard[4] == ttboard[7] and ttboard[1] != "-":
        winner = ttboard[1]
        return True
    elif ttboard[2] == ttboard[5] == ttboard[8] and ttboard[2] !="-":
        winner = ttboard[2]
        return True
    
def WinDiagonal(ttboard):
    global winner
    if ttboard[0] == ttboard[4] == ttboard[8] and ttboard[0] != "-":
        winner = ttboard[0]
        return True
    elif ttboard[2] == ttboard[4] == ttboard[6] and ttboard[2] != "-":
        winner = ttboard[0]
        return True
    
def Chck_Win():
    
    if WinDiagonal(ttboard) or WinHorizontal(ttboard) or WinVertical(ttboard):
        print(f"The Winner is {winner}!!!")
        GameRunning = False
        exit()
    
def ChckTie(ttboard):
    global GameRunning
    if "-" not in ttboard:
        printdis(ttboard)
        print("It's a Tie!!!")
        GameRunning = False

def Sw_Player():
    global c_player
    if c_player == "X":
        c_player = "O"
    else:
        c_player = "X"

def comp_player(ttboard):
    while c_player=="O":
        pos = random.randint(0,8)
        if ttboard[pos] == "-":
            ttboard[pos]="O"
            Sw_Player()


printdis(ttboard)
while GameRunning:

    playerInput(ttboard)
    Sw_Player()
    Chck_Win()
    ChckTie(ttboard)
    comp_player(ttboard)
    printdis(ttboard)
    Chck_Win()
    ChckTie(ttboard)
