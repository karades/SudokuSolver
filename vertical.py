import pprint
import copy

def create_dummy_vertical_line(dummy_board,column:int):
    dummy_v_line = [[0],[0],[0],[0],[0],[0],[0],[0],[0]]
    for row in range(9):
        dummy_possible_numbers = dummy_board[row][column-1]
        dummy_v_line[row]= copy.deepcopy(dummy_possible_numbers)
        if len(dummy_v_line)==0:
            dummy_v_line[row] = [0]
    #print(dummy_v_line)
    return dummy_v_line

def check_line_vertical(board,dummy_board,column):
    dummy_v_line = create_dummy_vertical_line(dummy_board,column)
    for row in range(9):
        value = board[row][column-1]
        if value in dummy_v_line[row]:
            dummy_v_line[row] = [0]
        for temp_row in range(9):
            if value in dummy_v_line[temp_row]:
                for x in range(9):
                    try:
                        if value !=0:
                            dummy_v_line[x].remove(value)
                    except ValueError:
                        pass
                    
            for x in range(9):
                try:
                    if value !=0:
                        dummy_v_line[x].remove(value)
                except ValueError:
                    pass
    for row in range(9):
        dummy_board[row][column-1] = dummy_v_line[row]
        try:
            lonely_value = dummy_board[row][column-1][0]
        except IndexError:
            lonely_value =[0]
            dummy_board[row][column-1] =[0]
        if len(dummy_board[row][column-1]) ==1 and lonely_value != 0:
            board[row][column-1] = lonely_value
            for y in range(9):
                try:
                    if lonely_value !=0:
                        dummy_board[y][column-1].remove(lonely_value)
                        if len(dummy_board[y][column-1]) ==0:
                            dummy_board[y][column-1] == [0]
                except ValueError:
                    pass
            dummy_board[row][column-1] = [0]
    only_value_v_line = check_one_occ_v_line(dummy_v_line)
    if only_value_v_line !=0:
        if only_value_v_line[0] in dummy_board[only_value_v_line[1]][column-1]:
            print("found!")
            board[only_value_v_line[1]][column-1] = only_value_v_line[0]
            dummy_board[only_value_v_line[1]][column-1] = [0]

    #pprint.pprint(dummy_board)
    return 3

def check_one_occ_v_line(dummy_v_line):

    temp_occ_list = [0 for _ in range(9)]
    result = [0,0]
    for row in range(9):
        for value in range(1,10):
            if (dummy_v_line[row].count(value)!=0):
                temp_occ_list[value-1] += dummy_v_line[row].count(value)
    #print(temp_occ_list)
    for x in range(9):
        if( temp_occ_list[x] == 1):
            for y in range(9):
                try:
                    dummy_v_line[y].index(x+1)
                    result[0]=x+1
                    result[1]=y
                    return result
                except ValueError:
                    pass
    return 0