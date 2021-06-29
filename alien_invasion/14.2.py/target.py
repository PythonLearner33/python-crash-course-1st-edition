import pygame

class Target(pygame.sprite.Sprite):
    def __init__(self, screen, settings, divider):
        super().__init__() 
        self.settings = settings
        self.divider = divider
        
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        
        self.image = pygame.image.load(r'C:\Users\Alvin\Desktop\desktop\python_work\Projects\alien_invasion\14.2.py\images\target.png')
        self.rect = self.image.get_rect()
        self.rect.right = self.screen_rect.right - 2
        self.rect.centery = self.screen_rect.centery

        self.top_hit = False

        self.speed_placeholder = self.rect.y

    def move(self):
        '''If the target hasn't reached the top and the top_hit flag is False, move up by 1. When the 
        target has reached the top, activate the top_hit flag; making the first if statement inaccessible. If
        target hasn't reached the bottom and top_hit flag is true, move down by 1. When the target has
        reached the bottom, deactivate the top_hit flag; making the second if statement inaccessible.
        '''
        
        if self.rect.top != self.divider.starter_pos[1]+1 and self.top_hit == False:
            self.speed_placeholder -= self.settings.target_movement_speed
            self.rect.y = self.speed_placeholder
            if self.rect.top <= self.divider.starter_pos[1]+1:
                self.top_hit = True

        elif self.rect.bottom != self.screen_rect.bottom and self.top_hit == True:
            self.speed_placeholder += self.settings.target_movement_speed
            self.rect.y = self.speed_placeholder
            if self.rect.bottom >= self.screen_rect.bottom:
                self.top_hit = False