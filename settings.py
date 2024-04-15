class Settings():
    """Хранение всех настроек игры"""

    def __init__(self):
        #Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (16, 78, 139)
        self.ship_speed_factor = 0.8
        #Параметры пули с скоростью, шириной, высотой, цветом
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 5, 5, 5
        self.bullets_allowed = 3
