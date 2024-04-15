import pygame
class Settings():
    """Хранение всех настроек игры"""

    def __init__(self):
        #Screen
        self.screen_width = 1200
        self.screen_height = 700
        self.background_image = pygame.image.load('images/fon.bmp')
        self.ship_speed_factor = 0.8
        #Параметры пули с скоростью, шириной, высотой, цветом
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 36, 255, 83
        self.bullets_allowed = 3
        # Настройка пришельцев
        self.alien_speed_factor = 0.6
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # 1 - вправо, -1 - влево
