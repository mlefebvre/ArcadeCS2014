import pygame
from effects.Effect import Effect

TRAIL_SIZE = 50


class VerticalTrail(Effect):
    def __init__(self, entity, image, screen):
        Effect.__init__(self,
                        entity,
                        pygame.image.load(image).convert_alpha(),
                        screen)
        self.trails = []

    def blit(self):
        if len(self.trails) == TRAIL_SIZE:
            self.trails.pop(0)

        self.trails.append([self.image, self.entity.x, self.entity.y + 10])

        for trail in self.trails:
            draw_pos = self.image.get_rect().move(trail[1], trail[2])
            self.screen.blit(trail[0], draw_pos)

    def kill(self):
        self.trails = []

        super(VerticalTrail, self).kill()