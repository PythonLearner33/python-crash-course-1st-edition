import pygame
import game_settings

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun, Bullets, target, Cartridges, settings, cartridge, hitsmisses):
        super().__init__() # Sprite class init.

        self.settings = settings

        self.Bullets = Bullets
        self.target = target
        self.Cartridges = Cartridges
        self.cartridge = cartridge
        self.hitsmisses = hitsmisses

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.color = settings.bullet_color
        
        self.rect = self.screen_rect
        self.rect.width = settings.bullet_width
        self.rect.height = settings.bullet_height
        self.rect.x = gun.rect.centerx + 45
        self.rect.y = gun.rect.centery - 23

    def move(self):
        '''Draw bullet at starter position if bullet is triggered (flag-based), then keep moving
        across the screen until it hits the target or misses, then remove instance from Bullets group.'''
        if self.cartridge.triggered == True:
            pygame.draw.rect(self.screen, self.color, self.rect) # Draw.
            self.rect.x += self.settings.bullet_speed
            if self.rect.right >= self.settings.screen_width: # Wall Hit.
                self.Bullets.remove(self)
                self.cartridge.triggered = False
                self.hitsmisses.misses += self.settings.miss_value
            elif pygame.sprite.spritecollide(self.target, self.Bullets, 1): # Target hit.
                self.hitsmisses.hits += self.settings.hit_value