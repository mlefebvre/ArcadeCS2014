#!/usr/bin/env python
#coding: utf8

import pygame
from pygame.surface import Surface


class TopMenu(Surface):

    fire_files = ['images/menus/top/fire1.png',
                  'images/menus/top/fire2.png',
                  'images/menus/top/fire3.png',
                  'images/menus/top/fire4.png']
    title_file = 'images/menus/top/title.png'

    fire_images = []
    title_image = None
    ticks = 0

    def __init__(self, size):
        Surface.__init__(self, size)
        self.width, self.height = size
        self._load_fire()
        self._load_title()

    def update(self, time_passed):
        pass

    def render(self):
        self.ticks += 1
        self.fill((0, 0, 0))

        image = self.fire_images[(self.ticks / 6) % len(self.fire_files)]
        rect = image.get_rect()
        draw_pos = image.get_rect().move(0, self.height - rect.height)
        self.blit(image, draw_pos)

        self.blit(self.title_image, self.title_image.get_rect().move(0, 0.1 * self.height))

        return self

    def _load_fire(self):
        for f in self.fire_files:
            image = pygame.image.load(f)
            rect = image.get_rect()
            image = pygame.transform.scale(image, (self.width, int((rect.height / float(rect.width)) * self.width)))
            self.fire_images.append(image)

    def _load_title(self):
        self.title_image = pygame.image.load(self.title_file)
        rect = self.title_image.get_rect()
        self.title_image = pygame.transform.scale(self.title_image,
                                                  (self.width, int((rect.height / float(rect.width)) * self.width)))