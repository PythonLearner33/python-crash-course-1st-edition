import pygame
import pygame.gfxdraw
import game_functions
from game_settings import Settings
from playbutton import PlayButton
from playbutton_text import PlayButtonText
from stats import Stats
from divider import Divider
from gun import Gun
from target import Target
from bullet import Bullet
from cartridge import Cartridge
from reload_animation import Reload_Animation

def start_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption('target_practice')

    Bullets = pygame.sprite.Group() # Stores bullet objects, bullet instantiated in game_functions.
    Cartridges = pygame.sprite.Group()

    gun = Gun(screen, settings, Cartridges)
    for x in range(settings.num_of_cartridges):
        cartridge = Cartridge(screen, Cartridges, settings)
    divider = Divider(screen, cartridge, settings)
    target = Target(screen, settings, divider)
    playbutton = PlayButton(screen, settings)
    stats = Stats(screen, settings, gun, playbutton, Bullets)
    reload_animation = Reload_Animation(screen, settings, gun)

    while True:
        game_functions.event_check(gun, Bullet, Bullets, screen, target, cartridge,
        Cartridges, settings, stats, playbutton, reload_animation)

        screen.fill(settings.background_color)
        for cartridge in Cartridges:
            screen.blit(cartridge.image, cartridge.rect)
        divider.blit()
        screen.blit(gun.image, gun.rect)
        screen.blit(target.image, target.rect)

        stats.blit()
        if gun.reload_animation:
            reload_animation.blit()
        playbutton.blit()

        gun.move()
        target.move()
        for bullet in Bullets: # Ignores if no bullets instantiated.
            bullet.move()

        pygame.display.flip()

start_game()