#!/usr/bin/env python
#coding: utf8

from collision_strategy import CollisionStrategy
from effects.dogetext import DogeText

class VodkaCollisionStrategy(CollisionStrategy):
    def __init__(self, game):
        CollisionStrategy.__init__(self, game)

    def on_collision(self):
        if not self.game.gameboard.player.is_immune():
            self.game.gameboard.rotate(5)
            self.game.gameboard.player.set_immune()
            #self.game.gameboard.blur(5)
            self.game.drink()
        self.game.gameboard.effects.append(DogeText(self.game.gameboard, 2000))
