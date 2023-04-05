#use is similar to FEN for chess
#char "b" indicates a box
#char "B" indicates a button
#char "d" indicates where the player "Dwayne" is
#char "D" indicates where a door is
#char "t" indicates a tripwire bomb
#char "e" indicates an exit
#integers indicate how many solid, unmovable walls are adjacent
from entity import Entity
import pygame


def level_creator(resolution, lvl_string):
    
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

    print(row_strings)

    arr_width = len(row_strings[0])
    arr_height = len(row_strings)

    lvl_array = []

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
    for row in range(arr_height):
        lvl_array.append([])
        for c in row_strings[cur_row]:
            print("Row = ", row)
            if c == "b":
                pass
            
            elif c == "d":
                #print("d found")
                lvl_array[row].append(Entity("../images/walk", sq_size, cur_row, cur_col, initial_x, initial_y))
            elif c == "B":
                pass
            
            elif c == "t":
                pass

            elif c == "e":
                pass

            elif c == "*":
                lvl_array[row].append(None)
            cur_col += 1
        cur_row += 1
        cur_col = 0
    
    return lvl_array


pygame.init()
clock = pygame.time.Clock()

screen_res = [525, 525]
screen = pygame.display.set_mode(screen_res)

pygame.display.set_caption("Dwayneson's Pancake Persuit")
icon = pygame.image.load('..\images\dwayneson.png')
pygame.display.set_icon(icon)

print(level_creator(screen_res, "4/2d1/4/4"))