# Tick-Tack-Toe project
# Ivan Pankov, 04.03.20

import os
import pdb

p1_turn = False
count = 0
board = [str(x) for x in range(1,10)]

win_lines = [[0, 1, 2], # Horizontals
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6], # Verticals
             [1, 4, 7],
             [2, 5 ,8],
             [2, 4, 6], # Diagonals
             [0, 4, 8]]

def getInput():
    inp = ''
    while (inp < '1' or inp > '9') or not inp.isdecimal() or len(inp) > 1:
        inp = input('Enter number: ')
    return int(inp)

def drawBoard():
    if p1_turn:
        print('Player 1 turn:')
    else:
        print('Player 2 turn:')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])

def makeTurn():

    while True:
        idx = getInput()
        if board[idx-1].isdecimal():
            break

    if p1_turn:
        board[idx-1] = 'X'
    else:
        board[idx-1] = 'O'

    return board

def isWin():
    for line in win_lines:
        if board[line[0]] == board[line[1]] == board[line[2]]:
            return True
    return False

while not isWin() and count < 9:
    #pdb.set_trace()
    p1_turn = not p1_turn
    os.system('cls' if os.name == 'nt' else 'clear')
    drawBoard()
    board = makeTurn()
    count += 1

os.system('cls' if os.name == 'nt' else 'clear')
drawBoard()
if isWin():
    print('Player ' + ('1' if p1_turn else '2') + ' won!')
else:
    print('Draw!')

input('Press ENTER to exit')
