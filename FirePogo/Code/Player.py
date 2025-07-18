import pygame.key

from Code.Const import ENTITY_SPEED, WIN_HEIGHT
from Code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple, control_type: str = 'human'):
        super().__init__(name, position)
        self.control_type = control_type
        self.target_ball_rect = None
        self.score = 0

    def move(self):
        if self.control_type == 'human':
            self._move_human()
        elif self.control_type == 'ai':
            self._move_ai()

    def _move_human(self):
        pressed_key = pygame.key.get_pressed()
        player_speed = ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= player_speed
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += player_speed

    def _move_ai(self):
        if self.target_ball_rect:
            ai_speed = ENTITY_SPEED[self.name]

            if self.rect.centery < self.target_ball_rect.centery:
                self.rect.centery += ai_speed
            elif self.rect.centery > self.target_ball_rect.centery:
                self.rect.centery -= ai_speed

            if self.rect.top < 0:
                self.rect.top = 0
            if self.rect.bottom > WIN_HEIGHT:
                self.rect.bottom = WIN_HEIGHT