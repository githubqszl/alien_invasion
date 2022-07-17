class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        #我的屏幕按书上那样1200*800会太大，显示不全
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)
