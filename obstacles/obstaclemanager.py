from random import randint
from obstacle import Obstacle
from beer import Beer


class ObstacleManager:
    obstacles = []

    def __init__(self, screen, max_obstacles):
        self.max_obstacles = max_obstacles
        self.screen = screen
        self.width = self.screen.get_rect().width

    def update(self, time_passed):
        for obstacle in self.obstacles:
            obstacle.update(time_passed)
            obstacle.blit()

    def create_obstacle(self, speed):
        obstacle = Beer(self.screen, (randint(0, self.width), -30), speed)

        self.obstacles.append(obstacle)
        return obstacle