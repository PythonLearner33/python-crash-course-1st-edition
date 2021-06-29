import pygame

class Pause():
    '''Class of pause text; is displayed on center of screen.'''
    def __init__(self, screen):
        # Load screen surface.
        self.screen = screen

        # Load font object for text image to utilize.
        self.font = pygame.font.SysFont(name=None, size=70)

        # Render image based on font object.
        self.image = self.font.render("PAUSED", True, (0,0,0), None)

        # Load and assign rects.
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect() # Assuming (0, 0).
        # print(self.rect) e.g. displays <rect(0, 0, 17, 31)>

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        # print(self.rect) e.g. displays <rect(963, 5, 17, 31)>