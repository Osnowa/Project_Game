import pygame
class Settings():
    """Хранение всех настроек игры"""

    def __init__(self):
        #Screen
        self.screen_width = 1200
        self.screen_height = 700
        self.background_image = pygame.image.load('images/fon.bmp')
        self.bg_color = (0, 0, 0)
        # Настройки корабля
        self.ship_speed_factor = 0.8
        self.ship_limit = 3
        #Параметры пули с скоростью, шириной, высотой, цветом
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 36, 255, 83
        self.bullets_allowed = 3
        # Настройка пришельцев
        self.alien_speed_factor = 0.6
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # 1 - вправо, -1 - влево
        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 0.8
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 0.6

        fleet_direction = 1 # 1 вправо, -1 влево
        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимсоти пришельцев."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
