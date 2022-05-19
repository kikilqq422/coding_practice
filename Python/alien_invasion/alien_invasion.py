import sys
import pygame
from pygame.sprite import Sprite
from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stat import Game_stat
from time import sleep

class AlienInvasion:
    '''管理游戏资源的类'''
    def __init__(self):
        #initialize the game
        pygame.init()
        #initializa a screen for the game, (width=1200,height = 800) pixel
        self.settings = Settings()

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        #!!!pygame,display.set_mode((width,height)); (width,heighth)should ba a squence
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #reset the screen size
        self.settings.width = self.screen.get_rect().width
        self.settings.height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        # initialize a ship,注意要使用本身这个实例
        self.ship = Ship(self)
        # self.alien = Alien(self)
        self.game_stat = Game_stat(self)

        #initialize a aline instance
        self._creat_fleet()

        #set background color,RGB
        self.bg_color = self.settings.bg_color

    def run_game(self):
        '''start the game'''
        while True:
            #不管是否运行，都要check
            self._check_event()

            if self.game_stat.game_active > 0:
                self.ship.update()
                # self.bullets.update()
                self._bullet_update()
                self._update_alien()

            self._update_screen()

    def _check_event(self):
        '''helper method,辅助方法：在类中执行任务，但非调用实例，以'_'下划线开头，不用调用实例
        隔离事件：_check_event; moniter the mouse and keyboard actions
        pygame.event.get()获取事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self._check_event_KEYDOWN(event)
            self._check_event_KEYUP(event)

    def _check_event_KEYDOWN(self,event):
        #如果玩家按右键的时候，ship向右移动一格，如果持续按键，则一直向右
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # self.ship.rect.x += 1
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_UP:
                self.ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                self.ship.moving_down = True
            #setting keyboard space to fire a bullet
            elif event.key == pygame.K_SPACE:
                self._bullet_fire()

    def _check_event_KEYUP(self,event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False
            elif event.key == pygame.K_UP:
                self.ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                self.ship.moving_down = False
            elif event.key == pygame.K_q:
                sys.exit()

    def _bullet_update(self):
        '''do not forget to update the location of the bullet'''
        self.bullets.update()
        '''remove the bullets reach the top of the screen:
         for loop the len of the list can not be changed, so self.bullets.copy()'''
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))
        #check if bullets and aliends collided, if so, empty bullets and creat a new fleet
        self._check_bullets_aliens_collision()

    def _check_bullets_aliens_collision(self):
        '''check if the bullets has hit aliens ,if hit, then remove'''
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        '''check if the aliens.sprint is empty, if true,create another fleet 
        when the self.aliens = [], it is False'''
        if not self.aliens:
            print(self.aliens)
            print("bullets:", self.bullets)
            self.bullets.empty()
            self._creat_fleet()

    #增加辅助方法（helper_method），creat a new bullet and add to the bullet sprint group
    def _bullet_fire(self):
        #if the amount of bullets are limited
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _creat_fleet(self):
         #creat an aline
        alien = Alien(self)

        #look how many aliens can be put into a row
        self.alien_width = alien.rect.width
        self.alien_height = alien.rect.height
        self.alien_width, self.alien_height = alien.rect.size

        '''self.alien_width * 2为预留的屏幕的边距，设成两个aliens的宽度
        available_space_x // (self.alien_width * 2)是预留一个alien以及alien右边的空白的位置'''
        available_space_x = self.settings.width - self.alien_width * 2
        num_aliens_x = available_space_x // (self.alien_width * 2)

        #look how many rows can be placed, should have enough room for height and rows
        available_space_y = self.settings.height - self.alien_height * 3 - self.ship.rect.height
        num_aliens_rows = available_space_y // (self.alien_height * 2)

        #creat the fleet use its x,y values
        for num_row in range(num_aliens_rows):
            for num_alien in range(num_aliens_x):
                self._creat_alien(num_alien,num_row)

    def _creat_alien(self, num_alien, num_row):
        #set up an alien and put it into the current row
        alien = Alien(self)
        self.alien_width, self.alien_height = alien.rect.size
        alien.x = self.alien_width + 2 * self.alien_width * num_alien
        #获取alien的x的坐标，用alien.rect.x 将 alien放置
        # alien.rect.x = alien.x
        alien.rect.y = self.alien_height + 2 * self.alien_height * num_row
        self.aliens.add(alien)

    def _update_alien(self):
        '''check if every alien reach the edge and the fleet as well need to be updated'''
        self._check_fleet_edge()
        self.aliens.update()
        ship_collisons = pygame.sprite.spritecollideany(self.ship, self.aliens)
        if ship_collisons:
            print('Danger,Ship crashes!')
            self._check_ships_hit()
        self._check_fleet_bottom()


    def _check_fleet_edge(self):
        #once the fleet reach the edge of the screen, the fleet change direction
        for alien in self.aliens.sprites():
            if alien.check_edges():
                print('alien.check_edges:',alien.check_edges)
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        #bring the whole fleet down and change direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.drop_fleet_speed
            print('y:',alien.rect.y)
        #注意是使每个alien粗碰屏幕后往下移动，但是只用改变方向一次，所以不在for循环里面
        self.settings.fleet_direction *= -1
        print('self.settings.fleet_direction',self.settings.fleet_direction)

    def _check_ships_hit(self):
        # ship_collisons = pygame.sprite.spritecollideany(self.ship, self.aliens)
        # if ship_collisons:

        if self.game_stat.ship_left > 0:
            self.game_stat.ship_left -= 1
            print('ship_left:', self.game_stat.ship_left)

            #清楚余下的alien和bullets
            self.aliens.empty()
            self.bullets.empty()

            self._creat_fleet()
            self.ship.center_ship()

            sleep(2)

        else:
            self.game_stat.game_active = False
            sys.exit()

    def _check_fleet_bottom(self):
        self.screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen_rect.bottom:
                self._check_ships_hit()
                break

    def _update_screen(self):
        # in the loop, redraw the surface
        self.screen.fill(self.bg_color)
        # 绘制ship
        self.ship.blitme()

        #draw bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        '''！！！aliens.draw需要调用一个关键参数，self.image，在class Alien里面，
        所以self.aliens是一组sprites，是class Alien的父类，可以调用子类里面的Aline的self.image'''
        self.aliens.draw(self.screen)

        #showup the screen
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()


