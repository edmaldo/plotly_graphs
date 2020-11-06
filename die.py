from random import randint

class Die:
	"""A class representing a single dice."""

	def __init__(self, num_sides=6):
		"""Assume a six-sided dice."""
		self.num_sides = num_sides

	def roll(self):
		return randint(1, self.num_sides)