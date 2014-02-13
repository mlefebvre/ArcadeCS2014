import random
import pygame
import math
from effects.VerticalTrail import VerticalTrail
from obstacles.obstacle import Obstacle


class Nyan(Obstacle):
    image_file = 'images/obstacles/nyan.png'
    trail_file = 'images/nyan_trail_obstacle.png'

    def __init__(self, screen, position, speed, player):
        Obstacle.__init__(self,
                          pygame.image.load(self.image_file).convert_alpha(),
                          screen,
                          position,
                          speed,
                          player)
        self.effects.append(VerticalTrail(self, self.trail_file, self.screen))
        self.last_x = self.x
        self.amplitude = random.randint(30,120)

    def update(self, time_passed):
        displacement = 0.5 * self.speed * time_passed
        self.last_y = self.y
        self.last_x = self.x
        self.y += displacement
        self.x += 5 * math.cos((self.y + 40) / self.amplitude)

        w, h = self.image.get_size()
        self._change_rect(self.x, self.y, w, h)

        for effect in self.effects:
            effect.blit()
