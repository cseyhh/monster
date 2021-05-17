import pygame
import random
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.alien_speed = 0.5  # 外星人运动速度
        self.alien_drop_speed = 5  # 外星人下降速度

        self.image = pygame.image.load('image/外星人3.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = (500, 100)
        # self.alien_image_rect.y = 0

        # 存储每个外星人的精确水平位置
        self.x = float(self.rect.x)

        # alien_direction 为1表示向右移，为-1表示往左移
        self.alien_direction_right = 1
        self.alien_direction_left = -1
        self.alien_direction = [self.alien_direction_left, self.alien_direction_right]
        self.direction = random.choice(self.alien_direction)

    def update(self):
        """向左或向右移动外星人"""
        self.x += (self.alien_speed * self.direction)
        self.rect.x = self.x
        self.determine_alien_if_crash_wall()

    def determine_alien_if_crash_wall(self):
        """判断外星人是否撞墙"""
        if self.rect.right == 950:  # 到达右边界
            if self.direction == 1:
                self.direction = -1
                self.rect.y += self.alien_drop_speed  # 撞墙后下移5个像素
            elif self.direction == -1:
                self.direction = 1
                self.rect.y += self.alien_drop_speed
        elif self.rect.left == 0:  # 到达左边界
            if self.direction == 1:
                self.direction = -1
                self.rect.y += self.alien_drop_speed
            elif self.direction == -1:
                self.direction = 1
                self.rect.y += self.alien_drop_speed

    def draw_alien(self):
        """绘制外星人"""
        self.screen.blit(self.image, self.rect)

