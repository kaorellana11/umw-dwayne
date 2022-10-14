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


        self.images = []
        img = pygame.image.load("..\images\dwayneson.png")
        self.images.append(img)
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, [sq_size, sq_size])
        self.rect = self.image.get_rect()
        prefix = "PH_down_"
        
        for i in range(6):
            cycle_num = i
            if i >= 3:
                prefix = "PH_right_"
                cycle_num -= 3
            img = pygame.image.load(os.path.join("../images", "walk", prefix + str(cycle_num) + '.png')).convert()
            self.images.append(img)
            self.image = self.images[0]
            self.image = pygame.transform.scale(self.image, [sq_size, sq_size])
            self.rect = self.image.get_rect()

    #controls movement
    def schmoove(self, x, y):
        self.move_x += x
        self.move_y += y
    
    def update_pos(self):

        ani = 4

        self.rect.x += self.move_x
        #print(self.move_x)
        self.rect.y += self.move_y
        
        if self.move_x < 0:
            self.frame += 1
            if self.frame > (3*ani):
                self.frame = 0
            self.image = self.images[self.frame//ani]

        if self.move_x > 0:
            self.frame += 1
            if self.frame > (3*ani):
                self.frame = 0
            self.image = self.images[self.frame//ani]

        