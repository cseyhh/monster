import pygame
from 按钮 import Button


class StartScreen:
    """游戏开始界面"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.button = Button(self)  # 实例化按钮类

        self.white = 255, 255, 255  # 白色RGB
        self.my_font = pygame.font.Font('华文行楷/华文行楷.ttf', 150)
        # self.my_font = pygame.font.SysFont('方正舒体', 150)  # 设置字体
        self.text_image = self.my_font.render('疯狂外星人', True, self.white)  # 设置字体对象

        self.font_rect = self.text_image.get_rect()  # 获取字体Font的外接矩形
        self.screen_rect = self.screen.get_rect()  # 获取整个屏幕的外接矩形

        # 将字体放在中间靠上
        self.font_rect.centerx = self.screen_rect.centerx  # font外接矩形的中间x坐标与屏幕矩形中间x相等
        self.font_rect.centery = self.screen_rect.centery - 200  # font外接矩形的中间y坐标与屏幕矩形中间y-200像素相等

    def start_screen(self):
        self.screen.blit(self.text_image, self.font_rect)  # 绘制疯狂外星人五个字
        self.button.draw_start_screen_button('开始游戏', 0)  # 绘制开始游戏按钮
        self.button.draw_start_screen_button('游戏说明', 100)  # 绘制游戏说明按钮
        self.button.draw_start_screen_button('结束游戏', 200)  # 绘制结束游戏按钮
        self.button.draw_start_screen_button('关于作者', 300)  # 绘制关于作者按钮
