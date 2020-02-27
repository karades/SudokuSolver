import pprint

board =[[0,0,7,0,9,6,2,0,0],
        [8,0,0,0,0,0,0,0,0],
        [9,0,0,1,2,0,5,0,0],
        [4,1,0,9,0,8,0,6,3],
        [0,0,0,0,1,0,4,9,2],
        [6,0,0,0,3,4,8,1,0],
        [0,0,0,8,0,1,5,4,0],
        [9,4,0,0,7,0,0,3,1],
        [0,5,0,4,6,0,2,8,0]]
        
possible_numbers = [1,2,3,4,5,6,7,8,9,]

line = [possible_numbers]*9

dummy_board = [[line],
                [line],
                [line],
                [line],
                [line],
                [line],
                [line],
                [line],
                [line]]

#pprint.pprint(dummy_board)

def print_sudoku(board):
    for row in range(len(board)):
        print("|",end=" ")
        for column in range(len(board)):
            print(board[row][column],end = " ")
        print("|")

def check_square(board,dummy_board,square_x,square_y):
    range = [1,2,3]
    range_x = [(x+(square_x-1)*3)-1 for x in range]
    range_y = [(y+(square_y-1)*3)-1 for y in range]
    for row in range_x :
        print("|",end=" ")
        for column in range_y :
            print(board[row][column],end = " ")
        print("|")

    return 1

check_square(board,dummy_board,3,1)