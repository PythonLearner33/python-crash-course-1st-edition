import pygame

class Stats():
    def __init__(self, screen, settings, gun, playbutton, Bullets):
        # Object
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.gun = gun
        self.playbutton = playbutton
        self.Bullets = Bullets

        self.hits = 0
        self.misses = 0
        self.accuracy = 0.0
        self.level = 1

        self.hits_font = pygame.font.SysFont(self.settings.hits_font, self.settings.hits_text_size)
        self.hits_image = self.hits_font.render(f'Hits: {self.hits}', True, self.settings.hits_text_color)
        self.hits_rect = self.hits_image.get_rect()
        self.hits_rect.y = 5

        self.misses_font = pygame.font.SysFont(self.settings.misses_font, self.settings.misses_text_size)
        self.misses_image = self.misses_font.render(f'Misses: {self.misses}', True, self.settings.misses_text_color)
        self.misses_rect = self.misses_image.get_rect()
        self.misses_rect.y = self.hits_rect.bottom

        self.accuracy_font = pygame.font.SysFont(self.settings.accuracy_font, self.settings.accuracy_text_size)
        self.accuracy_image = self.accuracy_font.render(f'Accuracy: ' + ('{:.6}'.format(str(self.accuracy)) + '%'), True, self.settings.accuracy_text_color)
        self.accuracy_rect = self.accuracy_image.get_rect()
        self.accuracy_rect.y = 15

        self.level_font = pygame.font.SysFont(self.settings.level_font, self.settings.level_text_size)
        self.level_image = self.level_font.render(f'Level: ' + str(self.level), True, self.settings.level_text_color)
        self.level_rect = self.level_image.get_rect()

    def check(self):
        '''Check stats.'''
        self.accuracy_check()
        self.misses_check()
        self.level_up_check()

    def accuracy_check(self):
        if self.misses or self.hits:
            self.accuracy = self.hits / (self.hits + self.misses)

    def misses_check(self):
        if self.misses == self.settings.misses_allowed:
            self.playbutton.active = True
            while self.playbutton.active:
                self.blit()
                self.Bullets.empty()
                self.playbutton.settings.playbutton_text = 'RESTART'
                self.playbutton.blit()

            self.gun.reload()
            self.reset()

    def level_up_check(self):
        '''If hits is equal to hit-tracking (default: 7), increase level by 1 and add
        (static) hits_to_level_up to (dynamic) hit-tracking and increase target speed.'''
        if self.hits == self.settings.hits_tracking:
            self.level = int(self.hits / self.settings.num_of_cartridges)+1
            self.settings.hits_tracking += self.settings.hits_to_level_up
            self.settings.target_movement_speed += self.settings.target_level_speed_increase

    def reset(self):
        '''Reset values to default state.'''
        self.hits = 0
        self.misses = 0
        self.accuracy = 0.0
        self.level = 1
        self.target_movement_speed = 0.5

    def blit(self):
        self.hits_image = self.hits_font.render(f'Hits: {self.hits}', True, self.settings.hits_text_color)
        self.misses_image = self.misses_font.render(f'Misses: {self.misses}/{self.settings.misses_allowed}', True, self.settings.misses_text_color)
        self.accuracy_image = self.accuracy_font.render('Accuracy: '+('{:.4}'.format(str(self.accuracy))+'%'), True, self.settings.accuracy_text_color)
        self.level_image = self.level_font.render(f'Level: ' + str(self.level), True, self.settings.level_text_color)
        self.hits_rect.right = self.screen_rect.right - self.hits_rect.width # Restatement to reassign rect pos.
        self.misses_rect.left = self.hits_rect.left # Restatement to reassign rect pos.

        self.accuracy_rect = self.accuracy_image.get_rect()
        self.accuracy_rect.centerx = self.screen_rect.centerx
        self.accuracy_rect.y = 15

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.hits_rect.left - 15
        self.level_rect.y = self.hits_rect.y

        self.screen.blit(self.hits_image, self.hits_rect)
        self.screen.blit(self.misses_image, self.misses_rect)
        self.screen.blit(self.accuracy_image, self.accuracy_rect)
        self.screen.blit(self.level_image, self.level_rect)
