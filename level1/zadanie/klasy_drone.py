from math import sqrt
from typing import List


class PhysicalObject:
    """
    Obiekty tej klasy mogą być symulowane, tzn. mają funkcję która mówi jak zmeinia się ich stan
    przy przejściu w czasie z t -> t+dt
    """

    def step(self, t, dt):
        pass


class LocalizedObject(PhysicalObject):
    """
    Obiekty tej klasy posiadają pozycję, i prędkość która mówi o zmianie tej pozycji w czasie.
    Klasa rozszerza (extends) typ PhysicalObject
    """
    position: List[float]
    velocity: List[float]


class Drone(LocalizedObject):
    """
    Specjalna klasa odpowiadająca za dron (z danymi które _on_ widzi)
    """

    def get_velocity_magnitude(self):
        vel = sqrt(sum([v ** 2 for v in self.velocity]))
        return vel


class Airplane(LocalizedObject):
    """
    Specjalna klasa odpowiadająca za zarejestrowany samolot
    """
    registration: str
    aircraft_type: str

    def __init__(self, registration_number: str):
        self.registration = registration_number


class Environment:
    flying_objects: List[LocalizedObject] = []

    def add_object(self, p: LocalizedObject):
        self.flying_objects.append(p)

    def simulate(self, t0, t1, dt):
        #todo: callbacks; add callback before_step(), after_step()
        """
        Symuluje zachowanie wszystkich obiektów środowiska od t0 do t1 z krokiem czasowym dt
        """
        t = t0
        while t <= t1:
            print('----')
            for p in self.flying_objects:
                p.step(t, dt)
                print(p.position)
            t += dt


class WindyEnvironment(Environment):
    wind_velocity: List[float] = []

    def __init__(self, wind_vel):
        self.wind_velocity = wind_vel


    def get_airspeed(self, object: LocalizedObject):
        vel1 = object.velocity[0] - self.wind_velocity[0]
        vel2 = object.velocity[1] - self.wind_velocity[1]
        vel3 = object.velocity[2] - self.wind_velocity[2]
        return [vel1, vel2, vel3]


class MonitoredEnvironment(WindyEnvironment):
    def get_possible_collisions(self, distance: float):
        collision_map = []
        for i in self.flying_objects:
            for j in self.flying_objects:
                if i != j:
                    if i.position[0] - j.position[0] <= distance or i.position[1] - j.position[1] <= distance:
                        collision_map.append(i)
                        collision_map.append(j)

    def get_TAWS_alarms(self, time_window:float) -> List[LocalizedObject]:
        underground_list : List[LocalizedObject] = []
        for i in self.flying_objects:
            if i.position[2] <= 0:
                underground_list.append(i)
        self.simulate(0, time_window, 0.01)
        for i in self.flying_objects:
            if not underground_list.__contains__(i):
                if i.position[2] <= 0:
                    underground_list.append(i)
        return underground_list
    def get_stall_alarms(self, min_airspeed: float) -> List[LocalizedObject]:
        stalled_objects: List[LocalizedObject] = []
        for i in self.flying_objects:
            speed: float
            for fastness in i.velocity:
                speed += fastness
            if speed < min_airspeed:
                stalled_objects.append(i)
        return stalled_objects

if __name__ == '__main__':
    d = Drone()
    d.position = [1, 2, 3]
    print(d.position)
    ap = Airplane('TC-JJL')
    ap.position = [51.1402, 18.7028, 37000]
    print(ap.registration)

    visible_objects: List[LocalizedObject]
    visible_objects = [d, ap]  # w liście udało się umieścić obiekty różnych klas, ale mające wspólnego "przodka"

    print('--------')
    for o in visible_objects:
        print(f'x={o.position[0]}    y={o.position[1]}')
