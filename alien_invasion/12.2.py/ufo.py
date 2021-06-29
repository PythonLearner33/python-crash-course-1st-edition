import pygame

class Ufo():
    def __init__(self, screen):
        self.screen = screen
        self.screenrect = screen.get_rect()
        self.image = pygame.image.load(r'C:\Users\Alvin\Desktop\Desktop\python_work\Projects\alien_invasion\images\ufo.bmp')
        self.imagerect = self.image.get_rect()

        self.imagerect.centerx = self.screenrect.centerx
        self.imagerect.centery = self.screenrect.centery

    def blitme(self):
        self.screen.blit(self.image, self.imagerect)