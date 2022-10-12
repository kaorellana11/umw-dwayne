#from entity import entity
from pygame import sprite
import pygame
import os

class Player(sprite.Sprite):
    def __init__(self):
        super().__init__(self)
        self.images = []
        img = pygame.image.load("..\images\dwayneson.png")
        self.images.append(img)
        self.image = self.images[0]
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
            self.rect = self.image.get_rect()

        

        