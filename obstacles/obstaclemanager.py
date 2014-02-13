from random import randint, random
from beer import Beer


class ObstacleManager:
    obstacles = []

    counter = 0

    def __init__(self, screen, obstacle_speed, max_obstacles):
        self.max_obstacles = max_obstacles
        self.screen = screen
        rect = self.screen.get_rect()
        self.width = rect.width
        self.height = rect.height
        self.obstacle_speed = obstacle_speed

    def update(self, time_passed):
        delete_list = []

        for obstacle in self.obstacles:
            if obstacle.y > self.height:
                delete_list.append(obstacle)
            else:
                obstacle.update(time_passed)
                obstacle.blit()

        for obstacle in delete_list:
            self.obstacles.remove(obstacle)
            obstacle.kill()

    def create_obstacle(self):
        if len(self.obstacles) <= self.max_obstacles:
            self.counter += 1
            if self.counter % 10 == 0:
                obstacle = Beer(self.screen,
                                (randint(0, self.width), -40),
                                self.obstacle_speed * (1 + (random()-0.5) * 0.2))

                self.obstacles.append(obstacle)