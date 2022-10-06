########  Sudoku Solver ########

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]


# Printing the board
def printBoard (board) :
    print(f"\n| {board[0][0]}  {board[0][1]}  {board[0][2]} | {board[0][3]}  {board[0][4]}  {board[0][5]} | {board[0][6]}  {board[0][7]}  {board[0][8]} |")
    print(f"\n| {board[1][0]}  {board[1][1]}  {board[1][2]} | {board[1][3]}  {board[1][4]}  {board[1][5]} | {board[1][6]}  {board[1][7]}  {board[1][8]} |")
    print(f"\n| {board[2][0]}  {board[2][1]}  {board[2][2]} | {board[2][3]}  {board[2][4]}  {board[2][5]} | {board[2][6]}  {board[2][7]}  {board[2][8]} |")
    print("_______________________________")
    print(f"\n| {board[3][0]}  {board[3][1]}  {board[3][2]} | {board[3][3]}  {board[3][4]}  {board[3][5]} | {board[3][6]}  {board[3][7]}  {board[3][8]} |")
    print(f"\n| {board[4][0]}  {board[4][1]}  {board[4][2]} | {board[4][3]}  {board[4][4]}  {board[4][5]} | {board[4][6]}  {board[4][7]}  {board[4][8]} |")
    print(f"\n| {board[5][0]}  {board[5][1]}  {board[5][2]} | {board[5][3]}  {board[5][4]}  {board[5][5]} | {board[5][6]}  {board[5][7]}  {board[5][8]} |")
    print("_______________________________")
    print(f"\n| {board[6][0]}  {board[6][1]}  {board[6][2]} | {board[6][3]}  {board[6][4]}  {board[6][5]} | {board[6][6]}  {board[6][7]}  {board[6][8]} |")
    print(f"\n| {board[7][0]}  {board[7][1]}  {board[7][2]} | {board[7][3]}  {board[7][4]}  {board[7][5]} | {board[7][6]}  {board[7][7]}  {board[7][8]} |")
    print(f"\n| {board[8][0]}  {board[8][1]}  {board[8][2]} | {board[8][3]}  {board[8][4]}  {board[8][5]} | {board[8][6]}  {board[8][7]}  {board[8][8]} |")
    print("_______________________________")


def isNumberInRow (board, number, row):
    for index in range(9):
        if board[row][index] == number :
            return True    
    return False

def isNumberInColumn (board, number, column):
    for index in range(9):
        if board[index][column] == number :
            return True
    return False

def IsNumberInBox (board, number, row, column):
    localBoxRow = row - row % 3
    localBoxColumn = column - column % 3

    for i in range(localBoxRow + 3) :
        for j in range(localBoxColumn + 3) :
            if board[i][j] == number :
                return True 
    return False

def IsValidPlacement (board, number, row, column) :
    return not isNumberInRow (board, number, row) and not isNumberInColumn (board, number, column) and not IsNumberInBox (board, number, row, column)


number = IsValidPlacement(board, 1, 0, 2)

# print(f"IsValidPlacement = {number}")

def solveBoard (board):
    for i in range(9):
        print(f"i = {i}")
        for j in range(9):
            print(f"j = {j}")
            if board[i][j] == 0 :
                print(f"checking 0 field in location : row {i+1} and column {j+1}")
                for number in range(1,10):
                    print(f"number is {number}")
                    if IsValidPlacement(board, number, i, j):
                        print(f"The number {number} is valid in ")
                        board[i][j] = number
                        if solveBoard (board):
                            return True
                        else:
                            board[i][j] = 0


solveBoard (board)

printBoard(board)