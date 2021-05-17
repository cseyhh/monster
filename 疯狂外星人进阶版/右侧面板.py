import pygame


class RightScreen:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.right_screen = ai_game.screen
        self.my_font_color = (255, 255, 255)
        # self.my_font = pygame.font.SysFont('华文仿宋', 20)
        self.my_font = pygame.font.Font('华文楷体/华文楷体.ttf', 20)

    def vertical_line(self):  # vertical_line:分界线
        """设置分界线"""
        self.rect_color = (255, 255, 255)
        self.vertical_line_rect = pygame.Rect(0, 0, 1, 700)
        self.vertical_line_rect.x = 950
        self.vertical_line_rect.y = 0

    def draw_vertical_line(self):
        """绘制分界线"""
        self.vertical_line()
        self.right_screen.fill(self.rect_color, self.vertical_line_rect)

    def set_level(self):

        self.level_text_str = '等级：' + str()
        self.level_text = self.my_font.render(self.level_text_str, True, self.my_font_color)
        self.level_rect = self.level_text.get_rect()
        self.level_rect.x = 960
        self.level_rect.y = 230

    def draw_level(self):
        self.set_level()
        self.right_screen.blit(self.level_text, self.level_rect)


