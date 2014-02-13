from beer_collision_strategy import BeerCollisionStrategy
from nyan_collision_strategy import NyanCollisionStrategy

from obstacles.beer import Beer
from obstacles.nyan import Nyan

class CollisionStrategyFactory:
    strategies = {}

    def __init__(self, machine):
        self.machine = machine
        self.strategies[Beer] = BeerCollisionStrategy(machine)
        self.strategies[Nyan] = NyanCollisionStrategy(machine)

    def get_strategy(self, classtype):
        return self.strategies[classtype]