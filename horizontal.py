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
    dummy_line= create_dummy_horizontal_line(dummy_board,row)
    for column in range(9):
        value = board[row-1][column]
        if value in dummy_line[column]:
            #if there is value in dummy line, try to delete it
            dummy_line[column]=[0]

        for temp_column in range(9):
            if value in dummy_line[temp_column]:
                #temp_found = True
                for y in range(9):
                    try:
                        if value !=0:
                            dummy_line[y].remove(value)
                    except ValueError:
                        pass    

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
    #if there is one occurence of value, set this value there
    only_value_h_line = check_one_occ_h_line(dummy_line)
    if only_value_h_line != 0:
        if only_value_h_line[0] in dummy_board[row-1][only_value_h_line[1]]:
            print("found!")
            board[row-1][only_value_h_line[1]] = only_value_h_line[0]
            dummy_board[row-1][only_value_h_line[1]] = [0]
    #pprint.pprint(dummy_board)
    return 2

def check_one_occ_h_line(dummy_h_line):
    temp_occ_list = [0 for _ in range(9)]
    result = [0,0]
    for column in range(9):
        for value in range(1,10):
            if (dummy_h_line[column].count(value)!=0):
                temp_occ_list[value-1] += dummy_h_line[column].count(value)
    #print(temp_occ_list)
    for x in range(9):
        if( temp_occ_list[x] == 1):
            for y in range(9):
                try:
                    dummy_h_line[y].index(x+1)
                    result[0]=x+1
                    result[1]=y
                    return result
                except ValueError:
                    pass
    return (0)