import pygame

from pygame.sprite import Sprite

class Bacon(Sprite):
    #Manage Bacon
    def __init__(self, ai_settings, screen, alien):
        super(Bacon, self).__init__()
        self.screen = screen

        #Create bullet at (0,0) and then set correct position
        self.image = pygame.image.load('bacon.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom

        #Store position as decimal value
        self.y = float(self.rect.y)

        #Speed of bullet
        self.speed_factor = ai_settings.bacon_speed_factor

    def update(self):
    #Move the bacon!
        self.y += self.speed_factor
        self.rect.y = self.y

    def draw_bacon(self):
    #Draw the bullet to the screen
        self.screen.blit(self.image, self.rect)
