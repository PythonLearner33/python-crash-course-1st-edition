import pygame
from rocket import Rocket
import sys

def run_rocket():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('rocket.py')
    rocket = Rocket(screen)

    while True:
        screen.fill((230, 230 ,230))
        rocket.blitme()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    rocket.moving_down = True
                elif event.key == pygame.K_UP:
                    rocket.moving_up = True
                elif event.key == pygame.K_RIGHT:
                    rocket.moving_right = True
                elif event.key == pygame.K_LEFT:
                    rocket.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    rocket.moving_down = False
                elif event.key == pygame.K_UP:
                    rocket.moving_up = False
                elif event.key == pygame.K_RIGHT:
                    rocket.moving_right = False
                elif event.key == pygame.K_LEFT:
                    rocket.moving_left = False

        if rocket.moving_up and rocket.image_rect.top > rocket.screen_rect.top:
            rocket.image_rect.centery -= 1
        if rocket.moving_down and rocket.image_rect.bottom < rocket.screen_rect.bottom:
            rocket.image_rect.centery += 1
        if rocket.moving_right and rocket.image_rect.right < rocket.screen_rect.right:
            rocket.image_rect.centerx += 1
        if rocket.moving_left and rocket.image_rect.left > rocket.screen_rect.left:
            rocket.image_rect.centerx -= 1

        #if rocket.moving_up:
            #print(
                #f"up={rocket.moving_up} " + 
                #f"top_screen={rocket.screen_rect.top} " +
                #f"top_image={rocket.image_rect.top}"
            #)

run_rocket()