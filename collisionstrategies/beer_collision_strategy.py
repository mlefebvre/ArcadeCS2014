from collision_strategy import CollisionStrategy


class BeerCollisionStrategy(CollisionStrategy):
    def __init__(self, machine):
        CollisionStrategy.__init__(self, machine)

    def on_collision(self):
        print "Beer"
        self.machine.player.speed += 0.05
