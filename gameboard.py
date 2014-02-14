from hgext import children
import pygame
from pygame.surface import Surface


class GameBoard(Surface):
    background_file = 'images/background.png'

    def __init__(self, size):
        Surface.__init__(self, size)
        self.children = []
        self.background = None
        self.width, self.height = size

    def add_child(self, child):
        self.children.append(child)

    def update(self, time_passed):
        self._draw_background()

        for child in self.children:
            child.update(time_passed)
            child.blit()

    def _draw_background(self):
        if not self.background:
            self.background = pygame.image.load(self.background_file)
        self.blit(self.background, (0, 0))