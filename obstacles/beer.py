#!/usr/bin/env python
#coding: utf8

import pygame

from obstacles.obstacle import Obstacle

class Beer(Obstacle):
    RATIO = 0.09
    image_file = 'images/obstacles/beer.png'
    image = None

    def __init__(self, gameboard, position, speed):
        Obstacle.__init__(self,
                          self._load_image(gameboard),
                          gameboard,
                          position,
                          speed)

    def _load_image(self, gameboard):
        if not Beer.image:
            Beer.image = pygame.image.load(Beer.image_file).convert_alpha()
            height1 = Beer.image.get_height()
            width1 = Beer.image.get_width()

            height2 = int(gameboard.height * Beer.RATIO)
            width2 = int((width1 / float(height1)) * height2)

            Beer.image = pygame.transform.scale(Beer.image, (width2, height2))
        return Beer.image