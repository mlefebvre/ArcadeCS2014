import pygame

from obstacles.obstacle import Obstacle


class Vodka(Obstacle):
    image_file = 'images/obstacles/vodka.png'

    def __init__(self, screen, position, speed, player):
        Obstacle.__init__(self,
                          pygame.image.load(self.image_file).convert_alpha(),
                          screen,
                          position,
                          speed,
                          player)