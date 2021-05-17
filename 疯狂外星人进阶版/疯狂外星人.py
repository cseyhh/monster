import pygame
import sys
import time
from 失败界面 import EndScreen
from 开始界面 import StartScreen
from 飞船 import Ship
from 按钮 import Button
from 界面箭头 import Arrow
from 游戏说明 import GameShows
from 右侧面板 import RightScreen
from 子弹 import Bullet
from 外星人 import Alien
from 得分 import Score
from 生命值 import HealthPoint
from 关于作者 import Author
import 其他设置 as setting
# level_ship = 1


class AlienInvasion:
    """游戏开始界面"""

    def __init__(self):
        pygame.init()  # 初始化游戏资源
        self.screen = pygame.display.set_mode((1200, 700))  # 创建屏幕
        pygame.display.set_caption("AlienInvasion")  # 添加标题
        self.screen_width = 1200  # 屏幕宽度
        self.screen_height = 700  # 屏幕高度
        self.bg_color = (0, 0, 0)  # 设置背景颜色为黑色
        self.start_screens = StartScreen(self)  # 实例化开始界面
        self.end_screens = EndScreen(self)  # 实例化结束界面
        self.button = Button(self)  # 实例化按钮
        self.ship = Ship(self, setting.level_ship)  # 实例化飞船
        self.arrow = Arrow(self)  # 实例化箭头
        self.game_show = GameShows(self)  # 实例化游戏说明
        self.right_screen = RightScreen(self)  # 实例化游戏界面
        self.bullet = Bullet(self, setting.level_ship)  # 实例化子弹
        self.score = Score(self)  # 实例化分数
        self.health_point = HealthPoint(self)  # 实例化生命值
        self.author = Author(self)
        self.bullets = pygame.sprite.Group()  # 创建子弹精灵组
        self.aliens = pygame.sprite.Group()  # 创建外星人精灵组

        # 界面标志
        self.screen_sign = True
        # 返回键标志
        self.backspace_sign = False

        self._create_alien_group()
        self.health_point.set_health_point()

    def run_game(self):
        """程序开始函数"""
        while True:
            self._check_event()  # 检测事件
            self.ship.update()  # 移动更新飞船

            self._update_bullets()  # 更新子弹位置
            self._update_alien_direction()  # 更新外星人位置
            self._update_screen()  # 更新屏幕

    def _check_event(self):
        """检查并获取所有事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 鼠标点击右上角x号就退出程序
                pygame.quit()  # 退出所有模块
                sys.exit()  # 退出程序
            elif event.type == pygame.KEYDOWN:  # 检测键盘按下
                self._check_key_down(event)
            elif event.type == pygame.KEYUP:  # 检测键盘抬起
                self._check_key_up(event)

    def _check_key_down(self, event):
        """检查按下键盘按键事件"""
        if event.key == pygame.K_d:  # 按下d键，飞船向左移动
            self.ship.move_right = True
        elif event.key == pygame.K_a:  # 按下a键，飞船向右移动
            self.ship.move_left = True
        elif event.key == pygame.K_UP:  # 按下上键，箭头向上移动
            self.arrow.move_key_down_arrow('up')
        elif event.key == pygame.K_DOWN:  # 按下下键，箭头向下移动
            self.arrow.move_key_down_arrow('down')
        elif event.key == pygame.K_RIGHT:  # 按下右键，箭头向右移动
            if self.arrow.end_screen_sign:
                self.arrow.move_key_down_arrow('right')
        elif event.key == pygame.K_LEFT:  # 按下左键，箭头向左移动
            if self.arrow.end_screen_sign:
                self.arrow.move_key_down_arrow('left')
        elif event.key == pygame.K_RETURN:  # 按下enter键，K_RETURN代表enter回车键
            self._check_enter_button()
        elif event.key == pygame.K_BACKSPACE:  # 按下backspace返回键
            self.backspace_sign = True
        elif event.key == pygame.K_SPACE:  # 按下空格键，开火
            self._fire_bullet()
        elif event.key == pygame.K_q:  # 按下q键，退出
            pygame.quit()
            sys.exit()

    def _check_key_up(self, event):
        """检查抬起键盘按键事件"""
        if event.key == pygame.K_d:  # 抬起d键
            self.ship.move_right = False
        elif event.key == pygame.K_a:  # 抬起a键
            self.ship.move_left = False
        elif event.key == pygame.K_UP:  # 抬起上键
            self.arrow.move_key_up_arrow('up')
        elif event.key == pygame.K_DOWN:  # 抬起下键
            self.arrow.move_key_up_arrow('down')
        elif event.key == pygame.K_RIGHT:
            self.arrow.move_key_up_arrow('right')
        elif event.key == pygame.K_LEFT:
            self.arrow.move_key_up_arrow('left')

    def _check_enter_button(self):
        """箭头移动到哪里，enter键就进入哪个选项"""
        if self.arrow.arrows_font_rect.centery == 350:
            self.arrow.start_sign1 = True  # 进入选项一
            self.arrow.start_sign2 = False
            self.arrow.start_sign3 = False
            self.arrow.start_sign4 = False
        if self.arrow.arrows_font_rect.centery == 450:
            self.arrow.start_sign1 = False
            self.arrow.start_sign2 = True  # 进入选项二
            self.arrow.start_sign3 = False
            self.arrow.start_sign4 = False
        if self.arrow.arrows_font_rect.centery == 550:
            self.arrow.start_sign1 = False
            self.arrow.start_sign2 = False
            self.arrow.start_sign3 = True  # 进入选项三
            self.arrow.start_sign4 = False
        if self.arrow.arrows_font_rect.centery == 650:
            self.arrow.start_sign1 = False
            self.arrow.start_sign2 = False
            self.arrow.start_sign3 = False
            self.arrow.start_sign4 = True  # 进入选项四
        if self.arrow.end_screen_sign:
            if self.arrow.end_arrow_font_rect.centerx == 200:
                self.arrow.end_sign1 = True
                self.arrow.end_sign2 = False
        if self.arrow.end_screen_sign:
            if self.arrow.end_arrow_font_rect.centerx == 800:
                self.arrow.end_sign1 = False
                self.arrow.end_sign2 = True

    def _enter_button(self):
        if self.arrow.start_sign1:  # 进入第一个选项
            self.screen.fill(self.bg_color)  # 重绘屏幕
            self.right_screen.draw_vertical_line()  # 绘制右边垂线
            self.ship.draw_ship()  # 绘制飞船
            self.aliens.draw(self.screen)  # 绘制外星人
            self.score.draw_present_score()  # 绘制当前得分
            self.score.draw_high_score()  # 绘制最高分
            self.health_point.draw_font()  # 绘制生命值解释字体
            self.health_point.draw_health_point()  # 绘制生命值
            self.right_screen.draw_level()  # 绘制等级
            self.determine_if_failure()
        if self.arrow.start_sign2:  # 进入第二个选项
            self.screen.fill(self.bg_color)  # 重绘屏幕
            self.game_show.draw_game_shows()  # 进入游戏说明界面
            if self.backspace_sign:  # 按下返回键，返回开始页面
                self.arrow.start_sign2 = False
                self.backspace_sign = False
        if self.arrow.start_sign3:  # 进入第三个选项
            pygame.quit()  # 退出所有模块
            sys.exit()  # 退出游戏
        if self.arrow.start_sign4:  # 进入第四个选项
            self.screen.fill(self.bg_color)  # 重绘屏幕
            self.author.draw_text()  # 绘制作者说明
            if self.backspace_sign:  # 按下返回键，返回开始页面
                self.arrow.start_sign4 = False
                self.backspace_sign = False
        if self.arrow.end_sign1:  # 进入失败界面第一个选项
            pygame.quit()
            sys.exit()
        if self.arrow.end_sign2:  # 进入失败界面第二个选项
            pygame.quit()
            sys.exit()

    def _fire_bullet(self):
        """开火"""
        self.new_bullet = Bullet(self,self.ship.ship_level)  # 每按下enter键就实例化创建一个子弹
        # self.new_bullet.bullet_width = self.ship.ship_level + 100
        self.bullets.add(self.new_bullet)  # 并将其加入到精灵中

    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹"""
        self.bullets.update()  # 更新子弹的位置

        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:  # 子弹到达主屏幕顶端
                self.bullets.remove(bullet)  # 删除子弹
        self.determine_bullet_and_alien_crash()

    def _create_alien(self, alien_number, row_number):
        """创建每一个外星人，并加入精灵组"""
        self.alien = Alien(self)
        alien_width, alien_height = self.alien.rect.size
        self.alien.x = alien_width + 2 * alien_width * alien_number
        self.alien.rect.x = self.alien.x
        self.alien.rect.y = self.alien.rect.height + 2 * self.alien.rect.height * row_number
        self.aliens.add(self.alien)

    def _create_alien_group(self):
        # 创建一个外星人并计算一行可以容纳多少个外星人
        # 外星人的间距为外星人的宽度
        self.alien = Alien(self)
        alien_width, alien_height = self.alien.rect.size
        available_space_x = self.screen_width - 200 - (2 * alien_width)
        number_alien_x = (available_space_x // (2 * alien_width))

        # 计算屏幕可容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # 创建外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)

    def _update_alien_direction(self):
        """检查外星人是否撞墙"""
        for alien in self.aliens.sprites():
            alien.update()  # 撞墙后向下移动
        self.determine_alien_and_ship_crash()  # 检测外星人与飞船是否相撞
        self.determine_alien_arrive_screen_bottom()

    def determine_bullet_and_alien_crash(self):
        """判断子弹与外星人是否相撞"""
        # 检查是否有子弹击中了外星人，如果是，就删除相应的子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:  # 如果碰撞为真
            self.score.score += self.score.alien_score  # 当前分数变更
            self.score.draw_present_score()  # 绘制当前分数
            self.score.check_high_score_produce()  # 检查最高分是否产生
        if not self.aliens:  # 如果外星人全被消灭
            # self.bullets.empty()  # 清空子弹
            self._create_alien_group()  # 重新创建外星人
            # self.ship.ship_level += 1  # 飞船等级加1
            # self.bullet.alien_wipe_out_sign = True
            self.new_bullet.bullet_width = setting.level_ship + 100

    def determine_health_if_belong_positive_number(self):
        """死亡后，检测生命值是否为正数"""
        if self.health_point.ship_health_point_change > 0:
            self.health_point.ship_health_point_change -= 1  # 生命值减1
            self.health_point.set_health_point()  # 重新设置生命值
            self.aliens.empty()  # 清空外星人
            self.bullets.empty()  # 清空子弹
            self.ship.center_ship()  # 将飞船放在中间
            self._create_alien_group()  # 重新创建外星人
            time.sleep(1)  # 暂停1秒

    def determine_alien_and_ship_crash(self):
        """检测飞船与外星人相撞"""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):  # 如果飞船与外星人相撞
            self.determine_health_if_belong_positive_number()  # 检测生命值是否为正数

    def determine_alien_arrive_screen_bottom(self):
        """判断外星人是否到达了屏幕底端"""
        screen_rect = self.screen.get_rect()  # 获取主屏幕矩形
        for alien in self.aliens.sprites():  # 遍历外星人
            if alien.rect.bottom >= screen_rect.bottom:  # 如果外星人到达屏幕底端
                self.determine_health_if_belong_positive_number()  # 检测生命值是否为正数

    def determine_if_failure(self):
        """检测是否失败"""
        if self.health_point.ship_health_point_change == 0:  # 如果生命值全部消失，就失败
            self.arrow.end_screen_sign = True
            if self.arrow.end_screen_sign:
                self.screen.fill(self.bg_color)  # 重绘背景
                self.end_screens.end_screen()  # 调用失败界面
                self.arrow.draw_end_screen_arrow()

    def _update_screen(self):
        """绘制各个图像"""
        self.screen.fill(self.bg_color)  # 填充背景色
        self.start_screens.start_screen()  # 调用开始界面函数
        self.arrow.draw_arrow()  # 调用绘制箭头函数
        self._enter_button()  # enter键进入哪个选项，就绘制哪个屏幕
        for bullet1 in self.bullets.sprites():
            bullet1.draw_bullet()
        pygame.display.flip()  # 更新屏幕


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
