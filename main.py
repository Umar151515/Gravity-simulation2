import math
import random

import pygame

from unit import Unit
from config import Config
from mouse import Mouse
from text import Text 
from star import Star
from controls import event, update

G = 6.67430e-11

pygame.init()

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Гравитационная симуляция")
clock = pygame.time.Clock()


class Core:
    def __init__(self):
        self.units = pygame.sprite.Group()
        self.group_text = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        self.config = Config(window.get_width(), window.get_height())
        self.mouse = Mouse(self)

        self.text_scale = Text('', 0, 0, window)
        self.text_cor = Text('', 0, 36, window)
        self.text_speed_time = Text('', 0, 72, window)

        self.group_text.add(self.text_scale)
        self.group_text.add(self.text_cor)
        self.group_text.add(self.text_speed_time)

        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def update(self):
        if self.left:
            self.config.camera_position_x -= self.config.speed_camera
        elif self.right:
            self.config.camera_position_x += self.config.speed_camera
        if self.up:
            self.config.camera_position_y -= self.config.speed_camera
        elif self.down:
            self.config.camera_position_y += self.config.speed_camera


core = Core()

for i in range(100):
    core.stars.add(Star(core))

earth = Unit(0, 0, 12742, 12742, 5.9742e+18, window, core, (34, 139, 34))
moon = Unit(384467, 0, 3475, 3475, 7.36e+16, window, core, (211, 211, 212))
sun = Unit(149597871, 0, 1392700, 1392700, 1.98892e+24, window, core, (255, 139, 34))

#earth = Unit(0, 0, 40, 40, 99, window, core, (34, 139, 34))
#moon = Unit(40, 20, 20, 20, 9, window, core, (211, 211, 212))
#sun = Unit(140, 60, 90, 90, 999, window, core, (255, 139, 34))

moon.vector.y = 50
earth.vector.y = 25

core.units.add(earth)
core.units.add(moon)
core.units.add(sun)

#core.e = earth


#for i in range(100):
#    core.units.add(Unit(random.randint(0, 1000), random.randint(0, 1000), random.randint(100, 300), random.randint(100, 300), random.randint(100, 500), window, core, (255, 255, 255)))


#core.units.add(Unit(500, 500, 50, 50, -1000000000000, window, core, (200, 200, 200)))

while True:
    event(window, core, core.config)
    update(window, core)

    pygame.display.flip()

    window.fill((0, 0, 0))
     
    clock.tick(60)
