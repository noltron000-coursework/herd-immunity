###############
# Virus Class #
###############

class Virus:
	'''
	Represents the virus that will be used
	to infect people within the `Simulation` class.
	'''

	def __init__(
			self,
			name: str,
			reproduction_rate: float,
			mortality_rate: float,
		):
		'''
		Sets up the virus to include its name,
		the reproduction rate that controls how infectious it is,
		and the mortality rate representing how deadly it is.
		'''

		self.name = name # type: str
		self.reproduction_rate = reproduction_rate # type: float
		self.mortality_rate = mortality_rate # type: float

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

# XXX TODO XXX
# Create your own tests that model other viruses.
