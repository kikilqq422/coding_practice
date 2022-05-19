'''rect能把所有图像当做简单几何，矩形进行处理rectangular一样处理'''
import pygame
from setting import Settings
class Ship:
    def __init__(self, ai_game):
        #使用alien_game里面的游戏资源的实例引用
        self.setting = Settings()
        self.screen = ai_game.screen
        #get_rect()为访问屏幕的rect属性，为后面ship放在一个对的位置准备
        self.screen_rect = ai_game.screen.get_rect()

        #加载飞船 image, 获取其surface的rect属性
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #屏幕矩形的属性，将飞船放置在midbottom下面
        self.rect.midbottom = self.screen_rect.midbottom

        #增加一个一直按右键，ship一直往右走的机制
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #define the location of the ship
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        #blit()绘制图像
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''根据移动调整飞船的位置，避免出框
        如果玩家一直按键，则一直向右移动的循环,避免出框, self.rect.right 为飞船的最右端点'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed

        #确认调整后的位置传递给ship，使其能定位到新位置
        self.rect.x = self.x

        if self.moving_up and self.rect.top > 0:
            self.y -= self.setting.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.setting.ship_speed

        # 确认调整后的位置传递给ship，使其能定位到新位置
        self.rect.y = self.y

    def center_ship(self):
        #重新在屏幕低端生成一个shop
        self.rect.midbottom = self.screen_rect.midbottom
        #重新更新ship的位置
        self.x = float(self.rect.x)


