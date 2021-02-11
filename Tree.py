import Sprites
from Tile import Tile

class Tree(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = Sprites.TREE
        self.collides = True