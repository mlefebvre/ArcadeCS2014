#!/usr/bin/env python
#coding: utf8

import pygame
from collision_strategy import CollisionStrategy
from effects.HorizontalTrail import HorizontalTrail


class NyanCollisionStrategy(CollisionStrategy):
    def __init__(self, game):
        CollisionStrategy.__init__(self, game)

    def on_collision(self):
        for effect in self.game.player.effects:
            if type(effect) == "HorizontalTrail":
                return

        self.game.player.effects.append(HorizontalTrail(self.game.player,
                                                        self.game.gameboard,
                                                        pygame.time.get_ticks()))

        self.game.score_manager.increment_score(500)
