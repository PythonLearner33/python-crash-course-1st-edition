import sys
import pygame
from star import Star

def check_events(ai_settings, screen):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen)

def check_keydown_events(event, ai_settings, screen):
    '''Respond to keypresses'''
    if event.key == pygame.K_q:
        sys.exit()

def update_screen(ai_settings, screen, stars):
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    
    stars.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def get_number_stars(ai_settings, star_width):
    available_space_x = ai_settings.screen_width
    number_stars_x = int(available_space_x / (2 * star_width))
    return number_stars_x

def create_star(ai_settings, screen, stars, star_number, row_number):
    '''Create an star and place it in the row.'''
    star = Star(ai_settings, screen)
    star_width = star.rect.width
    star.x = star_width + 2 * star_width * star_number
    star.rect.x = star.x
    star.rect.y = star.rect.height + 2 * star.rect.height * row_number
    stars.add(star)

def create_galaxy(ai_settings, screen, stars):
    '''Create a full fleet of stars.'''
    # Create an star and find the number of stars in a row.
    # Spacing between each star is equal to one star width.
    star = Star(ai_settings, screen)
    number_stars_x = get_number_stars(ai_settings, star.rect.width)
    number_rows = get_number_rows(ai_settings, star.rect.height)

    # Create the fleet of stars.
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(ai_settings, screen, stars, star_number, row_number)

def get_number_rows(ai_settings, star_height):
    '''Determine the number of rows of stars that fit on the screen.'''
    available_space_y = ai_settings.screen_height
    number_rows = int(available_space_y / (2 * star_height))
    print(available_space_y)
    return number_rows