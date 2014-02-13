import pygame
from pygame.sprite import Sprite


class Effect(Sprite):
    def __init__(self, entity, image, screen):
        Sprite.__init__(self)
        self.entity = entity
        self.screen = screen
        self.image = image

    def blit(self):
        pass