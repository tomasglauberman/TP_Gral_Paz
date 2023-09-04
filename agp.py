from car import Car
import numpy as np
import pygame
from pygame.locals import *


class AGP(pygame.sprite.Sprite):
    def __init__(self, length, dt):
        super().__init__() 
        self.length = length

        road_width = 150
        self.rect = pygame.Rect(0, 400-(road_width/2), length, road_width)
        self.line = pygame.Rect(0, 400-2, length, 4)
        
    def inside_limits(self, car):
        return -self.limits[1] <= car.pos[0] <= self.limits[1]

    def active_cars(self):
        vr = []
        for car in self.cars:
            if car.is_active():
                vr.append(car)
        return vr
    
    def draw(self, surface):
        pygame.draw.rect(surface, (50, 50, 50), self.rect)
        pygame.draw.rect(surface, (255, 255, 255), self.line)
    
