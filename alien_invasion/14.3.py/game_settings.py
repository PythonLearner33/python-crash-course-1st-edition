import pygame

class Settings():
    def __init__(self):
        # Audio
        self.audio_enabled = True # Default: True
        self.audio_volume = 0.05 # Default: 

        # Window
        self.background_color = (255, 255, 255) # Default: 

        # Screen
        self.screen_width, self.screen_height = (1150, 750) # Default: 

        # Play Button
        self.playbutton_width = 350 # Default: 
        self.playbutton_height = 200 # Default: 
        self.playbutton_color = (255,0,0) # Default: 
        self.playbutton_text = 'PLAY' # Default: 
        self.playbutton_font = 'QUAD' # Default: 
        self.playbutton_text_size = 99 # Default: 
        self.playbutton_text_color = (255,255,255) # Default: 

        # Stats
        self.hits_font = 'QUAD' # Default: 
        self.hits_text_size = 35 # Default: 
        self.hits_text_color = (0,0,0) # Default: 
        self.hit_value = 1 # Default:  

        self.misses_font = 'QUAD'# Default:  
        self.misses_text_size = 35 # Default: 
        self.misses_text_color = (0,0,0) # Default: 
        self.miss_value = 1 # Default: 

        self.misses_allowed = 10 # Default: 

        self.level = 0
        self.hits_to_level_up = 7 # Static value
        self.hits_tracking = self.hits_to_level_up # Dynamic value 7 + 7 = 14 // 14 + 7 = 21 etc

        self.accuracy_font = 'QUAD' # Default: 
        self.accuracy_text_size = 55 # Default: 
        self.accuracy_text_color = (0,0,0) # Default: 

        self.level_font = 'QUAD' # Default: 
        self.level_text_size = 35 # Default: 
        self.level_text_color = (0,0,0) # Default: 

        # Divider
        self.divider_color = (0,0,0) # Default: (0,0,0) Black

        # Gun
        self.gun_movement_speed = 3 # Default: 

        # Bullet
        self.bullet_speed = 5 # Default: 5
        self.bullet_color = (255, 204, 0) # Default: Orange-Yellow (255, 204, 0)
        self.bullet_width = 15 # Default: 15
        self.bullet_height = 7 # Default: 7

        # Cartridges
        self.num_of_cartridges = 7 # Default: 7

        # Reload Animation
        self.reload_animation_color = (255, 0, 0) # Default: 

        # Target
        self.target_movement_speed = 0.5 # Default: 1
        self.target_level_speed_increase = 0.25