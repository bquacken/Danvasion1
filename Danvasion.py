import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from bullet import Bullet
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from bacon import Bacon
from alien import Alien

def run_game():
    #Intialize the game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Danvastion')
    
    #Play Button
    play_button = Button(ai_settings, screen, "Play")
    
    
    #Make group to store bullets, aliens and bacon
    bullets = Group()
    aliens = Group()
    bacons = Group()
    
    #Stats and Scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    #Make a ship
    ship = Ship(ai_settings, screen)

    
    #Create fleet of Aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #Set the background color
    bg_color = (230,230,230)
    running = True
    #Play the music, baby
    pygame.mixer.init()
    pygame.mixer.music.load('soundtrack.ogg')
    pygame.mixer.music.play(-1)
    #Start Main Loop
    while running:
        #for event in pygame.event.get():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        running =  False
            gf.check_events(ship, event, ai_settings, stats, sb, play_button,  bullets, screen, aliens)
        if stats.game_active:
            #Update objects
            gf.update_ship(ship)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets, bacons)
            gf.update_bacon(ai_settings, stats, sb, screen, ship, aliens, bullets, bacons)
            #Delete old bullets
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
            #Delete old bacon
            for bacon in bacons.copy():
                if bacon.rect.bottom <= 0:
                    bacons.remove(bacon)
#Redraw the screen during each pass through the loop
        gf.update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button, bacons)

    pygame.quit()
    quit()
run_game()
