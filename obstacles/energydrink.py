#!/usr/bin/env python
#coding: utf8

import pygame

from obstacles.obstacle import Obstacle


class EnergyDrink(Obstacle):
    image_file = 'images/obstacles/energydrink.png'
    image = None

    def __init__(self, gameboard, position, speed, player):
        Obstacle.__init__(self,
                          self._load_image(),
                          gameboard,
                          position,
                          speed,
                          player)

    def _load_image(self):
        if not EnergyDrink.image:
            EnergyDrink.image = pygame.image.load(EnergyDrink.image_file).convert_alpha()
        return EnergyDrink.image