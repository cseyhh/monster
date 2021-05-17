import pygame


class Button:
    """设置所有按钮的类"""

    def __init__(self, ai_game):
        self.button_screen = ai_game.screen

        # 开始界面相关设置
        self.start_screen_button_color = (255, 255, 0)  # 黄色
        # self.start_screen_button_font = pygame.font.SysFont('华文仿宋', 40)                   # 开始界面的按钮外形字体和大小
        self.start_screen_button_font = pygame.font.Font('华文楷体/华文楷体.ttf', 40)
        self.start_screen_rect = self.button_screen.get_rect()                              # 获取开始界面屏幕矩形

        # 失败界面相关设置
        self.end_screen_button_color = (255, 255, 0)  # 黄色
        # self.end_screen_button_font = pygame.font.SysFont('华文仿宋', 40)                     # 结束界面的按钮字体和大小
        self.end_screen_button_font = pygame.font.Font('华文楷体/华文楷体.ttf', 40)
        self.end_screen_rect = self.button_screen.get_rect()                                # 获取结束界面屏幕矩形

    def draw_start_screen_button(self, msg, y_offset):  # offset:偏移量
        """绘制开始界面按钮"""
        self.start_screen_text_image = self.start_screen_button_font.render(msg, True,
                                                                            self.start_screen_button_color)
        self.start_screen_font_rect = self.start_screen_text_image.get_rect()               # 获取开始界面按钮字体矩形
        self.start_screen_font_rect.centerx = self.start_screen_rect.centerx                # 设置开始界面按钮的x坐标
        self.start_screen_font_rect.centery = self.start_screen_rect.centery + y_offset     # 设置开始界面按钮的y坐标

        self.button_screen.blit(self.start_screen_text_image, self.start_screen_font_rect)  # 绘制开始界面按钮

    def draw_end_screen_button(self, msg, x_offset, y_offset):
        """绘制失败界面按钮"""
        self.end_screen_text_image = self.end_screen_button_font.render(msg, True, self.end_screen_button_color)
        self.end_screen_font_rect = self.end_screen_text_image.get_rect()                   # 获取结束界面按钮字体矩形
        self.end_screen_font_rect.centerx = self.end_screen_rect.centerx + x_offset         # 设置结束界面按钮的x坐标
        self.end_screen_font_rect.centery = self.end_screen_rect.centery + y_offset         # 设置结束界面按钮的y坐标

        self.button_screen.blit(self.end_screen_text_image, self.end_screen_font_rect)      # 绘制结束界面按钮


