import random
random.seed(42)
from logger import Logger

class Person(object):
	def __init__(self, _id, is_vaccinated, is_infected=False):
		self._id = _id
		self.is_alive = True
		self.is_vaccinated = is_vaccinated
		self.is_infected = is_infected

	def resolve_infection(self, mortality_rate):
		if not self.is_infected:
			# The person is not infected. They live.
			return False

		# Randomly determine if person dies,
		# based on the virus' mortality rate.
		dice_roll = random.random()

		if dice_roll < mortality_rate:
			# The person dies...
			self.is_alive = False
			self.is_vaccinated = False
			self.is_infected = False
			return False
		else:
			# The person lives!
			self.is_vaccinated = True
			return True
