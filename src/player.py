#from entity import entity
from pygame import sprite
import pygame
import os

class Player(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []
        img = pygame.image.load("..\images\dwayneson.png")
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        prefix = "PH_down_"
        
        for i in range(6):
            if i == 3:
                prefix = "PH_right_"
            print("____TEST BELOW____")
            print(prefix + str(i))
            img = pygame.image.load(os.path.join(("../images", prefix + str(i) + '.png')).convert())
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

        

        