import os
import pygame
from pygame.sprite import Sprite

COLLISION_PADDING = 0.3   # %
EFFECTS_DURATION = 10000  # ms


class Player(Sprite):
    image_directory = 'images/player/'
    images = {-1: [], 1: []}
    effects = []
    orientation = 1
    counter = 0
    still_counter = 0
    image_id = 0
    direction = 1

    def __init__(self, gameboard, position, speed):
        Sprite.__init__(self)
        self.x = position[0]
        self.y = position[1]
        self.speed = speed
        self.gameboard = gameboard
        self._load_images()
        w, h = self.images[self.orientation][self.image_id].get_size()
        self._change_rect(self.x, self.y, w, h)

    def update(self, time_passed):

        if self.direction != 0:
            self.still_counter = 0
            self.counter += 1
            if self.counter % 5 == 0:
                self.image_id = (self.image_id + 1) % len(self.images[self.orientation])
        else:
            self.still_counter += 1
            if self.still_counter > 5:
                self.image_id = 0

        if self.orientation != self.direction and self.direction != 0:
            self.orientation = -self.orientation

        displacement = self.direction * self.speed * time_passed

        new_x = self.x + displacement
        w, h = self.images[self.orientation][self.image_id].get_size()

        if new_x > 0 and new_x + w < self.gameboard.width:
            self.x = new_x
            self._change_rect(self.x, self.y, w, h)

        for effect in self.effects:
            if effect.start_time + EFFECTS_DURATION < pygame.time.get_ticks():
                effect.kill()
                self.effects.remove(effect)
            else:
                effect.blit()

    def set_speed(self, speed):
        self.speed = speed

    def increment_speed(self):
        self.speed *= 1.1

    def blit(self):
        draw_pos = self.images[self.orientation][self.image_id].get_rect().move(self.x, self.y)
        self.gameboard.blit(self.images[self.orientation][self.image_id], draw_pos)

    def _load_images(self):
        for f in sorted(os.listdir(self.image_directory)):
            if f.endswith(".png"):
                self.images[1].append(pygame.image.load(self.image_directory + f).convert_alpha())
                self.images[-1].append(pygame.transform.flip(self.images[1][-1], True, False))

    def _change_rect(self, x, y, w, h):
        self.rect = pygame.Rect(x + w * COLLISION_PADDING,
                                y + h * COLLISION_PADDING,
                                w - 2 * w * COLLISION_PADDING,
                                h - 2 * h * COLLISION_PADDING)



