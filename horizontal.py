import pprint
import copy

def create_dummy_horizontal_line(dummy_board,row):
    #create dummy list with possible values for the horizontal line
    dummy_h_line = [0,0,0,0,0,0,0,0,0]
    for column in range(9):
        dummy_possible_numbers = dummy_board[row-1][column]
        dummy_h_line[column]= copy.deepcopy(dummy_possible_numbers)
    #print(dummy_h_line)

    return dummy_h_line

def check_line_horizontal(board,dummy_board,row):
    #check horizontal line for possibilities, in some cases put proper value
    dummy_line= create_dummy_horizontal_line(dummy_board,row)
    for column in range(9):
        value = board[row-1][column]
        if value in dummy_line[column]:
            #if there is value in dummy line, try to delete it
            dummy_line[column]=[0]    
        delete_existing_value(dummy_line,value)
    for column in range(9):
        dummy_board[row-1][column] = dummy_line[column]
    for column in range(9):
        #added this in case there is [] , then for safety set it to [0]
        try:
            lonely_value = dummy_board[row-1][column][0]
        except IndexError:
            dummy_board[row-1][column] = [0]
            lonely_value = dummy_board[row-1][column][0]

        if len(dummy_board[row-1][column]) ==1 and lonely_value != 0:
        #there must be one value and it shouldn't be 0
            board[row-1][column] = lonely_value #write this value on board
            for y in range(9): #delete this number from dummy list from line
                try:
                    if lonely_value !=0:
                        dummy_board[row-1][y].remove(lonely_value)
                        if len(dummy_board[row-1][y]) ==0:
                            dummy_board[row-1][y] == [0]
                except ValueError:
                    pass
            dummy_board[row-1][column] = [0]
    #if there is one occurence of value, set this value there
    only_value_h_line = check_one_occ_h_line(dummy_line)
    if only_value_h_line != 0:
        if only_value_h_line[0] in dummy_board[row-1][only_value_h_line[1]]:
            #here we dont have to use delete value functtion, because
            #if we find one occurence of value, we dont care about rest
            print("found!")
            board[row-1][only_value_h_line[1]] = only_value_h_line[0]
            dummy_board[row-1][only_value_h_line[1]] = [0]
    #pprint.pprint(dummy_board)
    return 2

def check_one_occ_h_line(dummy_h_line):
    #check if there is one possibility for value in horizontal line
    temp_occ_list = [0 for _ in range(9)]
    result = [0,0]
    for column in range(9):
        for value in range(1,10):
            if (dummy_h_line[column].count(value)!=0):
                #sum occurences into list
                temp_occ_list[value-1] += dummy_h_line[column].count(value)

    for x in range(9):
        if( temp_occ_list[x] == 1):
            for y in range(9):
                try:
                    #return coordinates and value, for which there is one occurence
                    dummy_h_line[y].index(x+1) 
                    result[0]=x+1
                    result[1]=y
                    return result
                except ValueError:
                    pass
    return (0)

def delete_existing_value(dummy_h_line,value):
    #if there is value , which is on board, try to remove it
    for y in range(9):
        try:
            if value !=0:
                dummy_h_line[y].remove(value)
        except ValueError:
        #if it isn't in list, catch error
            pass