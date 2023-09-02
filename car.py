import numpy as np

class Car:
    def __init__(self, 
                 pos=np.array([0.,0.]), 
                 vel=np.array([0.,0.]), 
                 acc=np.array([0.,0.]), 
                 props={'pref-speed': np.random.normal(90, 10, 1)[0], 'mistake-p': 0.1, 'reaction-time': 0.2}):
        # Position
        self.pos = pos
        # Velocity/Acceleration vectors
        self.vel = vel
        self.acc = acc        
        # Reaction time
        self.active = True
        # Properties of agent
        self.props = props

    def is_active(self):
        return self.active

    def get_pos(self):
        return self.pos
    
    def get_vel(self):
        return self.vel
    
    def set_prefspeed(self, speed):
        self.props['pref-speed'] = speed

    def update_dynamics(self, dt):
        if self.active:
            # self.vel += self.acc * dt + (np.random.normal(0, 0.1, 1)*self.vel)
            self.vel += self.acc * dt
            self.pos[0] += self.vel[0] * dt

        if self.pos[0] > 12000:
            self.active = False

    def acc_rate(self):
        if self.vel[0] > 120 or self.vel[0] < 5:
            return 0.05
        return -9.75e-5 * (self.vel[0]**2) + 0.0117 * self.vel[0] - 0.05
    
    def interact(self, dt, cars):
        # Try to reach preferred speed
        self.acc = self.acc_rate() * (self.props['pref-speed'] - self.vel)