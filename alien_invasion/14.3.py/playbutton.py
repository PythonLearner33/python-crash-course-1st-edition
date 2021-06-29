import pygame
import sys
import game_functions

class PlayButton():
    def __init__(self, screen, settings):
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.width = settings.playbutton_width
        self.height = settings.playbutton_height
        self.color = settings.playbutton_color
        
        self.rect = pygame.Rect((0,0),(self.width,self.height)) # left top width height
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.font = pygame.font.SysFont(self.settings.playbutton_font, self.settings.playbutton_text_size)
        self.font_image = self.font.render(self.settings.playbutton_text, True, self.settings.playbutton_text_color)
        self.font_image_rect = self.font_image.get_rect()
        self.font_image_rect.centerx = self.screen_rect.centerx
        self.font_image_rect.centery = self.screen_rect.centery

        self.active = True

    def blit(self):
        '''Pause game by going into while loop and draw box with specs above. If box is clicked,
        remove box and unpause.'''
        while self.active:
            pygame.gfxdraw.box(self.screen, self.rect, self.color)
            self.font_image = self.font.render(self.settings.playbutton_text, True, self.settings.playbutton_text_color)
            self.font_image_rect = self.font_image.get_rect()
            self.font_image_rect.centerx = self.screen_rect.centerx
            self.font_image_rect.centery = self.screen_rect.centery
            self.screen.blit(self.font_image, self.font_image_rect)
            pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if self.rect.collidepoint(pos) and click[0]==1:
                self.active = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pass

            pygame.display.flip()