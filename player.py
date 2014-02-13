import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    image_files = ['images/player/1.png']
    images = []

    def __init__(self, screen, position, speed):
        Sprite.__init__(self)
        self.x = position[0]
        self.y = position[1]
        self.speed = speed
        self.screen = screen
        self._load_images()
        self.image_id = 0

        w, h = self.images[self.image_id].get_size()
        self.rect = pygame.Rect(self.x, self.y, w, h)

    def update(self, time_passed, direction):
        displacement = direction * self.speed * time_passed

        bounds = self.screen.get_rect()
        new_x = self.x + displacement
        w, h = self.images[self.image_id].get_size()

        if new_x > bounds.left and new_x + w < bounds.right:
            self.x = new_x
            self.rect = pygame.Rect(self.x, self.y, w, h)

    def blit(self):
        draw_pos = self.images[self.image_id].get_rect().move(self.x, self.y)
        self.screen.blit(self.images[self.image_id], draw_pos)

    def _load_images(self):
        for f in self.image_files:
            self.images.append(pygame.image.load(f).convert_alpha())


