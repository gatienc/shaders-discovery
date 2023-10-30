from venv import logger
from .verlet import VerletObject, VerletSolver
import pygame as pg
from .config import OBJECT_RADIUS
import logging

logger = logging.getLogger('debug')


class Engine:
    def __init__(self):
        self.verlet_solver = VerletSolver()
        self.verlet_objects = [VerletObject()]

    def update(self, dt):
        self.verlet_solver.update(self.verlet_objects, dt)

    def add_object(self, obj):
        self.verlet_objects.append(obj)

    def remove_first_object(self):
        self.verlet_objects.pop(0)

    def get_number_of_objects(self):
        return len(self.verlet_objects)

    def draw(self, screen):
        for obj in self.verlet_objects:
            logger.debug(f'{obj.position=}')
            pg.draw.circle(screen, (255, 0, 0),
                           (obj.position[0], obj.position[1]), OBJECT_RADIUS)
