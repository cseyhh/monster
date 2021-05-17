'''
def run_game():
    while True:
        self._check_event()                             检测事件
            1.获取键盘按下
                2.按下空格键，建立一颗子弹
        self.ship.update()                              移动飞船
        self._update_bullets()                          释放子弹，并更新子弹的位置
            1.检测子弹与外星人是否相撞
                2.外星人全部消灭，飞船等级加1，将子弹的宽度增加
        self._update_alien_direction()                  更新外星人位置
        self.update_screen()                            更新屏幕
            1.调用开始界面
            2.调用箭头绘制
            3.检测回车键进入哪个选项
            4.绘制子弹


'''

global level_ship
level_ship = 1
