#!/usr/bin/env python
#coding: utf8

import pygame
from effects.effect import Effect

TRAIL_SIZE = 50


class VerticalTrail(Effect):
    image_file = 'images/nyan_trail_obstacle.png'
    image = None

    def __init__(self, entity, gameboard):
        Effect.__init__(self,
                        entity,
                        self._load_image(),
                        gameboard,
                        -1)
        self.trails = []

    def blit(self):
        if len(self.trails) == TRAIL_SIZE:
            self.trails.pop(0)

        self.trails.append([self.image, self.entity.x, self.entity.y + 10])

        for trail in self.trails:
            draw_pos = self.image.get_rect().move(trail[1], trail[2])
            self.gameboard.blit(trail[0], draw_pos)

    def kill(self):
        self.trails = []

        super(VerticalTrail, self).kill()

    def _load_image(self):
        if not VerticalTrail.image:
            VerticalTrail.image = pygame.image.load(VerticalTrail.image_file).convert_alpha()
        return VerticalTrail.image