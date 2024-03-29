class Settings():
    def __init__(self):
        '''Initialize the game's static settings'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Framerate
        self.framerate = 300

        # Ship settings
        self.ship_limit = 3

        # Ship Bullet settings
        self.bullet_width = 20
        self.bullet_height = 10
        self.bullet_color = 0, 255, 255
        self.bullets_allowed = 3

        # Alien Settings
        self.fleet_drop_speed = 10

        # Alien Bullet settings
        self.alien_bullet_width = 15
        self.alien_bullet_height = 15
        self.alien_bullet_color = 255, 0, 0

        # How quickly the game speeds up
        self.speedup_scale = 1.10

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 1
        self.alien_bullet_speed_factor = 0.25

        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        '''Increase speed settings and alien point values.'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_bullet_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)