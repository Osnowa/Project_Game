import pygame
import sys #для завершения игры
from settings import Settings
from ship import Ship
from hero import Hero
import game_functions as gf

def run_game():
    """Инициализация игры и объекта экрана"""
    pygame.init()
    ai_settings = Settings() # создаем экземпляр класса
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))   #Для отоброжения
    pygame.display.set_caption("Alien Invasion")
    bg_color = ai_settings.bg_color # цвет фона игры

    ship = Ship(screen) # создание корабля
    hero = Hero(screen) # создание hero

    # Запуск цикла игры
    while True:
        #Отслеживание ввода
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

run_game()
