import pygame
import sys
import random
import hand, ball, score, pause

def event_check(hand, pause, screen):
    '''Checks key-press and release events.'''
    for event in pygame.event.get():
        # Quit game.
        if event.type == pygame.QUIT: 
            sys.exit()

        # Check for key-state.
        elif event.type == pygame.KEYDOWN: # Key-press.
            if event.key == pygame.K_LEFT:
                hand.left_flag = True # Movement flag.
            if event.key == pygame.K_RIGHT:
                hand.right_flag = True
            if event.key == pygame.K_p: # Pause game.
                pause_game(pause, screen)

        elif event.type == pygame.KEYUP: # Key-release.
            if event.key == pygame.K_LEFT:
                hand.left_flag = False
            if event.key == pygame.K_RIGHT:
                hand.right_flag = False

def pause_game(pause, screen):
    '''Pause game by triggering while loop and display pause 
    text while retaining previous surfaces.'''
    clock = pygame.time.Clock()
    clock.tick(10) # Reduce FPS to 10.
    screen.blit(pause.image, pause.rect) # Draw on-top of surface.
    pygame.display.flip() # Display most recent frame.
    
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Still listens for exit event.
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p: # Unpause game.
                    paused = False

def collision_detection(hand, ball, score):
    '''Detects collision betwen hand and ball; if collided, respawn ball to starter position.'''
    if pygame.sprite.collide_rect(hand, ball):
        ball.rect.y = 0 # 0 is default y-axis.
        ball.rect.x = random.choice(range(0, 920)) # Place image on random x axis.
        ball.y = 0 # **Refer to Ball class.
        
        score.score += ball.xp # Increase score by 10.
