#!/usr/bin/env python
#coding: utf8

import pygame

from obstacles.obstacle import Obstacle


class EnergyDrink(Obstacle):
    RATIO = 0.09
    image_file = 'images/obstacles/energydrink.png'
    image = None

    def __init__(self, gameboard, position, speed):
        Obstacle.__init__(self,
                          self._load_image(gameboard),
                          gameboard,
                          position,
                          speed)

    def _load_image(self, gameboard):
        if not EnergyDrink.image:
            EnergyDrink.image = pygame.image.load(EnergyDrink.image_file).convert_alpha()
            height1 = EnergyDrink.image.get_height()
            width1 = EnergyDrink.image.get_width()

            height2 = int(gameboard.height * EnergyDrink.RATIO)
            width2 = int((width1 / float(height1)) * height2)

            EnergyDrink.image = pygame.transform.scale(EnergyDrink.image, (width2, height2))
        return EnergyDrink.image