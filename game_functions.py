import sys, pygame

def check_events():
    """Обработка нажатия клваиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Обновляет изобрадение на экране и отоброжает новый"""
    #при каждом проходе цикла перерисовывается экран
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # отображение последнего прорисованого экранаф
    pygame.display.flip()