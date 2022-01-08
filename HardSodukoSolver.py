"""
This kata is a harder version of http://www.codewars.com/kata/sudoku-solver/python made by @pineappleclock

Write a function that will solve a 9x9 Sudoku puzzle. 
The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

The Sudokus tested against your function will be "insane" and can have multiple solutions. 
The solution only need to give one valid solution in the case of the multiple solution sodoku.

It might require some sort of brute force.

Consider applying algorithm with

Backtracking https://www.wikiwand.com/en/Sudoku_solving_algorithms#Backtracking
Brute Force
For Sudoku rules, see the Wikipedia : http://www.wikiwand.com/en/Sudoku

Used puzzle from : http://www.extremesudoku.info/sudoku.html

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solve(puzzle)
"""

N = 9


def valid(board, num, row, col):

    # Check row
    for i in range(len(board)):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(len(board[0])):
        if board[i][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    # Check box
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- ' * 12 + " ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def solveSoduko(grid, row, col):
    if row == N - 1 and col == N:
        return True

    if col == N:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solveSoduko(grid, row, col + 1)

    for num in range(1, N + 1, 1):

        if valid(grid, num, row, col):
            grid[row][col] = num

            if solveSoduko(grid, row, col + 1):
                return True

            grid[row][col] = 0

    return False


def soduko(board):
    solution = [[board[i][j]
                 for j in range(len(board[0]))] for i in range(len(board))]

    solveSoduko(solution, 0, 0)

    return solution


def solve(board):
    solution = [[board[i][j]
                 for j in range(len(board[0]))] for i in range(len(board))]

    solveSoduko(solution, 0, 0)

    return solution


if __name__ == "__main__":
    board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 3, 0, 0, 1],
             [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0],
             [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    solution = [[board[i][j]
                 for j in range(len(board[0]))] for i in range(len(board))]
    print("Board:")
    print_board(board)
    solveSoduko(solution, 0, 0)
    solved = soduko(solution)
    print()

    #solution = solveSudokuHelper(0, 0, board, solution)
    # solve(board)
    print()
    print(f"Solution: ")
    print_board(solved)
