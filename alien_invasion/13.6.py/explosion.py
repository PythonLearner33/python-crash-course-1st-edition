import pygame
import random

class Explosion():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('C:/Users/Alvin/Desktop/desktop/python_work/Projects/alien_invasion/13.6.py/images/explosion.gif')
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx