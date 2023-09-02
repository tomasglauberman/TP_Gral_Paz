from simulator import PathSimulation
from AGP import AGP
import numpy as np
import matplotlib.pyplot as plt

simulation = PathSimulation(2, 0.1)
# simulation.randomize_start()
simulation.plot()

for car in simulation.agp.cars:
    print(car.props['pref-speed'])