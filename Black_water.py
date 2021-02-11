import Sprites
from Tile import Tile

class Black_water(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = Sprites.BLACK_WATER