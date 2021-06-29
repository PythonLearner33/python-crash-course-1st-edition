class Gamestats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # High score should never be reset.
        with open(r'C:\Users\Alvin\Desktop\desktop\python_work\Projects\alien_invasion\14.4.py\highscore.txt', 'r') as highscore:
            asd = highscore.read()
            self.high_score = int(asd)

        self.level = 1

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1