import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    def __init__(self, ai_settings, screen):
        '''Initialize the raindrops and set its starting position.'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the image and its rect attribute.
        self.image = pygame.image.load(r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\alien_invasion\images\raindrop.bmp')
        self.rect = self.image.get_rect()

    def update(self):
        '''Move the raindrops down.'''
        self.y = float(self.rect.y)
        self.y += self.ai_settings.rain_drop_speed
        self.rect.y = self.y