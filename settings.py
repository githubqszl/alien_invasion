class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        #我的屏幕按书上那样1200*800会太大，显示不全
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #飞船的设置
        #这样，每次移动1.5个像素，而不是1个像素
        self.ship_speed_factor = 1.5

        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        #外星人设置
        self.alien_speed_factor = 1



