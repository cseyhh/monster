import pygame


class Arrow:
    """绘制箭头的类"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen  # 获取主屏幕
        self.screen_rect = ai_game.screen.get_rect()  # 设置主屏幕矩形

        self.arrows_color = (255, 255, 255)  # 箭头颜色
        self.arrows_font = pygame.font.SysFont(None, 60)  # 箭头对象大小

        # 开始界面箭头相关设置
        self.arrows_text_image = self.arrows_font.render('->', True, self.arrows_color)
        self.arrows_font_rect = self.arrows_text_image.get_rect()  # 获取箭头矩形
        self.arrows_font_rect.centerx = self.screen_rect.centerx - 100  # 设置箭头x坐标
        self.arrows_font_rect.centery = self.screen_rect.centery  # 设置箭头y坐标

        # 失败界面箭头相关设置
        self.end_arrow_text_image = self.arrows_font.render('->', True, self.arrows_color)
        self.end_arrow_font_rect = self.end_arrow_text_image.get_rect()
        self.end_arrow_font_rect.centerx = self.screen_rect.centerx - 400
        self.end_arrow_font_rect.centery = self.screen_rect.centery + 300

        # 移动标志
        self.move_down = False
        self.move_up = False
        self.move_right = False
        self.move_left = False

        # 开始界面箭头移动标志
        self.start_sign1 = False
        self.start_sign2 = False
        self.start_sign3 = False
        self.start_sign4 = False

        # 结束界面箭头移动标志
        self.end_sign1 = False
        self.end_sign2 = False

        # 失败界面调用标志
        self.end_screen_sign = False

    def draw_arrow(self):
        """绘制开始界面箭头的函数"""
        self.screen.blit(self.arrows_text_image, self.arrows_font_rect)  # 绘制按钮

    def draw_end_screen_arrow(self):
        """绘制失败界面箭头的函数"""
        self.screen.blit(self.end_arrow_text_image, self.end_arrow_font_rect)

    def move_key_down_arrow(self, direction):
        """按下按键移动箭头"""
        if 550 >= self.arrows_font_rect.centery >= 350:  # 限制向下移动的范围
            self.move_down = True
            if self.move_down and direction == 'down':
                self.arrows_font_rect.centery += 100
        if 650 >= self.arrows_font_rect.centery >= 450:  # 限制向上移动的范围
            self.move_up = True
            if self.move_up and direction == 'up':
                self.arrows_font_rect.centery -= 100
        if self.end_screen_sign:
            if self.end_arrow_font_rect.centerx == 200:
                self.move_right = True
                if self.move_right and direction == 'right':
                    self.end_arrow_font_rect.centerx += 600
        if self.end_screen_sign:
            if self.end_arrow_font_rect.centerx == 800:
                self.move_left = True
                if self.move_left and direction == 'left':
                    self.end_arrow_font_rect.centerx -= 600

    def move_key_up_arrow(self, direction):
        """抬起按键移动箭头"""
        if direction == 'down':
            self.arrows_font_rect.y += 0  # 抬起的时候不动
        elif direction == 'up':
            self.arrows_font_rect.y -= 0  # 同上
        elif direction == 'right':
            self.end_arrow_font_rect.x += 0
        elif direction == 'left':
            self.end_arrow_font_rect.x -= 0
