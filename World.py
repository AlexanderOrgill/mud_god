import pygame
from Cursor import Cursor
from Sprites import CURSOR
from random import randint

from Golem import Golem
from Grass import Grass
from Arid_grass import Arid_grass
from Snow_grass import Snow_grass
from Tree import Tree
from Arid_tree import Arid_tree
from Snow_tree import Snow_tree
from Black_water import Black_water
from Bear import Bear

class World:
    def __init__(self):
        self.climate = "temperate"
        self.current_weather = "clear"
        self.grid = [['0' for x in range(0, 45)] for y in range(0, 30)]
        self.over_grid = [['0' for x in range(0, 45)] for y in range(0, 30)]
        self.cursor_grid = [['0' for x in range(0, 45)] for y in range(0, 30)]
        self.cursor = Cursor(352, 240)
        self.control_panel = pygame.Surface((720, 0))
        self.view_x = 0
        self.view_y = 0

        climate_number = randint(0, 2)
        if (climate_number == 0):
            self.climate = "temperate"
        elif (climate_number == 1):
            self.climate = "hot"
        else:
            self.climate = "cold"

        self.control_panel.fill((0, 100, 0))

    def turf(self):
        if (self.climate == "temperate"):
            for i in range(0, 30):
                for j in range(0, 45):
                    self.grid[i][j] = Grass(j*16, i*16)
        elif (self.climate == "hot"):
            for i in range(0, 30):
                for j in range(0, 45):
                    self.grid[i][j] = Arid_grass(j*16, i*16)
        else:
            for i in range(0, 30):
                for j in range(0, 45):
                    self.grid[i][j] = Snow_grass(j*16, i*16)
    
    def vegetate(self):
        if (self.climate == "temperate"):
            for i in range(0, 30):
                for j in range(0, 45):
                    if (randint(0, 10) == 0):
                        self.over_grid[i][j] = Tree(j*16, i*16)
        elif (self.climate == "hot"):
            for i in range(0, 30):
                for j in range(0, 45):
                    if (randint(0, 20) == 0):
                        self.over_grid[i][j] = Arid_tree(j*16, i*16)
        else:
            for i in range(0, 30):
                for j in range(0, 45):
                    if (randint(0, 8) == 0):
                        self.over_grid[i][j] = Snow_tree(j*16, i*16)
    
    def animate(self):
        for i in range(0, 30):
            for j in range(0, 45):
                if (randint(0, 1000) == 0):
                    self.over_grid[i][j] = Bear(j*16, i*16)

    def flood(self):
        for i in range(0, 30):
            for j in range(0, 45):
                if (randint(0, 100) == 0):
                    self.grid[i][j] = Black_water(j*16, i*16)

    def populate(self):
        rand_x = randint(0, 45)
        rand_y = randint(0, 30)
        self.over_grid[rand_y][rand_x] = Golem(rand_x*16, rand_y*16)

    def place_cursor(self):
        self.cursor_grid[15][22] = self.cursor

    def compute_agents(self):
        for i in range(0, 30):
            for j in range(0, 45):
                agent = self.over_grid[i][j]
                if (agent != '0'):
                    if (isinstance(agent, Bear)):
                        agent.wander()

    def update_agents(self):
        for i in range(0, 30):
            for j in range(0, 45):
                agent = self.over_grid[i][j]
                if (agent != '0'):
                    if (i != agent.y//16 or j != agent.x//16): #if needs update
                        self.over_grid[agent.y//16][agent.x//16] = agent #new location
                        self.over_grid[i][j] = '0' #remove old reference
    
    def update_cursor(self):
        for i in range(0, 30):
            for j in range(0, 45):
                cursor = self.cursor_grid[i][j]
                if (cursor != '0'):
                    if (i != cursor.y//16 or j != cursor.x//16): #if needs update
                        self.cursor_grid[cursor.y//16][cursor.x//16] = cursor #new location
                        self.cursor_grid[i][j] = '0' #remove old reference
