#!/usr/bin/env python
#coding: utf8

import pygame

from obstacles.obstacle import Obstacle


class Vodka(Obstacle):
    image_file = 'images/obstacles/vodka.png'
    image = None

    def __init__(self, gameboard, position, speed, player):
        Obstacle.__init__(self,
                          self._load_image(),
                          gameboard,
                          position,
                          speed,
                          player)

    def _load_image(self):
        if not Vodka.image:
            Vodka.image = pygame.image.load(Vodka.image_file).convert_alpha()
        return Vodka.image