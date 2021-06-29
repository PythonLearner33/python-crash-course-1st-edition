import pygame
import sys
from bullet import Bullet
import time

def event_check(gun, Bullet, Bullets, screen, target, cartridge, Cartridges, settings, stats, playbutton, reload_animation):
    '''Check for events such as a program exit, key-press, or key-release.'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                gun.moving_up = True
            elif event.key == pygame.K_DOWN:
                gun.moving_down = True
            elif event.key == pygame.K_SPACE:
                # Create a bullet instance, add it to the Bullets group, and fire the bullet through flag system.
                if len(Cartridges) != 0 and not gun.reload_animation:
                    bullet = Bullet(screen, gun, Bullets, target, Cartridges, settings, cartridge, stats)
                    Bullets.add(bullet)
                    cartridge.triggered = True
                    cartridge.fire()
                elif len(Cartridges) == 0:
                    if settings.audio_enabled:
                        pygame.mixer.music.set_volume(settings.audio_volume)
                        pygame.mixer.music.load(r'C:\Users\Alvin\Desktop\desktop\python_work\Projects\alien_invasion\14.2.py\audio\empty.mp3')
                        pygame.mixer.music.play()
            elif event.key == pygame.K_r:
                gun.reload()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                gun.moving_up = False
            elif event.key == pygame.K_DOWN:
                gun.moving_down = False
            elif event.key == pygame.K_SPACE:
                pass