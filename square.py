import pprint
import copy

def create_dummy_square(dummy_board,square_x,square_y):
    range = [1,2,3]
    range_x = [(x+(square_x-1)*3)-1 for x in range]
    range_y = [(y+(square_y-1)*3)-1 for y in range]
    dummy_square = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]
    #create square based on coordinates
    for row in range_x :
        for column in range_y :
            dummy_possible_numbers = dummy_board[row][column]
            dummy_square[range_x.index(row)][range_y.index(column)]= copy.deepcopy(dummy_possible_numbers)
    return dummy_square

def check_square(board,dummy_board,square_x,square_y):
    range_of_list = [1,2,3]
    range_x = [(x+(square_x-1)*3)-1 for x in range_of_list]
    range_y = [(y+(square_y-1)*3)-1 for y in range_of_list]
    #create square
    dummy_square = create_dummy_square(dummy_board,square_x,square_y)
    for row in range_x :
        for column in range_y :

            value = board[row][column] 
            if value in dummy_square[range_x.index(row)][range_y.index(column)]:
                #set 0, where there is already value at that place
                dummy_square[range_x.index(row)][range_y.index(column)] = [0]
            delete_existing_value(dummy_square,value)

    for row in range_x:
        for column in range_y:
            dummy_board[row][column] = dummy_square[range_x.index(row)][range_y.index(column)]

    for row in range_x :
        for column in range_y :
            #find value , which length is 1 and put this value on board, because its only possible value
            #added catch exception in case there is [] in list, then for safety set it to [0]
            try:
                lonely_value = dummy_board[row][column][0]
            except IndexError:
                dummy_board[row][column] = [0]
                lonely_value =dummy_board[row][column][0]
            if len(dummy_board[row][column]) == 1 and lonely_value !=0:
                # if its only value in board, at that coordinates it's our value, and set rest to 0 
                board[row][column] = lonely_value
                dummy_square[range_x.index(row)][range_y.index(column)] = [0]
                dummy_board[row][column] = [0]
                for x in range_x:
                    for y in range_y:
                        try:
                            if lonely_value !=0:
                                dummy_board[x][y].remove(lonely_value)
                                if len(dummy_board[x][y]) ==0:
                                    dummy_board[x][y] == [0]
                        except ValueError:
                            pass

    only_value_in_square = check_one_occ_square(dummy_square)
    if only_value_in_square !=0:
        #here we dont have to use delete value functtion, because
        #if we find one occurence of value, we dont care about rest
        #print("found!")
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

def delete_existing_value(dummy_square,value):
    for x in range(3):
        for y in range(3):
            try:
                if value !=0:
                    dummy_square[x][y].remove(value)
            except ValueError:
                pass
                #if there is no value, catch exception and go!