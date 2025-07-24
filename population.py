import math, random, sys
random.seed(42)
from person import Person
from virus import Virus

####################
# Population Class #
####################

class Population:
	'''
	This class will help organize people in a population.
	We'll have to frequently run filters and searches,
	and this will help us organize that logic into one unit.
	'''

	def __init__(
		self,
		population_size: int,
		vaccination_rate: float,
		initial_infections: int,
		virus: Virus,
	):
		'''Initializes a population, vaccinates some people, and infects others.'''

		# For now we will store the vaccination rate and initial infections in this class.
		self.vaccination_rate: float = vaccination_rate
		self.initial_infections: int = initial_infections
		initial_vaccinations = math.floor(vaccination_rate * population_size)
		self.initial_vaccinations: int = initial_vaccinations

		# Create a population based on the given population size.
		self.list: list[Person] = []
		for _id in range(population_size):
			person = Person(_id)
			self.list.append(person)

		# For our purposes, it's fine to vaccinate and infect the population right away.
		self.vaccinate_population(initial_vaccinations)
		self.infect_population(virus, initial_infections)

	@property
	def size(self): return len(self.list)

	def vaccinate_population(self, num_vaccinations: int):
		'''This method will vaccinate an amount of the population.'''

		# We can only vaccinate people who aren't already sick or vaccinated.
		can_be_vaccinated = self.filter(is_infected=False, is_vaccinated=False)
		num_vaccinations = min(num_vaccinations, len(can_be_vaccinated))

		# XXX TODO XXX
		# Add a log event a situation: can't vaccinate given number of people.
		# The number cannot be reached; too many people are vaccinated or sick already.

		# Vaccinate a random set of the population.
		people_to_vaccinate = random.sample(can_be_vaccinated, num_vaccinations)
		for person in people_to_vaccinate:
			person.is_vaccinated = True

	def infect_population(self, virus: Virus, num_infections: int):
		'''This method will infect an amount of the population with the given virus.'''

		# We can only infect people who aren't already sick or vaccinated.
		can_be_infected = self.filter(is_infected=False, is_vaccinated=False)
		num_infections = min(num_infections, len(can_be_infected))

		# XXX TODO XXX
		# Add a log event a situation: can't infect given number of people.
		# The number cannot be reached; too many people are vaccinated or sick already.

		# Infect a random set of the population (that is not vaccinated).
		people_to_infect = random.sample(can_be_infected, num_infections)
		for person in people_to_infect:
			person.infection = virus

	def filter(
		self,
		is_alive: bool | None = None,
		is_vaccinated: bool | None = None,
		is_infected: bool | None = None,
		is_dormant: bool | None = None,
	):
		'''
		Filters the population based on several flags, which can be combined.
		- `None` indicates no filter should be applied.
		- `True` or `False` indicates only the matching population should be gathered.
		- The `is_dormant` option also filters out healthy people, unless it is `None`.

		If you need more advanced filter options (such as those using `or` conditionals),
		then this won't do -- you'd have to make your own logic off of `self.population`.
		'''

		# Get the population.
		filtered_population = self.list

		# Filter for living (or dead) people.
		if is_alive != None:
			filtered_population = [
				person for person in filtered_population
				if person.is_alive == is_alive
			]

		# Filter for (un)vaccinated people.
		if is_vaccinated != None:
			filtered_population = [
				person for person in filtered_population
				if person.is_vaccinated == is_vaccinated
			]

		# Filter for infected (or healthy) people.
		if is_infected != None:
			filtered_population = [
				person for person in filtered_population
				if person.is_infected == is_infected
			]

		# Filter for dormant (or active) infections only.
		if is_dormant != None:
			filtered_population = [
				person for person in filtered_population
				if person.is_infected == True
				and person.is_dormant == is_dormant
			]

		# Return the result.
		return filtered_population
