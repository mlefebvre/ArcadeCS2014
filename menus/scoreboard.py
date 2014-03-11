#!/usr/bin/env python
#coding: utf8

import pygame
from pygame.surface import Surface

NUMBER_RATIO = 0.091

class ScoreBoard(Surface):

    score_file = 'images/menus/scoreboard/score.png'
    line_file = 'images/menus/scoreboard/rainbow.png'
    number_folder = 'images/menus/scoreboard/'

    score_image = None
    line_image = None
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

        i = 0.015
        self.blit(self.line_image, self.line_image.get_rect().move(0, self.height * i))
        i += 0.01
        self.blit(self.score_image, self.score_image.get_rect().move(0, self.height * i))
        i += 0.07
        self._display_score(self.score_manager.get_score(), self.height * i)
        i += 0.055
        self.blit(self.line_image, self.line_image.get_rect().move(0, self.height * i))

        return self

    def _display_score(self, score, y):
        i = 0
        x = 0.833 * self.width

        while score > 0:
            val = score % 10
            score /= 10
            i += 1
            image = self.number_images[val]
            self.blit(image, image.get_rect().move(x, y))
            x -= self.width * 0.11

        while i < 8:
            i += 1
            image = self.number_images[0]
            self.blit(image, image.get_rect().move(x, y))
            x -= self.width * 0.11


    def _load_images(self):
        self._load_title_image()
        self._load_line_image()
        self._load_number_images()

    def _load_title_image(self):
        self.score_image = pygame.image.load(self.score_file)
        rect = self.score_image.get_rect()
        self.score_image = pygame.transform.scale(self.score_image,
                                                  (self.width, int((rect.height / float(rect.width)) * self.width)))

    def _load_line_image(self):
        self.line_image = pygame.image.load(self.line_file)
        rect = self.line_image.get_rect()
        self.line_image = pygame.transform.scale(self.line_image,
                                                  (self.width, int((rect.height / float(rect.width)) * self.width)))

    def _load_number_images(self):
        for i in range(10):
            self.number_images[i] = pygame.image.load(self.number_folder + str(i) + ".png")
            width1 = self.number_images[i].get_width()
            height1 = self.number_images[i].get_height()

            width2 = int(self.width * NUMBER_RATIO)
            height2 = int((height1 / float(width1)) * width2)

            self.number_images[i] = pygame.transform.scale(self.number_images[i], (width2, height2))
