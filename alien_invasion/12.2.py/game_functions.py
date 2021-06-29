import sys
import pygame
from ship import Ship
from ufo import Ufo

def check_events():
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship, ufo):
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    ufo.blitme()
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()
