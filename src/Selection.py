from random import randint
import Sprites
from Tile import Tile

class Selection(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = Sprites.SELECTION
        self.isActive = False