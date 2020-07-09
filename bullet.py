import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    #Manage Bullets
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        #Create bullet at (0,0) and then set correct position
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Store position as decimal value
        self.y = float(self.rect.y)

        #Speed of bullet
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
    #Move the bullet!
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
    #Draw the bullet to the screen
        self.screen.blit(self.image, self.rect)
