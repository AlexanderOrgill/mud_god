import Sprites
from Tile import Tile

class Arid_grass(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = Sprites.ARID_GRASS