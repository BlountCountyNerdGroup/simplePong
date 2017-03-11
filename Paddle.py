import pygame


class Paddle(object):
    def __init__(self, x, y, width, height, speed, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx = 0
        self.speed = speed
        self.colour = colour

    def render(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)

    def update(self):
        self.x += self.vx

    def key_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.vx = -self.speed
            elif event.key == pygame.K_RIGHT:
                self.vx = self.speed
        elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.vx = 0

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)