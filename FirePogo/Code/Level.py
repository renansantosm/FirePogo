import sys

import pygame
import pygame.font as pgfont
from pygame.surface import Surface

from Code.Entity import Entity
from Code.EntityFactory import EntityFactory
from Code.Const import WIN_WIDTH


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

        self.entity_list.extend(EntityFactory.get_entity('Level1bg'))

        player1 = EntityFactory.get_entity('Player1')
        self.entity_list.append(player1)
        self.player1 = player1

        player2 = EntityFactory.get_entity('Player2')
        self.entity_list.append(player2)
        self.player2 = player2

        ball = EntityFactory.get_entity('Ball')
        self.entity_list.append(ball)
        self.ball_instance = ball

        pgfont.init()
        self.font = pgfont.SysFont("Arial", 30)

    def run(self):
        pygame.mixer_music.load('./asset/game_music.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.player2.control_type == 'ai':
                self.player2.target_ball_rect = self.ball_instance.rect

            self.window.fill((0, 0, 0))

            for ent in self.entity_list:
                scorer = ent.move()
                self.window.blit(source=ent.surf, dest=ent.rect)

                if scorer:
                    if scorer == 'Player1':
                        self.player1.score += 1
                        self.ball_instance.reset_ball(initial_direction_x=1)
                    elif scorer == 'Player2':
                        self.player2.score += 1
                        self.ball_instance.reset_ball(initial_direction_x=-1)

            if self.ball_instance.rect.colliderect(self.player1.rect):
                if self.ball_instance.direction_x == -1:
                    self.ball_instance.direction_x *= -1
                    self.ball_instance.rect.left = self.player1.rect.right
                    self.ball_instance.accelerate(1.05)

            if self.ball_instance.rect.colliderect(self.player2.rect):
                if self.ball_instance.direction_x == 1:
                    self.ball_instance.direction_x *= -1
                    self.ball_instance.rect.right = self.player2.rect.left
                    self.ball_instance.accelerate(1.05)

            player1_text = f"Jogador: {self.player1.score}"
            player2_text = f"Bot: {self.player2.score}"

            y_pos = 20

            self.draw_text(player1_text, (WIN_WIDTH / 4, y_pos), (255, 255, 255), centered_x=True)

            self.draw_text(player2_text, (WIN_WIDTH * 3 / 4, y_pos), (255, 255, 255), centered_x=True)

            pygame.display.flip()

    def draw_text(self, text: str, position: tuple, color: tuple, centered_x=False):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect()

        if centered_x:
            text_rect.centerx = position[0]
            text_rect.top = position[1]
        else:
            text_rect.topleft = position

        self.window.blit(text_surface, text_rect)