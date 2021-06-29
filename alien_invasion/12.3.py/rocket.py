import pygame

class Rocket():
    def __init__(self, screen):
        self.image = pygame.image.load(r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\alien_invasion\images\rocket.bmp')
        self.image_rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.centery = self.screen_rect.centery
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
    
    def blitme(self):
        self.screen.blit(self.image, self.image_rect)