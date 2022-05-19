import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load image and put onto the surface
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # print(self.rect)

       #每个alien都在屏幕左上角，设置alien的左边距为宽，高度为上边距
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #define the location of the aline
        self.x = float(self.rect.x)
        # print(self.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        # print('self.screen_rect:', screen_rect, 'self.rect.right', self.rect.right)
        if self.rect.x >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        #let the alien moving right or left
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x





