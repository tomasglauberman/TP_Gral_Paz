from car import Car
from AGP import AGP
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class PathSimulation:
    def __init__(self, n, agp, dt):
        self.cars = [Car(np.array([0, 0], dtype=np.float64)) for i in range(n)]
        self.agp = agp
        self.dt = dt
        self.t = 0

        self.ax, self.fig = plt.subplots()

    def randomize_start(self):
        for car in self.cars:
            # car.pos = np.array([0, 0])
            car.acc = np.random.rand(2) * 4 - 2

    def run(self):
        while len(self.agp.active_cars(self.cars)) > 0:
            for car in self.cars:
                car.update(self.dt)
            self.t += self.dt


    def plot(self):    
        
        fig, ax = plt.subplots()
        def init():
            ax.clear()
            # Set axis limits
            ax.set_xlim(-10, 10)
            ax.set_ylim(-10, 10)
            return []

        def animate(frame):
            ax.clear()
            ax.set_xlim(-10, 10)
            ax.set_ylim(-10, 10)
            
            for car in self.cars:
                car.update(self.dt)
                self.t += self.dt
                ax.add_patch(plt.Rectangle((car.pos[0] - 0.5, car.pos[1] - 0.5), 1, 1, color='blue'))
            
            return []

        ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=100, blit=True)
        plt.show()
