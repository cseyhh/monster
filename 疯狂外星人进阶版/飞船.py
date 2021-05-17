import pygame
from 右侧面板 import RightScreen
from pygame.sprite import Sprite


class Ship(Sprite):
    """描述飞船的类"""
    ship_level: object

    def __init__(self, ai_game, level):
        super().__init__()
        self.screen = ai_game.screen  # 获取主屏幕
        self.screen_rect = ai_game.screen.get_rect()  # 设置主屏幕矩形

        self.image = pygame.image.load('image/飞船.bmp')  # 载入飞船图像
        self.rect = self.image.get_rect()  # 获取飞船矩形

        self.rect.midbottom = self.screen_rect.midbottom  # 将飞船放在主屏幕最下方

        # 飞船速度
        self.ship_speed = 1.5  # 速度为每次移动1.5个像素

        # 飞船等级
        self.ship_level = level

        # 在飞船的属性x中存储小数值(rect的x等属性中只能存储整数值，所以要用float)
        self.x = float(self.rect.x)

        # 飞船移动标志
        self.move_right = False  # 向右移动
        self.move_left = False  # 向左移动

        self.game_screen = RightScreen(self)
        self.game_screen.vertical_line()

    def draw_ship(self):
        """绘制飞船的函数"""
        self.screen.blit(self.image, self.rect)  # 绘制飞船

    def update(self):
        """移动飞船的函数"""
        if self.move_right and self.rect.right < self.game_screen.vertical_line_rect.right - 2:
            self.x += self.ship_speed  # 如果move_right为真，且飞船右边界小于垂线右边界，就可以向右移动飞船
        if self.move_left and self.rect.left > 0:
            self.x -= self.ship_speed  # 如果move_left为真，且飞船左边界大于0，就可以向左移动飞船

        self.rect.x = self.x  # 将x的值传给飞船的x，以达到移动飞船的位置

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
