import random
random.seed(42)
from logger import Logger
# TODO: Import the virus class

'''
	Person objects will populate the simulation.
		_____Attributes______:
			- _id: Int.  A unique ID assigned to each person.
			- vaccinated: Bool.  Determines whether the person object is vaccinated against the disease in the simulation.
			- alive: Bool. All person objects begin alive (value set to true). Changed to false if person object dies from an infection.
			- infection:  None or Virus object.  Set to None for people that are not infected. If a person is infected, will instead be set to the virus object the person is infected with.

		_____Methods_____:
			- self.alive should be automatically set to true during instantiation.
			- all other attributes for self should be set to their corresponding parameter passed during instantiation.
			- If person is chosen to be infected for first round of simulation, then the object should create a Virus object and set it as the value for self.infected.  Otherwise, self.infected should be set to None.

		def __init__(self, _id, vaccinated, infection=None):
			- self.alive should be automatically set to true during instantiation.
			- all other attributes for self should be set to their corresponding parameter passed during instantiation.
			- If person is chosen to be infected for first round of simulation, then the object should create a Virus object and set it as the value for self.infected.  Otherwise, self.infected should be set to None.

		did_survive_infection(self):
			- Only called if infection attribute is not None.
			- Takes no inputs.
			- Generates a random number between 0 and 1.
			- Compares random number to mortality_rate attribute stored in person's infection attribute.
				- If random number is smaller, person has died from disease. alive is changed to false.
				- If random number is larger, person has survived disease. Person's vaccinated attribute is changed to True, and set self.infected to None.
'''

class Person(object):

	# TODO:  Finish this method. Follow the instructions in the class documentation to set the corret values for the following attributes.
	def __init__(self, identity, vaccinated, infection=None):
		self.alive = True
		self.identity = identity
		self.vaccinated = vaccinated
		self.infected = infection

	# TODO: Finish this method. Follow the instructions in the class documentation
	# TODO: You will need to decide what parameters you pass into this method based on how you structure your class.
	# For resolve_infection: If person dies, set alive to False and return False.
	# If person lives, set vaccinated = True, infection = None, return True.
	def resolve_infection(self, mortality_rate): # OPEN ISSUE ON GITHUB
		# This checks if infected people die.
		# Check if person is infected.
		if self.infected != None:
			# Randomly determine if person dies, based on disease mortality rate.
			mortality_rand = random.random()
			if mortality_rand < mortality_rate:
				# Person dies.
				self.alive = False
				return False
			else:
				# Person lives.
				self.vaccinated = True
				return True

		else:
			# Person is not infected.
			return None
