from random import randint
import Sprites
from Animal import Animal

class Bear(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = Sprites.BEAR
