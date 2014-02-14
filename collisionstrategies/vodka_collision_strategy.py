#!/usr/bin/env python
#coding: utf8

from collision_strategy import CollisionStrategy


class VodkaCollisionStrategy(CollisionStrategy):
    def __init__(self, game):
        CollisionStrategy.__init__(self, game)

    def on_collision(self):
        self.game.gameboard.rotate(5)
