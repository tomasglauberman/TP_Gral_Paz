from car import Car
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class AGP:
    def __init__(self, length, dt):
        self.length = length
        self.cars = []
        self.dt = dt

    def add_car(self, car):
        self.cars.append(car)
        
    def inside_limits(self, car):
        return -self.limits[1] <= car.pos[0] <= self.limits[1]

    def active_cars(self):
        vr = []
        for car in self.cars:
            if car.is_active():
                vr.append(car)
        return vr
    
    def update(self):
        for car in self.active_cars():
            car.interact(self.dt, self.cars)
            car.update_dynamics(self.dt)
    
    def plot(self):    
        fig, ax = plt.subplots()

        def init():
            ax.set_xlim(0, self.length)
            ax.set_ylim(-1000, 1000)
            return []

        def animate(frame):
            ax.clear()
            ax.set_xlim(0, self.length)
            ax.set_ylim(-1000, 1000)
            self.update()  # Assuming this function updates the car positions
            for car in self.cars:
                print(car.pos)
                plt.plot(car.pos[0], car.pos[1], 'ro')
            return []


        ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=10, blit=True)
        plt.axis('scaled')
        plt.show()

