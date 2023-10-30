'''
VerletObject class for verlet integration
freely adapted from JohnBuffer's VerletSFML
https://github.com/johnBuffer/VerletSFML
'''
import numpy as np

from ..config import OBJECT_RADIUS


class VerletObject:
    def __init__(self) -> None:
        self.position = np.array([250., 250.])
        self.radius = OBJECT_RADIUS
        self.position_old = np.array([250., 250.])
        self.acceleration = np.array([0., 0.])

    def update_position(self, dt):
        velocity = self.position - self.position_old
        self.position_old = self.position.copy()
        print(f'{self.acceleration=} {dt=} {velocity=}')

        self.position += velocity + self.acceleration * dt * dt
        self.acceleration = np.array([0., 0.])

    def accelerate(self, acceleration):
        self.acceleration += acceleration
