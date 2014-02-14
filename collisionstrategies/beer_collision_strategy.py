#!/usr/bin/env python
#coding: utf8

from collision_strategy import CollisionStrategy


class BeerCollisionStrategy(CollisionStrategy):
    def __init__(self, game):
        CollisionStrategy.__init__(self, game)

    def on_collision(self):
        self.game.reverse_controls(True)
        self.game.gameboard.blur(5)
