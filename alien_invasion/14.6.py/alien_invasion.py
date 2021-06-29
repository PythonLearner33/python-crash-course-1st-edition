import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import Gamestats
from button import Button
from scoreboard import Scoreboard
from background import Background

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Alien Invasion")

    # Background Image
    background = Background(screen)

    # Create an instance to store the game statistics and create a scoreboard.
    stats = Gamestats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    alien_bullets = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")
 
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, sb, stats, play_button, ship, aliens, bullets, alien_bullets)
        if stats.game_active:
            ship.update()
            gf.update_ship_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
            gf.fire_alien_bullets(ai_settings, screen, alien_bullets, aliens, stats)
            gf.update_alien_bullets(ai_settings, screen, stats, sb, aliens, alien_bullets, ship, bullets)
        gf.update_screen(ai_settings, screen, clock, stats, sb, ship, bullets, aliens, play_button, alien_bullets, background)

run_game()