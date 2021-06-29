import pygame

class Reload_Animation():
    def __init__(self, screen, settings, gun):
        self.screen = screen
        self.settings = settings
        self.gun = gun
        self.width = 0

    def blit(self):
        pygame.gfxdraw.box(self.screen, (self.gun.rect.left, self.gun.rect.bottom + 2, self.width, 5), self.settings.reload_animation_color)
        self.width += .075

        if self.width >= self.gun.rect.width:
            self.gun.reload_animation = False
            self.width = 0