#!/usr/bin/env python
#coding: utf8

import pygame
from pygame.surface import Surface
import random
from player import Player
from obstacles.obstacle_manager import ObstacleManager
from collisionstrategies.collision_strategy_factory import CollisionStrategyFactory
from effects.doge_text import DogeText

DEFAULT_BLUR = 5
MAX_OBSTACLES = 10
OBSTACLE_BASE_SPEED = 0.4
ACCELERATION = 0.0001

class GameBoard(Surface):
    background_file = 'images/background.png'
    background_doge_file = 'images/background_doge.jpg'
    rotate_time = 0
    blur_time = 0
    rotate_angle = 0
    effects = []
    background = None
    background_doge = None

    def __init__(self, size, game, acceleration=ACCELERATION):
        Surface.__init__(self, size)
        self.width, self.height = size
        self.game = game
        self.player = Player(self, (size[0]/2, size[1]*0.8))
        self.obstacle_manager = ObstacleManager(self,
                                                OBSTACLE_BASE_SPEED,
                                                MAX_OBSTACLES,
                                                CollisionStrategyFactory(self.game),
                                                self.player)
        self.children = [self.player, self.obstacle_manager]
        self.acceleration = acceleration

    def add_child(self, child):
        self.children.append(child)

    def tick(self, time_passed):
        self.obstacle_manager.accelerate_obstacles(self.acceleration)
        self.obstacle_manager.create_obstacle()
        self.obstacle_manager.detect_collision()

        self._draw_background()

        for child in self.children:
            child.update(time_passed)
            child.blit()

        for effect in self.effects:
            if effect.is_expired():
                effect.kill()
                self.effects.remove(effect)
            else:
                effect.blit()

    def render(self):
        surface = self
        if pygame.time.get_ticks() < self.rotate_time:
            surface = pygame.transform.rotate(surface, self.rotate_angle)

        if pygame.time.get_ticks() < self.blur_time:
            surface = self._blur(surface, DEFAULT_BLUR)

        return surface

    def set_player_direction(self, direction):
        self.player.direction = direction

    def rotate(self, duration):
        if duration == 0:
            self.rotate_time = 0
        else:
            self.rotate_angle = random.choice([90, 180, 270])
            self.rotate_time = pygame.time.get_ticks() + duration * 1000

    def blur(self, duration):
        if duration == 0:
            self.blur_time = 0
        else:
            self.blur_time = pygame.time.get_ticks() + duration * 1000

    def _draw_background(self):
        if not self.background:
            self.background = pygame.image.load(self.background_file)
            self.background = pygame.transform.smoothscale(self.background, (self.width, self.height))

            self.background_doge = pygame.image.load(self.background_doge_file)
            self.background_doge = pygame.transform.smoothscale(self.background_doge, (self.width, self.height))

        if len([e for e in self.effects if type(e) == DogeText]) == 0:
            self.blit(self.background, (0, 0))
        else:
            self.blit(self.background_doge, (0, 0))

    def _blur(self, surface, amt):
        if amt < 1.0:
            raise ValueError("Arg 'amt' must be greater than 1.0, passed in value is %s"%amt)
        scale = 1.0/float(amt)
        surf_size = surface.get_size()
        scale_size = (int(surf_size[0]*scale), int(surf_size[1]*scale))
        surf = pygame.transform.smoothscale(surface, scale_size)
        surf = pygame.transform.smoothscale(surf, surf_size)
        return surf

    def reset(self):
        self.player.reset()
        self.obstacle_manager.reset()

