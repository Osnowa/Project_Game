# Поведение корабля
import pygame
class Ship():
    """начальная позиция"""
    def __init__(self, ai_settings, screen):
        """корабль задаем начальную позицию"""
        self.screen = screen
        self.ai_settings = ai_settings

        #загрузка изображения кораблся и получение прямоугольника
        self.images = pygame.image.load('images/ship.bmp')
        self.rect = self.images.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Сохранение координаты центра корабля
        self.center = float(self.rect.centerx)

        #Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        # обновление атрибута centr, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Обновление атрибута rect на основании center
        self.rect.centerx = self.center

    def blitme(self):
        """рисуем корабль в текущей позиции"""
        self.screen.blit(self.images, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижней стороны"""
        self.center = self.screen_rect.centerx

