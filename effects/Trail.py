import pygame
from effects.Effect import Effect

TRAIL_SIZE = 50


class Trail(Effect):
    trails = []

    def __init__(self, entity, image, screen):
        Effect.__init__(self,
                        entity,
                        pygame.image.load(image).convert_alpha(),
                        screen)

    def blit(self):
        if len(self.trails) == TRAIL_SIZE:
            self.trails.pop(0)

        self.trails.append([self.image, self.entity.x, self.entity.y + 10])

        for trail in self.trails:
            draw_pos = self.image.get_rect().move(trail[1], trail[2])
            # Ca ne marche pas?
            #part.image.set_alpha(part.image.get_alpha() - part.fade_speed)
            self.screen.blit(trail[0], draw_pos)