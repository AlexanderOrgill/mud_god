import Sprites
from Tile import Tile

class Snow_tree(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = Sprites.SNOW_TREE
        self.collides = True