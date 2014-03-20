#!/usr/bin/env python
#coding: utf8

import pygame

from obstacles.obstacle import Obstacle


class Vodka(Obstacle):
    RATIO = 0.11
    image_file = 'images/obstacles/vodka.png'
    image = None

    def __init__(self, gameboard, position, speed):
        Obstacle.__init__(self,
                          self._load_image(gameboard),
                          gameboard,
                          position,
                          speed)

    def _load_image(self, gameboard):
        if not Vodka.image:
            Vodka.image = pygame.image.load(Vodka.image_file).convert_alpha()
            height1 = Vodka.image.get_height()
            width1 = Vodka.image.get_width()

            height2 = int(gameboard.height * Vodka.RATIO)
            width2 = int((width1 / float(height1)) * height2)

            Vodka.image = pygame.transform.smoothscale(Vodka.image, (width2, height2))
        return Vodka.image