import pprint
import copy

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
            for temp_row in range_x:
                for temp_column in range_y:
                    if value in dummy_square[range_x.index(temp_row)][range_y.index(temp_column)]:
                        #set 0, where there is already value at that place
                        dummy_square[range_x.index(temp_row)][range_y.index(temp_column)] = [0]
                    for x in range(3):
                        for y in range(3):
                            try:
                                if value !=0:
                                    dummy_square[x][y].remove(value)
                            except ValueError:
                                pass
                        #if there is no value, catch exception and go!
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
    only_value_in_square = check_one_occ_square(dummy_square)
    if only_value_in_square !=0:
        print("found!")
        board[range_x[only_value_in_square[1]]][range_y[only_value_in_square[2]]]= only_value_in_square[0]
        dummy_board[range_x[only_value_in_square[1]]][range_y[only_value_in_square[2]]] = [0]

    #pprint.pprint(dummy_board)

    return 1


def check_one_occ_square(dummy_square):
    temp_occ_list = [0 for _ in range(9)]
    result=[0,0,0] 
    for row in range(3):
        for column in range(3):
            for value in range(1,10):
                if (dummy_square[row][column].count(value) !=0):
                    temp_occ_list[value-1]+=dummy_square[row][column].count(value)
    #print(temp_occ_list)
    for x in range(9):
        if( temp_occ_list[x] == 1):
            for row in range(3):
                for column in range(3):
                    try:
                        dummy_square[row][column].index(x+1)
                        result[0]=x+1
                        result[1]=row
                        result[2]=column
                        return result
                    except ValueError:
                        pass
    return 0
