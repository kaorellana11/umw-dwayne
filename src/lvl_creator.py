#use is similar to FEN for chess
#char "b" indicates a box
#char "B" indicates a button
#char "d" indicates where the player "Dwayne" is
#char "D" indicates where a door is
#char "t" indicates a tripwire bomb
#char "e" indicates an exit
#integers indicate how many solid, immovable, and adjacent walls are in a row
from entity import Entity
import pygame
import pickle
import os




pygame.init()
clock = pygame.time.Clock()

screen_res = [525, 525]
screen = pygame.display.set_mode(screen_res)

pygame.display.set_caption("Dwayneson's Pancake Persuit")
icon = pygame.image.load('..\images\dwayneson.png')
pygame.display.set_icon(icon)

swag_arr = 


if not os.path.exists("../level_arrays/lvl_arr1.pkl",):
    filenum = 1
else:
    file_arr = os.listdir("../level_arrays/")
    filenum = int(file_arr[-1]) + 1
print(filenum)

pickle.dump(swag_arr,open('../level_arrays/lvl_arr' + str(filenum) + '.pkl', 'wb'))


##I LOVE GARTEN OF BANBAN