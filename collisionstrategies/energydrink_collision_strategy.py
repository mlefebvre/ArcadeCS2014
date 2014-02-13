from collision_strategy import CollisionStrategy


class EnergyDrinkCollisionStrategy(CollisionStrategy):
    def __init__(self, machine, player):
        CollisionStrategy.__init__(self, machine, player)

    def on_collision(self):
        self.machine.player.speed *= 1.1
