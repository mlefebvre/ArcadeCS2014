#!/usr/bin/env python
#coding: utf8

import pygame

from obstacles.obstacle import Obstacle


class Beer(Obstacle):
    image_file = 'images/obstacles/beer.png'
    image = None

    def __init__(self, gameboard, position, speed, player):
        Obstacle.__init__(self,
                          self._load_image(),
                          gameboard,
                          position,
                          speed,
                          player)

    def _load_image(self):
        if not Beer.image:
            Beer.image = pygame.image.load(Beer.image_file).convert_alpha()
        return Beer.image