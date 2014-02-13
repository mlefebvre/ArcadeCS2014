import pygame
from vec2d import vec2d
from obstacles.obstacle import Obstacle

TRACK_RATIO = 0.3

class HealthPack(Obstacle):
    image_file = 'images/obstacles/healthpack.png'

    def __init__(self, screen, position, speed, player):
        Obstacle.__init__(self,
                          pygame.image.load(self.image_file).convert_alpha(),
                          screen,
                          position,
                          speed,
                          player)

    def update(self, time_passed):
        direction = vec2d(self.player.x - self.x, self.player.y - self.y).normalized()

        displacement = vec2d(direction.x * TRACK_RATIO * self.speed * time_passed,
                             self.speed * time_passed)

        self.x += displacement.x
        self.y += displacement.y

        w, h = self.image.get_size()
        self._change_rect(self.x, self.y, w, h)