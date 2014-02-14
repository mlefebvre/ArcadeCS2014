#!/usr/bin/env python
#coding: utf8

import pygame
from pygame.surface import Surface


class ScoreBoard(Surface):

    def __init__(self, size, score_manager):
        Surface.__init__(self, size)
        self.background = None
        self.width, self.height = size
        self.score_manager = score_manager

    def update(self, time_passed):
        pass

    def render(self):
        self.fill((0, 0, 0))
        return self
