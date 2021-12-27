class Settings():
	"""A class to store all settings for Alien Invasion."""
	def __init__(self):
		"""Initialize the game's static settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (5, 5, 40)	
		# Ship settings
		self.ship_limit = 3
		# Bullet settings
		self.bullet_width = 8
		self.bullet_height = 25
		self.bullet_color = 247, 55, 24
		self.bullets_allowed = 3
		# Alien settings
		self.fleet_drop_speed = 20
		# fleet_direction of 1 represents right; -1 represents left.
		

		# How quickly the game speeds up
		self.speedup_scale = 1.1
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.ship_speed_factor = 0.6
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 0.1
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1
		# Scoring
		self.alien_points = 50

	def increase_speed(self):
		"""Increase speed settings."""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale