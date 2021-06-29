import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Stars")

    stars = Group()

    # Create the fleet of aliens.
    gf.create_galaxy(ai_settings, screen, stars)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen)
        # Redraw the screen during each pass through the loop.    
        # Make the most recently drawn screen visible.
        gf.update_screen(ai_settings, screen, stars)

run_game()