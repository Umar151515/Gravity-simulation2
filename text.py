import pygame


class Text(pygame.sprite.Sprite):
    def __init__(self, text, x, y, window, size=24, color=(255, 255, 255)):
        super().__init__()
        self.text = text
        self.x = x
        self.y = y
        self.window = window
        self.size = size
        self.color = color

        self.font = pygame.font.Font(None, size)
        self.text_surface = self.font.render(text, True, color)

    def draw(self):
        self.window.blit(self.text_surface, (self.x, self.y))

    def update(self):
        self.text_surface = self.font.render(self.text, True, self.color)