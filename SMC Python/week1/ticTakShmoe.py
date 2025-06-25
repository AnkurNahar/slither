def printTicTakToeResults():
    board = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print('small board:')
    printSmallBoard(board)
    print('\nmedium board:')
    printMediumBoard(board)
    print('\nlarge board:')
    printLargeBoard(board)

def printSmallBoard(board):
    for i in range(len(board)):
        row = board[i]
        row_string = ''
        for j in range(len(row)):
            row_string += f'{row[j]}'
        row_string += '\n'
        print(row_string)

def printMediumBoard(board):
    for i in range(len(board)):
        row = board[i]
        row_string = ''
        for j in range(len(row)):
            row_string += f'{row[j]}\t'
        row_string += '\n'
        print(row_string)

def printLargeBoard(board):
    for i in range(len(board)):
        row = board[i]
        row_string = ''
        for j in range(len(row)):
            row_string += f'{row[j]}\t\t'
        row_string += '\n'
        print(row_string)
    
printTicTakToeResults()