import numpy as np
import pygame
from pygame.locals import *

class Car(pygame.sprite.Sprite):
    def __init__(self, 
                 pos=np.array([-50, 420.]), 
                 vel=np.array([1.,0.]), 
                 acc=np.array([0.,0.]), 
                 props={'pref-speed': np.random.normal(90, 10, 1)[0], 'mistake-p': 0.1, 'reaction-time': 0.2}):
        super().__init__() 

        pos = pos + (0 if np.random.uniform() > 0.5 else 30)
        # Load image, scale and rotate
        self.image = pygame.image.load("./images/car.png")
        self.image = pygame.transform.scale(self.image, (22.2, 40))
        self.image = pygame.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect()
        self.rect.center = pos

        # # Position
        # self.pos = pos
        # Velocity/Acceleration vectors
        self.vel = vel
        self.acc = acc        
        # # Reaction time
        self.active = True
        # Properties of agent
        self.props = props

    def draw(self, surface):
        surface.blit(self.image, self.rect)  

    def update(self, agp, cars):
        # Update position and velocity
        if self.active:
            self.rect.move_ip(self.vel[0], self.vel[1])
            self.vel += self.acc

        # Check if car collided
        self.collision(cars)

        # Check if arrived at destination
        # If so, save stats and remove from simulation
        if self.rect.left > 1100:
            self.save_stats()
            self.active = False
            self.kill()

    def save_stats(self):
        pass

    def collision(self, cars):
        # To be run if collision occurs between 2 cars
        # Create a temporary copy of the group without the current car
        temp_group = cars.copy()
        temp_group.remove(self)
        if pygame.sprite.spritecollideany(self, temp_group):
            print("Collision!")

    def is_active(self):
        return self.active

    def get_pos(self):
        return self.pos
    
    def get_vel(self):
        return self.vel
    
    def set_pref_speed(self, speed):
        self.props['pref-speed'] = speed
    
    def acc_rate(self):
        if self.vel[0] > 120 or self.vel[0] < 5:
            return 0.05
        return -9.75e-5 * (self.vel[0]**2) + 0.0117 * self.vel[0] - 0.05
    
    def interact(self, dt, cars):
        # Try to reach preferred speed
        self.acc = self.acc_rate() * (self.props['pref-speed'] - self.vel)