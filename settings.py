import pygame
class Settings():
    #A class to store settings for AI
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 800
        self.image =  pygame.image.load('stars.png')
        self.rect =  self.image.get_rect()


        #Bullet Settings
        self.bullets_allowed = 5

        #Alien Settings
        self.fleet_drop_speed = 10
        #fleet direction + means right, -1 means left


        #Ship Limit
        self.ship_limit = 3

        #How quickly game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        #Changes that occur throughout the game
        self.ship_speed_factor = 15
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 8
        self.bacon_speed_factor = 5

        self.fleet_direction = 1

        #Scoring
        self.alien_points = 51

    def increase_speed(self):
        #Speed settings and alien point values
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bacon_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

        
