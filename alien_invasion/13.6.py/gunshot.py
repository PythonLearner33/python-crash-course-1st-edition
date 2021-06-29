import pygame
import random

class Gunshot():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load(r'C:\Users\Alvin\Desktop\desktop\python_work\Projects\alien_invasion\13.6.py\images\gunshot.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(range(0, 920)) # Place image on random x axis.
        self.rect.y = random.choice(range(0, 700))