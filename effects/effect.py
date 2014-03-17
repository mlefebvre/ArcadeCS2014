#!/usr/bin/env python
#coding: utf8

import pygame
from pygame.sprite import Sprite


class Effect(Sprite):
    def __init__(self, entity, image, gameboard, duration):
        Sprite.__init__(self)
        self.entity = entity
        self.gameboard = gameboard
        self.image = image
        self.start_time = pygame.time.get_ticks()
        self.duration = duration

    def is_expired(self):
        if self.duration == -1:
            return False
        else:
            return self.start_time + self.duration < pygame.time.get_ticks()

    def blit(self):
        pass