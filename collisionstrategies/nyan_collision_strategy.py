import pygame
from collision_strategy import CollisionStrategy
from effects.HorizontalTrail import HorizontalTrail


class NyanCollisionStrategy(CollisionStrategy):
    trail_file = 'images/nyan_trail_player.png'

    def __init__(self, machine):
        CollisionStrategy.__init__(self, machine)

    def on_collision(self):
        for effect in self.machine.player.effects:
            if type(effect) == "HorizontalTrail":
                return

        self.machine.player.effects.append(HorizontalTrail(self.machine.player, self.trail_file, self.machine.screen, pygame.time.get_ticks()))
