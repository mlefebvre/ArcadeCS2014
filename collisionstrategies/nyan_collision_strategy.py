from collision_strategy import CollisionStrategy


class NyanCollisionStrategy(CollisionStrategy):
    def __init__(self, machine):
        CollisionStrategy.__init__(self, machine)

    def on_collision(self):
        print "Nyan"
