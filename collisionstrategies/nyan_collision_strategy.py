#!/usr/bin/env python
#coding: utf8

import pygame
from collision_strategy import CollisionStrategy
from effects.HorizontalTrail import HorizontalTrail


class NyanCollisionStrategy(CollisionStrategy):
    trail_file = 'images/nyan_trail_player.png'

    def __init__(self, game):
        CollisionStrategy.__init__(self, game)

    def on_collision(self):
        for effect in self.game.player.effects:
            if type(effect) == "HorizontalTrail":
                return

        self.game.player.effects.append(HorizontalTrail(self.game.player,
                                                        self.trail_file,
                                                        self.game.gameboard,
                                                        pygame.time.get_ticks()))
