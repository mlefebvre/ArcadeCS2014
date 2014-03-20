#!/usr/bin/env python
#coding: utf8

import pygame
from pygame.surface import Surface

NUMBER_RATIO = 0.09
MAX_LIVES = 5
SCORE_SIZE = 6

class ScoreBoard(Surface):

    score_file = 'images/menus/scoreboard/score.png'
    line_file = 'images/menus/scoreboard/rainbow.png'
    number_folder = 'images/menus/scoreboard/'
    life_file = 'images/menus/scoreboard/beer.jpg'
    no_life_file = 'images/menus/scoreboard/empty_beer.jpg'
    help_file = 'images/menus/scoreboard/help.png'
    drunkest_schools_file = 'images/menus/scoreboard/drunkest_schools.png'
    cumulative_score_file = 'images/menus/scoreboard/best_cumulative_score.png'

    score_image = None
    line_image = None
    number_images = {}
    life_image = None
    no_life_image = None
    help_image = None
    drunkest_schools_image = None
    cumulative_score_image = None
    lives = MAX_LIVES
    ticks = 0
    update_life_display = False
    display_count = 0

    def __init__(self, size, score_manager):
        Surface.__init__(self, size)
        self.background = None
        self.width, self.height = size
        self.font = pygame.font.SysFont("Comic Sans MS", int(0.09 * self.width))
        self.font2 = pygame.font.SysFont("Comic Sans MS", int(0.07 * self.width))
        self.score_manager = score_manager
        self._load_images()
        self._init_board()

    def update(self, time_passed):
        pass

    def reset(self):
        self.lives = MAX_LIVES
        self._init_board()

    def _init_board(self):
        self.display_count += 1
        self.fill((0, 0, 0))
        i = 0.015
        self.blit(self.line_image, self.line_image.get_rect().move(0, self.height * i))
        i += 0.01
        self.blit(self.score_image, self.score_image.get_rect().move(0, self.height * i))
        i += 0.125
        self.blit(self.line_image, self.line_image.get_rect().move(0, self.height * i))
        i += 0.115
        self.blit(self.line_image, self.line_image.get_rect().move(0, self.height * i))

        i += 0.01

        if self.display_count % 2 == 0:
            self.display_cumulative_score(i)
        else:
            self.display_drunkest_schools(i)

        i = 0.615
        self.blit(self.line_image, self.line_image.get_rect().move(0, self.height * i))

        rect = self.help_image.get_rect()
        self.blit(self.help_image, rect.move(0, self.height - rect.height))

        self._display_life()

    def display_drunkest_schools(self, i):
        self.blit(self.drunkest_schools_image, self.drunkest_schools_image.get_rect().move(0, self.height * i))
        ds = self.score_manager.get_drunkest_schools()
        if len(ds) > 0:
            i += 0.07
            school = self.font.render(ds[0][0], 1, (255, 0, 0))
            sips = self.font2.render(str(ds[0][1] * 5) + " sips", 1, (255, 255, 0))
            self.blit(school, school.get_rect().move((self.width - school.get_rect().width) / 2, self.height * i))
            i += 0.045
            self.blit(sips, sips.get_rect().move((self.width - sips.get_rect().width) / 2, self.height * i))
            if len(ds) > 1:
                i += 0.04
                school = self.font.render(ds[1][0], 1, (255, 0, 0))
                sips = self.font2.render(str(ds[1][1] * 5) + " sips", 1, (255, 255, 0))
                self.blit(school, school.get_rect().move((self.width - school.get_rect().width) / 2, self.height * i))
                i += 0.045
                self.blit(sips, sips.get_rect().move((self.width - sips.get_rect().width) / 2, self.height * i))
                if len(ds) > 2:
                    i += 0.04
                    school = self.font.render(ds[2][0], 1, (255, 0, 0))
                    sips = self.font2.render(str(ds[2][1] * 5) + " sips", 1, (255, 255, 0))
                    self.blit(school, school.get_rect().move((self.width - school.get_rect().width) / 2, self.height * i))
                    i += 0.045
                    self.blit(sips, sips.get_rect().move((self.width - sips.get_rect().width) / 2, self.height * i))

    def display_cumulative_score(self, i):
        self.blit(self.cumulative_score_image, self.cumulative_score_image.get_rect().move(0, self.height * i))
        cs = self.score_manager.get_cumulative_school_score()
        if len(cs) > 0:
            i += 0.07
            cs1 = self.font.render(cs[0][0], 1, (255, 0, 0))
            self.blit(cs1, cs1.get_rect().move((self.width - cs1.get_rect().width) / 2, self.height * i))
            i += 0.045
            self._display_score(cs[0][1], self.height * i)
            if len(cs) > 1:
                i += 0.04
                cs2 = self.font.render(cs[1][0], 1, (255, 0, 0))
                self.blit(cs2, cs2.get_rect().move((self.width - cs2.get_rect().width) / 2, self.height * i))
                i += 0.045
                self._display_score(cs[1][1], self.height * i)
                if len(cs) > 2:
                    i += 0.04
                    cs3 = self.font.render(cs[2][0], 1, (255, 0, 0))
                    self.blit(cs3, cs3.get_rect().move((self.width - cs3.get_rect().width) / 2, self.height * i))
                    i += 0.045
                    self._display_score(cs[2][1], self.height * i)

    def render(self):
        self.ticks += 1
        if self.ticks % 3 == 0:
            self._display_score(self.score_manager.get_score(), self.height * 0.095)

        if self.update_life_display:
            self.update_life_display = False
            self._display_life()

        return self

    def _display_life(self):
        i = 0.175
        x = 0.05 * self.width
        for k in range(MAX_LIVES):
            rect = self.life_image.get_rect()
            x += (0.2/MAX_LIVES) * self.width
            if k >= self.lives:
                self.blit(self.no_life_image, rect.move(x, self.height * i))
            else:
                self.blit(self.life_image, rect.move(x, self.height * i))
            x += rect.width

    def _display_score(self, score, y):
        i = 0
        x = 0.9 * self.width

        while score > 0:
            val = score % 10
            score /= 10
            i += 1
            image = self.number_images[val]
            x -= image.get_rect().width
            self.blit(image, image.get_rect().move(x, y))
            x -= ((1 - (SCORE_SIZE * NUMBER_RATIO) - 0.2)/SCORE_SIZE) * self.width

        while i < SCORE_SIZE:
            i += 1
            image = self.number_images[0]
            x -= image.get_rect().width
            self.blit(image, image.get_rect().move(x, y))
            x -= ((1 - (SCORE_SIZE * NUMBER_RATIO) - 0.2)/SCORE_SIZE) * self.width

    def _load_images(self):
        self._load_title_image()
        self._load_line_image()
        self._load_number_images()
        self._load_life_images()
        self._load_help_image()
        self._load_drunkest_schools_image()
        self._load_cumulative_score_image()

    def _load_title_image(self):
        self.score_image = pygame.image.load(self.score_file)
        rect = self.score_image.get_rect()
        self.score_image = pygame.transform.smoothscale(self.score_image,
                                                  (self.width, int((rect.height / float(rect.width)) * self.width)))

    def _load_line_image(self):
        self.line_image = pygame.image.load(self.line_file)
        rect = self.line_image.get_rect()
        self.line_image = pygame.transform.smoothscale(self.line_image,
                                                  (self.width, int((rect.height / float(rect.width)) * self.width)))

    def _load_number_images(self):
        for i in range(10):
            self.number_images[i] = pygame.image.load(self.number_folder + str(i) + ".png")
            width1 = self.number_images[i].get_width()
            height1 = self.number_images[i].get_height()

            width2 = int(self.width * NUMBER_RATIO)
            height2 = int((height1 / float(width1)) * width2)

            self.number_images[i] = pygame.transform.smoothscale(self.number_images[i], (width2, height2))

    def remove_life(self):
        self.lives -= 1
        self.update_life_display = True

    def is_game_over(self):
        return self.lives <= 0

    def _load_life_images(self):
        self.life_image = pygame.image.load(self.life_file)
        self.no_life_image = pygame.image.load(self.no_life_file)
        width1 = self.life_image.get_width()
        height1 = self.life_image.get_height()

        width2 = int((self.width / MAX_LIVES) * 0.7)
        height2 = int((height1 / float(width1)) * width2)

        self.life_image = pygame.transform.smoothscale(self.life_image, (width2, height2))
        self.no_life_image = pygame.transform.smoothscale(self.no_life_image, (width2, height2))

    def _load_help_image(self):
        self.help_image = pygame.image.load(self.help_file)
        width1 = self.help_image.get_width()
        height1 = self.help_image.get_height()

        width2 = int(self.width)
        height2 = int((height1 / float(width1)) * width2)

        self.help_image = pygame.transform.smoothscale(self.help_image, (width2, height2))

    def _load_drunkest_schools_image(self):
        self.drunkest_schools_image = pygame.image.load(self.drunkest_schools_file)
        width1 = self.drunkest_schools_image.get_width()
        height1 = self.drunkest_schools_image.get_height()

        width2 = int(self.width)
        height2 = int((height1 / float(width1)) * width2)

        self.drunkest_schools_image = pygame.transform.smoothscale(self.drunkest_schools_image, (width2, height2))

    def _load_cumulative_score_image(self):
        self.cumulative_score_image = pygame.image.load(self.cumulative_score_file)
        width1 = self.cumulative_score_image.get_width()
        height1 = self.cumulative_score_image.get_height()

        width2 = int(self.width)
        height2 = int((height1 / float(width1)) * width2)

        self.cumulative_score_image= pygame.transform.smoothscale(self.cumulative_score_image, (width2, height2))