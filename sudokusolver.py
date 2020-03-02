import pprint
import copy

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
                #set 0, where there is already value at that place
                dummy_square[range_x.index(row)][range_y.index(column)] = [0]

                for x in range(3):
                    for y in range(3):
                        try:
                            if value !=0:
                                dummy_square[x][y].remove(value)
                        except ValueError:
                            pass
                        #if there is no value, catch exception and go!
    for row in range_x:
        for column in range_y:
            dummy_board[row][column] = dummy_square[range_x.index(row)][range_y.index(column)]
    #pprint.pprint(dummy_square)

    for row in range_x :
        for column in range_y :
            if len(dummy_board[row][column]) == 1 and dummy_board[row][column][0] !=0:
                board[row][column] = dummy_board[row][column][0]
                dummy_board[row][column][0] = 0
    
    #pprint.pprint(dummy_board)
    return 1

def create_dummy_horizontal_line(dummy_board,row):
    dummy_h_line = [0,0,0,0,0,0,0,0,0]
    for column in range(9):
        dummy_possible_numbers = dummy_board[row-1][column]
        dummy_h_line[column]= copy.deepcopy(dummy_possible_numbers)   
    #print(dummy_h_line)

    return dummy_h_line

def check_line_horizontal(board,dummy_board,row):
    dummy_line= create_dummy_horizontal_line(dummy_board,row)
    for column in range(9):
        value = board[row-1][column]
        if value in dummy_line[column]:
            dummy_line[column]=[0]
            for y in range(9):
                try:
                    if value !=0:
                        dummy_line[y].remove(value)
                except ValueError:
                    pass
    for column in range(9):
        dummy_board[row-1][column] = dummy_line[column]
        if len(dummy_board[row-1][column]) ==1 and dummy_board[row-1][column][0] != 0:
            board[row-1][column] = dummy_board[row-1][column][0]
            dummy_board[row-1][column][0] = 0
    #pprint.pprint(dummy_board)
    return 2

def create_dummy_vertical_line(dummy_board,column:int):
    dummy_v_line = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
    for row in range(9):
        dummy_possible_numbers = dummy_board[row][column-1]
        dummy_v_line[row]= copy.deepcopy(dummy_possible_numbers) 
    #print(dummy_v_line)
    return dummy_v_line

def check_line_vertical(board,dummy_board,column):
    dummy_v_line = create_dummy_vertical_line(dummy_board,column)
    for row in range(9):
        value = board[row][column-1]
        if value in dummy_v_line[row]:
            dummy_v_line[row] = [0]
            for x in range(9):
                try:
                    if value !=0:
                        dummy_v_line[x].remove(value)
                except ValueError:
                    pass
    for row in range(9):
        dummy_board[row][column-1] = dummy_v_line[row]
        if len(dummy_board[row][column-1]) ==1 and dummy_board[row][column-1][0] != 0:
            board[row][column-1] = dummy_board[row][column-1][0]
            dummy_board[row][column-1][0] = 0
    
    #pprint.pprint(dummy_board)
    return 3



check_square(board,dummy_board,2,2)
for xd in [4,5,6]:
    for yd in [4,5,6]:
        check_line_horizontal(board,dummy_board,xd)
        check_line_vertical(board,dummy_board,yd)

for x in [3,4,5]:
    for y in [3,4,5]:
        print(dummy_board[x][y])
#print(dummy_board)
#pprint.pprint(board)