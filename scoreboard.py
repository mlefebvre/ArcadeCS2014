#!/usr/bin/env python
#coding: utf8

import pygame
from pygame.surface import Surface


class ScoreBoard(Surface):

    scoreboard = {"Brock": 0,
                  "Concordia": 0,
                  "ÉTS": 0,
                  "McGill": 0,
                  "Polytechnique": 0,
                  "Queen's": 0,
                  "Ryerson": 0,
                  "Shippensburg": 0,
                  "Western Ontario": 0,
                  "UdeM": 0,
                  "Sherbrooke": 0,
                  "UQAC": 0,
                  "UQAM": 0,
                  "UQAR": 0,
                  "UQO": 0,
                  "Laval": 0,
                  "Guelph": 0,
                  "Manitoba": 0,
                  "Rochester": 0,
                  "Toronto": 0,
                  "Windsor": 0}

    def __init__(self, size):
        Surface.__init__(self, size)
        self.children = []
        self.background = None
        self.width, self.height = size

    def update(self, time_passed):
        pass

    def render(self):
        self.fill((0, 0, 255))
        return self
