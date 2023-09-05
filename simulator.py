import pygame, sys
from pygame.locals import *
import numpy as np
import pandas as pd
from agp import AGP
from car import Car

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

FPS = 60
clock = pygame.time.Clock()

class PathSimulation:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        self.start = pygame.time.get_ticks()
        self.spawn_timer = 0

        # Setting up the main display
        self.DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.DISPLAYSURF.fill(BLACK)
        pygame.display.set_caption("Traffic simulation")

        # Create cars group. Groups are useful to 
        # update and draw all sprites at once as well as
        # check for collisions
        self.cars = pygame.sprite.Group()

        # Create AGP
        self.agp = AGP(1250, 0.1)


        self.font = pygame.font.Font(None, 36)


    # Game loop: runs until quit event (X button)
    def run(self):
        while True:
            # Set background color
            self.DISPLAYSURF.fill(BLACK)

            # Draw and update AGP
            self.agp.draw(self.DISPLAYSURF)

            # Draw and update cars
            for car in self.cars:
                car.update(self.agp, self.cars)
                car.draw(self.DISPLAYSURF)

            # Generate cars
            current_time = (pygame.time.get_ticks() - self.start)/1000
            if self.spawn_timer <= current_time:
                self.cars.add(Car())
                self.spawn_timer += self.poisson_process()


            # Render and display lambda value
            text_surface = self.font.render(f"Lambda: {self.lambda_poisson():.2f}", True, (255, 255, 255))
            self.DISPLAYSURF.blit(text_surface, (50, 80))


            # Quit event 
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Update display
            pygame.display.update()
            clock.tick(FPS)


    # Poisson process that models the cars arriving at the AGP
    def poisson_process(self):
        # Tasa de llegada de autos (λ)
        lambda_ = self.lambda_poisson()

        # Generar una lista de tiempos en los que llegan los autos
        tiempos_llegada = np.random.exponential(1 / lambda_)

        return tiempos_llegada

    # Calculate lambda for Poisson process based on car freq
    # obtained from the dataset. The lambda is the average
    # number of cars arriving per second
    def lambda_poisson(self) -> float:
        # Load dataset
        df = pd.read_csv('./data/distribution.csv')
        current_time = (pygame.time.get_ticks() - self.start)/1000
        hora = int(current_time/3) + 6
        return (df['CANTIDAD'][hora] / 3600) 
        