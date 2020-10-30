
def get_selection():
    x = input (f'Select column 1, 2, or 3: ')
    while True:
        try:
            x = int(x)
            if x < 1 or x > 3:
                raise ValueError
            break
        except:
            print (f'"{x}" is an invalid column entry!')
            x = input (f'Select again column 1, 2, or 3: ')

    y = input (f'Select row 1, 2, or 3: ')
    while True:
        try:
            y = int(y)
            if y < 1 or y > 3:
                raise ValueError
            break
        except:
            print (f'"{y}" is an invalid row entry!')
            y = input (f'Select again row 1, 2, or 3: ')
    return x, y


def move(x, y): # does "player" need to be one of the variables as shown in the example?
    if x == 1 and y == 1:
        position = 0
    elif x == 2 and y == 1:
        position = 1
    elif x == 3 and y == 1:
        position = 2
    elif x == 1 and y == 2:
        position = 3
    elif x == 2 and y == 2:
        position = 4
    elif x == 3 and y == 2:
        position = 5
    elif x == 1 and y == 3:
        position = 6
    elif x == 2 and y == 3:
        position = 7
    elif x == 3 and y == 3:
        position = 8
    return position
    
        # while gameboard[position] == 'X' or gameboard[position] == 'Y':
        #     print (f'Position {x}, {y} is already taken. Please try again.')
        #     x = input (f'What column do you want to select?')
        #     y = input (f'What row do you want to select?')

gameboard = [' ' for x in range(9)] # builds list to record game board locations
while True:
    player = input ('Choose "X" or "O": ')
    player = player.capitalize()
    box_selection = get_selection() # calls function to get player selection and returns x, y in tuple
    position = move(box_selection[0], box_selection[1]) # returns box number when given player x, y choice
    
    while gameboard[position] == 'X' or gameboard[position] == 'O':
        print ('That position is already taken. Choose again.')
        box_selection = get_selection()
        position = move(box_selection[0], box_selection[1])

    gameboard[position] = player
    print (gameboard)
    print (gameboard[position])