import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        """Инициализирует пришельца и задает ему начальную позицию"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Загрузка изображения
        self.image = pygame.image.load("images/boss_enemy_head.bmp")
        # Изменение размера
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()

        #Каждый новый пришелец появляется в леовм верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Сохранение точной позиции пришельца.
        self.x = float(self.rect.x)

    def blitme(self):
        """Выводит пришельца в текушем положении"""
        self.screen.blit(self.image, self.rect)