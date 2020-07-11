import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from bacon import Bacon
from random import randint

def check_events(ship, event, ai_settings, stats, sb, play_button, bullets, screen, aliens):
        #Respond to keypresses and mouse events
#        for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                        #pygame.quit()
                        #quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x , mouse_y = pygame.mouse.get_pos()
                check_play_buttons(stats, ai_settings, screen, sb, play_button, ship,
                                   aliens, bullets,mouse_x, mouse_y)
        if event.type == pygame.KEYDOWN:
                check_keydown_events(ship, event, ai_settings, bullets, screen)
        elif event.type == pygame.KEYUP:
                check_keyup_events(ship, event, ai_settings, bullets, screen)

def check_play_buttons(stats, ai_settings, screen, sb, play_button, ship,
                       aliens, bullets, mouse_x, mouse_y):
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not stats.game_active:
                #Reset game settings
                ai_settings.initialize_dynamic_settings()

                #Hide the mouse cursor
                pygame.mouse.set_visible(False)

                #Reset Stats
                stats.reset_stats()
                stats.game_active = True

                #Reset Scoreboard Images
                sb.prep_score()
                sb.prep_high_score()
                sb.prep_level()
                sb.prep_ships()

                #Empty aliens and bullets.
                aliens.empty()
                bullets.empty()

                #Create new fleet and center the ships
                create_fleet(ai_settings, screen, ship, aliens)
                ship.center_ship()
        
                        
def update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button, bacons):
        
	#Redraw the screen during each pass through the loop
        screen.blit(ai_settings.image, ai_settings.rect)
        
	#Redraw bullets behind ships and aliens
        for bullet in bullets.sprites():
                bullet.draw_bullet()
        ship.blitme()
        aliens.draw(screen)
        for bacon in bacons.sprites():
                bacon.draw_bacon()


        #Draw the score information
        sb.show_score()


	#Draw play button if game is inactive
        if not stats.game_active:
                play_button.draw_button()
        
        #Make the most recently drawn screen visible
        pygame.display.flip()
def check_keydown_events(ship, event, ai_settings, bullets, screen):
        if event.key == pygame.K_RIGHT:
                        #Move Right
                        ship.moving_right = True
        elif event.key == pygame.K_LEFT:
                        #Move Right
                        ship.moving_left = True
        elif event.key == pygame.K_SPACE:
                #Create bullets
                if len(bullets) < ai_settings.bullets_allowed:
                        new_bullet = Bullet(ai_settings, screen, ship)
                        bullets.add(new_bullet)
                        pygame.mixer.init()
                        pew = pygame.mixer.Sound('pew.wav')
                        pygame.mixer.Sound.play(pew)

                        
def check_keyup_events(ship, event, ai_settings, bullets, screen):
        if event.key == pygame.K_RIGHT:
                        ship.moving_right = False
        elif event.key == pygame.K_LEFT:
                        ship.moving_left = False

def get_number_aliens(ai_settings, alien_width):
        #Find number of columns for aliens
        alien_width = 55
        avalaible_space_x = ai_settings.screen_width - 2 * alien_width
        number_aliens_x = int(avalaible_space_x  / (2 * alien_width))
        return number_aliens_x
def get_number_rows(ai_settings, ship_height, alien_height):
        #Find the number of rows for aliens
        available_space_y = (ai_settings.screen_height -
                             (3*alien_height) - ship_height)
        number_rows = int(available_space_y / (2*alien_height))
        return number_rows        

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
        alien = Alien(ai_settings, screen)
        alien_width = alien.rect.width
        alien_width = 55
        alien.x = alien_width + 2 * (alien_width )* (alien_number)
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height *row_number
        aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
        #Create a full fleet
        #Spacing each alien
        alien = Alien(ai_settings, screen)
        number_aliens_x = get_number_aliens(ai_settings, alien.rect.width)
        number_rows = get_number_rows(ai_settings, ship.rect.height,
                                      alien.rect.height)
 

        #creat the first row of aliens
        for row_number in range(number_rows):
                for alien_number in range(number_aliens_x):
                        #Create and place
                        create_alien(ai_settings, screen, aliens, alien_number, row_number)

