import pygame
import random
from pygame.sprite import Sprite

class Star(Sprite):
	"""A class to represent a single star in the background."""
	def __init__(self, ai_settings, screen):
		"""Initialize the star and set its starting position."""
		super().__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		# Load the star image and set its rect attribute.
		self.image = pygame.image.load('images/star.bmp')
		self.rect = self.image.get_rect()
		# Start each new star near the top left of the screen.
		self.rect.x = random.randint(0, ai_settings.screen_width)
		self.rect.y = random.randint(0, ai_settings.screen_height)
		# Store the alien's exact position.
		self.x = float(self.rect.x)

	def blitme(self):
		"""Draw the alien at its current location."""
		self.screen.blit(self.image, self.rect)