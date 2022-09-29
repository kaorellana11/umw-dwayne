from entity import entity
from pygame import sprite
import pygame

class Player(sprite.Sprite):
    def __init__(self):
        super.__init__(self)
        self.images = []

        img = pygame.image.load("..\images\dwayneson.png")

        

        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.imgae.get_rect()