def update_aliens(ai_settings,stats, sb, screen, ship, aliens, bullets, bacons):
        #Update positions of fleet
        check_fleet_edges(ai_settings, aliens)
        aliens.update()

        #Look for alien-ship collisions
        if pygame.sprite.spritecollideany(ship, aliens):
               ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets)
        #Check for aliens at bottom
        check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets, bacons)

def update_bullets(ai_settings, screen,stats, sb, ship, aliens, bullets):
        #Update Bullet Position
        bullets.update()
        #Collision?
        check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def update_bacon(ai_settings, stats, sb, screen, ship, aliens, bullets, bacons):
        #Draw bacon
        if len(aliens) > 5:
                for alien in aliens.sprites():
                        random_integer = randint(0,ai_settings.bacon_frequency)
                        if random_integer == 10:
                                new_bacon = Bacon(ai_settings, screen, alien)
                                bacons.add(new_bacon)
        else:
                for alien in aliens.sprites():
                        random_integer = randint(0,int(ai_settings.bacon_frequency/2))
                        if random_integer == 10:
                                new_bacon = Bacon(ai_settings, screen, alien)
                                bacons.add(new_bacon)
        bacons.update()               
        check_bacon_ship_collisions(ai_settings, stats, sb, screen, ship, aliens, bullets, bacons)

def check_bacon_ship_collisions(ai_settings, stats, sb, screen, ship, aliens, bullets, bacons):
        #Check Bacon collisions with Ship
        for bacon in bacons.sprites():
                if bacon.rect.colliderect(ship.rect):
                        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets, bacons)
                        pygame.mixer.init()
                        ow_daniel = pygame.mixer.Sound("ow_daniel.wav")
                        pygame.mixer.Sound.play(ow_daniel)

 
def update_ship(ship):
        ship.update()


def check_fleet_edges(ai_settings, aliens):
        #Respond if alien hits edge
        for alien in aliens.sprites():
                if alien.check_edges():
                        change_fleet_direction(ai_settings, aliens)
                        break
def change_fleet_direction(ai_settings, aliens):
        #Drop fleet and change direction
        for alien in aliens.sprites():
                alien.rect.y += ai_settings.fleet_drop_speed
        ai_settings.fleet_direction *= -1


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
        #Respond to Alien-Bullet Collisions
        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        if collisions:
                pygame.mixer.init()
                ow_list = [pygame.mixer.Sound('ow_cody.wav'), pygame.mixer.Sound('ow_lizzy.wav'), pygame.mixer.Sound('ow_millie.wav'),
                           pygame.mixer.Sound('ow_paige.wav'), pygame.mixer.Sound('ow_rachel.wav'), pygame.mixer.Sound('ow_sophie.wav'),pygame.mixer.Sound('ow_brendan.wav')]
                random_integer = randint(0,len(ow_list)-1)
                pygame.mixer.Sound.play(ow_list[random_integer])
                
                for aliens in collisions.values():
                        stats.score += ai_settings.alien_points*len(aliens)
                        sb.prep_score()
                check_high_score(stats, sb)
        if len(aliens) == 0:
                #Destroy existing bullets and create new fleet
                bullets.empty()
                ai_settings.increase_speed()

                #Increase Level
                stats.level += 1
                sb.prep_level()
                create_fleet(ai_settings, screen, ship, aliens)

def ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets, bacons):
        if stats.ships_left >0:
                #Respond to ship being hit
                stats.ships_left -= 1

                #Update Scoreboard
                sb.prep_ships()

                #Empty aliens and bullets
                aliens.empty()
                bullets.empty()
                bacons.empty()

                #Create new fleet and center the ship
                create_fleet(ai_settings, screen, ship, aliens)
                ship.center_ship()

                #pause
                sleep(0.5)
        else:
                stats.game_active = False
                pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, sb, screen, ship, aliens, bullets, bacons):
        #Check to see if Daniel dies
        screen_rect = screen.get_rect()
        for alien in aliens.sprites():
                if alien.rect.bottom >= screen_rect.bottom:
                        ship_hit(ai_settings, stats, sb, screen, ship, aliens, bullets, bacons)
                        break
def check_high_score(stats, sb):
        """Check to see if score is high score"""
        if stats.score > stats.high_score:
                stats.high_score = stats.score
                high_score = open('high_score.txt', 'r+')
                high_score.truncate()
                high_score_str = str(stats.high_score)
                high_score.write(high_score_str)
                sb.prep_high_score()
        







