from beer_collision_strategy import BeerCollisionStrategy
from nyan_collision_strategy import NyanCollisionStrategy
from healthpack_collision_strategy import HealthPackCollisionStrategy
from energydrink_collision_strategy import EnergyDrinkCollisionStrategy
from collision_strategy import CollisionStrategy

from obstacles.beer import Beer
from obstacles.nyan import Nyan
from obstacles.healthpack import HealthPack
from obstacles.energydrink import EnergyDrink


class CollisionStrategyFactory:
    strategies = {}

    def __init__(self, machine):
        self.machine = machine
        self.strategies[Beer] = BeerCollisionStrategy(machine)
        self.strategies[Nyan] = NyanCollisionStrategy(machine)
        self.strategies[HealthPack] = HealthPackCollisionStrategy(machine)
        self.strategies[EnergyDrink] = EnergyDrinkCollisionStrategy(machine)
        self.no_collision_strategy = CollisionStrategy(machine)

    def get_strategy(self, object):
        t = type(object)
        if t in self.strategies:
            return self.strategies[t]
        else:
            return self.no_collision_strategy