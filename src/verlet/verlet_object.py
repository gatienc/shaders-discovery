'''
VerletObject class for verlet integration
freely adapted from JohnBuffer's VerletSFML
https://github.com/johnBuffer/VerletSFML
'''
import numpy as np

from ..config import OBJECT_RADIUS
import logging

logger = logging.getLogger('debug')


class VerletObject:
    def __init__(self, position=np.array([(250.), (250.)])) -> None:
        self.position = position
        self.radius = OBJECT_RADIUS
        self.position_old = position.copy()
        self.acceleration = np.array([0., 0.])

    def update_position(self, dt):
        velocity = self.position - self.position_old
        self.position_old = self.position.copy()
        logger.debug(f'{self.acceleration=} {dt=} {velocity=}')

        self.position += velocity + self.acceleration * (dt * dt)
        self.acceleration = np.array([0., 0.])

    def accelerate(self, acceleration):
        self.acceleration += acceleration
