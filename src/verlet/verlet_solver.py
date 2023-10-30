import numpy as np
from ..config import WINDOW_WIDTH as w, WINDOW_HEIGHT as h, MAP, SUBSTEP

import logging

logger = logging.getLogger('debug')


class VerletSolver:
    def __init__(self):
        self.gravity = np.array([0., 1000.])

    def update(self, verlet_objects, dt):
        '''
        update all verlet objects
        '''
        dt = dt/SUBSTEP
        for i in range(SUBSTEP):
            self.apply_gravity(verlet_objects)
            self.apply_constraint(verlet_objects)
            self.check_collisions(verlet_objects)
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

    def check_collisions(self, verlet_objects, response_coef=1.):
        '''
        check collisions between all verlet objects
        '''
        objects_count = len(verlet_objects)
        for i in range(objects_count):
            object_1 = verlet_objects[i]
            for k in range(i+1, objects_count):
                object_2 = verlet_objects[k]
                v = object_1.position - object_2.position
                dist2 = v[0]*v[0] + v[1]*v[1]
                min_dist = object_1.radius + object_2.radius
                if dist2 < min_dist*min_dist:
                    dist = np.sqrt(dist2)

                    n = v / dist
                    # print(f'{v=} {n=}')

                    mass_ratio_1 = object_1.radius / \
                        (object_1.radius + object_2.radius)
                    mass_ratio_2 = object_2.radius / \
                        (object_1.radius + object_2.radius)
                    delta = 0.5 * response_coef * (min_dist-dist)
                    object_1.position += n * (mass_ratio_2 * delta)
                    object_2.position -= n * (mass_ratio_1 * delta)

    def apply_constraint(self, verlet_objects):
        '''
        apply constraints to all verlet objects
        '''
        if MAP == 'CIRCLE':
            self.apply_circle_constraint(verlet_objects)

    def apply_circle_constraint(self, verlet_objects):
        '''
        apply constraints to all verlet objects when map is a circle
        '''
        center = np.array([w/2., h/2.])
        radius = min(w, h)/2.

        for obj in verlet_objects:
            to_obj = center - obj.position
            distance = np.sqrt(to_obj[0]*to_obj[0] + to_obj[1]*to_obj[1])
            logger.debug(f'{distance=}')
            if distance > (radius - obj.radius):
                angle = to_obj / distance
                logger.debug(f'angle={angle}')
                obj.position = center - \
                    angle * (radius - obj.radius)

                logger.debug(f'obj.position={obj.position}')
