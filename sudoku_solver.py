size = 9

def printSudoku(arr):
    for i in range(size):
        for j in range(size):
            print(arr[i][j], end=" ")
        print()

def ifSafe(grid, row, col, num):
    for x in range(9):  # if same number in row return false
        if grid[row][x] == num:
            return False
    for x in range(9):  # if same num in colmn returnn false
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):  # if same num in 3x3 box, return false
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def solveSudoku(grid, row, col):
    if (row == size - 1 and col == size):  # traverse through entire sudoku
        return True

    if col == size:
        row += 1
        col = 0

    if grid[row][col] > 0:  # if num present
        return solveSudoku(grid, row, col + 1)  # check next slot
    for num in range(1, size + 1, 1):  # check which number fits
        if ifSafe(grid, row, col, num):  # check if num fits

            grid[row][col] = num  # found possible number
            if solveSudoku(grid, row, col + 1):  # fitting and checkinng
                return True

        grid[row][col] = 0  # if fit failed, replace
    return False

def readSudokuFromFile(filename):
    with open(filename, 'r') as file:
        sudoku = []
        for line in file:
            row = list(map(int, line.strip().split()))  # convert to integers
            sudoku.append(row)
        return sudoku

def writeSudokuToFile(sudoku, filename):
    with open(filename, 'w') as file:
        for row in sudoku:
            file.write(' '.join(map(str, row)) + '\n')

# " " means unassigned cells

# Read unsolved sudoku from file
unsolved_sudoku = readSudokuFromFile("sudoku_unsolved.txt")

if solveSudoku(unsolved_sudoku, 0, 0):
    # Print solved sudoku
    print("Sudoku solved:")
    printSudoku(unsolved_sudoku)

    # Write solved sudoku to file
    writeSudokuToFile(unsolved_sudoku, "sudoku_solved.txt")
    print("Solved sudoku written to 'sudoku_solved.txt'")
else:
    print("Sudoku not solvable exists")
