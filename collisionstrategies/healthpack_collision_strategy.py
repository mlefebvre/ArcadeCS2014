from collision_strategy import CollisionStrategy


class HealthPackCollisionStrategy(CollisionStrategy):
    def __init__(self, machine):
        CollisionStrategy.__init__(self, machine)

    def on_collision(self):
        self.machine.reverse_controls(False)
