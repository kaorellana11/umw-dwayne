from pygame import sprite
import pygame


class Entity(sprite.Sprite):

    def __init__(self):
        super().__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        
