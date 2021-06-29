import pygame
from pygame.sprite import Sprite

class Background(Sprite):
    def __init__(self, screen):
    # def __init__(self, screen, ai_settings):
        super().__init__()
        self.image = pygame.image.load(r'C:\Users\Alvin\Desktop\desktop\python_work\Projects\alien_invasion\14.6.py\assets\bgblue.png')
        self.rect = self.image.get_rect()
        # self.ai_settings = ai_settings
        self.rect = (0, 0)