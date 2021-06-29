import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        '''Initialize the alien and set its starting position.'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the image and its rect attribute.
        self.image = pygame.image.load(r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\alien_invasion\images\alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

        print(type(self.rect.y))
        
    def check_edges(self):
        '''Return True if the alien is at the edge of screen.''' 
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

    def update(self):
        '''Move the alien right or left.'''
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

        
