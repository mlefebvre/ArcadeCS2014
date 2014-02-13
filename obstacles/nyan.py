import pygame

from obstacles.obstacle import Obstacle


class Nyan(Obstacle):
    image_file = 'images/obstacles/nyan.png'

    def __init__(self, screen, position, speed):
        Obstacle.__init__(self,
                          pygame.image.load(self.image_file).convert_alpha(),
                          screen,
                          position,
                          speed)