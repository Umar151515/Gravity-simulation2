import pygame
from pygame.math import Vector2


class Mouse:
    def __init__(self, core):
        self.core = core
        self.config = core.config

        self.x = 0
        self.y = 0
        self.x_window = 0
        self.y_window = 0
        
        self.vector = Vector2(0, 0)
        self.selected_unit = None
        self.offset = Vector2(0, 0)

    def update(self):
        mouse_buttons = pygame.mouse.get_pressed()
        self.x_window, self.y_window = pygame.mouse.get_pos()

        self.x = (self.x_window + self.config.camera_position_x) / self.config.scale
        self.y = (self.y_window + self.config.camera_position_y) / self.config.scale

        if mouse_buttons[1]:
            if self.selected_unit is None:
                for unit in self.core.units:
                    if unit.rect.collidepoint(self.x, self.y):
                        self.selected_unit = unit
                        self.offset = Vector2(self.x, self.y) - unit.pos
                        break
            else:
                self.selected_unit.pos = Vector2(self.x, self.y) - self.offset
                self.selected_unit.vector = -self.vector / self.config.scale
        elif not mouse_buttons[1] and self.selected_unit:
            self.selected_unit = None

        if mouse_buttons[2]:
            for unit in self.core.units:
                if unit.rect.collidepoint(self.x, self.y):
                    unit.vector.xy = -self.vector / self.config.scale
                    break