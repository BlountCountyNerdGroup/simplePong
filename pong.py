import sys
import math
from Ball import *
from Paddle import *


class Pong(object):
    CLR = {"WHITE": (255,255,255), "RED": (255,0,0)}

    def __init__(self):
        pygame.init()
        (WIDTH, HEIGHT) = (640, 480)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pong Game")
        self.ball = Ball(5, 5, 35, 35, 5, 5, Pong.CLR["RED"])
        self.paddle = Paddle(WIDTH / 2, HEIGHT - 50, 100, 10, 3, Pong.CLR["RED"])

    def play(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                    self.paddle.key_handler(event)

            self.collision_handler()
            self.draw()

    def collision_handler(self):
        if self.ball.rect.colliderect(self.paddle.rect):
            self.ball.vy *= -1

        if self.ball.x + self.ball.width >= self.screen.get_width():
            self.ball.vx = -(math.fabs(self.ball.vx))
        elif self.ball.x <= 0:
            self.ball.vx = math.fabs(self.ball.vx)

        if self.ball.y + self.ball.height >= self.screen.get_height():
            pygame.quit()
            sys.exit()
        elif self.ball.y <= 0:
            self.ball.vy = math.fabs(self.ball.vy)

        if self.paddle.x + self.paddle.width >= self.screen.get_width():
            self.paddle.x = self.screen.get_width() - self.paddle.width
        elif self.paddle.x <= 0:
            self.paddle.x = 0

    def draw(self):
        self.screen.fill(Pong.CLR["WHITE"])
        self.ball.update()
        self.ball.render(self.screen)
        self.paddle.update()
        self.paddle.render(self.screen)

        pygame.display.update()

Pong().play()