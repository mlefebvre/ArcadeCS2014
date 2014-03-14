#!/usr/bin/env python
#coding: utf8

import pygame
from pygame.surface import Surface


class MainMenu(Surface):
    fire_files = ['images/menus/top/fire1.png',
                  'images/menus/top/fire2.png',
                  'images/menus/top/fire3.png',
                  'images/menus/top/fire4.png']
    background_file = 'images/menus/mainmenu/mainmenu.png'
    star_file = 'images/menus/mainmenu/star.png'

    fire_images = []
    background_image = None
    star_image = None

    column_selected = False
    column_id = 0
    row_id = 0

    switch = False
    select = False

    schools = [['brock', 'concordia', 'ets', 'guelph', 'laval', 'manitoba'],
               ['mcgill', 'ottawa', 'poly', 'queens', 'rochester', 'sherbrooke'],
               ['shippensburg', 'toronto', 'udem', 'uqac', 'uqam', 'uqar'],
               ['uqo', 'windsor', 'york']]

    def __init__(self, size, game):
        Surface.__init__(self, size)
        self.width, self.height = size
        self.game = game
        self._load_images()
        self.font = pygame.font.SysFont("Comic Sans MS", 60)
        self.select_column_text = self.font.render("Select column", 1, (255, 255, 0))
        self.select_school_text = self.font.render("Select school", 1, (255, 255, 0))

    def reset(self):
        self.column_selected = False
        self.column_id = 0
        self.row_id = 0

    def update(self, switch, select):
        if switch:
            self.switch = True
        elif select:
            self.select = True
        elif self.switch:
            if not self.column_selected:
                self.column_id = (self.column_id + 1) % len(self.schools)
            else:
                self.row_id = (self.row_id + 1) % len(self.schools[self.column_id])
            self.switch = False
        elif self.select:
            if not self.column_selected:
                self.column_selected = True
                self.select = False
            else:
                school = self.schools[self.column_id][self.row_id]
                self.reset()
                self.game.start_game(school)

    def render(self):
        self.blit(self.background_image, self.background_image.get_rect())

        fire = self.fire_images[(pygame.time.get_ticks() / 150) % len(self.fire_files)]
        rect = fire.get_rect()
        draw_pos = fire.get_rect().move(int(self.width * 0.07), int(0.15 * self.height))
        self.blit(fire, draw_pos)

        if ((pygame.time.get_ticks()) / 300) % 2 == 0:
            self.blit(self.star_image, self.star_image.get_rect().move(int(self.width * 0.07), int(self.height * 0.04)))

        if ((pygame.time.get_ticks()) / 300) % 2 == 1:
            self.blit(self.star_image, self.star_image.get_rect().move(int(self.width * 0.84), int(self.height * 0.04)))

        if not self.column_selected:
            self.blit(self.select_column_text, self.select_column_text.get_rect().move(int(self.width * 0.22), int(self.height * 0.02)))
        else:
            self.blit(self.select_school_text, self.select_school_text.get_rect().move(int(self.width * 0.22), int(self.height * 0.02)))

        if not self.column_selected:
            pygame.draw.rect(self,
                             (255, 255, 0),
                             pygame.Rect((0.075 * self.width + 0.213 * self.width * self.column_id,
                                          0.224 * self.height),
                                         (0.213 * self.width,
                                          self.height * 0.0925 * len(self.schools[self.column_id]))),
                             10)
        else:
            pygame.draw.rect(self,
                             (255, 255, 0),
                             pygame.Rect((0.075 * self.width + 0.213 * self.width * self.column_id,
                                          0.224 * self.height + 0.0925 * self.height * self.row_id),
                                         (0.213 * self.width,
                                          0.0925 * self.height)),
                             10)

        return self

    def _load_images(self):
        self._load_background()
        self._load_fire()
        self._load_star()

    def _load_fire(self):
        for f in self.fire_files:
            image = pygame.image.load(f)
            rect = image.get_rect()
            image = pygame.transform.scale(image, (int(self.width * 0.85), int((rect.height / float(rect.width)) * self.width * 0.85 * 0.80)))
            self.fire_images.append(image)

    def _load_background(self):
        self.background_image = pygame.image.load(self.background_file)
        rect = self.background_image.get_rect()
        self.background_image = pygame.transform.scale(self.background_image,
                                                      (self.width, int((rect.height / float(rect.width)) * self.width)))

    def _load_star(self):
        self.star_image = pygame.image.load(self.star_file).convert_alpha()
        height1 = self.star_image.get_height()
        width1 = self.star_image.get_width()

        height2 = int(self.height * 0.10)
        width2 = int((width1 / float(height1)) * height2)

        self.star_image = pygame.transform.scale(self.star_image, (width2, height2))