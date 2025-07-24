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
		size: int,
		vaccination_rate: float,
		initial_infected: int,
		virus: Virus,
	):

		self.size = size # type: int
		self.vaccination_rate = vaccination_rate # type: float
		self.initial_infected = initial_infected # type: int

		# Generate a population with the correct number of vaccinations and infections.
		self.list = self.populate(virus) # type: list[Person]

	def populate(self, virus: Virus):
		'''
		1. This method will create the initial population (a list of `Person` objects)\
			based on the given population size.
		2. Then, the method will vaccinate a percentage of them from a virus.
		3. Finally, it will infect a given number of people in the population.\
			If too many people are vaccinated to reach the set number,\
			then as many unvaccinated people as possible are infected.
		4. The method returns the generated list.

		Returns:
			list:
				A list of `Person` objects.
		'''

		# Initialize a list of person objects.
		population: list[Person] = []
		for _id in range(self.size):
			person = Person(_id)
			population.append(person)

		# Determine how many people to vaccinate.
		num_vaccinated = self.size * self.vaccination_rate
		num_vaccinated = math.floor(num_vaccinated)

		# Vaccinate a random set of the population.
		people_to_vaccinate = random.sample(population, num_vaccinated)
		for person in people_to_vaccinate:
			person.is_vaccinated = True

		# Determine the remaining unvaccinated population.
		unvaccinated_population = self.filter(is_vaccinated=False)

		# Next, determine if we can infect the correct number of people.
		if self.initial_infected > len(unvaccinated_population):
			# We cannot - too many people are vaccinated!
			# The server must adjust the number of initially infected people.
			self.initial_infected = len(unvaccinated_population)

			# XXX TODO XXX
			# Add a log event of this situation.
			# The number of initial infected cannot be reached;
			# there are too many vaccinated people in the population.

		# Infect a random set of the population (that is not vaccinated).
		people_to_infect = random.sample(unvaccinated_population, self.initial_infected)
		for person in people_to_infect:
			person.infection = virus

		return population

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
