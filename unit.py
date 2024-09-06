import random

import pygame
from pygame.math import Vector2


G = 6.67 * 10**-11
MIN_BOUNCE_VELOCITY = 0.005
 
class Unit(pygame.sprite.Sprite):
    def __init__(self, x, y, size_x, size_y, mass, window, core, color=None, moving=True):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.mass = mass
        self.window = window
        self.core = core
        self.config = core.config
        self.moving = moving
        self.color = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
        if color:
            self.color = color

        self.vector = Vector2(0, 0)
        self.pos = Vector2(x, y)

        self.rect = pygame.Rect(x, y, size_x, size_y)

    def universal_gravity(self):
        for unit in self.core.units:
            if unit is not self:
                direction = unit.pos - self.pos
                distance = direction.length()

                if distance == 0:
                    continue
                force_magnitude = G * (self.mass * unit.mass) / distance ** 2
                force = direction.normalize() * force_magnitude
                self.vector += force / self.mass * self.config.speed_time

    def update(self):
        for unit in self.core.units:
            if unit is not self and self.collide_with(unit):
                self.handle_collision(unit)
        self.universal_gravity()

        if self.moving:
            self.pos += self.vector * self.config.speed_time

        self.rect.topleft = self.pos


    def draw(self):
        x = (self.pos.x * self.config.scale) - (self.config.camera_position_x)
        y = (self.pos.y * self.config.scale) - (self.config.camera_position_y)
        size_x = self.size_x * self.config.scale
        size_y = self.size_y * self.config.scale
        pygame.draw.rect(self.window, self.color, pygame.Rect(x, y, size_x, size_y))

    def collide_with(self, other):
        return self.rect.colliderect(other.rect)

    def handle_collision(self, other):
        overlap_x = min(self.rect.right, other.rect.right) - max(self.rect.left, other.rect.left)
        overlap_y = min(self.rect.bottom, other.rect.bottom) - max(self.rect.top, other.rect.top)

        if overlap_x < overlap_y:
            if self.pos.x < other.pos.x:
                self.pos.x -= overlap_x
            else:
                self.pos.x += overlap_x
        else:
            if self.pos.y < other.pos.y:
                self.pos.y -= overlap_y
            else:
                self.pos.y += overlap_y

        self.rect.topleft = self.pos
        m1, m2 = self.mass, other.mass
        v1, v2 = self.vector, other.vector

        new_v1 = v1 - (2 * m2 / (m1 + m2)) * ((v1 - v2).dot(self.pos - other.pos) / (self.pos - other.pos).length_squared()) * (self.pos - other.pos)
        new_v2 = v2 - (2 * m1 / (m1 + m2)) * ((v2 - v1).dot(other.pos - self.pos) / (other.pos - self.pos).length_squared()) * (other.pos - self.pos)

        new_v1 *= 0.8
        new_v2 *= 0.8

        if new_v1.length() > MIN_BOUNCE_VELOCITY:
            self.vector = new_v1
        if new_v2.length() > MIN_BOUNCE_VELOCITY:
            other.vector = new_v2
