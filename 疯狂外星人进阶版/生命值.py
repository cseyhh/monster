import pygame
from pygame.sprite import Sprite, Group


class HealthPoint(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.ai_game = ai_game
        self.screen = ai_game.screen

        self.ship_health_point = 3

        self.image = pygame.image.load('image/红心.bmp')
        self.rect = self.image.get_rect()

        self.my_font_color = (255, 255, 255)
        # self.set_font = pygame.font.SysFont('华文仿宋', 20)
        self.set_font = pygame.font.Font('华文楷体/华文楷体.ttf', 20)
        self.font_text = self.set_font.render('当前剩余生命值为：', True, self.my_font_color)
        self.font_text_rect = self.font_text.get_rect()
        self.font_text_rect.x = 960
        self.font_text_rect.y = 130

        self.ship_health_point_changes()

    def draw_font(self):
        """绘制字体"""
        self.screen.blit(self.font_text, self.font_text_rect)

    def ship_health_point_changes(self):
        self.ship_health_point_change = 3

    def set_health_point(self):
        self.health_points = Group()
        for health_number in range(self.ship_health_point_change):
            health = HealthPoint(self.ai_game)
            health.rect.x += 965 + health_number * health.rect.width
            health.rect.y = 170
            self.health_points.add(health)

    def draw_health_point(self):
        self.health_points.draw(self.screen)
