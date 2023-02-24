#use is similar to FEN for chess
#char "b" indicates a box
#char "B" indicates a button
#char "d" indicates where the player "Dwayne" is
#char "t" indicates a tripwire bomb
#char "e" indicates an exit
#integers indicate how many solid, unmovable walls are adjacent


def level_creator(self, lvl_string, resolution):
    
    row_strings = []

    row_str = ""
    for s in lvl_string:
        try:
            x = int(s)
            row_str += ("*" * x)

        except Exception as e:
            if s == "/":
                row_strings.append(row_str)
                row_str = ""
            else:
                row_str += s
    row_strings.append(row_str)

    

    arr_width = len(row_strings[0])
    arr_height = len(row_strings)

    lvl_array = [ [0]*arr_width for i in range(arr_height)]

    if arr_height < arr_width:
        #resolution[0] = width
        sq_size = (resolution[1] / arr_height)
        initial_x = resolution[0] - (sq_size * arr_width) #total width that array occupies
        initial_x /= 2 #gets remainder of width so that screen can be properly letterboxed
        initial_y = 0
    else:
        sq_size = (resolution[0] / arr_width)
        initial_y = resolution[1] - (sq_size * arr_height)
        initial_y /= 2
        initial_x = 0

    cur_row = 0
    cur_col = 0
    for row in lvl_array:
        for c in row_strings[cur_col]:
            if c == "b":
                pass
            
            elif c == "B":
                pass
            
            elif c == "d":
                pass

            if c == "t":
                pass

            if c == "e":
                pass

            elif c == "*":
                row.append(None)
            cur_row += 1
        cur_col += 1
        cur_row = 0

