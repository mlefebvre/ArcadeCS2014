#!/usr/bin/env python
#coding: utf8

from collision_strategy import CollisionStrategy
from effects.DogeText import DogeText

class BeerCollisionStrategy(CollisionStrategy):
    def __init__(self, game):
        CollisionStrategy.__init__(self, game)

    def on_collision(self):
        self.game.reverse_controls(True)
        #self.game.gameboard.blur(5)
        self.game.gameboard.effects.append(DogeText(self.game.gameboard, 2000))
