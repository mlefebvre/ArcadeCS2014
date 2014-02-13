from collision_strategy import CollisionStrategy


class BeerCollisionStrategy(CollisionStrategy):
    def __init__(self, machine, player):
        CollisionStrategy.__init__(self, machine, player)

    def on_collision(self):
        self.machine.reverse_controls(True)
