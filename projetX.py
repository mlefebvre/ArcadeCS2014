import pygame
from pygame.surface import Surface
from player import Player
from obstacles.obstaclemanager import ObstacleManager
from collisionstrategies.collision_strategy_factory import CollisionStrategyFactory

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
GAME_WIDTH = 640
GAME_HEIGHT = 480
FPS = 60
LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT
PLAYER_SPEED = 0.3
MODE = 0  # pygame.FULLSCREEN
MAX_OBSTACLES = 10
OBSTACLE_BASE_SPEED = 0.3
ACCELERATION = 0.0001
DEBUG = True

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Machine:
    background_file = 'images/background.png'
    controls_reversed = False

    def __init__(self):
        self.done = False
        self.clock = pygame.time.Clock()
        self.screen = None
        self.time_passed = 0
        self.player = None
        self.background = None
        self.obstacle_manager = None

    def start(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), MODE)
        self.game_surface = Surface((GAME_WIDTH, GAME_HEIGHT))
        self.player = Player(self.game_surface, (GAME_WIDTH/2, GAME_HEIGHT*0.8), PLAYER_SPEED)
        self.obstacle_manager = ObstacleManager(self.game_surface,
                                                OBSTACLE_BASE_SPEED,
                                                MAX_OBSTACLES,
                                                CollisionStrategyFactory(self, self.player),
                                                self.player)

        while not self.done:
            key = pygame.key.get_pressed()
            left, right = self._get_movement(key)

            if key[pygame.K_ESCAPE]:
                self.done = True
            self._tick(left, right)
            pygame.display.flip()
            self.time_passed = self.clock.tick(FPS)
        pygame.quit()

    def reverse_controls(self, reversed):
        self.controls_reversed = reversed

    def _get_movement(self, key):
        left = key[LEFT_KEY] == 1
        right = key[RIGHT_KEY] == 1

        if self.controls_reversed:
            left = not left
            right = not right

        return left, right

    def _tick(self, left, right):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

        self._draw_background()

        direction = 0
        if not (left and right):
            if left:
                direction = -1
            elif right:
                direction = 1

        self.player.update(self.time_passed, direction)
        self.player.blit()

        self.obstacle_manager.obstacle_speed += ACCELERATION
        self.obstacle_manager.create_obstacle()
        self.obstacle_manager.update(self.time_passed)
        self.obstacle_manager.obstacle_collide(self.player)

        self.screen.blit(self.game_surface, (0,0))

    def _draw_background(self):
        if not self.background:
            self.background = pygame.image.load(self.background_file)
        self.game_surface.blit(self.background, (0, 0))



if __name__ == "__main__":
    machine = Machine()
    machine.start()
