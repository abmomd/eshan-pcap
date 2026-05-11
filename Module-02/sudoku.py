
def dict_tracker():
    d={}
    for i in range(1,10):
        d[i] = -1
    return d

def validate_rows(list):
    # list is going to be 9*9

    for r in range(9):
        # Looping through all the rows
        dictRow = dict_tracker()
        for c in range(9):
            # Looping through all the columns.
            num = list[r][c]
            if dictRow[num] == -1:
                dictRow[num] = 1
            else:
                return False

    return True


def validate_cols(list):
    # list is going to be 9*9

    for i in range(9):
        # Looping through all the rows
        dictCol = dict_tracker()
        for j in range(9):
            # Looping through all the columns.
            num = list[j][i]
            if dictCol[num] == -1:
                dictCol[num] = 1
            else:
                return False

    return True

def validate_box(list):

    for x in range(9):

        start_c = 3*(x%3)
        start_r = 3 * (x//3)
        dictBox = dict_tracker()
        for r in range(start_r,start_r+3):

            for c in range(start_c,start_c+3):

                num = list[r][c]
                if dictBox[num] == -1:
                    dictBox[num] = 1
                else:

                    print(num,r,c)
                    return False

    return True




valid_sudoku = [
    [5, 2, 3, 6, 7, 9, 8, 1, 4],
    [9, 8, 4, 5, 2, 1, 3, 7, 6],
    [1, 6, 7, 8, 4, 3, 5, 9, 2],
    [6, 1, 9, 4, 8, 5, 7, 2, 3],
    [3, 7, 5, 1, 6, 2, 4, 8, 9],
    [8, 4, 2, 9, 3, 7, 1, 6, 5],
    [2, 3, 1, 7, 9, 4, 6, 5, 8],
    [7, 9, 6, 3, 5, 8, 2, 4, 1],
    [4, 5, 8, 2, 1, 6, 9, 3, 7]
]

print(validate_rows(valid_sudoku))
print(validate_cols(valid_sudoku))
print(validate_box(valid_sudoku))