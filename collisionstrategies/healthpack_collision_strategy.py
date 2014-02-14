#!/usr/bin/env python
#coding: utf8

from collision_strategy import CollisionStrategy


class HealthPackCollisionStrategy(CollisionStrategy):
    def __init__(self, game):
        CollisionStrategy.__init__(self, game)

    def on_collision(self):
        self.game.reverse_controls(False)
        self.game.gameboard.blur(0)
        self.game.gameboard.rotate(0)
