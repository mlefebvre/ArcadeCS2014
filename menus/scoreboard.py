#!/usr/bin/env python
#coding: utf8

import pygame
from pygame.surface import Surface

class ScoreBoard(Surface):

    score_file = 'images/menus/scoreboard/score.png'
    score_image = None

    number_folder = 'images/menus/scoreboard/'

    number_images = {}

    def __init__(self, size, score_manager):
        Surface.__init__(self, size)
        self.background = None
        self.width, self.height = size
        self.score_manager = score_manager
        self._load_images()

    def update(self, time_passed):
        pass

    def render(self):
        self.fill((0, 0, 0))

        self.blit(self.score_image, self.score_image.get_rect().move(0, self.height * 0.10))
        self._display_score(self.score_manager.get_score(), self.height * 0.17)
        return self

    def _display_score(self, score, y):
        i = 0
        x = self.width - 55

        while score > 0:
            val = score % 10
            score /= 10
            i += 1
            image = self.number_images[val]
            self.blit(image, image.get_rect().move(x, y))
            x -= 35

        while i < 8:
            i += 1
            image = self.number_images[0]
            self.blit(image, image.get_rect().move(x, y))
            x -= 35


    def _load_images(self):
        self.score_image = pygame.image.load(self.score_file)

        for i in range(10):
            self.number_images[i] = pygame.image.load(self.number_folder + str(i) + ".png")
