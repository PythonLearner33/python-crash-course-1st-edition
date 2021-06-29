import pygame

class Divider():
    def __init__(self, screen, cartridge, settings):
        self.screen = screen
        self.cartridge = cartridge
        self.settings = settings

        self.color = self.settings.divider_color
        self.starter_pos = (0, self.cartridge.rect.height+8)
        self.end_pos = (self.settings.screen_width, self.cartridge.rect.height+8)

    def blit(self):
        pygame.draw.line(self.screen, self.color, self.starter_pos, self.end_pos, 1)