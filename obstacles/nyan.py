import pygame
import math
from effects.Trail import Trail

from obstacles.obstacle import Obstacle

TRAIL_SIZE = 50

class Nyan(Obstacle):
    rainbow = []
    image_file = 'images/obstacles/nyan.png'
    trail_file = 'images/trail.png'

    def __init__(self, screen, position, fall_speed, player):
        Obstacle.__init__(self,
                          pygame.image.load(self.image_file).convert_alpha(),
                          screen,
                          position,
                          fall_speed,
                          player)

        self.last_x = self.x

    def trail(self):
        if len(self.rainbow) == TRAIL_SIZE:
            self.rainbow.pop(0)

        self.rainbow.append(Trail(pygame.image.load(self.trail_file).convert_alpha(),
                                self.screen,
                                [self.x, self.y + 10],
                                15))

        for part in self.rainbow:
            draw_pos = self.image.get_rect().move(part.x, part.y)
            # Ca ne marche pas?
            #part.image.set_alpha(part.image.get_alpha() - part.fade_speed)
            self.screen.blit(part.image, draw_pos)

    def update(self, time_passed):
        displacement = 0.5 * self.fall_speed * time_passed
        self.last_y = self.y
        self.last_x = self.x
        self.y += displacement
        self.x += 5 * math.cos((self.y + 40) / 100)

        w, h = self.image.get_size()
        self._change_rect(self.x, self.y, w, h)

        if self.alive():
            self.trail()

    def kill(self):
        del self.rainbow[:]

        super(Nyan, self).kill()
