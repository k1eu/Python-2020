from math import sin, cos

from level1.zadanie.klasy_drone import Drone, Environment


class TrueCircularDrone(Drone):

    def __init__(self):
        self.position = [1, 0, 0]
        self.velocity = [0, 1, 0]

    def step(self, t, dt):
        self.position = [cos(t), sin(t), 0]
        self.velocity = [-sin(t), cos(t), 0]


class TrueParabolicDrone(Drone):

    def __init__(self):
        self.position = [0, 0, 0]
        self.velocity = [0, 1, 0]

    def step(self, t, dt):
        self.position = [t, t ** 2, 0]
        self.velocity = [1, 2 * t, 0]


class SimulatedDrone(Drone):
    true_drone: Drone  # próbujemy odczytać parametry (pozycja, prędkość) z tego drona i symulować gdzie obecnie jesteśmy

    def __init__(self, true_drone: Drone):
        self.position = true_drone.position
        self.velocity = true_drone.velocity
        self.true_drone = true_drone

    def step(self, t, dt):
        current_velocity = self.true_drone.velocity
        new_position = [pos + dt * vel for (pos, vel) in zip(self.position, current_velocity)]

        self.position = new_position
        self.velocity = current_velocity


td = TrueCircularDrone()
sd = SimulatedDrone(td)

pd = TrueParabolicDrone()
sd2 = SimulatedDrone(pd)

env = Environment()
env.add_object(td)
env.add_object(sd)
env.add_object(pd)
env.add_object(sd2)


env.simulate(0, 2 * 2 * 3.14159265358, 0.001)
