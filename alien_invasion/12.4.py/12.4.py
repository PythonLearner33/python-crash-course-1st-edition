import pygame
import sys

def event_key_print():
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('Listen for event, then print in IDE interpreter.')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(event.key)

event_key_print()