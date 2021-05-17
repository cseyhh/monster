import pygame


class Score:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.ai_game = ai_game
        self.screen_rect = self.screen.get_rect()
        self.alien_score = 1  # 每个外星人1分

        self.score = 0  # 新游戏初始0分
        self.high_score = 0  # 最高分
        self.score_color = (255, 255, 255)
        self.high_score_color = (255, 255, 0)
        # self.score_font = pygame.font.SysFont('华文仿宋', 20)
        self.score_font = pygame.font.Font('华文楷体/华文楷体.ttf', 20)
        # self.high_score_font = pygame.font.SysFont('华文仿宋', 30)
        self.high_score_font = pygame.font.Font('华文楷体/华文楷体.ttf', 20)

    def set_present_score(self):
        """建立当前分数矩形并设置其位置"""
        self.score_str = '当前得分：' + str(self.score)
        self.score_font_text = self.score_font.render(self.score_str, True, self.score_color)

        self.score_font_text_rect = self.score_font_text.get_rect()

        # 设置矩形在屏幕上的位置
        self.score_font_text_rect.x = 960
        self.score_font_text_rect.y = 70

    def set_high_score(self):
        """建立最高分"""
        self.high_score_str = '最高分：' + str(self.high_score)
        self.high_score_font_text = self.high_score_font.render(self.high_score_str, True, self.high_score_color)
        self.high_score_font_text_rect = self.high_score_font_text.get_rect()

        self.high_score_font_text_rect.x = 960
        self.high_score_font_text_rect.y = 5

    def draw_present_score(self):
        """绘制当前分数"""
        self.set_present_score()
        self.screen.blit(self.score_font_text, self.score_font_text_rect)

    def draw_high_score(self):
        """绘制最高分"""
        self.set_high_score()
        self.screen.blit(self.high_score_font_text, self.high_score_font_text_rect)

    def check_high_score_produce(self):
        """检查最高分是否产生"""
        if self.score > self.high_score:
            self.high_score = self.score
            self.draw_high_score()
