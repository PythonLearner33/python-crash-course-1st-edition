import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self, ai_settings, screen):
        '''Initialize the alien and set its starting position.'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the image and its rect attribute.
        self.image = pygame.image.load(r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\alien_invasion\images\star.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)