from random import randint
import Sprites
from Tile import Tile

class Animal(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.collides = True

    def wander(self):
        if (randint(0, 40) == 0):
            direction = randint(0, 8)
            if (direction < 3 and self.y > 0):
                self.y -= 16
            elif (direction >= 6 and self.y < 464):
                self.y += 16
            if (direction % 3 == 0 and self.x > 0):
                self.x -= 16
            elif (direction % 3 == 2 and self.x < 704):
                self.x += 16