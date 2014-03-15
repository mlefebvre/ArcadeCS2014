#!/usr/bin/env python
#coding: utf8

import os
import pygame
from pygame.sprite import Sprite

COLLISION_PADDING = 0.3   # %
SPEED = 0.3
RATIO = 0.12
IMMUNITY_DELAY = 2000

class Player(Sprite):
    image_directory = 'images/player/'
    image_drunk_directory = 'images/player/drunk/'
    images = {-1: [], 1: []}
    images_drunk = {-1: [], 1: []}
    effects = []
    orientation = 1
    counter = 0
    still_counter = 0
    image_id = 0
    direction = 1
    immunity_start = -10000
    ticks = 0

    def __init__(self, gameboard, position):
        Sprite.__init__(self)
        self.x = position[0]
        self.y = position[1]
        self.gameboard = gameboard
        self.speed = SPEED
        self._load_images(gameboard)
        self._load_drunk_images(gameboard)
        w, h = self.images[self.orientation][self.image_id].get_size()
        self._change_rect(self.x, self.y, w, h)

    def update(self, time_passed):

        if self.direction != 0:
            self.still_counter = 0
            self.counter += 1
            if self.counter % 5 == 0:
                self.image_id = (self.image_id + 1) % len(self.images[self.orientation])
                # L'image 0 est pour quand on bouge pas
                if self.image_id == 0:
                    self.image_id = 1
        else:
            self.still_counter += 1
            if self.still_counter > 5:
                self.image_id = 0


        if self.orientation != self.direction and self.direction != 0:
            self.orientation = -self.orientation

        displacement = self.direction * self.speed * time_passed

        new_x = self.x + displacement
        w, h = self.images[self.orientation][self.image_id].get_size()

        if new_x > 0 and new_x + w < self.gameboard.width:
            self.x = new_x
            self._change_rect(self.x, self.y, w, h)

        for effect in self.effects:
            if effect.is_expired():
                effect.kill()
                self.effects.remove(effect)
            else:
                effect.blit()

    def set_speed(self, speed):
        self.speed = speed

    def increment_speed(self):
        if self.speed * 1.2 < 0.7:
            self.speed *= 1.2


    def blit(self):
        self.ticks += 1
        #print (self.ticks / 5)
        draw_pos = self.images[self.orientation][self.image_id].get_rect().move(self.x, self.y)
        if self.is_immune() and (self.ticks / 10) % 2 == 0:
           self.gameboard.blit(self.images_drunk[self.orientation][self.image_id], draw_pos)
        else:
            self.gameboard.blit(self.images[self.orientation][self.image_id], draw_pos)

    def _load_images(self, gameboard):
        for f in sorted(os.listdir(self.image_directory)):
            if f.endswith(".png"):
                image = pygame.image.load(self.image_directory + f).convert_alpha()
                height1 = image.get_height()
                width1 = image.get_width()
                height2 = int(gameboard.height * RATIO)
                width2 = int((width1 / float(height1)) * height2)
                image = pygame.transform.smoothscale(image, (width2, height2))

                self.images[1].append(image)
                self.images[-1].append(pygame.transform.flip(self.images[1][-1], True, False))

    def _load_drunk_images(self, gameboard):
        for f in sorted(os.listdir(self.image_directory)):
            if f.endswith(".png"):
                image = pygame.image.load(self.image_drunk_directory + f).convert_alpha()
                height1 = image.get_height()
                width1 = image.get_width()
                height2 = int(gameboard.height * RATIO)
                width2 = int((width1 / float(height1)) * height2)
                image = pygame.transform.smoothscale(image, (width2, height2))

                self.images_drunk[1].append(image)
                self.images_drunk[-1].append(pygame.transform.flip(self.images_drunk[1][-1], True, False))

    def _change_rect(self, x, y, w, h):
        self.rect = pygame.Rect(x + w * COLLISION_PADDING,
                                y + h * COLLISION_PADDING,
                                w - 2 * w * COLLISION_PADDING,
                                h - 2 * h * COLLISION_PADDING)

    def set_immune(self):
        self.immunity_start = pygame.time.get_ticks()

    def is_immune(self):
        return self.immunity_start + IMMUNITY_DELAY > pygame.time.get_ticks()

    def reset(self):
        self.speed = SPEED




