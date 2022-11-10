#from entity import entity
from pygame import sprite
import pygame
import os

class Player(pygame.sprite.Sprite):


    
    def __init__(self, sq_size):
        super().__init__()

        self.move_x = 0 # move along X
        self.move_y = 0 # move along Y
        self.frame = 0 # count frames

        sq_size *= 2

        self.x_images = []
        self.down_images = []
        self.up_images = []
        self.dir = "d" #indicates last direction that the sprite moved in


        #gets highest value of a given sprite, used for the range in the loop
        imgs_path = "../images/walk"
        dir_list = os.listdir(imgs_path)
        self.g_num = 0; #number of sprites per anim cycle
        self.cycle_count = 0 #counts number of anim cycles

        #finds the amount of files per direction in anim cycle
        for file in dir_list:
            file_str = str(file)
            num = int(file[-5])

            if (num > self.g_num):
                self.g_num = num

            if (num == 0):
                self.cycle_count += 1

        
        print(self.cycle_count)
        print(self.g_num)

        for i in range(self.cycle_count+1):
            num = i
            if (i == self.g_num+1):
                num = 0
            img = pygame.image.load(os.path.join("../images", "walk", "PH_right_" + str(num) + '.png')).convert()
            self.x_images.append(img)
            self.image = self.x_images[0]
            self.image = pygame.transform.scale(self.image, [sq_size, sq_size])
            self.rect = self.image.get_rect()

            img = pygame.image.load(os.path.join("../images", "walk", "PH_down_" + str(num) + '.png')).convert()
            self.down_images.append(img)
            self.image = self.down_images[0]
            self.image = pygame.transform.scale(self.image, [sq_size, sq_size])
            self.rect = self.image.get_rect()

            img = pygame.image.load(os.path.join("../images", "walk", "PH_up_" + str(num) + ".png")).convert()
            self.up_images.append(img)
            self.image = self.up_images[0]
            self.image = pygame.transform.scale(self.image, [sq_size, sq_size])
            self.rect = self.image.get_rect()

        

    #controls movement
    def schmoove(self, x, y):
        self.move_x += x
        self.move_y += y
    
    def update_pos(self):
        
        #ani decides speed of animation cycle
        ani = 20

        sprites_num = len(self.x_images) - 1

        self.rect.x += self.move_x
        self.rect.y += self.move_y
        
        
        if self.move_x < 0:
            self.frame += 1
            if self.frame > (sprites_num * ani):
                self.frame = 0
            self.image = pygame.transform.flip(self.x_images[self.frame//ani], True, False)
            self.dir = "l"

        if self.move_x > 0:
            self.frame += 1
            if self.frame > (sprites_num * ani):
                self.frame = 0
            self.image = self.x_images[self.frame//ani]
            self.dir = "r"

        if self.move_y < 0:
            self.frame += 1
            if self.frame > (sprites_num * ani):
                self.frame = 0
            self.image = self.up_images[self.frame//ani]
            self.dir = "u"

        if self.move_y > 0:
            self.frame += 1
            if self.frame > (sprites_num * ani):
                self.frame = 0
            self.image = self.down_images[self.frame//ani]
            self.dir = "d"

        if self.move_x == 0 and self.move_y == 0:
            self.frame = 0
            if self.dir == "l":
                self.image = pygame.transform.flip(self.x_images[self.frame//ani], True, False)
            if self.dir =="r":
                self.image = self.x_images[self.frame//ani]
            if self.dir == "u":
                self.image = self.up_images[self.frame//ani]
            if self.dir == "d":
                self.image = self.down_images[self.frame//ani]        