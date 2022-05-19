from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #(0,0)放一个表示bullet的矩形, 再将bullet放在ship的顶端
        self.rect = pygame.Rect(0,0,self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #设置bullet发射的位置
        self.y = float(self.rect.y)

    def update(self):
        ''' bullet fire upside:
        because the bullets ought to be remove, so self.y > 0 could not be the case:'''
        self.y -= self.settings.bullet_speed

        #reset the location of the bullet
        self.rect.y = self.y

    def draw_bullet(self):
        #在屏幕上绘制bullet的颜色
        pygame.draw.rect(self.screen, self.color, self.rect)



