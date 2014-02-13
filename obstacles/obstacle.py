from pygame.sprite import Sprite


class Obstacle(Sprite):
    images = []

    def __init__(self, image, screen, position, speed):
        Sprite.__init__(self)
        self.x = position[0]
        self.y = position[1]
        self.speed = speed
        self.screen = screen
        self.image = image

    def update(self, time_passed):
        displacement = self.speed * time_passed
        self.y += displacement

    def blit(self):
        draw_pos = self.image.get_rect().move(self.x, self.y)
        self.screen.blit(self.image, draw_pos)



