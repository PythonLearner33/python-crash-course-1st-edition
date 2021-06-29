import sys, time, random
import pygame
from ship import Ship
from ship_bullet import ShipBullet
from alien import Alien
from alien_bullet import AlienBullet
# from ship_explosion import Ship_Explosion
from game_stats import Gamestats


#***UPDATES***

def update_screen(ai_settings, screen, clock, stats, sb, ship, bullets, aliens, play_button, alien_bullets, background):
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    screen.blit(background.image, background.rect)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for alien_bullet in alien_bullets:
        alien_bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Draw the score information.
    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
    clock.tick(ai_settings.framerate)

def update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets):
    '''
    Check if the fleet is at an edge, 
    and then update the positions of all aliens in the fleet.
    '''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets)

def update_ship_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets):
    '''Update position of bullets and get rid of old bullets.'''
    # Update bullet positions.
    if ship.firing_bullet:
        fire_bullet(ai_settings, screen, ship, bullets)
    bullets.update()

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets)

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_alien_bullets(ai_settings, screen, stats, sb, aliens, alien_bullets, ship, bullets):
    '''Update position of bullets and get rid of old bullets.'''
    # Update bullet positions.
    fire_alien_bullets(ai_settings, screen, alien_bullets, aliens, stats)
    alien_bullets.update()

    check_alienbullet_ship_collisions(ai_settings, screen, stats, sb, aliens, alien_bullets, ship, bullets)

    # # Get rid of bullets that have disappeared.
    for alien_bullet in alien_bullets:
        if alien_bullet.rect.top >= ai_settings.screen_height:
            alien_bullets.remove(alien_bullet)

#***FUNCTIONS***

def get_number_aliens(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''Create an alien and place it in the row.'''
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = (2 * alien.rect.height) + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    '''Create a full fleet of aliens.'''
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_rows(ai_settings, ship_height, alien_height):
    '''Determine the number of rows of aliens that fit on the screen.'''
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def change_fleet_direction(ai_settings, aliens):
    '''Drop the entire fleet and change the fleet's direction.'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        # Decrement ships left.
        stats.ships_left -= 1
        
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        
        # Update scoreboard.
        sb.prep_ships()

        # Pause.
        time.sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def fire_bullet(ai_settings, screen, ship, bullets):
    '''Fire a bullet if limit not reached yet.'''
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        if bullets:
            prev_bullet_rect = list(bullets)[-1].rect.bottom
            if prev_bullet_rect < ai_settings.screen_height/2:
                new_bullet = ShipBullet(ai_settings, screen, ship)
                bullets.add(new_bullet)
        else:
            new_bullet = ShipBullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def fire_alien_bullets(ai_settings, screen, alien_bullets, aliens, stats):
    '''Aliens fire bullet(s) when levels increase by increments of 5.'''
    # Choose a random alien, then create a new bullet and add it to the
    # alien_bullets group. Progressively increases bullets as level increases.
    stats.alien_bullets = int(stats.level / 5) # Increase bullets by 1 every 5 levels.
    if len(alien_bullets) == 0: # Fires once, increasing the length of alien_bullets group.
        for alien_bullet in range(stats.alien_bullets):
            alien = random.choice(list(aliens))
            new_alien_bullet = AlienBullet(ai_settings, screen, alien)
            alien_bullets.add(new_alien_bullet)

#*** CHECKS ****

def check_events(ai_settings, screen, sb, stats, play_button, ship, aliens, bullets, alien_bullets):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, aliens, alien_bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, sb, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, alien_bullets)

def check_keydown_events(event, ai_settings, screen, ship, bullets, aliens, alien_bullets):
    '''Respond to keypresses'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        ship.firing_bullet = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    '''Respond to key releases'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_SPACE:
        ship.firing_bullet = False

def check_play_button(ai_settings, screen, sb, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, alien_bullets):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        # Reset the game statistics.
        stats.reset_stats()
        # Reset the scoreboard images. 
        sb.prep_score() # THIS WAS AN ERROR I THINK, I ADDED THIS TO RESET THE SCORE TO 0 INSTEAD OF HAVING THE 
                        # PREVIOUS SCORE SHOWING UP. BETTER AESTHETICS. // NOT AN ERROR. JUST CAME AFTER.
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        stats.game_active = True
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets):
    '''Respond to bullet-alien collisions.'''
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # If the entire fleet is destroyed, erase existing bullets, increase point multiplier, speed up game, 
        # start a new level, and create new fleet, and allow bullets to be fired.
        bullets.empty()
        alien_bullets.empty()
        ai_settings.increase_speed()
        
        # Increase level.
        stats.level += 1
        sb.prep_level()
        
        create_fleet(ai_settings, screen, ship, aliens)

def check_alienbullet_ship_collisions(ai_settings, screen, stats, sb, aliens, alien_bullets, ship, bullets):
    '''Respond to alien_bullet to ship collisions.'''
    # Remove any alien bullets that have collided.
    collisions = pygame.sprite.spritecollide(ship, alien_bullets, False, collided = None)
    
    if collisions:
        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
        alien_bullets.empty()

def check_fleet_edges(ai_settings, aliens):
    '''Respond appropriately if any aliens have reached an edge.'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

#************