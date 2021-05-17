import pygame


class GameShows:
    """游戏说明的类"""

    def __init__(self, ai_game):
        self.game_show_screen = ai_game.screen
        # self.my_font = pygame.font.SysFont('华文仿宋', 30)
        self.my_font = pygame.font.Font('华文楷体/华文楷体.ttf', 30)
        self.font_color = (255, 255, 0)  # 黄色
        self.backspace_font_color = (255, 255, 255)  # 白色

    def add_tips(self, msg, x_offset, y_offset):
        """小技巧绘制"""
        self.game_show_font_text = self.my_font.render(msg, True, self.font_color)
        self.screen_rect = self.game_show_screen.get_rect()
        self.game_show_font_text_rect = self.game_show_font_text.get_rect()

        self.game_show_font_text_rect.x = self.screen_rect.centerx + x_offset
        self.game_show_font_text_rect.y = self.screen_rect.centery + y_offset
        self.game_show_screen.blit(self.game_show_font_text, self.game_show_font_text_rect)

    def draw_backspace(self):
        """返回键绘制"""
        # self.backspace_font = pygame.font.SysFont('华文仿宋', 20)
        self.backspace_font = pygame.font.Font('华文楷体/华文楷体.ttf', 20)
        self.backspace_font_text = self.backspace_font.render('BackSpace返回', True, self.backspace_font_color)
        self.backspace_font_text_rect = self.backspace_font_text.get_rect()
        self.backspace_font_text_rect.x = 10
        self.backspace_font_text_rect.y = 10
        self.game_show_screen.blit(self.backspace_font_text, self.backspace_font_text_rect)

    def draw_game_shows(self):
        """绘制游戏说明"""
        tip1 = '1. 空格键开火'
        tip2 = '2. 按住Q键退出游戏'
        tip3 = '3. A向左移动，D向右移动'
        tip4 = '4. 吃到各种胶囊，子弹可以进化'
        tip5 = '5. 听说超级横屏子弹和穿透buff更搭哦！'

        self.add_tips(tip1, -500, -300)
        self.add_tips(tip2, -500, -250)
        self.add_tips(tip3, -500, -200)
        self.add_tips(tip4, -500, -150)
        self.add_tips(tip5, -500, -100)
        self.draw_backspace()
