#!/usr/bin/env python
#coding: utf8

import pygame
import os
from pygame.surface import Surface


class GameOverMenu(Surface):
    title_files = ['images/menus/gameover/title/1.png',
                  'images/menus/gameover/title/2.png',
                  'images/menus/gameover/title/3.png',
                  'images/menus/gameover/title/4.png']

    baby_directory = 'images/menus/gameover/baby/'

    title_images = []
    baby_images = []

    score = 0

    def __init__(self, size, game):
        Surface.__init__(self, size)
        self.width, self.height = size
        self.game = game
        self._load_images()
        self.font = pygame.font.SysFont("Comic Sans MS", int(0.09 * self.width))

    def update(self, select, switch):
        pass

    def render(self):
        self.fill((0,0,0))
        ###################################### Title ###############################
        title = self.title_images[(pygame.time.get_ticks() / 100) % len(self.title_files)]
        rect = title.get_rect()
        draw_pos = title.get_rect().move(int(self.width * 0.07), int(0.02 * self.height))
        self.blit(title, draw_pos)

        ###################################### Baby ################################
        baby = self.baby_images[(pygame.time.get_ticks() / 100) % len(self.baby_images)]
        rect = baby.get_rect()
        self.blit(baby, baby.get_rect().move(int(0.03 * self.width), int(0.17 * self.height)))
        self.blit(baby, baby.get_rect().move(int(0.79 * self.width), int(0.17 * self.height)))

        ###################################### Score ################################
        score = self.font.render(str(self.score), 1, (255, 255, 0))
        rect = score.get_rect()
        self.blit(score, rect.move(int((self.width - rect.width) / 2), int(0.18 * self.height)))

        return self

    def _load_images(self):
        self._load_title()
        self._load_baby()

    def _load_title(self):
        for f in self.title_files:
            image = pygame.image.load(f)
            rect = image.get_rect()
            image = pygame.transform.scale(image, (int(self.width * 0.85), int((rect.height / float(rect.width)) * self.width * 0.85)))
            self.title_images.append(image)

    def _load_baby(self):
        dict = {}
        for f in sorted(os.listdir(self.baby_directory)):
            if f.endswith(".gif"):
                image = pygame.image.load(self.baby_directory + f).convert_alpha()
                width1 = image.get_width()
                height1 = image.get_height()
                width2 = int(self.width * 0.15)
                height2 = int((height1 / float(width1)) * width2)
                image = pygame.transform.smoothscale(image, (width2, height2))
                dict[int(f[:f.find(".")])] = image

        self.baby_images = [dict[c] for c in sorted(dict)]

    def set_score(self, score):
        self.score = score

