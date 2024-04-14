# Поведение корабля
import pygame
class Hero():
    """начальная позиция"""
    def __init__(self, screen):
        """задаем начальную позицию"""
        self.screen = screen

        #загрузка изображения кораблся и получение прямоугольника
        self.images = pygame.image.load('images/hero.png')
        self.rect = self.images.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """рисуем корабль в текущей позиции"""
        self.screen.blit(self.images, self.rect)

