import pprint
import copy
import horizontal
import vertical
import square

board =[[0,1,0,6,0,4,3,0,7],
        [3,5,6,0,0,0,0,0,0],
        [0,0,0,0,5,3,6,9,0],
        [0,8,3,2,6,0,4,0,9],
        [0,0,0,0,0,0,0,0,0],
        [4,0,5,0,7,8,2,6,0],
        [0,4,2,5,3,0,0,0,0],
        [0,0,0,0,0,0,7,2,4],
        [7,0,9,4,0,2,0,8,0]]

possible_numbers = [1,2,3,4,5,6,7,8,9]
dummy_board = [[possible_numbers for _ in range(9)] for _ in range(9)]

#dummy_board = copy.deepcopy(dummy_board_temp)
#pprint.pprint(dummy_board)

def print_sudoku(board):
    for row in range(len(board)):
        print("|",end=" ")
        for column in range(len(board)):
            print(board[row][column],end = " ")
        print("|")

def solve_sudoku(board,dummy_board):
    for row in range(1,10):
        for column in range(1,10):
            if (row==9):
                horizontal.check_line_horizontal(board,dummy_board,row)
                vertical.check_line_vertical(board,dummy_board,column)
            else:
                horizontal.check_line_horizontal(board,dummy_board,row)
                vertical.check_line_vertical(board,dummy_board,column)
            
    for row in range(1,4):
        for column in range(1,4):
            square.check_square(board,dummy_board,row,column)
    print(dummy_board)


for x in range (3):
    solve_sudoku(board,dummy_board)


pprint.pprint(board)