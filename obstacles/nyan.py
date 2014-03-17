#!/usr/bin/env python
#coding: utf8

import random
import pygame
import math
from effects.vertical_trail import VerticalTrail
from obstacles.obstacle import Obstacle


class Nyan(Obstacle):
    RATIO = 0.1
    image_file = 'images/obstacles/nyan.png'
    image = None

    def __init__(self, gameboard, position, speed):
        Obstacle.__init__(self,
                          self._load_image(gameboard),
                          gameboard,
                          position,
                          speed)
        self.effects.append(VerticalTrail(self, self.gameboard))
        self.last_x = self.x
        self.amplitude = random.randint(30,120)

    def update(self, time_passed):
        displacement = 0.5 * self.speed * time_passed
        self.last_y = self.y
        self.last_x = self.x
        self.y += displacement
        self.x += 5 * math.cos((self.y + 40) / self.amplitude)

        w, h = self.image.get_size()
        self._change_rect(self.x, self.y, w, h)

        for effect in self.effects:
            effect.blit()

    def _load_image(self, gameboard):
        if not Nyan.image:
            Nyan.image = pygame.image.load(Nyan.image_file).convert_alpha()
            height1 = Nyan.image.get_height()
            width1 = Nyan.image.get_width()

            height2 = int(gameboard.height * Nyan.RATIO)
            width2 = int((width1 / float(height1)) * height2)

            Nyan.image = pygame.transform.scale(Nyan.image, (width2, height2))
        return Nyan.image
