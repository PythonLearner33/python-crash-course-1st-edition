import pygame

class Hand(pygame.sprite.Sprite):
    '''Class of Hand object; centered x-axis and bottom y-axis spawn. Responds to left and
    right key-presses for movement across x-axis.'''
    def __init__(self, screen):
        # Initialize sprite module.
        super(Hand, self).__init__()

        # Load image and get rects of screen and image.
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(r'Projects\alien_invasion\13.6.py\images\hand.png')
        self.rect = self.image.get_rect()

        # Rect placement.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Movement flags.
        self.left_flag = False 
        self.right_flag = False

    def move(self):
        '''If movement flags are activated and x rects are within the screen rect,
        move left or right.'''
        if self.left_flag and self.rect[0] > 0:
            self.rect.x = self.rect[0] - 1
            self.rect.y = self.rect[1]

        if self.right_flag and self.rect[0] < 920:
            self.rect.x = self.rect[0] + 1
            self.rect.y = self.rect[1]