#!/usr/bin/env python
#coding: utf8

import pygame
from pygame.surface import Surface


class TopMenu(Surface):

    fire_files = ['images/menus/top/fire1.png',
                  'images/menus/top/fire2.png',
                  'images/menus/top/fire3.png',
                  'images/menus/top/fire4.png']
    title_file = 'images/menus/top/title.jpg'

    fire_images = []
    title_image = None
    ticks = 0
    fire_id = 0

    def __init__(self, size):
        Surface.__init__(self, size)
        self.width, self.height = size
        self._load_title()
        self._load_fire()
        self._init_board()

    def update(self, time_passed):
        pass

    def _init_board(self):
        self.fill((0, 0, 0))
        self.blit(self.title_image, self.title_image.get_rect().move(0, 0.12 * self.height))

    def render(self):
        self.ticks += 1
        id = (self.ticks / 6) % len(self.fire_files)
        if id != self.fire_id:
            self.fire_id = id
            image = self.fire_images[id]
            rect = image.get_rect()
            draw_pos = image.get_rect().move(0, self.height - rect.height)
            self.blit(image, draw_pos)

        return self

    def _load_fire(self):
        for f in self.fire_files:
            image = pygame.image.load(f)
            rect = image.get_rect()
            image = pygame.transform.scale(image, (self.width, int(0.88 * self.height) - self.title_image.get_rect().height))
            self.fire_images.append(image)

    def _load_title(self):
        self.title_image = pygame.image.load(self.title_file)
        rect = self.title_image.get_rect()
        self.title_image = pygame.transform.scale(self.title_image,
                                                  (self.width, int((rect.height / float(rect.width)) * self.width)))