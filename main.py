import pygame
import sys #для завершения игры
from settings import Settings
from ship import Ship

def run_game():
    """Инициализация игры и объекта экрана"""
    pygame.init()
    ai_settings = Settings() # создаем экземпляр класса
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))   #Для отоброжения
    pygame.display.set_caption("Alien Invasion")
    bg_color = ai_settings.bg_color # цвет фона игры

    ship = Ship(screen) # создание корабля

    # Запуск цикла игры
    while True:
        #Отслеживание ввода
        for event in pygame.event.get():
            # При каждом проходе цикла перерисовывается экран
            screen.fill(bg_color)
            ship.blitme()
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip() # Отоброжение последнего прорисованного экрана

run_game()
