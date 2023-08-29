import numpy as np


class Car:
    def __init__(self, pos, vel=np.array([0.,0.]), acc=np.array([0.,0.]), props={'risk': 0.5, 'max_vel': 5, 'max_acc': 1}):
        # Position
        self.pos = pos
        # Velocity/Acceleration vectors
        self.vel = vel
        self.acc = acc
        # Properties of agent
        self.props = props

    def update(self, dt):
        self.vel += self.acc * dt
        self.pos += self.vel * dt

        # Agregar algun facto de desaceleracion
        self.acc *= 0.95
        self.vel *= 0.95


    def plot(self, ax):
        ax.plot(self.pos[0], self.pos[1], 'ro')