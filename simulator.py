from car import Car
from AGP import AGP
import numpy as np


class PathSimulation:
    def __init__(self, n, dt):
        self.agp = AGP(12500, dt)
        for i in range(n):
            car = Car(props={'pref-speed': np.random.normal(90, 20, 1)[0]})
            self.agp.add_car(car)
        self.t = 0

    def randomize_start(self):
        for car in self.agp.cars:
            car.set_prefspeed(np.random.normal(90, 10, 1)[0])

    def run(self):
        while len(self.agp.active_cars(self.cars)) > 0:
            self.agp.update(self.dt)
            self.t += self.dt

    def plot(self):
        self.agp.plot()
