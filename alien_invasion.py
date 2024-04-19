import pygame
from pygame.sprite import Group
import sys #для завершения игры
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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
    play_button = Button(ai_settings, screen, 'Play') # создание кнопки play
    bg_color = ai_settings.background_image # цвет фона игры

    ship = Ship(ai_settings ,screen) # создание корабля
    bullets = Group() # для хранения пуль
    aliens = Group()
    hero = Hero(screen) # создание hero
    alien = Alien(ai_settings, screen) # Создание пришельца

    gf.create_fleet(ai_settings, screen, ship, aliens) # Создание флота пришельцев

    # Создание экземпляра для хранения игровой статистики.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Запуск цикла игры
    while True:
        #Отслеживание ввода
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
