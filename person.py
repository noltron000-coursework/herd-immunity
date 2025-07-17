import random
random.seed(42)
from virus import Virus

class Person:
	'''
	The simulation will contain people, who make up a population.
	'''

	def __init__(self, _id, is_vaccinated, infection=None):
		'''
		We start out with `is_alive = True`, because we don't make vampires or zombies.
		All other values will be set by the simulation when it makes each Person object.

		If person is chosen to be infected when the population is created,
		then the simulation should instantiate a `Virus` object
		and set it as the value of`self.infection`.
		Otherwise, `self.infection` should be set to `None`.
		'''

		self._id = None  # int
		self.is_alive = True  # boolean
		self.is_vaccinated = None  # boolean
		self.infection = None  # `Virus` object or `None`

	def did_survive_infection(self):
		'''
		Generate a random number and compare it to the `mortality_rate`.
		If random number is smaller, `Person` dies from the disease.
		If the `Person` survives, then they become vaccinated, and they have no infection.
		Return a boolean value indicating whether or not they survived the infection.
		'''

		# Only called if infection attribute is not None.
		# TODO:
		# Finish this method.
		# Should return a Boolean.
		pass

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

	# TODO:
	# Complete your own assert statements that test the values at each attribute.
	# assert ...
	pass

def test_sick_person_instantiation():
	# Create a `Virus` object to give a `Person` object an infection.
	virus = Virus("Dysentery", 0.7, 0.2)

	# Create a `Person` object and give them the virus infection.
	person = Person(3, False, virus)

	# TODO:
	# Complete your own assert statements that test the values at each attribute.
	# assert ...
	pass

def test_did_survive_infection():
	# TODO:
	# Create a `Virus` object to give a `Person` object an infection.
	virus = Virus("Dysentery", 0.7, 0.2)

	# TODO:
	# Create a `Person` object and give them the virus infection.
	person = Person(4, False, virus)

	# Resolve whether the `Person` survives the infection or not.
	survived = person.did_survive_infection()

	# Check if the `Person` survived or not.
	if survived:
		assert person.is_alive is True

		# TODO:
		# Write your own assert statements that test the values of
		# each attribute for a `Person` who survived.
		assert False # Replace with something else.

	else:
		assert person.is_alive is False

		# TODO:
		# Write your own assert statements that test the values of
		# each attribute for a `Person` who did not survive.
		assert False # Replace with something else.
