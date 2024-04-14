import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Для управления пулями, выпущенными кораблями"""
    def __init__(self, ai_settings, screen, ship):
        """создает объект пули в текущей позиции корабля"""
        super(Bullet, self).__init__()
        self.screen = screen

        # создание пули в позиции (0,0) и назначение правильнйо позиции
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Позиция пули хранится в вещественном формате
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Перемещает пулю вверх по экрану"""
        #Обновление позиции пули
        self.y -= self.speed_factor
        #Обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод пули на экрна"""
        pygame.draw.rect(self.screen, self.color, self.rect)

