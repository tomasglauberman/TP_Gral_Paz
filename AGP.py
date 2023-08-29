from car import Car
import numpy as np

class AGP:
    def __init__(self, length):
        self.limits = np.array([0, length])
        
    def inside_limits(self, car):
        return -self.limits[1] <= car.pos[0] <= self.limits[1]

    def active_cars(self, cars):
        vr = []
        for car in cars:
            if self.inside_limits(car):
                vr.append(car)
        return vr
