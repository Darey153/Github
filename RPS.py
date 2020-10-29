import random

def RPS():
    cMove = random.randint(1,4)
    if cMove == 1:
        cMove_Rock()
    elif cMove == 2:
        cMove_Paper()
    else:
        cMove_Scissors()
def cMove_Rock():
    Player_Move = input('type: R  for ROCK, P for Paper or S for Scissors.')
    if Player_Move == 'R' :
        print ('TIE, computer chose Rock')
        try_again()
    elif Player_Move == 'P':
        print ('WIN, computer chose Rock')
        try_again()
    elif Player_Move == 'S':
        print ('YOU LOSE, computer chose Rock')
        try_again()
    else:
        print('Try again, make sure the letter are upper case')
        cMove_Rock()

def cMove_Paper():
    Player_Move = input('type: R  for ROCK, P for Paper or S for Scissors.')
    if Player_Move == 'R' or 'r':
        print ('YOU LOSE, computer chose Paper')
        try_again()
    elif Player_Move == 'P' or 'p':
        print ('TIE, computer chose Paper')
        try_again()
    elif Player_Move == 'S' or 's':
        print ('WiIN, computer chose Paper')
        try_again()
    else:
        print('Try again, make sure the letter are upper case')
        cMove_Paper()

def cMove_Scissors():
    Player_Move = input('type: R  for ROCK, P for Paper or S for Scissors.')
    if Player_Move == 'R':
        print ('WIN, computer chose Scissors')
        try_again()
    elif Player_Move == 'P':
        print ('YOU LOSE, computer chose Scissors')
        try_again()
    elif Player_Move == 'S':
        print ('TIE, computer chose Scissors')
        try_again()
    else:
        print('Try again, make sure the letter are upper case')
        cMove_Scissors()

def try_again():
    choice = input('Type Y if you would like to play again and N to stop the game:')
    if choice == 'y' or choice == 'Y':
        print('You really want to win??')
        RPS()
    elif choice == 'N' or choice == 'n' :
        print ('You can always try again :)')
        quit()
    else:
        print ('Try again!!!!!!!')
        try_again()

RPS()
    
