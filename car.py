import numpy as np
import pygame
from pygame.locals import *
import time

class Car(pygame.sprite.Sprite):
    def __init__(self,
                 id, 
                 pos=np.array([-1, 420.]), 
                 vel=5, 
                 acc=0,
                 max_speed = 8, 
                 mistake_p=0.1,
                 reaction_time=0.2,
                 ):
        
        # Initialize sprite class
        super().__init__() 
        self.start = time.time()
        self.total_time = 0

        #pos = pos + (0 if np.random.uniform() > 0.5 else 30)
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
        self.pref_speed = np.random.normal(6,  1)
        self.mistake_p = mistake_p
        self.reaction_time = reaction_time
        self.active = True

        self.font = pygame.font.Font(None, 15)
        self.id = id
        self.crash_time = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)  
        speed_text = self.font.render(f"ID:{self.id}, {self.pref_speed:.2f}, {self.vel:.2f}", True, (0, 0, 0))
        surface.blit(speed_text, (self.rect.center[0], self.rect.center[1]+15))

    def update_state(self, agp, cars, dt):

        # Update position and velocity
        if self.active:
            self.rule_1(cars, dt)
            self.vel += self.acc * dt
            self.rect.move_ip(self.vel, 0)

        # # Check if car collided
        # if self.collision(cars):
        #     print("collision!")
        #     inicio = time.time()
        #     self.vel = 0
        #     self.acc = 0
        #     while(time.time()-inicio<3):
        #         print("espero")
        #     self.vel = 6
        #     self.acc = 1
        


        # Check if arrived at destination
        # If so, save stats and remove from simulation
        if self.rect.left > 1400:
            self.save_stats()
            self.active = False
            self.total_time = time.time() - self.start
            self.pos = 10000000
            self.vel = 1000000

    def save_stats(self):
        print("Saving stats...")
        pass

    def collision(self, cars):
        # To be run if collision occurs between 2 cars
        # Create a temporary copy of the group without the current car
        id_prev = self.id + 1
        id_next = self.id - 1
        collision = False
        if not id_next < 0:
            collision = collision or pygame.sprite.collide_rect(self, cars[id_next])
        if not id_prev >= len(cars):
             collision = collision or pygame.sprite.collide_rect(self, cars[id_next])
        return collision

    def is_active(self):
        return self.active

    def get_pos(self):
        return self.rect.center[0]
    
    def get_vel(self):
        return self.vel
    
    def set_pref_speed(self, speed):
        self.pref_speed = speed
    
    def rule_1(self, cars, dt):   
        # Try to reach preferred speed
        if self.id > 0:
            id_next = self.id - 1
            vel_next = cars[id_next].get_vel()  # no se la velocidad exacta
            pos_next = cars[id_next].rect.left 
            if vel_next <= self.get_vel():
                self.acc = (vel_next-self.vel)*(1/(pos_next - self.rect.right+0.1)) * dt
            else:
                  self.acc = (self.acc_rate() * (self.pref_speed - self.vel)) * dt
            #(self.acc_rate() * (self.pref_speed - self.vel))
        else:
            self.acc = (self.acc_rate() * (self.pref_speed - self.vel)) * dt

    
    def acc_rate(self):
        # if self.vel[0] > 120 or self.vel[0] < 5:
        #     return 0.05
        # return -9.75e-5 * (self.vel[0]**2) + 0.0117 * self.vel[0] - 0.05
        return 0.05
    

        
