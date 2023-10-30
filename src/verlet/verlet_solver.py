import numpy as np
from ..config import WINDOW_WIDTH as w, WINDOW_HEIGHT as h


class VerletSolver:
    def __init__(self):
        self.gravity = np.array([0., 10000.])

    def update(self, verlet_objects, dt):
        '''
        update all verlet objects
        '''
        self.apply_gravity(verlet_objects)
        self.apply_constraint(verlet_objects)
        self.update_position(verlet_objects, dt)

    def apply_gravity(self, verlet_objects):
        '''
        apply gravity to all verlet objects
        '''
        for obj in verlet_objects:
            obj.accelerate(self.gravity)

    def update_position(self, verlet_objects, dt):
        '''
        update position of all verlet objects
        '''
        for obj in verlet_objects:
            obj.update_position(dt)

    def apply_constraint(self, verlet_objects):
        '''
        apply constraints to all verlet objects
        '''
        center = np.array([w/2., h/2.])
        radius = min(w, h)/2.

        for obj in verlet_objects:
            to_obj = center - obj.position
            distance = np.sqrt(to_obj[0]*to_obj[0] + to_obj[1]*to_obj[1])
            print(f'{distance=}')
            if distance > (radius - obj.radius):
                angle = to_obj / distance
                print(f'angle={angle}')
                obj.position = center - \
                    angle * (radius - obj.radius)

                print(f'obj.position={obj.position}')
