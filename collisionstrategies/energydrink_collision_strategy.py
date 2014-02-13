from collision_strategy import CollisionStrategy


class EnergyDrinkCollisionStrategy(CollisionStrategy):
    def __init__(self, machine):
        CollisionStrategy.__init__(self, machine)

    def on_collision(self):
        self.machine.player.speed *= 1.1
