from collision_strategy import CollisionStrategy


class NyanCollisionStrategy(CollisionStrategy):
    def __init__(self, machine, player):
        CollisionStrategy.__init__(self, machine, player)

    def on_collision(self):
        print "Nyan"
