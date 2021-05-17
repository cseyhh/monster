import pygame
from 按钮 import Button
from 界面箭头 import Arrow


class EndScreen:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.button = Button(self)
        # self.my_font = pygame.font.SysFont('华文楷体', 30)
        self.my_font = pygame.font.Font('华文楷体/华文楷体.ttf', 30)
        self.white = 255, 255, 255
        self.fail_word = '真是可惜呢，我亲爱的宝贝，想要再来一次吗？'
        self.text_image = self.my_font.render(self.fail_word, True, self.white)
        self.font_rect = self.text_image.get_rect()  # 获取字体Font的外接矩形
        self.screen_rect = self.screen.get_rect()  # 获取整个屏幕的外接矩形

        # 将字体放在中间靠上
        self.font_rect.centerx = self.screen_rect.centerx  # font外接矩形的中间x坐标与屏幕矩形中间x相等
        self.font_rect.centery = self.screen_rect.centery - 200  # font外接矩形的中间y坐标与屏幕矩形中间y-200像素相等

        self.arrow = Arrow(self)

    def end_screen(self):
        self.screen.blit(self.text_image, self.font_rect)
        self.button.draw_end_screen_button('再来一次', -300, +300)
        self.button.draw_end_screen_button('我不行了', +300, +300)

