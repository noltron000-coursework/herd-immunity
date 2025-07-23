import random
random.seed(42)
from virus import Virus

################
# Person Class #
################

class Person:
	'''
	The simulation will contain people, who make up a population.
	'''

	@property
	def is_infected(self):
		return self.infection is not None

	def __init__(self, _id: int, is_vaccinated = False, infection: Virus | None = None):
		'''
		Initializes a new person.
		'''

		self._id = _id # type: int
		self.is_vaccinated = is_vaccinated # type: bool

		# We start out with `is_alive = True`, because we don't make vampires or zombies.
		# All other values are set by the simulation when it makes each Person object.
		self.is_alive = True # type: bool

		# If the person is chosen to be infected when the population is created,
		# then the simulation should instantiate a `Virus` object
		# and pass it into the instance via the `infection` parameter.
		# Otherwise, `infection` defaults to `None` (to represent no infection).
		self.infection = infection # type: Virus | None

		# This helps us find whether an infection is dormant or not later...
		# If there is no infection, then this must be set to `False`.
		self.is_dormant = False

	def resolve_infection(self):
		'''
		Generates a random number and compare it to the `mortality_rate`.
		If the random number is smaller, then `Person` dies from the disease.
		If the `Person` survives, then they become vaccinated, and they have no infection.
		Returns a boolean value indicating whether or not they survived the infection.
		'''

		if self.infection is None:
			# The person is not infected. They live.
			return True

		# Randomly determine if the person dies,
		# based on the virus' mortality rate.
		dice_roll = random.random()

		if dice_roll < self.infection.mortality_rate:
			# The person dies...
			self.is_alive = False
			self.is_vaccinated = False
			self.is_dormant = False
			self.infection = None
			return False
		else:
			# The person lives!
			self.is_vaccinated = True
			self.is_dormant = False
			self.infection = None
			return True

##############
# Unit Tests #
##############

# The following functions are simple tests
# to ensure that you are instantiating your `Person` class correctly.

def test_vacc_person_instantiation():
	# Create some people to test if our init method works as expected...
	person = Person(1, True)
	assert person._id == 1
	assert person.is_alive is True
	assert person.is_vaccinated is True
	assert person.infection is None

def test_not_vacc_person_instantiation():
	person = Person(2, False)

	# XXX TODO XXX
	# Complete your own assert statements that test the values at each attribute.
	# assert ...
	pass

def test_sick_person_instantiation():
	# Create a `Virus` object to give a `Person` object an infection.
	virus = Virus("Dysentery", 0.7, 0.2)

	# Create a `Person` object and give them the virus infection.
	person = Person(3, False, virus)

	# XXX TODO XXX
	# Complete your own assert statements that test the values at each attribute.
	# assert ...
	pass

def test_did_survive_infection():
	# XXX TODO XXX
	# Create a `Virus` object to give a `Person` object an infection.
	virus = Virus("Dysentery", 0.7, 0.2)

	# XXX TODO XXX
	# Create a `Person` object and give them the virus infection.
	person = Person(4, False, virus)

	# Resolve whether the `Person` survives the infection or not.
	survived = person.did_survive_infection()

	# Check if the `Person` survived or not.
	if survived:
		assert person.is_alive is True

		# XXX TODO XXX
		# Write your own assert statements that test the values of
		# each attribute for a `Person` who survived.
		assert False # Replace with something else.

	else:
		assert person.is_alive is False

		# XXX TODO XXX
		# Write your own assert statements that test the values of
		# each attribute for a `Person` who did not survive.
		assert False # Replace with something else.
