print ("test")
print ('testtest')

'''class Player :
    def __init__(self, name , token):
        self.name = name
        self.token = token
# class Game(Player):
#     # def __init__(self, name, token, board):
#     #     super().__init__(length, width)
#     #     self.board = board
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


player1n = input('What is your name Player 1: ')
player1t = input('Do you wnat to use the X or O: ')
player2n = input('What is your name Player 2: ') 

if player1t == 'X':
    player2t = 'O'
else:
    player2t == 'X'

gameboard = [' ' for x in range(9)]
gameboard[0] = 'X'
gameboard[1] = 'X'
board()

player1= Player(player1n, player1t)
player2= Player(player2n, player2t)

print('Upload')'''

'''class Player :
    def __init__(self, name , token):
        self.name = name
        self.token = token
# class Game(Player):
#     # def __init__(self, name, token, board):
#     #     super().__init__(length, width)
#     #     self.board = board
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

player1n = input('What is your name Player 1: ')
player1t = input('Do you wnat to use the X or O: ')
player2n = input('What is your name Player 2: ') 

if player1t == 'X':
    player2t = 'O'
else:
    player2t == 'X'

gameboard = [' ' for x in range(9)]
gameboard[0] = 'X'
gameboard[1] = 'X'
board()

player1= Player(player1n, player1t)
player2= Player(player2n, player2t)

print('Upload')'''
gameboard = ['o','x','x','o','o','o','o','x','o']


def winning (gameboard):
    if gameboard[0]==  'x' and gameboard[1] == 'x' and gameboard[2] == 'x':
        print('X wins')
    elif gameboard[3]==  'x' and gameboard[4] == 'x' and gameboard[5] == 'x':
        print('X wins')
    elif gameboard[6]==  'x' and gameboard[7] == 'x' and gameboard[8] == 'x':
        print('X wins')
    elif gameboard[0]==  'x' and gameboard[3] == 'x' and gameboard[6] == 'x':
        print('X wins')
    elif gameboard[1]==  'x' and gameboard[4] == 'x' and gameboard[7] == 'x':
        print('X wins')
    elif gameboard[2]==  'x' and gameboard[5] == 'x' and gameboard[8] == 'x':
        print('X wins')
    elif gameboard[0]==  'x' and gameboard[4] == 'x' and gameboard[8] == 'x':
        print('X wins')
    elif gameboard[2]==  'x' and gameboard[4] == 'x' and gameboard[6] == 'x':
        print('X wins')
    if gameboard[0]==  'o' and gameboard[1] == 'o' and gameboard[2] == 'o':
        print('o wins')
    elif gameboard[3]==  'o' and gameboard[4] == 'o' and gameboard[5] == 'o':
        print('O wins')
    elif gameboard[6]==  'o' and gameboard[7] == 'o' and gameboard[8] == 'o':
        print('o wins')
    elif gameboard[0]==  'o' and gameboard[3] == 'o' and gameboard[6] == 'o':
        print('o wins')
    elif gameboard[1]==  'o' and gameboard[4] == 'o' and gameboard[7] == 'o':
        print('o wins')
    elif gameboard[2]==  'o' and gameboard[5] == 'o' and gameboard[8] == 'o':
        print('o wins')
    elif gameboard[0]==  'o' and gameboard[4] == 'o' and gameboard[8] == 'o':
        print('o wins')
    elif gameboard[2]==  'o' and gameboard[4] == 'o' and gameboard[6] == 'o':
        print('o wins')
    else:
        print ('tie game')

winning (gameboard)

'''if gameboard[0]== gameboard[1] and gameboard[0] == gameboard[2]:
  print('you win')
elif gameboard[3]== gameboard[4] and gameboard[3] == gameboard[5]:
  print('you win') 
elif gameboard[6]== gameboard[7] and gameboard[6] == gameboard[8]:
  print('you win') 
elif gameboard[0]== gameboard[3] and gameboard[0] == gameboard[6]:
  print('you win') 
elif gameboard[1]== gameboard[4] and gameboard[1] == gameboard[7]:
  print('you win') 
elif gameboard[2]== gameboard[5] and gameboard[2] == gameboard[8]:
  print('you win') 
elif gameboard[0]== gameboard[4] and gameboard[0] == gameboard[8]:
  print('you win') 
elif gameboard[2]== gameboard[4] and gameboard[2] == gameboard[6]:
  print('you win') 
else:
  print ('tie game')'''

