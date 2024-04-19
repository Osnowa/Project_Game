import pygame
from pygame.sprite import Group
import sys #для завершения игры
from settings import Settings
from ship import Ship
from alien import Alien
from hero import Hero
import game_functions as gf

def run_game():
    """Инициализация игры и объекта экрана"""
    pygame.init()
    ai_settings = Settings() # создаем экземпляр класса для настроек
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))   #Для отоброжения
    pygame.display.set_caption("Alien Invasion")
    bg_color = ai_settings.background_image # цвет фона игры

    ship = Ship(ai_settings ,screen) # создание корабля
    bullets = Group() # для хранения пуль
    aliens = Group()
    hero = Hero(screen) # создание hero
    alien = Alien(ai_settings, screen) # Создание пришельца

    gf.create_fleet(ai_settings, screen, ship, aliens) # Создание флота пришельцев

    # Запуск цикла игры
    while True:
        #Отслеживание ввода
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings ,aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
