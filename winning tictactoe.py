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
    elif gameboard[0]==  'o' and gameboard[1] == 'o' and gameboard[2] == 'o':
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
