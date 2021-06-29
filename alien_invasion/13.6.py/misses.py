import pygame

class Misses():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont(name=None, size=45)
        self.count = 0

    def update(self):
        self.image = self.font.render(f"Misses: {self.count}", True, (255,0,0), None)
        self.rect = self.image.get_rect()
        self.rect.top = self.screen_rect.top + 5
        self.rect.left = self.screen_rect.left + 8