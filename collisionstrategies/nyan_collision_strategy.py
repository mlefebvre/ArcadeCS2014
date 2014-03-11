#!/usr/bin/env python
#coding: utf8

import pygame
from collision_strategy import CollisionStrategy
from effects.HorizontalTrail import HorizontalTrail


class NyanCollisionStrategy(CollisionStrategy):
    def __init__(self, game):
        CollisionStrategy.__init__(self, game)

    def on_collision(self):
        for effect in self.game.gameboard.player.effects:
            if type(effect) == "HorizontalTrail":
                return

        self.game.gameboard.player.effects.append(HorizontalTrail(self.game.gameboard.player,
                                                        self.game.gameboard,
                                                        pygame.time.get_ticks()))

        self.game.score_manager.increment_score(500)
