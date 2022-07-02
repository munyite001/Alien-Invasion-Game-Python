

class Settings:
    """ A class to store all settings for Alien invasion"""
    def __init__(self):
        """Initializing the game's settings """
        self.screen_width = 1360
        self.screen_height = 720
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 60, 60)
        self.bullets_count = 5

        #Aliens settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # A fleet_direction of 1 represents right movement, -1 represents left movement.
        self.fleet_direction = 1

