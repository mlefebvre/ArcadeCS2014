#!/usr/bin/env python
#coding: utf8

import pygame
import os
from pygame.surface import Surface
import time
from game_state import GameState

DISPLAY_TIME = 5

class GameOverMenu(Surface):
    title_files = ['images/menus/gameover/title/1.png',
                  'images/menus/gameover/title/2.png',
                  'images/menus/gameover/title/3.png',
                  'images/menus/gameover/title/4.png']

    baby_directory = 'images/menus/gameover/baby/'

    background_file = 'images/menus/gameover/background.png'
    background = None

    title_images = []
    baby_images = []
    start_time = 0

    score = 0

    def __init__(self, size, game):
        Surface.__init__(self, size)
        self.width, self.height = size
        self.game = game
        self._load_images()
        self.font = pygame.font.SysFont("Comic Sans MS", int(0.09 * self.width))
        self.hsfont = pygame.font.SysFont("Comic Sans MS", int(0.09 * self.width))

    def update(self, score):
        self.score = score
        self.start_time = time.time()

        self.blit(self.background, (0, 0))

        ###################################### Score ################################
        score = self.font.render(str(self.score), 1, (255, 255, 0))
        rect = score.get_rect()
        self.blit(score, rect.move(int((self.width - rect.width) / 2), int(0.18 * self.height)))

        ################################# High scores ###############################
        hs = self.game.score_manager.get_high_scores()

        hs1 = self.font.render(hs[0][0] + ":  " + str(hs[0][1]), 1, (255, 255, 0))
        rect = hs1.get_rect()
        self.blit(hs1, rect.move(int((self.width - rect.width) / 2), int(0.495 * self.height)))

        if len(hs) >= 2:
            hs2 = self.font.render(hs[1][0] + ":  " + str(hs[1][1]), 1, (255, 255, 0))
            rect = hs2.get_rect()
            self.blit(hs2, rect.move(int((self.width - rect.width) / 2), int(0.635 * self.height)))

            if len(hs) >= 3:
                hs3 = self.font.render(hs[2][0] + ":  " + str(hs[2][1]), 1, (255, 255, 0))
                rect = hs3.get_rect()
                self.blit(hs3, rect.move(int((self.width - rect.width) / 2), int(0.78 * self.height)))

    def render(self):
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

        if time.time() > self.start_time + DISPLAY_TIME:
            self.game.state = GameState.MainMenu

        return self

    def _load_images(self):
        self._load_title()
        self._load_baby()
        self._load_background()

    def _load_title(self):
        for f in self.title_files:
            image = pygame.image.load(f)
            rect = image.get_rect()
            image = pygame.transform.smoothscale(image, (int(self.width * 0.85), int((rect.height / float(rect.width)) * self.width * 0.85)))
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

    def _load_background(self):
        self.background = pygame.image.load(self.background_file)
        self.background = pygame.transform.smoothscale(self.background, (self.width, self.height))


