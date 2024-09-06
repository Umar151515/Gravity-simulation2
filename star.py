import random
import pygame

class Star(pygame.sprite.Sprite):
    def __init__(self, core):
        super().__init__()
        config = core.config

        self.center_x = random.randint(0, config.size_x)
        self.center_y = random.randint(0, config.size_y)
        self.radius = random.uniform(config.min_radius_star, config.max_radius_star)
