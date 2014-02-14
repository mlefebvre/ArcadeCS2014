from collision_strategy import CollisionStrategy


class VodkaCollisionStrategy(CollisionStrategy):
    def __init__(self, machine):
        CollisionStrategy.__init__(self, machine)

    def on_collision(self):
        self.machine.gameboard.rotate(5)
