import pygame
from 游戏说明 import GameShows


class Author:
    def __init__(self, ai_game):
        self.screen = ai_game.screen

        self.screen_rect = self.screen.get_rect()
        self.font_color = (255, 255, 255)
        # self.my_font = pygame.font.SysFont('华文仿宋', 20)
        self.my_font = pygame.font.Font('华文楷体/华文楷体.ttf', 20)

        self.game_shows = GameShows(self)

    def set_word(self, text, x_offset, y_offset):
        self.font_text = self.my_font.render(text, True, self.font_color)
        self.font_text_rect = self.font_text.get_rect()
        self.font_text_rect.centerx = self.screen_rect.centerx + x_offset
        self.font_text_rect.centery = self.screen_rect.centery + y_offset

    def draw_text(self):
        self.game_shows.draw_backspace()
        text1 = '欢迎大家找我聊天，作者QQ：1605861524'
        self.set_word(text1, 0, 0)
        self.screen.blit(self.font_text, self.font_text_rect)
