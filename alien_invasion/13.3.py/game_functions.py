import sys
import pygame
from raindrop import Raindrop
import game_functions as gf
import time

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, raindrops):
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    raindrops.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def get_number_raindrops(ai_settings, raindrop_width):
    available_space_x = ai_settings.screen_width
    number_raindrops_x = int(available_space_x / (2 * raindrop_width))
    return number_raindrops_x

def create_raindrop(ai_settings, screen, raindrops, raindrop_number, row_number):
    '''Create an raindrop and place it in the row.'''
    raindrop = Raindrop(ai_settings, screen)
    raindrop_width = raindrop.rect.width
    raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
    raindrop.rect.x = raindrop.x
    raindrop.y = 2 * raindrop.rect.height * row_number
    raindrop.rect.y = raindrop.y
    raindrops.add(raindrop)

def create_fleet(ai_settings, screen, raindrops):
    '''Create a full fleet of raindrops.'''
    # Create an raindrop and find the number of raindrops in a row.
    # Spacing between each raindrop is equal to one raindrop width.
    raindrop = Raindrop(ai_settings, screen)
    number_raindrops_x = get_number_raindrops(ai_settings, raindrop.rect.width)
    number_rows = get_number_rows(ai_settings, raindrop.rect.height)

    # Create the fleet of raindrops.
    for row_number in range(number_rows):
        for raindrop_number in range(number_raindrops_x):
            create_raindrop(ai_settings, screen, raindrops, raindrop_number, row_number)

def get_number_rows(ai_settings, raindrop_height):
    '''Determine the number of rows of raindrops that fit on the screen.'''
    available_space_y = ai_settings.screen_height
    number_rows = int(available_space_y / (2 * raindrop_height))
    return number_rows

def check_bottom(raindrops):
    '''Check if the raindrops have reached the bottom'''
    for raindrop in raindrops.sprites():
        if raindrop.rect.top > 800:
            raindrops.remove(raindrop)

def update_raindrops(raindrops):
    '''
    Check if the fleet is at an edge, 
    and then update the positions of all raindrops in the fleet.
    '''
    check_bottom(raindrops)
    raindrops.update()