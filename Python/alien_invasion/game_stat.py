'''跟踪游戏的信息统计系统'''

from ship import Ship
import pygame

class Game_stat:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit



