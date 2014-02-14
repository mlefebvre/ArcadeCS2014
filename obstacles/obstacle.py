from pygame.sprite import Sprite
import pygame


class Obstacle(Sprite):
    images = []

    def __init__(self, image, gameboard, position, speed, player):
        Sprite.__init__(self)
        self.x = position[0]
        self.y = position[1]
        self.last_y = self.y
        self.speed = speed
        self.gameboard = gameboard
        self.image = image
        self.player = player
        self.effects = []

        w, h = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, w, h)

    def update(self, time_passed):
        displacement = self.speed * time_passed
        self.y += displacement

        w, h = self.image.get_size()
        self._change_rect(self.x, self.y, w, h)

    def blit(self):
        draw_pos = self.image.get_rect().move(self.x, self.y)
        self.gameboard.blit(self.image, draw_pos)

    def _change_rect(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

    def set_speed(self, speed):
        self.speed = speed

    def kill(self):
        for effect in self.effects:
            effect.kill()

        super(Obstacle, self).kill()



