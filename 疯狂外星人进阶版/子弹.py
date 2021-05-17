import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理子弹的类"""

    def __init__(self, ai_game, level):
        super().__init__()
        self.screen = ai_game.screen

        self.bullet_width = level + 100  # 子弹宽度
        self.bullet_height = 5  # 子弹高度
        self.bullet_speed = 1.5  # 子弹速度
        self.bullet_color = (255, 255, 255)  # 子弹颜色为白色

        # self.update_bullet_date()

        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 存储用小数表示的子弹竖直位置
        self.y = float(self.rect.y)

        # 存储用小数表示的子弹水平宽度
        self.x = float(self.rect.x)

        # 飞船等级每提升1，子弹相关数据就增加
        self.up_width_date = 100
        self.up_speed_date = 0.1

        # 外星人被消灭标志
        self.alien_wipe_out_sign = False

    def update_bullet_date(self):

        self.bullet_width = 3  # 子弹宽度
        self.bullet_speed = 1.5  # 子弹速度

    def game_update_bullet_date(self):
        self.bullet_width += 100
        self.bullet_speed += self.up_speed_date

    def update(self):  # 精灵Sprite类的update方法被重写了
        """更新子弹竖直位置"""
        # 更新表示子弹位置的小数值
        self.y -= self.bullet_speed

        # 更新表示子弹的rect的位置
        self.rect.y = self.y

        # 如果外星人全部被消灭
        if not self.alien_wipe_out_sign:
            self.bullet_width += self.up_width_date
            # self.rect.width = self.x

    def draw_bullet(self):
        """绘制子弹函数"""
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)

