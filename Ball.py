import pygame


class Ball(object):
    def __init__(self, x, y, width, height, vx, vy, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx = vx
        self.vy = vy
        self.colour = colour

    def render(self, screen):
        pygame.draw.ellipse(screen, self.colour, self.rect)

    def update(self):
        self.x += self.vx
        self.y += self.vy

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)