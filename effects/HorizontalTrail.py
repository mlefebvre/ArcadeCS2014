#!/usr/bin/env python
#coding: utf8

import math
import pygame
from effects.Effect import Effect

TRAIL_SIZE = 10
RIGHT_OFFSET = 10
LEFT_OFFSET = 20


class HorizontalTrail(Effect):
    image_file = 'images/nyan_trail_player.png'
    image = None

    def __init__(self, entity, screen, start_time):
        Effect.__init__(self,
                        entity,
                        self._load_image(),
                        screen)
        self.start_time = start_time
        self.trails = []
        self.trail_offset = 0

    def blit(self):
        if len(self.trails) == TRAIL_SIZE:
            self.trails.pop(0)

        if self.entity.orientation == 1:
            self.trail_offset = RIGHT_OFFSET
        else:
            self.trail_offset = LEFT_OFFSET

        self.trails.append([self.image, self.entity.x + 10, self.entity.y + 10])

        for trail in self.trails:
            draw_pos = self.image.get_rect().move(self.trail_offset + trail[1],
                                                  15 + trail[2] + 5 * math.cos((trail[1] + 40) / 20))
            self.screen.blit(trail[0], draw_pos)

    def kill(self):
        self.trails = []

        super(HorizontalTrail, self).kill()

    def _load_image(self):
        if not HorizontalTrail.image:
            HorizontalTrail.image = pygame.image.load(HorizontalTrail.image_file).convert_alpha()
        return HorizontalTrail.image