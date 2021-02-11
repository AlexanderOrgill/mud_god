import Sprites
from Tile import Tile
from Selection import Selection

class Cursor(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = Sprites.CURSOR
        self.collides = False
        self.selection_1 = Selection(0, 0)
        self.selection_2 = Selection(0, 0)

    def move_left(self):
        self.x -= 16
    def move_right(self):
        self.x += 16
    def move_up(self):
        self.y -= 16
    def move_down(self):
        self.y += 16