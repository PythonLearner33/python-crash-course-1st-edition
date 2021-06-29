import pygame
from ball import Ball
from hand import Hand
from game_functions import *
from score import Score
from pause import Pause
from misses import Misses
from gunshot import Gunshot
from explosion import Explosion
from game_over import GameOver

def run_game():
    '''Simple game, catch the basketball by pressing left and right arrow keys.
    Scoreboard and pause functionality added. Score and speed of hand and ball increases over time.
    If you miss catching a ball, the score resets. '''

    # Initialize module.
    pygame.init()

    # Window Settings.
    ball_icon = pygame.image.load(r'Projects\alien_invasion\13.6.py\images\ball.png')
    pygame.display.set_icon(ball_icon)
    pygame.display.set_caption('ball_catch')
    
    size = width, height = (1000, 700)
    color = (255, 255, 255)
    screen = pygame.display.set_mode(size) # Create window and store in screen.

    # Instantiate objects.
    hand = Hand(screen)
    ball = Ball(screen)
    score = Score(screen)
    pause = Pause(screen)
    misses = Misses(screen)
    explosion = Explosion(screen)
    gameover = GameOver(screen)

    # Main game loop.
    while True:
        event_check(hand, pause, screen) # Event-listener.

        # Moves and integer updates.
        hand.move()
        ball.move(misses)
        score.update()
        misses.update()

        # Fill and draws to the screen surface.
        screen.fill(color) # Background Color.
        screen.blit(hand.image, hand.rect)
        screen.blit(ball.image, ball.rect)
        screen.blit(score.image, score.rect)
        screen.blit(misses.image, misses.rect)

        collision_detection(hand, ball, score) # Detect collisions.
        count_misses(screen, misses, Gunshot, explosion, gameover)

        pygame.display.flip() # Display most recent frame.

run_game()