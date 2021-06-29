import pygame
import random

class Ball(pygame.sprite.Sprite):
    '''Class of a Ball object; random x-axis placement spawn 
    and continuous downward y-axis movement.'''
    def __init__(self, screen):
        # Initialize sprite module.
        super(Ball, self).__init__()

        # Load image and get rect of image.
        self.image = pygame.image.load(r'Projects\alien_invasion\13.5.needtodo.py\images\ball.png')
        self.rect = self.image.get_rect()

        # Rect placement.
        self.rect.x = random.choice(range(0, 920)) # Place image on random x axis.
        self.rect.y = 0 # 0 is default y-axis.

        # Value placeholder:
        # This is necessary because rect objects cannot add by decimal numbers.
        self.y = 0

        # Score XP.
        self.xp = 1000

    def move(self):
        '''If y-pos is less than the height of screen, keep moving down by 0.75;
        otherwise, respawn on random x-pos and starter y-pos and reset y placeholder.'''
        if self.y < 700:
            self.y += 0.75
            self.rect.y = int(self.y)
        else:
            self.rect.x = random.choice(range(0, 920))
            self.y = 0