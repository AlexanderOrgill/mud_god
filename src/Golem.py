from random import randint
import Sprites
from Tile import Tile

class Golem(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = Sprites.GOLEM
        self.collides = True
        self.hydration = "high"

    def move_left(self):
        self.x -= 16
    def move_right(self):
        self.x += 16
    def move_up(self):
        self.y -= 16
    def move_down(self):
        self.y += 16