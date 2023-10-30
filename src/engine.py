# imports
import pygame as pg
import sys

from .config import WINDOW_WIDTH as w, WINDOW_HEIGHT as h, FPS


class Engine:
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

    def update(self):
        pg.display.flip()

        # number of milliseconds that passed between the previous two calls to Clock.tick(), giving the framerate add a delay if needed
        self.delta_time = self.clock.tick(FPS)

    def draw(self):
        # get mouse position
        mouse_pos = pg.mouse.get_pos()
        pg.draw.rect(self.screen, (0, 0, 0), (0, 0, w, h))
        print(mouse_pos)
        pg.draw.circle(self.screen, (255, 0, 0), mouse_pos, 50)

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    engine = Engine()
    engine.run()
