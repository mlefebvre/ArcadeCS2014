from beer_collision_strategy import BeerCollisionStrategy
from nyan_collision_strategy import NyanCollisionStrategy
from healthpack_collision_strategy import HealthPackCollisionStrategy

from obstacles.beer import Beer
from obstacles.nyan import Nyan
from obstacles.healthpack import HealthPack

class CollisionStrategyFactory:
    strategies = {}

    def __init__(self, machine):
        self.machine = machine
        self.strategies[Beer] = BeerCollisionStrategy(machine)
        self.strategies[Nyan] = NyanCollisionStrategy(machine)
        self.strategies[HealthPack] = HealthPackCollisionStrategy(machine)

    def get_strategy(self, object):
        t = type(object)
        if t in self.strategies:
            return self.strategies[t]