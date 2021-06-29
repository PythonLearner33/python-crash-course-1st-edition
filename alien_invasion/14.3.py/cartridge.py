import pygame

class Cartridge(pygame.sprite.Sprite):
    def __init__(self, screen, Cartridges, settings):
        super().__init__()
        self.Cartridges = Cartridges
        self.Cartridges.add(self)

        self.settings = settings

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(r'C:\Users\Alvin\Desktop\desktop\python_work\Projects\alien_invasion\14.2.py\images\cartridge.png')
        self.rect = self.image.get_rect()
        self.rect.left = self.screen_rect.left + 5 + ((len(self.Cartridges) - 1) * self.rect.width)
        self.rect.top = self.screen_rect.top + 5

        self.triggered = False

    def fire(self):
        pygame.sprite.Sprite.kill(self)
        if self.settings.audio_enabled:
            pygame.mixer.music.set_volume(self.settings.audio_volume)
            pygame.mixer.music.load(r'C:\Users\Alvin\Desktop\desktop\python_work\Projects\alien_invasion\14.2.py\audio\gunshot.mp3')
            pygame.mixer.music.play()