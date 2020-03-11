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

board1=[[2,0,0,0,0,0,0,6,0],
        [0,0,0,5,0,6,4,0,0],
        [0,5,0,0,1,0,0,0,7],
        [5,0,0,6,0,8,7,1,0],
        [0,0,0,0,0,0,0,0,0],
        [0,2,7,1,0,9,0,0,8],
        [6,0,0,0,5,0,0,9,0],
        [0,0,2,4,0,1,0,0,0],
        [0,8,0,0,0,0,0,0,2]]

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

def solve_once(board,dummy_board):
    for row in range(1,10):
        for column in range(1,10):
                horizontal.check_line_horizontal(board,dummy_board,row)
                vertical.check_line_vertical(board,dummy_board,column)

    for row in range(1,4):
        for column in range(1,4):
            square.check_square(board,dummy_board,row,column)
    #print(dummy_board)

def if_Solved(board):
    temp_sum =0
    for number in range(9):
        temp_sum +=board[number].count(0)
    if temp_sum >1:
        print("Not solved")
        return False
    else:
        return True

def put_poss_number(board,dummy_board):
    index = [0,0]
    for number in range(9):
        if 0 in board[number]:
            index[1] = board[number].index(0)
            index[0]=number
            break
    return index

i=0

def solve(board,dummy_board):
    guard_board = copy.deepcopy(board)
    while True:
        global i
        i+=1
        dummy_board_bef = copy.deepcopy(dummy_board)
        board_bef = copy.deepcopy(board)
        solve_once(board,dummy_board)
        #print(i)
        if dummy_board_bef == dummy_board and board == board_bef:
            print("No change after: ",i," iterations")
            if if_Solved(board):
                pprint.pprint(board)
                return(print("solved"))
            else:
                index = put_poss_number(board,dummy_board)
                for possis in dummy_board[index[0]][index[1]]:
                    if possis ==0:
                        return False
                    board[index[0]][index[1]] = possis
                    solve(board,dummy_board)
                    board = copy.deepcopy(guard_board)
                    
    return(print("The End"))



solve(board1,dummy_board)


print_sudoku(board1)