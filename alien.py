import pygame
from pygame.sprite import Sprite
from random import randint

class Alien(Sprite):
    #Aliens!
    
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #load image
        image_list = ['brendan.png', 'blaine.png', 'cody.png', 'millie.png', 'sophie.png',
                      'lizzy.png', 'rachel.png', 'paige.png']
        self.person = randint(0,7)
        self.image = pygame.image.load(image_list[self.person])
        self.rect = self.image.get_rect()
        
        #Each alien starts top left
        self.rect.x = 25
        self.rect.y = 25
        
        #Store alien's position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)



        
    def blitme(self):
        #Draw alien
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor
                   *self.ai_settings.fleet_direction)
        self.rect.x = self.x
        screen_rect = self.screen.get_rect()
#        random_integer = randint(0,100)
#        if random_integer > 50:
#            self.x += (self.ai_settings.alien_speed_factor
#                       * self.ai_settings.fleet_direction)
#        else :
#            self.x -= (self.ai_settings.alien_speed_factor
#                       * self.ai_settings.fleet_direction)
#        self.rect.x = self.x
#        random_integer = randint(0,100)
#        random_integer1 = randint(0, 100)
#        if random_integer1 < 50:           
#            self.rect.y += 2
#        else:
#            self.rect.y -=2
#        if self.rect.left <= 0:
#            self.rect.x += 50
#        if self.rect.right >= screen_rect.right:
#            self.rect.x -= 50


    
        
