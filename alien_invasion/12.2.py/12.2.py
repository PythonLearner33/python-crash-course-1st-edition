import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from ufo import Ufo

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship.
    ship = Ship(screen)
    # Make a UFO.
    ufo = Ufo(screen)
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events()
        # Redraw the screen during each pass through the loop.    
        # Make the most recently drawn screen visible.
        gf.update_screen(ai_settings, screen, ship, ufo)

run_game()