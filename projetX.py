import pygame
from pygame.surface import Surface
from player import Player
from obstacles.obstaclemanager import ObstacleManager
from collisionstrategies.collision_strategy_factory import CollisionStrategyFactory
from gameboard import GameBoard

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
GAME_SIZE = 640
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
    controls_reversed = False

    def __init__(self):
        self.done = False
        self.clock = pygame.time.Clock()
        self.screen = None
        self.time_passed = 0
        self.player = None
        self.obstacle_manager = None

    def start(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), MODE)
        self.gameboard = GameBoard((GAME_SIZE, GAME_SIZE))
        self.player = Player(self.gameboard, (GAME_SIZE/2, GAME_SIZE*0.8), PLAYER_SPEED)
        self.obstacle_manager = ObstacleManager(self.gameboard,
                                                OBSTACLE_BASE_SPEED,
                                                MAX_OBSTACLES,
                                                CollisionStrategyFactory(self),
                                                self.player)
        self.gameboard.add_child(self.player)
        self.gameboard.add_child(self.obstacle_manager)

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

        direction = 0
        if not (left and right):
            if left:
                direction = -1
            elif right:
                direction = 1

        self.player.direction = direction
        self.obstacle_manager.accelerate_obstacles(ACCELERATION)
        self.obstacle_manager.create_obstacle()
        self.obstacle_manager.obstacle_collide(self.player)

        self.gameboard.update(self.time_passed)
        self.screen.blit(self.gameboard.render(), (0, 0))

if __name__ == "__main__":
    machine = Machine()
    machine.start()
