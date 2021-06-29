import pygame
from cartridge import Cartridge

class Gun():
    def __init__(self, screen, settings, Cartridges):
        self.settings = settings
        self.Cartridges = Cartridges

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(r'C:\Users\Alvin\Desktop\desktop\python_work\Projects\alien_invasion\14.2.py\images\m1911.png')
        self.rect = self.image.get_rect()
        self.rect.left = self.screen_rect.left + 2
        self.rect.centery = self.screen_rect.centery

        self.moving_up = False
        self.moving_down = False
        self.reload_animation = False

        self.settings_speed_placeholder = self.rect[1] # Rects cannot handle floats, is converted to closest int.

    def move(self):
        '''Move the gun up and down only if the flags are activated, which allows for continuous 
        movement, and rects which are restricted only within the screen.'''
        if self.moving_up == True and self.rect.top != self.screen_rect.top:
            if self.rect.top > self.screen_rect.top+59.8:
                self.settings_speed_placeholder -= self.settings.gun_movement_speed # Up screen.
                self.rect.y = self.settings_speed_placeholder

        if self.moving_down == True and self.rect.bottom != self.screen_rect.bottom:
            if self.rect.bottom < self.screen_rect.bottom-7.1:
                self.settings_speed_placeholder += self.settings.gun_movement_speed # Up screen.
                self.rect.y = self.settings_speed_placeholder

    def reload(self):
        '''Reload cartridges to default number and play sound.'''
        if len(self.Cartridges) < self.settings.num_of_cartridges:
            self.reload_animation = True
            if self.settings.audio_enabled:
                pygame.mixer.music.set_volume(self.settings.audio_volume)
                pygame.mixer.music.load(r'C:\Users\Alvin\Desktop\desktop\python_work\Projects\alien_invasion\14.2.py\audio\reload.mp3')
                pygame.mixer.music.play()

            for x in range(self.settings.num_of_cartridges - len(self.Cartridges)):
                cartridge = Cartridge(self.screen, self.Cartridges, self.settings)
                self.Cartridges.add(cartridge)