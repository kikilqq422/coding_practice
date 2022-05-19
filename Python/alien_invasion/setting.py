
class Settings:
    def __init__(self):
        #setting the performing screen
        self.width = 1200
        self.height = 800
        self.bg_color = (230, 230, 230)

        #setting the ship
        self.ship_speed = 1.5

        #setting the bullet
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 1.5
        # set the total num of fired bullets
        self.bullet_allowed = 10

        #define aliens
        self.alien_speed = 1.0
        #drop_fleet_speed need to be over 1
        self.drop_fleet_speed = 30
        self.fleet_direction = 1

        #计分需求
        self.ship_speed = self.ship_speed + 1
        self.ship_limit = 3

