import numpy as np
import pygame
from pygame.locals import *

class Car(pygame.sprite.Sprite):
    def __init__(self, 
                 pos=np.array([-10, 420.]), 
                 vel=np.array([0.,0.]), 
                 acc=np.array([0.,0.]), 
                 pref_speed=80,
                 mistake_p=0.1,
                 reaction_time=0.2):
        
        # Initialize sprite class
        super().__init__() 

        pos = pos + (0 if np.random.uniform() > 0.5 else 30)
        # Load image, scale and rotate
        self.image = pygame.image.load("./images/car.png")
        self.image = pygame.transform.scale(self.image, (22.2, 40))
        self.image = pygame.transform.rotate(self.image, 90)

        # Position is given by the center of the image
        self.rect = self.image.get_rect()
        self.rect.center = pos

        # Velocity/Acceleration vectors
        self.vel = vel
        self.acc = acc        

        # Properties of agent
        self.pref_speed = np.random.normal(2, 0.5)
        self.mistake_p = mistake_p
        self.reaction_time = reaction_time
        self.active = True

        self.font = pygame.font.Font(None, 15)

    def draw(self, surface):
        surface.blit(self.image, self.rect)  
        speed_text = self.font.render(f"{self.pref_speed:.2f}, {self.vel[0]:.5f}", True, (255, 255, 255))
        surface.blit(speed_text, self.rect.center)

    def update_state(self, agp, cars):

        # Update position and velocity
        if self.active:
            self.rule_1()
            self.vel += self.acc
            self.rect.move_ip(self.vel[0], 0)

        # Check if car collided
        self.collision(cars)

        # Check if arrived at destination
        # If so, save stats and remove from simulation
        if self.rect.left > 1200:
            self.save_stats()
            self.active = False
            self.kill()

    def save_stats(self):
        print("Saving stats...")
        pass

    def collision(self, cars):
        # To be run if collision occurs between 2 cars
        # Create a temporary copy of the group without the current car
        temp_group = cars.copy()
        temp_group.remove(self)
        if pygame.sprite.spritecollideany(self, temp_group):
            return True
    
        return False

    def is_active(self):
        return self.active

    def get_pos(self):
        return self.pos
    
    def get_vel(self):
        return self.vel
    
    def set_pref_speed(self, speed):
        self.pref_speed = speed
    
    def rule_1(self):   
        # Try to reach preferred speed
        self.acc = (self.acc_rate() * (self.pref_speed - self.vel))
    
    def acc_rate(self):
        # if self.vel[0] > 120 or self.vel[0] < 5:
        #     return 0.05
        # return -9.75e-5 * (self.vel[0]**2) + 0.0117 * self.vel[0] - 0.05
        return 0.05