def printInitials():
    myInitials = [
        ['aa', '  ', 'aa', '  ', 'aa', '  ', 'nn', 'nn', 'nn', '  ', 'nn'],  
        ['aa', '  ', '  ', '  ', 'aa', '  ', 'nn', '  ', 'nn', '  ', 'nn'],  
        ['aa', '  ', 'aa', '  ', 'aa', '  ', 'nn', '  ', 'nn', '  ', 'nn'],  
        ['aa', '  ', '  ', '  ', 'aa', '  ', 'nn', '  ', 'nn', '  ', 'nn'], 
        ['aa', '  ', '  ', '  ', 'aa', '  ', 'nn', '  ', 'nn', 'nn', 'nn'], 
    ]

    happyFace = [
        ['  ', '  ', '  ', ' .', '..', '. ', '  ', '  ', '  '],
        ['  ', '. ', '  ', '  ', '  ', '  ', '  ', ' .', '  '],
        [' .', '  ', '  ', ' ^', '  ', '^ ', '  ', '  ', '. '],
        ['  ', '. ', '  ', '  ', '--', '  ', '  ', ' .', '  '],
        ['  ', '  ', '  ', ' .', '..', '. ', '  ', '  ', '  ']
    ]

    printMatrix(myInitials)
    print('\n')
    printMatrix(happyFace)

def printMatrix(matrix):
    for i in range(len(matrix)):
        row = matrix[i]
        row_string = ''
        for j in range(len(row)):
            row_string += row[j]
        row_string += '\n'
        print(row_string)


    
printInitials()