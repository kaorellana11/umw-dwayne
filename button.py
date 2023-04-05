from pygame import sprite
import pygame
import os


class Button(pygame.sprite.Sprite):
    def __init__(self, img_path, row, col):
        super().__init__(self)
        self.click = False
        ##Function to make sure they can coexist in the same spot

        