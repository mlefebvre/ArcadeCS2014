#!/usr/bin/env python
#coding: utf8

import pygame
from vec2d import vec2d
from obstacles.obstacle import Obstacle

TRACK_RATIO = 0.8
SPEED_MODIFIER = 0.5

class HealthPack(Obstacle):
    RATIO = 0.05
    image_file = 'images/obstacles/healthpack.png'
    image = None

    def __init__(self, gameboard, position, speed):
        Obstacle.__init__(self,
                          self._load_image(gameboard),
                          gameboard,
                          position,
                          speed)

    def update(self, time_passed):
        direction = vec2d(self.gameboard.player.x - self.x, self.gameboard.player.y - self.y).normalized()

        displacement = vec2d(direction.x * TRACK_RATIO * self.speed * SPEED_MODIFIER * time_passed,
                             self.speed * time_passed)

        self.x += displacement.x
        self.y += displacement.y

        w, h = self.image.get_size()
        self._change_rect(self.x, self.y, w, h)

    def _load_image(self, gameboard):
        if not HealthPack.image:
            HealthPack.image = pygame.image.load(HealthPack.image_file).convert_alpha()
            height1 = HealthPack.image.get_height()
            width1 = HealthPack.image.get_width()

            height2 = int(gameboard.height * HealthPack.RATIO)
            width2 = int((width1 / float(height1)) * height2)

            HealthPack.image = pygame.transform.smoothscale(HealthPack.image, (width2, height2))
        return HealthPack.image