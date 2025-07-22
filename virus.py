###############
# Virus Class #
###############

class Virus:
	'''
	Represents the virus that will be used
	to infect people within the `Simulation` class.
	'''
	def __init__(self, name, reproduction_rate, mortality_rate):
		'''
		Sets up the virus to include its name,
		the reproduction rate that controls how infectious it is,
		and the mortality rate representing how deadly it is.
		'''
		self.name = name # a string
		self.reproduction_rate = reproduction_rate # a float number between 0.0 and 1.0
		self.mortality_rate = mortality_rate # a float number between 0.0 and 1.0

##############
# Unit Tests #
##############

def test_virus_instantiation():
	'''
	Check to make sure that the `Virus` instantiator is working.
	'''

	virus = Virus("HIV", 0.8, 0.3)
	assert virus.name == "HIV"
	assert virus.reproduction_rate == 0.8
	assert virus.mortality_rate == 0.3

# TODO:
# Create your own tests that model other viruses.
