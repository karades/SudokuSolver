import pprint
import copy
import horizontal
import vertical
import square

#define boards
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

#define full dummy_board for possible values for board
possible_numbers = [1,2,3,4,5,6,7,8,9]
dummy_board = [[possible_numbers for _ in range(9)] for _ in range(9)]



def print_sudoku(board):
    #function for printing board
    for row in range(len(board)):
        print("|",end=" ")
        for column in range(len(board)):
            print(board[row][column],end = " ")
        print("|")

def solve_once(board,dummy_board):
    #function to use basic solving functions to try to solve or add new information to board and dummy board
    for row in range(1,10):
        horizontal.check_line_horizontal(board,dummy_board,row)
    for column in range(1,10):
        vertical.check_line_vertical(board,dummy_board,column)

    for row in range(1,4):
        for column in range(1,4):
            square.check_square(board,dummy_board,row,column)

def if_Solved(board):
    #function to check if board is solved
    for number in range(9):
        if 0 in board[number]:
            #if there is 0 (empty) return False
            return False
    return True

def put_poss_number(board,dummy_board):
    #function to find first empty cell in board, then it returns index and value 
    index = [0,0]
    for number in range(9):
        if 0 in board[number]:
            index[1] = board[number].index(0)
            index[0]=number
            break
    return index

i=0
#define global result, so it will be saved through recursions
final_result =[[0 for _ in range(9)] for _ in range(9)]

def solve(board,dummy_board):
    global final_result
    #define guard boards for backup
    guard_board = copy.deepcopy(board)
    guard_dummy = copy.deepcopy(dummy_board)
    while True:
        global i
        i+=1
        #define boards before solving
        dummy_board_bef = copy.deepcopy(dummy_board)
        board_bef = copy.deepcopy(board)
        #checking if our new iteration is already solved
        if if_Solved(board):
            print("solved")
            final_result = copy.deepcopy(board)
            return final_result

        #try to solve with basic rules
        solve_once(board,dummy_board)

        if dummy_board_bef == dummy_board and board == board_bef:
            #if there is no change after iteration
            #find first empty cell in board
            index = put_poss_number(board,dummy_board)
            for possis in dummy_board[index[0]][index[1]]:

                #put possible value into board
                board = copy.deepcopy(guard_board)
                dummy_board = copy.deepcopy(guard_dummy) 
                #reset our board to check another value

                if possis == 0:
                    #if there are no possible values return false
                    return False
                board[index[0]][index[1]] = possis
                dummy_board[index[0]][index[1]] =[0]
                #recursion starts here

                if (solve(board,dummy_board) == board):
                    #checking if our function will return board
                    return final_result

                elif if_Solved(final_result):
                    #ensuring that our board is solved
                    return final_result
                else: break



board = solve(board,dummy_board)


print_sudoku(board)