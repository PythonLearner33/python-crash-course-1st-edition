import pygame

class PlayButtonText():
    def __init__(self, screen, settings):
        self.settings = settings
        
        self.font = pygame.font.SysFont('arial', self.settings.playbutton_text_size)
        self.text_image = self.font.render(self.settings.playbutton_text, True, self.settings.playbutton_text_color)
        self.text_image.rect = self.text_image.get_rect()