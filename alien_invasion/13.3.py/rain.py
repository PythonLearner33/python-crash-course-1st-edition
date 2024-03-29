import pygame
from pygame.sprite import Group
from settings import Settings
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Rain")

    raindrops = Group()

    # Create the fleet of raindrops.
    gf.create_fleet(ai_settings, screen, raindrops)

    # Start the main loop for the game.
    while True:
        gf.check_events()
        gf.update_raindrops(raindrops)
        gf.update_screen(ai_settings, screen, raindrops)

run_game()