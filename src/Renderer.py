# imports
from venv import logger
import pygame as pg
import sys
import numpy as np
from src.verlet.verlet_object import VerletObject

from .Engine import Engine

from .config import WINDOW_WIDTH as w, WINDOW_HEIGHT as h, FPS

import logging

logger = logging.getLogger('debug')


class Renderer:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(True)
        self.screen = pg.display.set_mode(
            size=(w, h), flags=pg.RESIZABLE, vsync=1)
        pg.event.set_grab(False)
        pg.display.set_caption(f'Engine test ({w}x{h})')

        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        self.engine = Engine()

        self.add_object_trigger = False

    def update(self):
        pg.display.flip()
        # number of milliseconds that passed between the previous two calls to Clock.tick(), giving the framerate add a delay if needed
        self.delta_time = self.clock.tick(FPS)*0.001

    def clean_window(self):
        self.screen.fill((0, 0, 0))

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = np.array(pg.mouse.get_pos(), dtype=np.float64)
                    # print(mouse_pos)
                    self.engine.add_object(VerletObject(position=mouse_pos))
                if event.button == 3:
                    self.engine.remove_first_object()
            elif event.type == self.global_event:
                self.global_trigger = True

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.engine.update(self.delta_time)
            self.clean_window()
            self.engine.draw(self.screen)

            pg.display.set_caption(
                f'Engine test ({self.engine.get_number_of_objects()} objects, {self.clock.get_fps():.0f} FPS)')


if __name__ == '__main__':
    renderer = Renderer()
    renderer.run()
