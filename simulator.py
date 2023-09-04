from agp import AGP
from car import Car

import pygame
from pygame.locals import *
import sys

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

FPS = 60
FramePerSec = pygame.time.Clock()

class PathSimulation:
    def __init__(self, n):
        # Initialize pygame
        pygame.init()
        # Setting up the main display
        self.DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.DISPLAYSURF.fill(BLACK)
        pygame.display.set_caption("Traffic simulation")

        # Create cars
        self.cars = pygame.sprite.Group()
        for i in range(n):
            car = Car()
            self.cars.add(car)

        # Create AGP
        self.agp = AGP(1250, 0.1)

    def run(self):
        # Game loop: runs until quit event (X button)
        while True:
            # Quit event 
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        
            # Set background color
            self.DISPLAYSURF.fill(BLACK)

            # Draw and update AGP
            self.agp.draw(self.DISPLAYSURF)

            # Draw and update cars
            for car in self.cars:
                car.update(self.agp, self.cars)
                car.draw(self.DISPLAYSURF)

            # Update display
            pygame.display.update()
            FramePerSec.tick(FPS)