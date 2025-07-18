import random

from Code.Const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT
from Code.Entity import Entity


class Ball(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.initial_speed_x = ENTITY_SPEED['BallX']
        self.initial_speed_y = ENTITY_SPEED['BallY']

        self.speed_x = self.initial_speed_x
        self.speed_y = self.initial_speed_y

        self.direction_x = 0
        self.direction_y = 0
        self.reset_ball()

    def reset_ball(self, initial_direction_x=None):
        self.rect.center = (WIN_WIDTH / 2, WIN_HEIGHT / 2)

        if initial_direction_x is None:
            self.direction_x = random.choice([-1, 1])
        else:
            self.direction_x = initial_direction_x

        self.direction_y = random.choice([-1, 1])

        self.speed_x = self.initial_speed_x
        self.speed_y = self.initial_speed_y

    def accelerate(self, acceleration_factor=1.1):
        self.speed_x *= acceleration_factor
        self.speed_y *= acceleration_factor

    def move(self):
        self.rect.centerx += self.speed_x * self.direction_x
        self.rect.centery += self.speed_y * self.direction_y

        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction_y *= -1
        if self.rect.bottom >= WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT
            self.direction_y *= -1

        scorer = None
        if self.rect.left <= 0:
            scorer = 'Player2'
        elif self.rect.right >= WIN_WIDTH:
            scorer = 'Player1'

        if scorer:
            return scorer
        return None