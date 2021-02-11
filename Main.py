import Sprites
import pygame
import time
from World import World

# setup frame
pygame.init()
WIDTH = 900
HEIGHT = 480
FONT = pygame.font.Font("font.ttf", 16)
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Mud God")
pygame.display.set_icon(Sprites.GOLEM)

class Main:
    def __init__(self):
        self.world = World()
        self.setup_world()
        self.play()   

    def setup_world(self):
        self.world.turf()
        self.world.flood()
        self.world.vegetate()
        self.world.animate()
        self.world.populate()
        self.world.place_cursor()

    def draw_grids(self):
        for list in self.world.grid:
            for element in list:
                DISPLAY.blit(element.image, (element.x, element.y))
        for list in self.world.over_grid:
            for element in list:
                if (element != '0'):
                    DISPLAY.blit(element.image, (element.x, element.y))
        for list in self.world.cursor_grid:
            for element in list:
                if (element != '0'):
                    DISPLAY.blit(element.image, (element.x, element.y))

    def draw_control_panel(self):
        DISPLAY.blit(self.world.control_panel, (720, 0))
                
    def play(self):
        game_end = False
        paused = False
        while not game_end:
            for event in pygame.event.get():#closing function
                if event.type == pygame.QUIT:
                    game_end = True

                elif event.type == pygame.KEYDOWN:#arrow key events
                    if event.key == pygame.K_LEFT:
                        self.world.cursor.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.world.cursor.move_right()
                    elif event.key == pygame.K_UP:
                        self.world.cursor.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.world.cursor.move_down()
                    elif event.key == pygame.K_SPACE:
                        paused = not paused
                               

            self.world.update_cursor()

            if not paused:
                self.world.compute_agents()
                self.world.update_agents()
                
            self.draw_grids()
            self.draw_control_panel()

            if paused:
                DISPLAY.blit(FONT.render("--PAUSED--", True, (255,0,0)), (0, 10))

            
            pygame.display.update()
            CLOCK.tick(60) 
        self.setdown()

    def setdown(self):
        pygame.quit()
        exit()
   
############

main = Main()
quit()