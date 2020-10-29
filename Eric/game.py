class Player :
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

print('Upload')