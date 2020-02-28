import pprint
import copy

board =[[0,0,7,0,9,6,2,0,0],
        [8,0,0,0,0,0,0,0,0],
        [9,0,0,1,2,0,5,0,0],
        [4,1,0,9,0,8,0,6,3],
        [0,0,0,0,1,0,4,9,2],
        [6,0,0,0,3,4,8,1,0],
        [0,0,0,8,0,1,5,4,0],
        [9,4,0,0,7,0,0,3,1],
        [0,5,0,4,6,0,2,8,0]]
        
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

def create_dummy_square(dummy_board,square_x,square_y):
    range = [1,2,3]
    range_x = [(x+(square_x-1)*3)-1 for x in range]
    range_y = [(y+(square_y-1)*3)-1 for y in range]
    dummy_square = [[None,None,None],
                    [None,None,None],
                    [None,None,None],]
    for row in range_x :
        for column in range_y :
            #print(dummy_board[row][column])
            dummy_possible_numbers = dummy_board[row][column]
            dummy_square[range_x.index(row)][range_y.index(column)]= copy.deepcopy(dummy_possible_numbers)
    #pprint.pprint(dummy_square)
    return dummy_square

def check_square(board,dummy_board,square_x,square_y):
    range_of_list = [1,2,3]
    range_x = [(x+(square_x-1)*3)-1 for x in range_of_list]
    range_y = [(y+(square_y-1)*3)-1 for y in range_of_list]
    dummy_square = create_dummy_square(dummy_board,square_x,square_y)
    for row in range_x :
        for column in range_y :
            #print(board[row][column])
            value = board[row][column] 

            if value in dummy_square[range_x.index(row)][range_y.index(column)]:
                dummy_square[range_x.index(row)][range_y.index(column)] = [0]
                for x in range(3):
                    for y in range(3):
                        try:
                            dummy_square[x][y].remove(value)
                        except ValueError:
                            pass
                        #if there is no value, catch exception and go!
    for row in range_x:
        for column in range_y:
            dummy_board[row][column] = dummy_square[range_x.index(row)][range_y.index(column)]
    pprint.pprint(dummy_square)

    return 1

check_square(board,dummy_board,1,1)
#create_dummy_square(dummy_board,1,1)
pprint.pprint(dummy_board)