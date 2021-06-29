import pygame

class Score():
    '''Class of scoreboard text; is displayed on upper-right corner of screen.'''
    def __init__(self, screen):
        # Load screen surface.
        self.screen = screen

        # Load font object for text image to utilize.
        self.font = pygame.font.SysFont(name=None, size=45)

        # Score.
        self.score = 0

    def update(self):
        '''Display text image of score onto screen surface.
        Constantly reassigns new rects due to expanding nature of scoreboard.'''
        # Render image based on font object.
        self.image = self.font.render(str(self.score), True, (0,0,0), None)

        # Load and assign rects.
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect() # Assuming (0, 0).
        # print(self.rect) e.g. displays <rect(0, 0, 17, 31)>

        self.rect.top = self.screen_rect.top + 5
        self.rect.right = self.screen_rect.right - 8
        # print(self.rect) e.g. displays <rect(963, 5, 17, 31)>
