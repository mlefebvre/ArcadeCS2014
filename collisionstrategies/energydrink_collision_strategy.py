#!/usr/bin/env python
#coding: utf8

from collision_strategy import CollisionStrategy


class EnergyDrinkCollisionStrategy(CollisionStrategy):
    def __init__(self, game):
        CollisionStrategy.__init__(self, game)

    def on_collision(self):
        self.game.player.increment_speed()
