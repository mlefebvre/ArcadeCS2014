import pygame
from pygame.sprite import Sprite

class Trail(Sprite):
    trail_file = 'images/trail.png'

    def __init__(self, image, screen, position, fade_speed):
        Sprite.__init__(self)
        self.x = position[0]
        self.y = position[1]
        self.fade_speed = fade_speed
        self.screen = screen
        self.image = image