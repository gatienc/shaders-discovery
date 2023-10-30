from .verlet import VerletObject, VerletSolver
import pygame as pg
from .config import OBJECT_RADIUS


class Engine:
    def __init__(self):
        self.verlet_solver = VerletSolver()
        self.verlet_objects = [VerletObject()]

    def update(self, dt):
        self.verlet_solver.update(self.verlet_objects, dt)

    def draw(self, screen):
        for obj in self.verlet_objects:
            print(f'{obj.position=}')
            pg.draw.circle(screen, (255, 0, 0),
                           (obj.position[0], obj.position[1]), OBJECT_RADIUS)
