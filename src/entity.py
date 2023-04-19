#new entity file

from pygame import sprite
import pygame
import os

class Entity(pygame.sprite.Sprite):
    def __init__(self, cyc_path, sq_size, row, col, initial_x, initial_y):
        super().__init__()
        ALPHA = (0, 0, 0)
        
        self.sprites = []
        self.dir = "d" # indicates last direction that the sprite moved in

        self.row = row
        self.col = col

        self.initial_x = initial_x
        self.initial_y = initial_y

        self.sq_size = sq_size

        """
        dir_list = os.listdir(cyc_path)
        self.g_num = 0 #number of sprites
        self.cyc_count = 0 #counts number of anim cycles
        """

        for i in range(3):
            img = pygame.image.load(os.path.join(cyc_path, "PH_" + str(i) +  '.png')).convert()
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.sprites.append(img)
            self.sprites[len(self.sprites) - 1] = pygame.transform.scale(self.sprites[len(self.sprites) - 1], [sq_size, sq_size])
            self.rect = self.image.get_rect()
        """
        #finds the amount of files per direction in anim cycle
        for file in dir_list:
            file_str = str(file)

            try:
                num = int(file_str[-5]) #-5 is passed b/c thats where the last char in the file name is
            except:
                print("Could not convert char to number.")
            else:
                pass

            if (num > self.g_num):
                self.g_num = num

            if (num == 0):
                cycle_count += 1
        """


    def schmoove(self, x_change, y_change, lvl_arr):
        self.x_change = x_change
        self.y_change = y_change
        x2 += self.x + x_change
        y2 += self.y + y_change


        if(lvl_arr[x2][y2] == None):
            lvl_arr[self.x][self.y] = None
            self.row += x_change
            self.col += y_change    

        """
        elif(lvl_arr[x2][y2] == Door):
            pass
        elif(lvl_arr[x2][y2] == Box):
            pass
        elif(lvl_arr[x2][y2] == Button):
            pass
        elif(lvl_arr[x2][y2] == Trip):
            pass
        elif(lvl_arr[x2][y2] == Door):
            pass
        elif(lvl_arr[x2][y2] == Exit):
            pass
        """
        
    def update_pos(self):
        self.rect.x = (self.row * self.sq_size) + self.initial_x
        self.rect.y = (self.col * self.sq_size) + self.initial_y

        if self.x_change < 0: 
            self.image = pygame.transform.flip(self.sprites[1])
        if self.x_change > 0:
            self.image = self.sprites[1]
        if self.y_change < 0:
            self.image = self.sprites[0]
        if self.y_change > 0:
            self.image = self.sprites[2]

            
