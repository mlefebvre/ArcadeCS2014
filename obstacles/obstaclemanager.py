import random
from beer import Beer
from nyan import Nyan
from pygame.sprite import Sprite, Group, spritecollide


class ObstacleManager:

    obstacle_types = {Beer: 95,
                      Nyan: 5}
    obstacles = []
    counter = 0

    def __init__(self, screen, obstacle_speed, max_obstacles, collision_strategy_factory):
        self.max_obstacles = max_obstacles
        self.screen = screen
        rect = self.screen.get_rect()
        self.width = rect.width
        self.height = rect.height
        self.obstacle_speed = obstacle_speed
        self.obstacle_group = Group()
        self.collision_strategy_factory = collision_strategy_factory

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
                obstacle = self.__select_obstacle_type()(self.screen,
                                (random.randint(0, self.width), -40),
                                self.obstacle_speed * (1 + (random.random()-0.5) * 0.2))

                self.obstacles.append(obstacle)
                self.obstacle_group.add(obstacle)

    def __select_obstacle_type(self):
        total = sum(w for c, w in self.obstacle_types.items())
        r = random.uniform(0, total)
        upto = 0
        for c, w in self.obstacle_types.items():
            if upto + w > r:
                return c
            upto += w

    def obstacle_collide(self, player):
        collisions = spritecollide(player, self.obstacle_group, True)

        for c in collisions:
            self.obstacles.remove(c)
            c.kill()
            self.collision_strategy_factory.get_strategy(type(c)).on_collision()
