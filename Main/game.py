class Player :
    def __init__(self, name , token):
        self.name = name
        self.token = token
    def display (self):
        s ="It Your Turn " + str(self.name)
        return s
class Game(Player):
    def __init__(self, name, token, board):
        super().__init__(length, width)
        self.board = board
def board():
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(gameboard[0], gameboard[1], gameboard[2]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(gameboard[3], gameboard[4], gameboard[5]))
    print('\t_____|_____|_____')
    print("\t     |     |") 
    print("\t  {}  |  {}  |  {}".format(gameboard[6], gameboard[7], gameboard[8]))
    print("\t     |     |")
    print("\n")

def winning (gameboard):
    if gameboard[0]==  'X' and gameboard[1] == 'X' and gameboard[2] == 'X':
        print('X wins')
        return True
    elif gameboard[3]==  'X' and gameboard[4] == 'X' and gameboard[5] == 'X':
        print('X wins')
        return True
    elif gameboard[6]==  'X' and gameboard[7] == 'X' and gameboard[8] == 'X':
        print('X wins')
        return True
    elif gameboard[0]==  'X' and gameboard[3] == 'X' and gameboard[6] == 'X':
        print('X wins')
        return True
    elif gameboard[1]==  'X' and gameboard[4] == 'X' and gameboard[7] == 'X':
        print('X wins')
        return True
    elif gameboard[2]==  'X' and gameboard[5] == 'X' and gameboard[8] == 'X':
        print('X wins')
        return True
    elif gameboard[0]==  'X' and gameboard[4] == 'X' and gameboard[8] == 'X':
        print('X wins')
        return True
    elif gameboard[2]==  'X' and gameboard[4] == 'X' and gameboard[6] == 'X':
        print('X wins')
        return True
    if gameboard[0]==  'O' and gameboard[1] == 'O' and gameboard[2] == 'O':
        print('o wins')
        return True
    elif gameboard[3]==  'O' and gameboard[4] == 'O' and gameboard[5] == 'O':
        print('O wins')
        return True
    elif gameboard[6]==  'O' and gameboard[7] == 'O' and gameboard[8] == 'O':
        print('o wins')
        return True
    elif gameboard[0]==  'O' and gameboard[3] == 'O' and gameboard[6] == 'O':
        print('o wins')
        return True
    elif gameboard[1]==  'O' and gameboard[4] == 'O' and gameboard[7] == 'O':
        print('o wins')
        return True
    elif gameboard[2]==  'O' and gameboard[5] == 'O' and gameboard[8] == 'O':
        print('o wins')
        return True
    elif gameboard[0]==  'O' and gameboard[4] == 'O' and gameboard[8] == 'O':
        print('o wins')
        return True
    elif gameboard[2]==  'O' and gameboard[4] == 'O' and gameboard[6] == 'O':
        print('o wins')
        return True
    else:
        return False
   



def XO():
    while True:
     xo = input(f'Do you want to be X or O: ')
     xo.capitalize()
     if  xo == 'X' or xo == 'O':   
          return xo
     else:
          print('\nInvaid input X or O!')



player1n = input('What is your name Player 1: ')
player1t = XO()
player2n = input('What is your name Player 2: ') 

if player1t == 'X':
    player2t = 'O'
else:
    player2t = 'X'

gameboard = [' ' for x in range(9)] # Clear Board
# gameboard[0] = 'X'
# gameboard[1] = 'X'
# board()

player1= Player(player1n, player1t)
player2= Player(player2n, player2t)

turn = 1
while turn != 10:
    if (turn % 2) != 0:
        print(player1.display())
        input("your Move :")
        # print(player1.token) Testline
        board()
        wincheck =  winning(gameboard)
        if wincheck == True:
            break
        turn +=1
    
    else:
        print(player2.display())
        input("your Move :")
        # print(player2.token) Testline
        gameboard[1] = 'O'
        gameboard[4] = 'O'
        gameboard[7] = 'O'
        board()
        wincheck =  winning(gameboard)
        if wincheck == True:
            break
        turn +=1
if turn == 10:
    print('Draw')



