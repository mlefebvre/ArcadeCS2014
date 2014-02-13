from pygame.sprite import Sprite
import pygame


class Obstacle(Sprite):
    images = []
    effects = []

    def __init__(self, image, screen, position, speed, player):
        Sprite.__init__(self)
        self.x = position[0]
        self.y = position[1]
        self.last_y = self.y
        self.speed = speed
        self.screen = screen
        self.image = image
        self.player = player

        w, h = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, w, h)

    def update(self, time_passed):
        displacement = self.speed * time_passed
        self.y += displacement

        w, h = self.image.get_size()
        self._change_rect(self.x, self.y, w, h)

    def blit(self):
        draw_pos = self.image.get_rect().move(self.x, self.y)
        self.screen.blit(self.image, draw_pos)
        #pygame.draw.rect(self.screen, (255, 0, 0), self.rect, 1)

    def _change_rect(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)

    def kill(self):
        for effect in self.effects:
            effect.kill()

        super(Obstacle, self).kill()



